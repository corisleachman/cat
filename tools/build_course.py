#!/usr/bin/env python3
"""Generates the static CBT course pages. Run: python3 tools/build_course.py course"""
import sys, pathlib
OUT = pathlib.Path(sys.argv[1])

HELP = """<aside class="safety" data-fade>
  <strong>If you need support right now.</strong>
  This course is self-guided and is not a crisis or emergency service. If you are in severe
  distress, or having thoughts of harming yourself, please contact your GP, call NHS 111
  (option 2 for urgent mental health support), or call 999 in an emergency.
  Samaritans are free, day or night, on <a href="tel:116123">116 123</a>, and you can text
  SHOUT to <a href="sms:85258">85258</a>.
</aside>"""

def shell(title, desc, body, *, hero=False, noindex=False, nav_right=None):
    nav_right = nav_right or '<a class="n" href="/course#modules" data-drop>Modules</a><a class="n" href="/course#join">Buy</a>'
    robots = '<meta name="robots" content="noindex"/>' if noindex else ''
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
{robots}
<meta name="theme-color" content="#EFEDE9"/>
<link rel="icon" href="/catherine-leachman-1.jpeg"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="/course/course.css"/>
</head>
<body>
<nav class="nav" id="nav" data-solid="{'false' if hero else 'true'}">
  <div class="wrap">
    <div class="nav-side left">
      <a class="n" href="/">Counselling</a>
      <a class="n" href="/course" data-drop>CBT course</a>
    </div>
    <a class="nav-mark" href="/">Catherine Leachman</a>
    <div class="nav-side right">{nav_right}</div>
  </div>
</nav>
<main id="top">
{body}
</main>
<footer class="foot">
  <div class="wrap">
    <div class="foot-cols">
      <div><p class="label">The course</p><ul>
        <li><a href="/course">Course overview</a></li>
        <li><a href="/course#modules">The six modules</a></li>
        <li><a href="/course#join">Buy the course</a></li></ul></div>
      <div><p class="label">Catherine</p><ul>
        <li><a href="/">Counselling &amp; coaching</a></li>
        <li><a href="/#about">About Catherine</a></li>
        <li><a href="/#enquiry">Make an enquiry</a></li></ul></div>
      <div><p class="label">Support now</p><ul>
        <li>Samaritans: <a href="tel:116123">116 123</a></li>
        <li>NHS 111, option 2</li>
        <li>Text SHOUT to 85258</li></ul></div>
    </div>
    <div class="foot-base">
      <span class="label">© 2026 Catherine Leachman · BACP Registered Member</span>
      <span class="label">A self-guided course, not a substitute for therapy</span>
    </div>
  </div>
</footer>
<script src="/course/course.js"></script>
</body>
</html>
"""

SHOW_FILES = False  # worksheet links hidden; module pages show a summary instead

def files(*items):
    if not SHOW_FILES:
        return ""
    rows = "".join(
        f'<li><a href="/course/resources/{f}" target="_blank" rel="noopener"><span><span class="ft">{t}</span><span class="fd">{d}</span></span><span class="fx">PDF ↗</span></a></li>'
        for f, t, d in items)
    return f'<ul class="files" data-fade>{rows}</ul>'

def scale(mod, q="Right now, how are you feeling overall?", lo="1 · really struggling", hi="10 · really well"):
    return f"""<div class="scale" data-scale="{mod}" data-fade>
  <p class="label">Check in · {q}</p>
  <div class="scale-row"><input type="range" min="1" max="10" step="1" value="5" aria-label="{q}"/><output>5</output></div>
  <div class="scale-ends"><span>{lo}</span><span>{hi}</span></div>
  <p class="scale-note">Your number stays private, in this browser only. Notice it, without judging it.</p>
</div>"""

def section(label, heading, inner, id_=None):
    idattr = f' id="{id_}"' if id_ else ''
    return f"""<section class="band"{idattr}>
  <div class="wrap g">
    <p class="label rail" data-fade>{label}</p>
    <div class="body">
      <div class="head"><h2 data-fade>{heading}</h2></div>
      <div class="prose" data-fade>{inner}</div>
    </div>
  </div>
</section>"""

SETTLE = """<div class="panel" data-fade>
  <p class="label">Before you begin · two minutes</p>
  <h4>Settle first</h4>
  <p>Find somewhere you won't be interrupted. Put both feet on the floor and let the chair hold your weight.
  Breathe in gently through your nose for a count of four, and out slowly through your mouth for a count of six.
  Do this five or six times. Then name <strong>five things you can see, four you can hear, three you can feel,
  two you can smell and one you can taste</strong>.</p>
  <p>We start every module like this on purpose. A calmer body makes it easier to look at your thoughts with curiosity rather than alarm.</p>
</div>"""

BUN_SVG = """<figure class="diagram" data-fade>
<svg viewBox="0 0 440 400" role="img" aria-label="The hot cross bun: thoughts, feelings, physical sensations and behaviour all connect to each other, around a situation">
  <g fill="none" stroke="currentColor" stroke-opacity="0.35" stroke-width="1.2">
    <circle cx="125" cy="115" r="88"/><circle cx="315" cy="115" r="88"/>
    <circle cx="125" cy="285" r="88"/><circle cx="315" cy="285" r="88"/>
    <path d="M213 115 H227 M213 285 H227 M125 203 V197 M315 203 V197"/>
    <path d="M190 180 L250 220 M250 180 L190 220"/>
  </g>
  <rect x="160" y="182" width="120" height="36" fill="#EFEDE9" stroke="currentColor" stroke-opacity="0.35"/>
  <g text-anchor="middle" font-size="15">
    <text x="220" y="205" font-size="12" letter-spacing="2">SITUATION</text>
    <text x="125" y="112">Thoughts</text><text x="125" y="132" font-size="11" opacity="0.7">what goes through my mind</text>
    <text x="315" y="112">Feelings</text><text x="315" y="132" font-size="11" opacity="0.7">emotions and moods</text>
    <text x="125" y="282">Behaviour</text><text x="125" y="302" font-size="11" opacity="0.7">what I do, or avoid</text>
    <text x="315" y="282">Physical</text><text x="315" y="302" font-size="11" opacity="0.7">what I notice in my body</text>
  </g>
</svg>
<figcaption>The “hot cross bun”. Each part feeds the others, so a change in one can change them all.</figcaption>
</figure>"""

CYCLE_SVG = """<figure class="diagram" data-fade>
<svg viewBox="0 0 440 400" role="img" aria-label="The low mood cycle: feeling low leads to doing less, which leads to less achievement and pleasure, which deepens low mood">
  <g fill="none" stroke="currentColor" stroke-opacity="0.35" stroke-width="1.2">
    <circle cx="220" cy="85" r="70"/><circle cx="340" cy="295" r="70"/><circle cx="100" cy="295" r="70"/>
  </g>
  <g fill="none" stroke="currentColor" stroke-opacity="0.6" stroke-width="1.4">
    <path d="M292 100 Q 360 150 360 215"/><path d="M352 205 L360 218 L368 205"/>
    <path d="M272 340 Q 220 365 168 340"/><path d="M180 334 L166 340 L178 348"/>
    <path d="M80 222 Q 85 130 148 98"/><path d="M134 96 L150 97 L142 110"/>
  </g>
  <g text-anchor="middle" font-size="14">
    <text x="220" y="80">I feel low,</text><text x="220" y="98">down or flat</text>
    <text x="340" y="290">I do less and</text><text x="340" y="308">withdraw</text>
    <text x="100" y="282">Less achievement,</text><text x="100" y="300">less pleasure,</text><text x="100" y="318">I feel “useless”</text>
  </g>
