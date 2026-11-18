(function(){
  "use strict";

  // Progress is kept only in this browser (nothing is sent anywhere).
  var store = {
    get: function(k){ try { return localStorage.getItem("cbt:" + k); } catch(e){ return null; } },
    set: function(k, v){ try { localStorage.setItem("cbt:" + k, v); } catch(e){} }
  };

  function boot(){
    document.documentElement.classList.add("ready");

    // Nav turns solid once past the header
    var nav = document.getElementById("nav");
    var head = document.querySelector(".hero, .phead");
    var transparent = !!document.querySelector(".hero");
    function onScroll(){
      var past = transparent ? (window.scrollY > (head ? head.offsetHeight - 90 : 40)) : true;
      if (nav) nav.setAttribute("data-solid", past ? "true" : "false");
    }
    window.addEventListener("scroll", onScroll, { passive:true });
    window.addEventListener("resize", onScroll, { passive:true });
    onScroll();

    // Gentle fades
    var items = [].slice.call(document.querySelectorAll("[data-fade]"));
    if ("IntersectionObserver" in window){
      var io = new IntersectionObserver(function(es){
        es.forEach(function(e){ if (e.isIntersecting){ e.target.classList.add("in"); io.unobserve(e.target); } });
      }, { rootMargin:"0px 0px -8% 0px", threshold:0.05 });
      items.forEach(function(el){ io.observe(el); });
    } else { items.forEach(function(el){ el.classList.add("in"); }); }

    // 1–10 scales, remembered per module
    [].forEach.call(document.querySelectorAll("[data-scale]"), function(box){
      var key = "scale:" + box.getAttribute("data-scale");
      var input = box.querySelector("input");
      var out = box.querySelector("output");
      var saved = store.get(key);
      if (saved) input.value = saved;
      function show(){ out.textContent = input.value; }
      input.addEventListener("input", function(){ show(); store.set(key, input.value); });
      show();
    });

    // "I've finished this module"
    [].forEach.call(document.querySelectorAll("[data-done]"), function(btn){
      if (btn.tagName !== "BUTTON") return;
      var key = "done:" + btn.getAttribute("data-done");
      function paint(){
        var on = store.get(key) === "1";
        btn.setAttribute("aria-pressed", on ? "true" : "false");
        btn.textContent = on ? "Marked as finished ✓" : "Mark this module as finished";
      }
      btn.addEventListener("click", function(){ store.set(key, store.get(key) === "1" ? "0" : "1"); paint(); });
      paint();
    });
    // Ticks on the course overview
    [].forEach.call(document.querySelectorAll(".mods .go[data-mod]"), function(el){
      if (store.get("done:" + el.getAttribute("data-mod")) === "1"){ el.textContent = "Finished ✓"; el.setAttribute("data-done","true"); }
    });

    // Interest form → /api/contact
    var form = document.getElementById("form");
    if (form){
      form.addEventListener("submit", function(e){
        e.preventDefault();
        var s = document.getElementById("status");
        var btn = form.querySelector("button[type=submit]");
        function say(msg){ s.textContent = msg; s.setAttribute("data-shown","true"); }
        var data = {};
        new FormData(form).forEach(function(v, k){ data[k] = v; });
        btn.disabled = true; say("Sending…");
        fetch(form.getAttribute("action"), {
          method:"POST",
          headers:{ "Content-Type":"application/json", "Accept":"application/json" },
          body: JSON.stringify(data)
        }).then(function(r){ return r.json().catch(function(){ return { ok:r.ok }; }); })
          .then(function(j){
            if (j && j.ok){ form.reset(); say("Thank you. Catherine will be in touch by email soon."); }
            else { say((j && j.error) || "Something went wrong. Please try again."); }
          })
          .catch(function(){ say("Something went wrong. Please try again."); })
          .then(function(){ btn.disabled = false; });
      });
    }
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
