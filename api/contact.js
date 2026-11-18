// Vercel serverless function: receives the enquiry form and emails Catherine via Resend.
// Needs the RESEND_API_KEY environment variable set in the Vercel project.

const TO = process.env.CONTACT_TO || "catherineleachmanwellness@gmail.com";
const FROM = process.env.CONTACT_FROM || "Catherine Leachman website <enquiries@corisleachman.com>";

const esc = (v) => String(v || "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const clip = (v, n) => String(v || "").trim().slice(0, n);

async function readBody(req) {
  if (req.body && typeof req.body === "object") return req.body;
  let raw = typeof req.body === "string" ? req.body : "";
  if (!raw) { for await (const chunk of req) raw += chunk; }
  const type = req.headers["content-type"] || "";
  if (type.includes("application/json")) { try { return JSON.parse(raw); } catch { return {}; } }
  return Object.fromEntries(new URLSearchParams(raw));
}

module.exports = async (req, res) => {
  if (req.method !== "POST") { res.setHeader("Allow", "POST"); return res.status(405).json({ ok: false }); }

  const body = await readBody(req);
  const wantsJson = (req.headers.accept || "").includes("application/json");
  const done = (status, payload) => wantsJson || status !== 200
    ? res.status(status).json(payload)
    : res.redirect(303, "/?sent=1#enquiry");

  // Honeypot: bots fill the hidden "website" field. Pretend success.
  if (body.website) return done(200, { ok: true });

  const name = clip(body.name, 200);
  const email = clip(body.email, 320);
  const interest = clip(body.interest, 100) || "Not given";
  const message = clip(body.message, 5000);

  if (!name || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return done(400, { ok: false, error: "Please give your name and a valid email address." });
  if (!process.env.RESEND_API_KEY) return done(500, { ok: false, error: "Email is not configured." });

  const text = `New enquiry from the website\n\nName: ${name}\nEmail: ${email}\nEnquiring about: ${interest}\n\nMessage:\n${message || "(none)"}\n\nReply to this email to answer ${name} directly.`;
  const html = `<div style="font-family:Georgia,serif;font-size:16px;line-height:1.6;color:#35322E">
  <p style="font-size:13px;letter-spacing:.15em;text-transform:uppercase;color:#8E877D">New enquiry from the website</p>
  <p><strong>Name:</strong> ${esc(name)}<br/><strong>Email:</strong> <a href="mailto:${esc(email)}">${esc(email)}</a><br/><strong>Enquiring about:</strong> ${esc(interest)}</p>
  <p><strong>Message:</strong></p><p style="white-space:pre-wrap">${esc(message) || "(none)"}</p>
  <p style="color:#8E877D;font-size:14px">Reply to this email to answer ${esc(name)} directly.</p></div>`;

  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${process.env.RESEND_API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify({ from: FROM, to: [TO], reply_to: email, subject: `New enquiry: ${name} (${interest})`, text, html }),
  });

  if (!r.ok) {
    console.error("Resend error", r.status, await r.text());
    return done(502, { ok: false, error: "The message could not be sent." });
  }
  return done(200, { ok: true });
};