</svg>
<figcaption>The low-mood cycle. Behavioural activation breaks it at “I do less”.</figcaption>
</figure>"""

# ─────────────────────────────── Sales page ───────────────────────────────

MODS = [
  ("1", "Understanding your thoughts", "What CBT is, the hot cross bun model, what fight-or-flight is doing in your body, and noticing your automatic negative thoughts."),
  ("2", "Settling and fact-checking", "Grounding and the vagus nerve, then rational and irrational thinking, and how to weigh up the evidence for and against a thought."),
  ("3", "Facing what bothers you", "Listing the things that bother you, gently working through them one by one, and testing worries with small, planned experiments."),
  ("4", "Feelings are not facts", "Learning to be objective, catching emotional reasoning, the STOP skill, and lifting low mood through what you do."),
  ("5", "Putting it into practice", "Checking in on your progress, recording a real moment where you used the tools, and noticing what support you might still want."),
  ("6", "Your toolkit for life", "Reviewing everything you now have, measuring how far you have come, and a plan for keeping it going."),
]

def mods_list():
    rows = "".join(
        f'<li data-fade><a href="/course/module-{n}"><span class="n">Module {n}</span><span><span class="t">{t}</span><span class="d">{d}</span></span><span class="go" data-mod="{n}">Open →</span></a></li>'
        for n, t, d in MODS)
    return f'<ul class="mods">{rows}</ul>'

sales_body = f"""
<a class="buy-fab" id="buy" href="#join">Buy the course <span aria-hidden="true">→</span></a>
<header class="hero hero-course">
  <img class="hero-img" src="/catherine-leachman-6.jpeg" alt="Catherine Leachman, smiling, standing in a calm room with plants"/>
  <div class="hero-inner"><div class="hero-copy">
    <p class="label" data-fade>A six-week self-guided CBT course</p>
    <h1 data-fade data-d="1">Steady your mind, <em>one week at a time</em></h1>
    <p class="label" data-fade data-d="2">Work through it at home, at your own pace</p>
    <div class="hero-cta" data-fade data-d="3"><a class="ulink" href="#join">Buy the course</a></div>
  </div></div>
</header>

<section class="band" id="intro">
  <div class="wrap g">
    <p class="label rail" data-fade>Why this course</p>
    <div class="body">
      <p class="lead" data-fade style="max-width:34ch; margin-bottom:var(--s-3)">
        Some thoughts arrive so fast and feel so true that they quietly run the day.
        They shape what you do, what you avoid, and how you feel in your body.
      </p>
      <p class="measure" data-fade data-d="1" style="color:var(--ink-mid); max-width:52ch">
        This course is a gentle, structured way to slow that down. Over six weeks you will
        learn the same practical Cognitive Behavioural Therapy (CBT) tools I use with clients,
        laid out step by step so you can work through them on your own. Each module takes
        about an hour, with a small practice to carry into your week.
      </p>
      <p class="measure" data-fade data-d="2" style="color:var(--ink-mid); max-width:52ch">
        It is also a space to pause. To give yourself time, to get to know yourself a little
        better, and to practise being kinder to yourself along the way.
      </p>
    </div>
  </div>
</section>

<section class="statement"><div class="wrap">
  <p data-fade>You cannot always choose your first thought. You can learn to choose what happens next.</p>
</div></section>

<section class="band" id="outcomes">
  <div class="wrap">
    <div class="head g">
      <p class="label rail" data-fade>What you will come away with</p>
      <div class="body"><h2 data-fade>Six weeks from now, <em>you will have</em></h2></div>
    </div>
    <div class="media">
      <figure class="media-fig fig-portrait" data-fade>
        <img src="/catherine-leachman-3.jpeg" alt="Catherine Leachman, sitting and smiling"/>
        <figcaption class="label">Created by Catherine Leachman · BACP Registered Member</figcaption>
      </figure>
      <div>
        <ul class="rows" style="border-top:0">
          <li data-fade><span class="n">I</span><div><span class="t">Confidence using CBT tools on your own</span>
            <p>You will know how to catch an unhelpful thought, check it against the facts, and find a more balanced one, so the thoughts and habits that get in the way of daily life, or of what you want to achieve, lose some of their grip.</p></div></li>
          <li data-fade><span class="n">II</span><div><span class="t">A better relationship with your feelings</span>
            <p>Rather than being swept along by emotions, you will be able to notice them, name them, and understand what they are telling you.</p></div></li>
          <li data-fade><span class="n">III</span><div><span class="t">An understanding of what your body is doing</span>
            <p>The racing heart, tight chest or churning stomach will make more sense. You will know why they happen and what helps them settle.</p></div></li>
          <li data-fade><span class="n">IV</span><div><span class="t">Ways to feel safer and more regulated</span>
            <p>Simple grounding and breathing practices that help bring you out of fight-or-flight and back into a calmer state, wherever you are.</p></div></li>
          <li data-fade><span class="n">V</span><div><span class="t">More self-awareness, and more self-compassion</span>
            <p>Time set aside each week to slow down, reflect, and practise speaking to yourself the way you would speak to someone you care about.</p></div></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<hr class="rule"/>

