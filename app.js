"use strict";

const WEAK_SPEC = [
  "# My App",
  "",
  "## Problem",
  "People forget follow-ups after meetings.",
  "",
  "## Target users",
  "Small sales teams.",
  "",
  "## Goals and scope",
  "v1: record a follow-up list and send reminders.",
  "",
  "## Workflows",
  "User adds a follow-up, picks a date, gets reminded.",
  "",
  "## Risks",
  "Reminder emails land in spam.",
  ""
].join("\n");

const FALLBACK_FULL_SPEC = [
  "# Spec",
  "",
  "## Problem", "x", "",
  "## Target users", "x", "",
  "## Goals and scope", "x", "",
  "## Non-goals", "x", "",
  "## Workflows", "x", "",
  "## Acceptance criteria", "x", "",
  "## Data and models", "x", "",
  "## Risks", "x", "",
  "## Success metrics", "x", ""
].join("\n");

function $(id) { return document.getElementById(id); }

function verdictFor(score) {
  if (score >= 90) return "Build-ready. An AI can build this with few inventions.";
  if (score >= 70) return "Buildable. Fill the gaps before they become scope.";
  if (score >= 40) return "Risky. The builder will invent the missing sections.";
  return "Not a spec yet. Start from the kit's spec template.";
}

function render() {
  const r = lintText($("spec-input").value);
  $("score-num").textContent = String(r.score);
  $("score-verdict").textContent = verdictFor(r.score);
  $("found-list").innerHTML = r.found.map((n) => "<li>" + n + "</li>").join("");
  $("missing-list").innerHTML = r.missing.map((n) => "<li>Missing: " + n + "</li>").join("");
}

function applyTheme(theme) {
  document.documentElement.setAttribute("data-theme", theme);
  $("btn-theme").textContent = theme === "dark" ? "☀️" : "🌙";
}

document.addEventListener("DOMContentLoaded", () => {
  if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) applyTheme("dark");
  $("btn-theme").addEventListener("click", () => {
    applyTheme(document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark");
  });
  $("spec-input").addEventListener("input", render);
  $("btn-weak").addEventListener("click", () => { $("spec-input").value = WEAK_SPEC; render(); });
  $("btn-full").addEventListener("click", async () => {
    try {
      const res = await fetch("templates/spec-template.md");
      if (!res.ok) throw new Error("fetch failed");
      $("spec-input").value = await res.text();
    } catch (e) {
      $("spec-input").value = FALLBACK_FULL_SPEC;
    }
    render();
  });
  $("spec-input").value = WEAK_SPEC;
  render();
});
