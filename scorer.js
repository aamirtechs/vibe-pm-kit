"use strict";

// Browser and Node port of tools/spec_lint.py. Keep the sections, weights
// and synonyms in sync with the Python version.
const SECTIONS = [
  ["Problem", 15, ["problem", "why", "motivation", "pain point"]],
  ["Target users", 10, ["target users", "users", "audience", "personas", "who is it for"]],
  ["Goals and scope", 15, ["goals and scope", "scope", "goals", "in scope", "requirements"]],
  ["Non-goals", 10, ["non-goals", "non goals", "out of scope", "not doing"]],
  ["Workflows", 10, ["workflows", "user stories", "user flow", "how it works", "journeys"]],
  ["Acceptance criteria", 15, ["acceptance criteria", "definition of done", "done when", "success criteria"]],
  ["Data and models", 10, ["data and models", "data", "models", "training", "tuning", "fine-tuning", "rag"]],
  ["Risks", 5, ["risks", "risk", "edge cases", "failure modes"]],
  ["Success metrics", 10, ["success metrics", "metrics", "kpis", "measurement", "how we measure"]]
];

function extractHeadings(text) {
  const headings = [];
  for (const line of text.split(/\r?\n/)) {
    const m = line.trim().match(/^(#{1,6})\s+(.*)$/);
    if (m) headings.push(m[2].trim().toLowerCase());
  }
  return headings;
}

function escapeRegExp(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function lintText(text) {
  const headings = extractHeadings(text);
  const body = text.toLowerCase();
  const found = [];
  const missing = [];
  let score = 0;
  for (const [name, weight, synonyms] of SECTIONS) {
    let hit = headings.some((h) => synonyms.some((syn) => h.includes(syn)));
    if (!hit) {
      hit = synonyms.some((syn) =>
        new RegExp("^\\s*(\\*\\*|__)" + escapeRegExp(syn) + "(\\*\\*|__)", "m").test(body));
    }
    if (hit) { found.push(name); score += weight; } else { missing.push(name); }
  }
  return { score, found, missing };
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { SECTIONS, extractHeadings, lintText };
}