<section class="band" id="learn">
  <div class="wrap g">
    <p class="label rail" data-fade>A little of what you will learn</p>
    <div class="body">
      <div class="head"><h2 data-fade>Your body, your nervous system, <em>and your thoughts</em></h2></div>
      <div class="duo">
        <div data-fade>
          <p class="label" style="margin-bottom:var(--s-2)">Fight-or-flight</p>
          <h3 style="font-size:var(--t-h3); margin-bottom:var(--s-2)">An old alarm in a modern world</h3>
          <p style="color:var(--ink-mid)">When your brain senses danger, it sounds an alarm. Adrenaline and cortisol are
          released, your heart beats faster, your breathing quickens and your muscles tense, ready
          to fight or run. Digestion slows, which is why anxiety can feel like butterflies or nausea.</p>
          <p style="color:var(--ink-mid)">That alarm kept our ancestors alive. The trouble is it cannot tell the
          difference between a predator and a difficult email, a worry about money or a critical thought.
          When it goes off often, or stays on, we feel on edge, exhausted and stuck. Understanding it is
          the first step to calming it.</p>
        </div>
        <div data-fade data-d="1">
          <p class="label" style="margin-bottom:var(--s-2)">The vagus nerve</p>
          <h3 style="font-size:var(--t-h3); margin-bottom:var(--s-2)">Your body’s built-in brake</h3>
          <p style="color:var(--ink-mid)">If fight-or-flight is the accelerator, the parasympathetic
          “rest and digest” system is the brake. The vagus nerve is a big part of it: a long nerve running
          from the brainstem down through the throat, heart, lungs and gut, carrying messages both ways
          between body and brain.</p>
          <p style="color:var(--ink-mid)">You can gently press that brake yourself. A long, slow out-breath,
          humming, splashing cool water on your face and feeling your feet on the ground all send a
          message of safety, so your heart rate settles and your thinking brain comes back online.</p>
        </div>
        <div data-fade>
          <p class="label" style="margin-bottom:var(--s-2)">Grounding</p>
          <h3 style="font-size:var(--t-h3); margin-bottom:var(--s-2)">Coming back to the here and now</h3>
          <p style="color:var(--ink-mid)">Anxious minds tend to live in the future and low moods in the past.
          Grounding brings your attention back to this moment, through your senses: what you can see,
          hear, touch and feel right now. It interrupts the spiral and reminds your nervous system that,
          in this moment, you are safe enough.</p>
        </div>
        <div data-fade data-d="1">
          <p class="label" style="margin-bottom:var(--s-2)">Then, CBT</p>
          <h3 style="font-size:var(--t-h3); margin-bottom:var(--s-2)">Why we settle first</h3>
          <p style="color:var(--ink-mid)">It is hard to question a thought while your body is in alarm mode.
          So each module begins by settling, and only then turns to the CBT tools: noticing thoughts,
          checking the evidence, testing predictions and changing what you do. Calm body, clearer mind.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="band" id="modules">
  <div class="wrap g">
    <p class="label rail" data-fade>What is involved</p>
    <div class="body">
      <div class="head"><h2 data-fade>Six modules, <em>one a week</em></h2></div>
      <p class="measure" data-fade style="color:var(--ink-mid); max-width:52ch; margin-bottom:var(--s-3)">
        Each module follows the same shape: a moment to settle and check in, a short recap, something new
        to learn, a practical activity with printable worksheets, and one small thing to try during the week.
        Use the arrows to look through them.
      </p>
      %%CAROUSEL%%
    </div>
  </div>
</section>

<section class="band" id="included">
  <div class="wrap g">
    <p class="label rail" data-fade>Practical things</p>
    <div class="body">
      <div class="head"><h2 data-fade>What is <em>included</em></h2></div>
      <dl class="facts">
        <div data-fade><dt>Six modules</dt><dd>Written in plain, warm language, designed to be worked through one a week, at home, at your own pace.</dd></div>
        <div data-fade data-d="1"><dt>25+ worksheets</dt><dd>Printable thought records, mood diaries, experiment planners and check-in questionnaires, each placed at the point you need it.</dd></div>
        <div data-fade data-d="2"><dt>Lasting access</dt><dd>Come back to the tools whenever you need them. Many people find them most useful after the six weeks are over.</dd></div>
      </dl>
    </div>
  </div>
</section>

<section class="band" id="fit">
  <div class="wrap g">
    <p class="label rail" data-fade>Is it right for you</p>
    <div class="body">
      <div class="head"><h2 data-fade>Who this course <em>is for</em></h2></div>
      <div class="prose" data-fade>
        <p>This course suits adults who are coping with everyday anxiety, worry, stress or low mood, and who
        would like practical tools they can use on their own. It works best if you can set aside about an hour
        a week, plus a few minutes most days for the practice.</p>
        <p>It is not a replacement for therapy, and it is not designed for a mental health crisis. If you are
        struggling a lot right now, please speak to your GP, or <a href="/#enquiry">get in touch with me</a>
        about one-to-one counselling. The course can also sit well alongside it.</p>
      </div>
    </div>
  </div>
</section>

<section class="band-lg cta-band" id="join">
  <div class="wrap g">
    <p class="label rail" data-fade>Buy the course</p>
    <div class="body">
      <div class="head"><h2 data-fade>Buy the <em>course</em></h2></div>
      <p class="measure" data-fade style="color:var(--ink-mid); margin-bottom:var(--s-4)">
        Leave your details below and I will email you with the cost, how to pay, and your access
        to all six modules and their worksheets. If you have any questions about whether it is right for you, just ask.
      </p>
      <form class="form" id="form" action="/api/contact" method="POST" data-fade>
        <div style="position:absolute; left:-9999px" aria-hidden="true">
          <label>Leave this empty <input type="text" name="website" tabindex="-1" autocomplete="off"/></label>
        </div>
        <input type="hidden" name="interest" value="Six-week CBT course"/>
        <div class="field"><label class="label" for="n">Your name</label>
          <input id="n" name="name" type="text" placeholder="First name is fine" required/></div>
        <div class="field"><label class="label" for="e">Email address</label>
          <input id="e" name="email" type="email" placeholder="Where I can send your details" required/></div>
        <div class="field"><label class="label" for="m">Anything you would like to ask</label>
          <textarea id="m" name="message" placeholder="Optional"></textarea></div>
        <label class="consent"><input type="checkbox" name="consent" required/>
          <span>I am happy for Catherine to hold my details in order to reply about the course.</span></label>
        <button class="ulink" type="submit">Buy the course</button>
        <p class="status" id="status" role="status" aria-live="polite"></p>
      </form>
      {HELP}
    </div>
  </div>
</section>
"""


# ─────────────────────────────── Module pages ───────────────────────────────

WRITE_MODULE_PAGES = False
MODULES = []

def module(n, title_html, title_plain, lead, sections, homework, kind, gets=()):
    """Collects each module's overview for the carousel on the course page.
    The full session content below is kept for reference but no longer published."""
    MODULES.append(dict(n=int(n), title=title_html, lead=lead, gets=list(gets)))
    if not WRITE_MODULE_PAGES:
        return
    n = int(n)
    prev_link = f'<a class="ulink" href="/course/module-{n-1}">← Module {n-1}</a>' if n > 1 else '<a class="ulink" href="/course">← Course overview</a>'
    next_link = f'<a class="ulink" href="/course/module-{n+1}">Module {n+1} →</a>' if n < 6 else '<a class="ulink" href="/course">Course overview →</a>'
    body = f"""
<header class="phead">
  <div class="wrap g">
    <p class="label rail crumbs"><a href="/course">CBT course</a><span>Module {n} of 6</span></p>
    <div class="body">
      <p class="label" data-fade>Module {n} · about an hour</p>
      <h1 data-fade data-d="1">{title_html}</h1>
      <p class="lead" data-fade data-d="2">{lead}</p>
    </div>
  </div>
</header>

<section class="band gets-band">
  <div class="wrap g">
    <p class="label rail" data-fade>In this module</p>
    <div class="body">
      <div class="head"><h2 data-fade>What you will <em>get from it</em></h2></div>
      <ul class="rows gets">{"".join(f'<li data-fade><span class="n">{["I","II","III","IV","V"][i]}</span><span class="t">{g}</span></li>' for i, g in enumerate(gets))}</ul>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap g">
    <p class="label rail" data-fade>Start here</p>
    <div class="body">
      {SETTLE}
      {scale(f"m{n}")}
    </div>
  </div>
