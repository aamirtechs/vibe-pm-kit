"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const { lintText } = require("../scorer.js");

const COMPLETE = [
  "# Widget", "",
  "## Problem", "x", "",
  "## Target users", "x", "",
  "## Goals and scope", "x", "",
  "## Non-goals", "x", "",
  "## Workflows", "x", "",
  "## Acceptance criteria", "x", "",
  "## Data and models", "Prompting only, no fine-tuning.", "",
  "## Risks", "x", "",
  "## Success metrics", "x", ""
].join("\n");

test("complete spec scores 100", () => {
  const r = lintText(COMPLETE);
  assert.equal(r.score, 100);
  assert.deepEqual(r.missing, []);
});

test("empty spec scores low and reports Problem missing", () => {
  const r = lintText("# Untitled\n\nSome thoughts.\n");
  assert.ok(r.score < 30);
  assert.ok(r.missing.includes("Problem"));
});

test("weak example scores 55 like the Python CLI", () => {
  const text = ["# X", "", "## Problem", "p", "", "## Target users", "u", "",
    "## Goals and scope", "g", "", "## Workflows", "w", "", "## Risks", "r", ""].join("\n");
  assert.equal(lintText(text).score, 55);
});

test("bundled spec template scores 100", () => {
  const tpl = fs.readFileSync(path.join(__dirname, "..", "templates", "spec-template.md"), "utf8");
  assert.equal(lintText(tpl).score, 100);
});

test("bold labels count as sections", () => {
  const r = lintText("**Problem**\nIt hurts.\n");
  assert.ok(r.found.includes("Problem"));
});