</section>
{''.join(section(*s) for s in sections)}
<section class="band">
  <div class="wrap g">
    <p class="label rail" data-fade>This week</p>
    <div class="body">
      <div class="head"><h2 data-fade>Your practice <em>for the week</em></h2></div>
      <div class="panel" data-fade>{homework}</div>
      <div class="panel kind" data-fade><p>{kind}</p></div>
      <button class="ulink done-btn" type="button" data-done="{n}" aria-pressed="false">Mark this module as finished</button>
      <div class="pager">{prev_link}{next_link}</div>
      {HELP}
    </div>
  </div>
</section>
"""
    (OUT / f"module-{n}.html").write_text(shell(
        f"Module {n}: {title_plain} — CBT course", f"Module {n} of Catherine Leachman's six-week CBT course: {title_plain}.",
        body, noindex=True,
        nav_right=f'<a class="n" href="/course#modules">All modules</a>'))

# Module 1 ------------------------------------------------------------
module(1, "Understanding <em>your thoughts</em>", "Understanding your thoughts",
  "Welcome. This week is about getting to know how CBT works, what your body does when it feels under threat, and starting to notice the thoughts that pop up on their own.",
  [
   ("Welcome", "Before <em>we start</em>", f"""
<p>This is your space. Nobody else will see what you write, and there are no right or wrong answers.
Go at whatever pace feels manageable. If a week takes you two weeks, that is fine.</p>
<p>A few things to know:</p>
<ul>
<li><strong>Keep a notebook.</strong> A paper notebook or a notes app, just for this course. You will use it every week.</li>
<li><strong>Print the worksheets if you can.</strong> Writing by hand slows things down in a helpful way. You can also copy them into your notebook.</li>
<li><strong>Use the 1 to 10 check-in.</strong> Each module starts with it. Over six weeks it shows you how things are shifting.</li>
<li><strong>Look after yourself.</strong> Some of this may stir things up. Take breaks, and use the support details at the bottom of each page if you need them.</li>
</ul>
<h3>Where are you starting from?</h3>
<p>These short questionnaires give you a snapshot of how you are doing now. You will fill them in again in
Module 5, so you can see the change for yourself. Plot your anxiety and mood inventory scores on the graphs each week if you would like to track them more closely.</p>
{files(
 ("gad-7-anxiety-questionnaire.pdf", "GAD-7 anxiety questionnaire", "Seven questions about the last two weeks. Add up your total."),
 ("phq-9-mood-questionnaire.pdf", "PHQ-9 mood questionnaire", "Nine questions about low mood over the last two weeks."),
 ("anxiety-inventory.pdf", "Anxiety inventory", "A fuller checklist of how anxiety shows up for you, physically and mentally."),
 ("depression-inventory.pdf", "Depression inventory", "A fuller checklist of how low mood shows up for you."),
 ("anxiety-scores-graph.pdf", "Anxiety scores graph", "Plot your anxiety inventory score each week."),
 ("depression-scores-graph.pdf", "Depression scores graph", "Plot your depression inventory score each week."),
 ("resilience-questionnaire.pdf", "Resilience questionnaire", "Optional. A look at your strengths, across eight areas of resilience."))}
<div class="panel"><p class="label">Please read</p>
<p>If any of your answers tell you that you have been having thoughts of being better off dead, or of hurting
yourself, please don't carry that alone. Speak to your GP, call NHS 111 (option 2), or call Samaritans
on <a href="tel:116123">116 123</a> at any time. You can still do this course, and it is best done with support around you.</p></div>
"""),
   ("What is CBT", "Thoughts, feelings, body, <em>behaviour</em>", f"""
<p>Cognitive Behavioural Therapy (CBT) is built on a simple idea: it is not only what happens to us that affects
how we feel, but how we <em>interpret</em> what happens. Our thoughts, feelings, physical sensations and actions are
all connected, and they keep each other going.</p>
<p>CBT focuses on the here and now. It gives you practical ways to notice those patterns and gently change them.
A useful way to picture it is the “hot cross bun”.</p>
{BUN_SVG}
<h3>An example</h3>
<p>Chris is invited to a party. The <strong>situation</strong> is simple, but his <strong>thoughts</strong> race:
“People find me boring. If I talk to a stranger I'll blush and make a fool of myself.” He <strong>feels</strong> anxious.
His <strong>body</strong> feels hot and his heart beats fast. So his <strong>behaviour</strong> follows: he avoids going if he can,
and if he does go, he pretends to text to avoid small talk. Avoiding it brings short-term relief, but it also means
he never finds out his fears might not come true, so the cycle continues.</p>
{files(
 ("hot-cross-bun-example.pdf", "Chris's hot cross bun", "The worked example above, filled in."),
 ("hot-cross-bun-blank.pdf", "Blank hot cross bun", "Use this for your own situation."))}
<div class="panel"><p class="label">Activity · 15 minutes</p><h4>Map your own bun</h4>
<ol><li>Think of a recent moment that left you feeling anxious, low or stuck. Not the hardest thing, just something recent.</li>
<li>Write the situation in the middle of the blank hot cross bun.</li>
<li>Fill in the four parts: what went through your mind, what you felt, what you noticed in your body, and what you did (or avoided).</li>
<li>Look at how the parts connect. Can you see how each one fed the others?</li></ol></div>
"""),
   ("Your body's alarm", "Understanding <em>fight-or-flight</em>", """
<p>Look at the “physical” part of your bun. A racing heart, shallow breathing, tight shoulders, a churning stomach,
feeling hot or shaky. These are not signs that something is wrong with you. They are your body's alarm system,
the <strong>fight-or-flight response</strong>, doing exactly what it was designed to do.</p>
<p>When your brain senses a threat, a small area called the amygdala sounds the alarm. Adrenaline and cortisol flood
your system in seconds:</p>
<ul>
<li>Your <strong>heart</strong> beats faster to pump blood to your muscles.</li>
<li>Your <strong>breathing</strong> speeds up to take in more oxygen.</li>
<li>Your <strong>muscles</strong> tense, ready to act.</li>
<li><strong>Digestion</strong> slows down, which can cause butterflies, nausea or needing the loo.</li>
<li>Your <strong>attention</strong> narrows onto the threat, and the calmer, thinking part of the brain takes a back seat.</li>
</ul>
<p>This was brilliant when the threat was a wild animal. Today the alarm goes off for a deadline, a difficult conversation,
or simply a frightening thought, and there is nothing to fight or run from. So the energy has nowhere to go, and we feel it as anxiety.</p>
<p>Two things are worth remembering. First, these feelings are uncomfortable but <strong>not dangerous</strong>, and they always
pass. Second, because thoughts can set the alarm off, learning to work with your thoughts can help turn it down. That is
what the rest of this course is about.</p>
"""),
   ("A first look", "Weighing up <em>the evidence</em>", """
<p>Here is a taste of the main CBT skill you will build. Think of one negative thought from your hot cross bun, the one you
believe the most. Now imagine putting it <strong>on trial in court</strong>.</p>
<p>Draw two columns in your notebook. In one, write the <em>evidence for</em> the thought: facts that support it. In the other,
write the <em>evidence against</em> it: facts that don't fit. Only facts count in court, not feelings or guesses.</p>
<p>Don't worry if it feels hard, or if you only find one or two things for each side. You are just practising stepping back
and looking. We will go into this properly next week.</p>
"""),
  ],
  """<p class="label">Homework</p><h4>Notice · Capture · Write it down</h4>
<p>This week, your only job is to become a thought-spotter. Automatic negative thoughts (sometimes called ANTs) are the quick,
critical thoughts that pop up on their own: “I'll mess this up”, “they don't like me”, “what's the point”.</p>
<ol><li><strong>Notice</strong> when your mood dips or your body tenses. Ask, “what was just going through my mind?”</li>
<li><strong>Capture</strong> the thought, word for word if you can.</li>
<li><strong>Write it down</strong> with the situation and how you felt. Columns 1 to 3 of the thought record are perfect for this.</li></ol>
<p>You don't need to change anything yet. Just notice.</p>"""
  + files(("thought-record.pdf", "Thought record", "This week, fill in the first three columns: situation, moods and automatic thoughts.")),
  "Noticing a painful thought is not the same as believing it. This week, see if you can watch your thoughts with the kind of curiosity you would offer a friend.",
  gets=['A clear, simple picture of what CBT is and how it can help you', 'A map of how your thoughts, feelings, body and behaviour feed each other, using your own example', 'An understanding of fight-or-flight, so the racing heart and churning stomach make sense and feel less frightening', 'A snapshot of where you are starting from, so you can see your progress later', 'The first skill of CBT: noticing and capturing your automatic negative thoughts'])

# Module 2 ------------------------------------------------------------
module(2, "Settling, and <em>fact-checking</em>", "Settling and fact-checking",
  "This week you will learn how to calm your nervous system on purpose, and then how to tell the difference between a thought that is based on fact and one that is driven by feeling.",
  [
   ("Recap", "Looking back <em>at last week</em>", """
<p>Look at the thoughts you captured. Did any patterns come up? Did the same kinds of thoughts appear in the same kinds of
situations? Were some easier to notice than others? Write a few lines in your notebook about what you found.</p>
<p>If you found it hard to catch your thoughts, that is completely normal. They are automatic precisely because we are so
used to them. Keep going, it gets easier.</p>
"""),
   ("The vagus nerve", "Your body's <em>built-in brake</em>", f"""
<p>Last week we met the fight-or-flight response, your body's accelerator. You also have a brake: the parasympathetic or
“rest and digest” system. The <strong>vagus nerve</strong> is a key part of it. It runs from the brainstem down through your
throat, heart, lungs and gut, and it carries messages in both directions. Most of its traffic actually goes
<em>from the body to the brain</em>.</p>
<p>That is good news, because it means you can send your brain signals of safety through your body. Some ways that work for many people:</p>
<ul>
<li><strong>A longer out-breath.</strong> Breathing out for longer than you breathe in (in for 4, out for 6 or 7) slows the heart. This is the quickest brake you have.</li>
<li><strong>Humming or singing.</strong> The vibration and slow exhale both help.</li>
<li><strong>Cool water.</strong> Splash cold water on your face or hold something cold.</li>
<li><strong>Soft eyes and a relaxed jaw.</strong> Unclench, drop your shoulders, and let your gaze widen.</li>
<li><strong>Gentle movement.</strong> A slow walk, a stretch, rolling your shoulders.</li>
</ul>
<p>None of these are magic, and they work best with practice, when you are already fairly calm. Then they are there for you when you need them.</p>
"""),
   ("Grounding", "Coming back to <em>the here and now</em>", f"""
<p>When we are anxious our minds race into the future. When we are low they get pulled into the past. Grounding gently brings
your attention back to the present moment through your senses, which helps your nervous system register that, right now, you are safe enough.</p>
<p>The <strong>5, 4, 3, 2, 1</strong> exercise at the start of each module is one form of grounding. Others include feeling your feet
pressing into the floor, holding a warm drink and noticing its weight and warmth, or describing an object in front of you in detail.</p>
<p>Our attention is selective. We tend to notice only a small part of what is around us, and when we are stressed it locks
onto threats. Practising noticing everything around you, on purpose, helps to widen it again.</p>
{files(("selective-attention-worksheet.pdf", "Selective attention worksheet", "Take five minutes to notice everything around you: sights, sounds, temperature, your position, and more."))}
"""),
   ("How we see things", "Our minds take <em>shortcuts</em>", f"""
<p>Our brains are constantly filling in gaps. When we feel anxious or low, they tend to fill them in with the most negative
version of events, and to notice the things that confirm how we already feel. These short exercises help you see how your own mind does this.
Do them with curiosity, not judgement.</p>
{files(
 ("how-we-process-the-world.pdf", "How we process the world around us", "Imagine ten everyday scenarios and notice the first outcome that comes to mind. Do your outcomes lean positive or negative?"),
 ("colour-task.pdf", "The colour task", "Look at the words and notice which ones catch your eye first."),
 ("self-description-questionnaire.pdf", "Self-description questionnaire", "Tick how much each word describes you. Which words were easiest to agree with?"))}
"""),
   ("Rational or irrational", "Fact-check <em>your thoughts</em>", """
<p><strong>Rational thoughts</strong> are based on evidence. They tend to be more balanced, and they often help us feel motivated.
<strong>Irrational thoughts</strong> are based on emotion. They are less reliable, and they tend to create anxiety or low mood.</p>
<p>When you catch a thought that is making you feel worse, fact-check it with three questions:</p>
<ol>
<li><strong>Is this thought based on fact?</strong> Try to “put a camera on it”. If you filmed your day, what would the camera actually show? Sometimes you can't know until the event is over.</li>
<li><strong>Does this thought help me achieve my goals?</strong> Or does it get in the way of what I want to do?</li>
<li><strong>Does this thought help me feel how I want to feel?</strong> Usually an irrational thought has a negative impact on your feelings, actions and the situation as a whole.</li>
</ol>
<p>Then ask: <strong>can I turn it around?</strong> What would a more rational, balanced version of the thought be? Look for what you might have missed, and fact-check it again.</p>
<p>This short video explains it well: <a href="https://www.youtube.com/watch?v=AtOys5GqQxE&t=393s" target="_blank" rel="noopener">Rational vs irrational thoughts (YouTube)</a>.</p>
"""),
   ("Cognitive restructuring", "Challenging <em>negative thoughts</em>", f"""
<p>Why challenge a negative thought at all? Because automatic thoughts feel like facts, but they are often guesses, shaped by
mood, tiredness, old experiences and that alarm system we met last week. Left unchallenged, they decide how we feel and what we do.</p>
<p><strong>Cognitive restructuring</strong> is the process of slowing a thought down and checking it, so you can replace it with
something more accurate and balanced. It is not about forcing yourself to “think positive”. It is about being fair.</p>
<p>Look at the worked example first. Someone made a small mistake at work, and their boss pointed it out. Their automatic
thought was “my boss is mad and I'm going to get the sack”, which they believed 75%. Once they listed the evidence on each side,
a more balanced thought emerged, and their belief in the original thought, and their worry, dropped.</p>
{files(
 ("cognitive-restructuring-example.pdf", "Cognitive restructuring: worked example", "See how the steps fit together."),
 ("cognitive-restructuring-worksheet.pdf", "Cognitive restructuring worksheet", "Use this for one of your own thoughts."))}
<div class="panel"><p class="label">Activity · 20 minutes</p><h4>Put one thought on trial</h4>
<ol><li>Choose one thought from last week's list, ideally the one you believe the most.</li>
<li>Write down the situation, how it made you feel, and how much you believe the thought (0 to 100%).</li>
<li>List the evidence for, and the evidence against. Facts only.</li>
<li>Ask: is there an alternative thought that fits the evidence better? Write it down.</li>
<li>Re-rate how much you believe the original thought now, and how you feel.</li></ol></div>
"""),
  ],
  """<p class="label">Homework</p><h4>Challenge your automatic negative thoughts</h4>
<p>Each day this week, catch at least one automatic negative thought and work through it using the cognitive restructuring
worksheet or the full thought record (all seven columns now). Settle yourself with a longer out-breath first.</p>
<p>Notice how much you believe the thought before and after. Even a small drop, from 80% to 60%, is real progress.</p>"""
  + files(("thought-record.pdf", "Thought record", "Now using all seven columns."), ("cognitive-restructuring-worksheet.pdf", "Cognitive restructuring worksheet", "Print a few copies for the week.")),
  "You are not trying to win an argument with yourself. You are learning to be a fair witness, and that includes being fair to you.",
  gets=['A quick, reliable way to calm your body using your breath and the vagus nerve', 'Grounding techniques that bring you back to the present moment when your mind races', 'Insight into the shortcuts your mind takes when you feel anxious or low', 'Three questions to fact-check any thought, rational or irrational', 'Confidence using cognitive restructuring to find a fairer, more balanced thought'])

# Module 3 ------------------------------------------------------------
module(3, "Facing what <em>bothers you</em>", "Facing what bothers you",
  "This week you will look at what gets in the way, gently line up the things that bother you, and start to test your worries out in real life.",
  [
   ("Recap", "How did the challenging <em>go?</em>", """
<p>Have you been challenging your negative thoughts? Look back at your worksheets and ask yourself:</p>
<ul>
<li>Which thoughts were easiest to challenge, and which were hardest?</li>
<li>What got in the way? Forgetting, feeling too upset in the moment, not believing the balanced thought?</li>
<li>What is in front of you right now that feels most difficult?</li>
</ul>
<p>Barriers are normal, and they are useful information. Write them down. Some will be solved by the tools in this module, and
some just need more practice. If the alternative thought doesn't feel true yet, that is fine. Belief often follows action, which is what this week is about.</p>
"""),
   ("Activity", "Your list of <em>bothersome things</em>", """
<div class="panel"><p class="label">Activity · 25 minutes</p><h4>From least to most</h4>
<ol>
<li>Settle yourself with a few slow breaths. Close your eyes if that feels OK, and picture the things that are bothering you at the moment, big and small.</li>
<li>Write them as a list, in order: the <strong>least bothersome at the top</strong>, the <strong>most bothersome at the bottom</strong>.</li>
<li>Go through the list one item at a time, starting at the top. For each one, reflect: what is it about this that bothers me? What am I telling myself about it?</li>
<li>Try to think about it rationally. Use your fact-check questions. Then write down one possible solution or next step, however small.</li>
<li>Stop whenever you need to. You don't have to reach the bottom of the list today.</li>
</ol></div>
<p>Starting with the smaller things builds confidence and momentum, so that by the time you reach the bigger ones you have already had some practice.</p>
<h3>If anxiety is the main thing for you</h3>
<p>You can use the same list as a <strong>graded hierarchy</strong>. If there is a situation you avoid, break it into steps from least to
most frightening. For example, for social anxiety: say hello to a neighbour, make small talk with a shop assistant, go to a short
gathering with a friend, go to a party. Then work up the steps one at a time, staying with each until the anxiety starts to settle.
Avoidance keeps fear going, while gentle, repeated facing shrinks it.</p>
"""),
   ("Behavioural experiments", "Testing a worry <em>in real life</em>", f"""
<p>Some thoughts are predictions: “if I speak up, I'll go bright red and everyone will notice.” The best way to check a prediction
is to test it. A <strong>behavioural experiment</strong> is a small, planned, safe test of whether a thought is true.</p>
<p>In the worked example, someone believed (95%) they couldn't talk to a stranger without going bright red. They planned to talk to a
stranger in a pub, and to be filmed so they could see what really happened. They also wrote down what might stop them, and how they would get past it.</p>
<p>After an experiment, review it. What actually happened? How much do you believe the original thought now? What have you learned?</p>
{files(
 ("behavioural-experiment-example.pdf", "Behavioural experiment: worked example", "See how one is planned."),
 ("behavioural-experiment-plan.pdf", "Behavioural experiment planning sheet", "Plan your own: the thought, the test, where, when, and what might get in the way."),
 ("behavioural-experiment-review.pdf", "Behavioural experiment review sheet", "Use this afterwards to see what you learned."),
 ("thought-experiment.pdf", "Experiment record", "An alternative format for logging several experiments."),
 ("action-plan.pdf", "Action plan", "For a solution from your list: steps, timing, possible problems and how you will handle them."))}
"""),
  ],
  """<p class="label">Homework</p><h4>Do something you love, on purpose</h4>
<p>When we are anxious or low, the things that nourish us are often the first to go. This week, choose at least one thing you
genuinely enjoy and do it <em>on purpose</em>. Plan it, put it in your diary, and protect the time. Notice how you feel before, during and after.</p>
<p>The butterfly of balance and the mood battery can help you see what drains you and what restores you. Fill one wing (or the top of
the battery) with the pressures and stressors in your life, and the other with the things that recharge you. Is there a good balance?</p>
<p>If you feel ready, plan one small behavioural experiment too.</p>"""
  + files(("butterfly-of-balance.pdf", "Butterfly of balance", "Pressures on one wing, restoring activities on the other."),
          ("mood-battery.pdf", "The mood battery", "Sort your day into stressors (red) and de-stressors (green).")),
  "Rest and enjoyment are not rewards you have to earn. They are part of what keeps you well.",
  gets=['A better understanding of what gets in the way, and how to work around it', 'A calm, step-by-step way to face the things that bother you, smallest first', 'A graded approach to situations you avoid, if anxiety is holding you back', 'The skill of testing a worry in real life with a small, safe experiment', 'A clearer view of what drains you and what restores you, and a nudge to do more of what you love'])

# Module 4 ------------------------------------------------------------
module(4, "Feelings are <em>not facts</em>", "Feelings are not facts",
  "This week is about learning to be objective: noticing when a feeling is being treated as proof, pausing before you react, and lifting low mood through what you do.",
  [
   ("Recap", "Looking back <em>at last week</em>", """
<p>Did you do something you love on purpose? How did it feel? Did you try an experiment, and what did you find out?
And have you kept challenging your negative thoughts? Note down anything you noticed, especially anything that surprised you.</p>
"""),
   ("Emotional reasoning", "“I feel it, so <em>it must be true</em>”", """
<p><strong>Emotional reasoning</strong> is when we treat a feeling as evidence. “I feel guilty, so I must have done something wrong.”
“I feel anxious, so something bad must be about to happen.” “I feel useless, so I must be useless.”</p>
<p>Feelings are real and they matter. They tell us something important about what we are going through. But they are
<strong>not facts about the world</strong>. Anxiety can be triggered by a thought, by tiredness, by caffeine, by an old memory. Feeling
like a failure does not make you one.</p>
<p>Being objective means stepping back and looking at the situation as an outside observer would. Some questions that help:</p>
<ul>
<li>Is this a fact, or my opinion or feeling about it?</li>
<li>If a friend told me this, what would I say to them?</li>
<li>What would someone who cares about me say about this situation?</li>
<li>What's the bigger picture? Will this matter in six months?</li>
<li>Is my reaction in proportion to what actually happened?</li>
</ul>
{files}
""".replace("{files}", files(("thought-record-stopp.pdf", "Thought record with STOPP prompts", "A thought record with helpful questions built in, including “is this fact or opinion?”")))),
   ("The STOP skill", "Pause <em>before you react</em>", f"""
<p>When emotions are running high, it is hard to be objective in the moment. The STOP skill gives you a pause button:</p>
<ol>
<li><strong>Stop.</strong> Don't react. Freeze for a moment, so your emotions don't act for you. Name the emotion.</li>
<li><strong>Take a step back.</strong> Take a breath, and keep breathing slowly until you feel more in control. Very few things need a split-second decision.</li>
<li><strong>Observe.</strong> What is happening around you and inside you? What automatic thoughts are showing up? What are the facts?</li>
<li><strong>Proceed mindfully.</strong> Ask, “what do I want from this situation? What would make it better, or worse?” Then choose your response.</li>
</ol>
<p>Notice how the “take a step back” part uses the same long, slow breath from Module 2. You are pressing the brake so your thinking brain can catch up.</p>
{files(("stop-skill.pdf", "The STOP skill", "The steps, plus a practice sheet to reflect on a time you used it."))}
"""),
   ("If your mood is low", "Doing more, <em>to feel better</em>", f"""
<p>When we feel low, we naturally do less. We withdraw from people, drop hobbies and put things off. It makes sense, because everything feels like
effort. But doing less means less achievement, less connection and less pleasure, and that makes us feel lower still.</p>
{CYCLE_SVG}
<p><strong>Behavioural activation</strong> breaks the cycle at the point where we do less. Instead of waiting to feel motivated before acting,
we act first, in small, planned steps, and the mood often follows.</p>
<ol>
<li>For a few days, use the activity log to note what you do each hour, and rate each activity for <strong>achievement</strong>, <strong>closeness</strong> (connection to others), <strong>enjoyment</strong> and <strong>importance</strong>.</li>
<li>Look for patterns. What lifts you, even slightly? What drains you? When are the empty stretches?</li>
<li>Plan in a few more of the activities that lift you, and a few that matter to you, starting small. A ten-minute walk counts.</li>
<li>Do them as planned, whether or not you feel like it, and notice what happens.</li>
</ol>
{files(("activity-log.pdf", "Activity log", "Track each hour and rate achievement, closeness, enjoyment and importance."))}
"""),
  ],
  """<p class="label">Homework</p><h4>How aware are you now?</h4>
<p>This week, notice how conscious you have become of your thoughts, feelings and behaviour. Each day, record at least one moment where you
noticed what was going on for you: the thought, the feeling, what you noticed in your body, and what you did. Did you catch any emotional reasoning? Did you use STOP?</p>
<p>Keep a mood diary alongside it, rating your mood morning, afternoon and evening, and noting anything that affected it.</p>"""
  + files(("mood-diary.pdf", "Mood diary", "Rate your mood three times a day and note what was going on."), ("thought-record-stopp.pdf", "Thought record with STOPP prompts", "For recording your moments of awareness.")),
  "Your feelings deserve to be listened to, not obeyed. You can say to a feeling: “I hear you, and I'm going to check the facts.”",
  gets=['The ability to spot emotional reasoning, when a feeling is being treated as a fact', 'Questions that help you step back and see a situation more objectively', 'The STOP skill: a pause button for moments when emotions run high', 'A practical way to lift low mood by changing what you do, one small step at a time', 'A growing awareness of your thoughts, feelings and behaviour, day to day'])

# Module 5 ------------------------------------------------------------
module(5, "Putting it <em>into practice</em>", "Putting it into practice",
  "This week you will take stock of how far you have come, notice what is helping, and start preparing for life after the course.",
  [
   ("Recap", "What did you <em>notice?</em>", """
<p>Look back at last week's records. How aware were you of your thoughts, feelings and behaviour? Compare that to how it felt
in Module 1, when you were just starting to spot your automatic thoughts. Have you been challenging your negative thoughts? Which tools have you found yourself reaching for?</p>
"""),
   ("Progress check", "How far <em>have you come?</em>", f"""
<p>Now is a good time to fill in the questionnaires from Module 1 again, and to compare your scores. Look at your 1 to 10 check-ins too.</p>
{files(
 ("gad-7-anxiety-questionnaire.pdf", "GAD-7 anxiety questionnaire", "Compare with your Module 1 score."),
 ("phq-9-mood-questionnaire.pdf", "PHQ-9 mood questionnaire", "Compare with your Module 1 score."),
 ("anxiety-inventory.pdf", "Anxiety inventory", "Add your score to your graph."),
 ("depression-inventory.pdf", "Depression inventory", "Add your score to your graph."))}
<p>Progress is rarely a straight line. There will be good weeks and harder ones. Look at the overall direction, and at the small changes:
catching a thought sooner, believing it a little less, settling a little faster.</p>
<h3>Do you need more support?</h3>
<p>Be honest with yourself here. If your scores haven't shifted, have gone up, or if things feel heavier than when you started, that is
not a failure. It is useful information, and it may mean you would benefit from more support than a self-guided course can give.</p>
<ul>
<li>Your GP can talk through options with you.</li>
<li>In England you can refer yourself to <a href="https://www.nhs.uk/service-search/mental-health/find-an-nhs-talking-therapies-service" target="_blank" rel="noopener">NHS Talking Therapies</a> for free.</li>
<li>You are very welcome to <a href="/#enquiry">get in touch with me</a> about one-to-one counselling.</li>
</ul>
"""),
   ("Preparing to finish", "Looking <em>ahead</em>", """
<p>Next week is the last module. Before then, take a few minutes to think about:</p>
<ul>
<li>Which tool has been most helpful? Which do you want to keep using?</li>
<li>What situations are likely to be difficult in the coming months?</li>
<li>What early warning signs tell you things are starting to slip? (Sleep changing, withdrawing, a familiar thought coming back.)</li>
</ul>
<p>Write your answers down. You will use them to build your plan next week.</p>
"""),
  ],
  """<p class="label">Homework</p><h4>Record a real moment</h4>
<p>This week, record an actual situation where you feel you applied what you have learned about challenging irrational thoughts.
Write down what happened, the thought that came up, what you did with it, and how things turned out. Use a thought record if it helps.</p>
<p>It doesn't need to be a big moment or a perfect one. A small win, noticed, is worth a lot.</p>"""
  + files(("thought-record.pdf", "Thought record", "For recording your real-life moment.")),
  "Look at how much you have shown up for yourself over these weeks. Whatever your scores say, that effort deserves to be recognised.",
  gets=['A clear sense of how far you have come since Module 1', 'Recognition of which tools are working best for you', 'An honest check on whether more support would help, and where to find it', 'Your early warning signs, written down, so you can act on them sooner', 'A real example of you using CBT in your own life'])

# Module 6 ------------------------------------------------------------
module(6, "Your toolkit <em>for life</em>", "Your toolkit for life",
  "In this final module you will gather together everything you have learned, see how far you have come, and make a plan to keep it going.",
  [
   ("Recap", "Your <em>real moment</em>", """
<p>Read back the situation you recorded last week. What did you do differently from how you might have handled it six weeks ago?
What does that tell you about what you are capable of?</p>
"""),
   ("Your toolkit", "The tools <em>you now have</em>", """
<p>These are yours to keep. They help you stay in charge of your own thoughts, actions and behaviour.</p>
<ul class="rows" style="margin-top:var(--s-2); padding:0">
<li><span class="n">Settle</span><div><span class="t">Calm the body first</span><p>Long out-breaths, grounding through your senses, and the vagus nerve brake. Use them before you try to think things through.</p></div></li>
<li><span class="n">Notice</span><div><span class="t">Spot the pattern</span><p>The hot cross bun. Notice, capture, write it down. Name the feeling.</p></div></li>
<li><span class="n">Check</span><div><span class="t">Fact-check the thought</span><p>Rational or irrational? Put a camera on it. Evidence for and against. Find the balanced thought.</p></div></li>
<li><span class="n">Pause</span><div><span class="t">STOP before you react</span><p>Stop, take a step back, observe, proceed mindfully. Remember that feelings are not facts.</p></div></li>
<li><span class="n">Test</span><div><span class="t">Try it out</span><p>Behavioural experiments and graded steps to test predictions instead of avoiding them.</p></div></li>
<li><span class="n">Act</span><div><span class="t">Do what nourishes you</span><p>Plan activities that bring achievement, closeness and enjoyment, especially when your mood is low.</p></div></li>
</ul>
"""),
   ("Looking back", "How far <em>you have come</em>", f"""
<p>Use the 1 to 10 scale at the top of this page one more time, and compare it to your very first check-in. If you filled in the resilience
questionnaire in Module 1, try it again now and see which areas have grown.</p>
{files(("resilience-questionnaire.pdf", "Resilience questionnaire", "Compare with your first go."))}
<div class="panel"><p class="label">Reflection · 15 minutes</p><h4>A letter to yourself</h4>
<p>Write a short letter to yourself, to read on a hard day in the future. Include what you have learned, which tools help most, the early warning
signs to watch for, and what you would say to yourself, kindly, when things feel difficult. Keep it somewhere you will find it.</p></div>
"""),
   ("Keeping it going", "Support <em>for the road ahead</em>", f"""
<p>The skills you have practised get stronger with use, like a muscle. Keep challenging your negative thoughts and keep a mood journal,
even when things are going well. That is when the practice is easiest, and it makes the tools easier to reach when you need them.</p>
{files(("mood-diary.pdf", "Mood diary", "Print a fresh one whenever you need it."), ("thought-record.pdf", "Thought record", "Your everyday tool."))}
<h3>Useful websites</h3>
<ul>
<li><a href="https://www.nhs.uk/every-mind-matters/" target="_blank" rel="noopener">NHS Every Mind Matters</a>: free, practical tips and a personalised mind plan.</li>
<li><a href="https://www.mind.org.uk/" target="_blank" rel="noopener">Mind</a>: clear information on mental health and where to get help.</li>
<li><a href="https://www.getselfhelp.co.uk/" target="_blank" rel="noopener">Get Self Help</a>: a large library of free CBT worksheets and information.</li>
<li><a href="https://www.nhs.uk/service-search/mental-health/find-an-nhs-talking-therapies-service" target="_blank" rel="noopener">NHS Talking Therapies</a>: free NHS therapy you can refer yourself to (England).</li>
<li><a href="https://www.samaritans.org/" target="_blank" rel="noopener">Samaritans</a>: someone to talk to, any time, on 116 123.</li>
</ul>
<p>And if you would like ongoing, one-to-one support to build on this work, I would be glad to hear from you. <a href="/#enquiry">Make an enquiry</a>.</p>
"""),
  ],
  """<p class="label">Take away</p><h4>Keep going, gently</h4>
<ul><li>Keep challenging your negative thoughts.</li>
<li>Keep a mood journal.</li>
<li>Start each day, or each hard moment, by settling your body first.</li>
<li>Come back to these modules whenever you need a refresher.</li></ul>""",
  "You have given yourself six weeks of time, attention and care. Keep offering yourself that kindness. You deserve it.",
  gets=['A complete, easy-to-remember toolkit: settle, notice, check, pause, test and act', 'A final measure of your progress across the six weeks', 'A letter from you to you, for the harder days ahead', 'A plan for keeping the skills going, and trusted places to turn for support', 'The confidence that you can look after your mind on your own'])

def carousel():
    slides = []
    for m in MODULES:
        items = "".join(f"<li>{g}</li>" for g in m["gets"])
        slides.append(f'''<article class="slide" id="module-{m["n"]}" role="group" aria-roledescription="slide" aria-label="Module {m["n"]} of {len(MODULES)}">
  <p class="label">Module {m["n"]} · about an hour</p>
  <h3>{m["title"]}</h3>
  <p class="slide-lead">{m["lead"]}</p>
  <p class="label slide-sub">In this module · what you will get from it</p>
  <ol class="slide-gets">{items}</ol>
</article>''')
    dots = "".join(f'<button type="button" class="dot" aria-label="Go to module {m["n"]}" data-go="{i}"></button>' for i, m in enumerate(MODULES))
    return f'''<div class="carousel" data-fade aria-roledescription="carousel" aria-label="The six modules">
  <div class="track" tabindex="0">{"".join(slides)}</div>
  <div class="car-ctrl">
    <button type="button" class="arrow prev" aria-label="Previous module">←</button>
    <div class="dots">{dots}</div>
    <span class="car-count label" aria-live="polite">1 / {len(MODULES)}</span>
    <button type="button" class="arrow next" aria-label="Next module">→</button>
  </div>
</div>'''

sales_body = sales_body.replace("%%CAROUSEL%%", carousel())
(OUT / "index.html").write_text(shell(
  "Six-week CBT course — Catherine Leachman",
  "A six-week, self-guided CBT course by Catherine Leachman. Learn to challenge unhelpful thoughts, understand your body's stress response, and feel calmer and more in control.",
  sales_body, hero=True))

print("built", sorted(p.name for p in OUT.glob("*.html")))
