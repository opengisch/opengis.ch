#!/usr/bin/env python3
"""Render a human-readable HTML viewer for sitemap audit JSON reports."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

ISSUE_META = {
    "source_fetch_failed": {
        "label": "Source fetch failed",
        "severity": 5,
        "tone": "critical",
    },
    "local_page_missing": {
        "label": "Local page missing",
        "severity": 4,
        "tone": "high",
    },
    "text_mismatch": {
        "label": "Text mismatch",
        "severity": 3,
        "tone": "warning",
    },
    "content_found_under_different_url": {
        "label": "Content found elsewhere",
        "severity": 2,
        "tone": "info",
    },
    "text_diff_within_threshold": {
        "label": "Minor text diff",
        "severity": 1,
        "tone": "muted",
    },
}

SUMMARY_KEYS = (
    ("checked_pages", "Checked pages"),
    ("local_page_missing", "Missing locally"),
    ("text_mismatch", "Text mismatches"),
    ("content_found_under_different_url", "Content moved"),
    ("source_fetch_failed", "Fetch failures"),
)

HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Sitemap Audit Viewer</title>
  <style>
    :root {
      color-scheme: light dark;
      --bg: #f4f7f4;
      --bg-accent: #dce7d2;
      --panel: rgba(255, 255, 255, 0.9);
      --panel-strong: #ffffff;
      --text: #152018;
      --muted: #5d6c60;
      --border: rgba(21, 32, 24, 0.12);
      --shadow: 0 18px 50px rgba(33, 50, 31, 0.12);
      --brand: #5f9d15;
      --brand-strong: #407010;
      --critical: #a52b2b;
      --critical-bg: rgba(165, 43, 43, 0.12);
      --high: #b35d00;
      --high-bg: rgba(179, 93, 0, 0.12);
      --warning: #946200;
      --warning-bg: rgba(148, 98, 0, 0.12);
      --info: #0f5c8a;
      --info-bg: rgba(15, 92, 138, 0.12);
      --muted-tone: #58656c;
      --muted-bg: rgba(88, 101, 108, 0.12);
      --clean: #20643a;
      --clean-bg: rgba(32, 100, 58, 0.12);
    }

    html[data-theme="dark"] {
      --bg: #101712;
      --bg-accent: #18231a;
      --panel: rgba(20, 28, 22, 0.88);
      --panel-strong: #18211b;
      --text: #eef5ef;
      --muted: #a8b8aa;
      --border: rgba(238, 245, 239, 0.1);
      --shadow: 0 22px 60px rgba(0, 0, 0, 0.38);
      --brand: #95ca47;
      --brand-strong: #b6df7a;
      --critical-bg: rgba(255, 121, 121, 0.14);
      --high-bg: rgba(255, 173, 92, 0.14);
      --warning-bg: rgba(255, 211, 94, 0.14);
      --info-bg: rgba(118, 201, 255, 0.14);
      --muted-bg: rgba(164, 179, 188, 0.14);
      --clean-bg: rgba(100, 216, 140, 0.14);
    }

    * { box-sizing: border-box; }

    body {
      margin: 0;
      min-height: 100vh;
      background:
        radial-gradient(circle at top left, var(--bg-accent), transparent 28rem),
        linear-gradient(180deg, var(--bg), color-mix(in srgb, var(--bg) 86%, #000 14%));
      color: var(--text);
      font: 16px/1.5 "Segoe UI", "Helvetica Neue", Helvetica, Arial, sans-serif;
    }

    a { color: var(--brand-strong); }

    .page {
      width: min(1400px, calc(100vw - 2rem));
      margin: 0 auto;
      padding: 1.25rem 0 2.5rem;
    }

    .hero,
    .panel {
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 24px;
      box-shadow: var(--shadow);
      backdrop-filter: blur(10px);
    }

    .hero {
      padding: 1.5rem;
      display: grid;
      gap: 1.25rem;
    }

    .hero-top {
      display: flex;
      justify-content: space-between;
      gap: 1rem;
      align-items: flex-start;
      flex-wrap: wrap;
    }

    .eyebrow {
      margin: 0 0 0.45rem;
      color: var(--brand);
      font-size: 0.82rem;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      font-weight: 700;
    }

    h1 {
      margin: 0;
      font-size: clamp(2rem, 5vw, 3.8rem);
      line-height: 1;
      letter-spacing: -0.04em;
    }

    .lede {
      margin: 0.55rem 0 0;
      max-width: 60rem;
      color: var(--muted);
    }

    .meta-grid,
    .summary-grid,
    .controls,
    .footer-meta {
      display: grid;
      gap: 1rem;
    }

    .meta-grid {
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    }

    .summary-grid {
      margin-top: 1rem;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    }

    .panel {
      padding: 1rem 1.1rem;
    }

    .meta-label,
    .summary-label,
    .section-title,
    .input-label {
      margin: 0;
      color: var(--muted);
      font-size: 0.84rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-weight: 700;
    }

    .meta-value,
    .summary-value {
      margin: 0.35rem 0 0;
      font-weight: 700;
    }

    .summary-value {
      font-size: 1.9rem;
      line-height: 1;
      letter-spacing: -0.04em;
    }

    .toolbar {
      margin-top: 1rem;
      display: grid;
      gap: 1rem;
    }

    .controls {
      grid-template-columns: 1.6fr 1fr 1fr auto;
      align-items: end;
    }

    .field {
      display: grid;
      gap: 0.4rem;
    }

    .field input,
    .field select,
    .button {
      width: 100%;
      border: 1px solid var(--border);
      border-radius: 14px;
      background: var(--panel-strong);
      color: var(--text);
      font: inherit;
      padding: 0.8rem 0.95rem;
    }

    .button {
      cursor: pointer;
      font-weight: 700;
      background: linear-gradient(135deg, var(--brand), var(--brand-strong));
      color: #fff;
      border: none;
      box-shadow: 0 10px 26px rgba(95, 157, 21, 0.25);
    }

    .button.secondary {
      background: var(--panel-strong);
      color: var(--text);
      border: 1px solid var(--border);
      box-shadow: none;
    }

    .issue-filters {
      display: flex;
      flex-wrap: wrap;
      gap: 0.65rem;
    }

    .chip {
      border: 1px solid var(--border);
      border-radius: 999px;
      background: var(--panel-strong);
      color: var(--text);
      padding: 0.55rem 0.85rem;
      font: inherit;
      cursor: pointer;
    }

    .chip.active {
      border-color: var(--brand);
      color: var(--brand-strong);
      box-shadow: inset 0 0 0 1px var(--brand);
    }

    .results-panel {
      margin-top: 1rem;
      overflow: hidden;
    }

    .results-header {
      display: flex;
      justify-content: space-between;
      gap: 1rem;
      align-items: center;
      flex-wrap: wrap;
      margin-bottom: 1rem;
    }

    .results-count {
      margin: 0;
      color: var(--muted);
    }

    .table-wrap {
      overflow: auto;
      border-radius: 18px;
      border: 1px solid var(--border);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      min-width: 980px;
      background: var(--panel-strong);
    }

    thead th {
      position: sticky;
      top: 0;
      background: color-mix(in srgb, var(--panel-strong) 92%, var(--bg) 8%);
      color: var(--muted);
      font-size: 0.82rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      text-align: left;
      padding: 0.9rem 1rem;
      border-bottom: 1px solid var(--border);
    }

    tbody td {
      padding: 0.9rem 1rem;
      border-bottom: 1px solid var(--border);
      vertical-align: top;
    }

    tbody tr:hover {
      background: color-mix(in srgb, var(--panel-strong) 88%, var(--bg-accent) 12%);
    }

    .status-badge,
    .issue-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.28rem 0.6rem;
      border-radius: 999px;
      font-size: 0.78rem;
      font-weight: 700;
      white-space: nowrap;
    }

    .tone-critical { color: var(--critical); background: var(--critical-bg); }
    .tone-high { color: var(--high); background: var(--high-bg); }
    .tone-warning { color: var(--warning); background: var(--warning-bg); }
    .tone-info { color: var(--info); background: var(--info-bg); }
    .tone-muted { color: var(--muted-tone); background: var(--muted-bg); }
    .tone-clean { color: var(--clean); background: var(--clean-bg); }

    .url-link {
      color: var(--text);
      font-weight: 700;
      text-decoration: none;
    }

    .url-link:hover { color: var(--brand-strong); }

    .path-text,
    .mono,
    .empty-state {
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
    }

    .path-text,
    .subtle,
    .detail-grid dd,
    .detail-grid dt {
      color: var(--muted);
    }

    .issue-stack {
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
    }

    details {
      min-width: 18rem;
    }

    summary {
      cursor: pointer;
      color: var(--brand-strong);
      font-weight: 700;
    }

    .detail-grid {
      margin: 0.7rem 0 0;
      display: grid;
      gap: 0.5rem 0.8rem;
      grid-template-columns: max-content 1fr;
    }

    .detail-grid dt,
    .detail-grid dd {
      margin: 0;
      font-size: 0.92rem;
    }

    .pagination {
      margin-top: 1rem;
      display: flex;
      justify-content: space-between;
      gap: 1rem;
      align-items: center;
      flex-wrap: wrap;
    }

    .pagination-buttons {
      display: flex;
      gap: 0.6rem;
      flex-wrap: wrap;
    }

    .footer-meta {
      margin-top: 1rem;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    }

    .empty-state {
      padding: 2rem;
      text-align: center;
      color: var(--muted);
    }

    .theme-toggle {
      width: auto;
      min-width: 8.5rem;
    }

    @media (max-width: 980px) {
      .controls {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>
  <div class="page">
    <section class="hero">
      <div class="hero-top">
        <div>
          <p class="eyebrow">Sitemap report</p>
          <h1>Sitemap Audit Viewer</h1>
          <p class="lede">Human-readable view of the generated audit report with filters, severity sorting, search, pagination, and dark mode.</p>
        </div>
        <button class="button secondary theme-toggle" id="themeToggle" type="button">Toggle theme</button>
      </div>

      <div class="meta-grid" id="metaGrid"></div>
      <div class="summary-grid" id="summaryGrid"></div>
    </section>

    <section class="panel toolbar">
      <div class="controls">
        <label class="field">
          <span class="input-label">Search</span>
          <input id="searchInput" type="search" placeholder="Filter by URL, path, local file, or matched URL">
        </label>
        <label class="field">
          <span class="input-label">Issue filter</span>
          <select id="issueSelect"></select>
        </label>
        <label class="field">
          <span class="input-label">Sort by</span>
          <select id="sortSelect">
            <option value="severity">Severity</option>
            <option value="similarity">Similarity</option>
            <option value="url">URL</option>
          </select>
        </label>
        <button class="button secondary" id="problemsOnlyButton" type="button">Problems only: on</button>
      </div>
      <div class="issue-filters" id="issueFilters"></div>
    </section>

    <section class="panel results-panel">
      <div class="results-header">
        <div>
          <p class="section-title">Pages</p>
          <p class="results-count" id="resultsCount"></p>
        </div>
      </div>

      <div class="table-wrap" id="tableWrap"></div>

      <div class="pagination">
        <p class="results-count" id="pageCount"></p>
        <div class="pagination-buttons">
          <button class="button secondary" id="prevButton" type="button">Previous</button>
          <button class="button secondary" id="nextButton" type="button">Next</button>
        </div>
      </div>
    </section>

    <section class="footer-meta" id="footerMeta"></section>
  </div>

  <script id="viewer-data" type="application/json">__VIEWER_DATA__</script>
  <script>
    const data = JSON.parse(document.getElementById("viewer-data").textContent);
    const state = {
      query: "",
      issue: "all",
      sort: "severity",
      problemsOnly: true,
      page: 1,
      pageSize: 50,
    };

    const els = {
      metaGrid: document.getElementById("metaGrid"),
      summaryGrid: document.getElementById("summaryGrid"),
      footerMeta: document.getElementById("footerMeta"),
      issueFilters: document.getElementById("issueFilters"),
      issueSelect: document.getElementById("issueSelect"),
      searchInput: document.getElementById("searchInput"),
      sortSelect: document.getElementById("sortSelect"),
      problemsOnlyButton: document.getElementById("problemsOnlyButton"),
      tableWrap: document.getElementById("tableWrap"),
      resultsCount: document.getElementById("resultsCount"),
      pageCount: document.getElementById("pageCount"),
      prevButton: document.getElementById("prevButton"),
      nextButton: document.getElementById("nextButton"),
      themeToggle: document.getElementById("themeToggle"),
    };

    function setTheme(theme) {
      document.documentElement.setAttribute("data-theme", theme);
      localStorage.setItem("sitemap-audit-theme", theme);
    }

    function initTheme() {
      const savedTheme = localStorage.getItem("sitemap-audit-theme");
      if (savedTheme === "light" || savedTheme === "dark") {
        setTheme(savedTheme);
        return;
      }
      const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
      setTheme(prefersDark ? "dark" : "light");
    }

    function makePanel(label, value) {
      const article = document.createElement("article");
      article.className = "panel";

      const title = document.createElement("p");
      title.className = "meta-label";
      title.textContent = label;

      const body = document.createElement("p");
      body.className = "meta-value";
      body.textContent = value;

      article.append(title, body);
      return article;
    }

    function makeSummaryPanel(label, value) {
      const article = document.createElement("article");
      article.className = "panel";

      const title = document.createElement("p");
      title.className = "summary-label";
      title.textContent = label;

      const body = document.createElement("p");
      body.className = "summary-value";
      body.textContent = value;

      article.append(title, body);
      return article;
    }

    function formatSimilarity(value) {
      if (value === null || value === undefined) {
        return "-";
      }
      return `${Math.round(value * 1000) / 10}%`;
    }

    function filteredPages() {
      const query = state.query.trim().toLowerCase();
      let pages = data.pages.filter((page) => {
        if (state.problemsOnly && page.is_clean) {
          return false;
        }
        if (state.issue === "clean") {
          if (!page.is_clean) {
            return false;
          }
        } else if (state.issue !== "all" && !page.issues.includes(state.issue)) {
          return false;
        }
        if (!query) {
          return true;
        }
        return page.search_text.includes(query);
      });

      pages = pages.slice().sort((left, right) => {
        if (state.sort === "url") {
          return left.url.localeCompare(right.url);
        }
        if (state.sort === "similarity") {
          const leftScore = left.text_similarity === null ? Number.POSITIVE_INFINITY : left.text_similarity;
          const rightScore = right.text_similarity === null ? Number.POSITIVE_INFINITY : right.text_similarity;
          if (leftScore !== rightScore) {
            return leftScore - rightScore;
          }
        } else {
          if (left.severity !== right.severity) {
            return right.severity - left.severity;
          }
        }

        return left.url.localeCompare(right.url);
      });

      return pages;
    }

    function renderMeta() {
      const cards = [
        ["Generated", data.generated_at],
        ["Source sitemap", data.source_sitemap_url],
        ["JSON report", data.report_label],
        ["Local public dir", data.local_public_dir || "-"],
        ["Offline mirror", data.offline_dir || "-"],
        ["Allowed domains", data.allowed_domains.join(", ") || "-"],
      ];

      els.metaGrid.innerHTML = "";
      cards.forEach(([label, value]) => els.metaGrid.appendChild(makePanel(label, value)));
    }

    function renderSummary() {
      els.summaryGrid.innerHTML = "";
      data.summary_cards.forEach((item) => {
        els.summaryGrid.appendChild(makeSummaryPanel(item.label, item.value));
      });
    }

    function renderIssueControls() {
      const options = [
        { key: "all", label: "All pages", count: data.total_pages },
        { key: "clean", label: "Clean pages", count: data.clean_pages },
        ...data.issue_counts,
      ];

      els.issueSelect.innerHTML = "";
      els.issueFilters.innerHTML = "";

      options.forEach((option) => {
        const optionEl = document.createElement("option");
        optionEl.value = option.key;
        optionEl.textContent = `${option.label} (${option.count})`;
        els.issueSelect.appendChild(optionEl);

        const chip = document.createElement("button");
        chip.type = "button";
        chip.className = `chip${state.issue === option.key ? " active" : ""}`;
        chip.textContent = `${option.label} (${option.count})`;
        chip.addEventListener("click", () => {
          state.issue = option.key;
          state.page = 1;
          els.issueSelect.value = option.key;
          render();
        });
        els.issueFilters.appendChild(chip);
      });

      els.issueSelect.value = state.issue;
    }

    function badge(text, tone, className) {
      const span = document.createElement("span");
      span.className = `${className} tone-${tone}`;
      span.textContent = text;
      return span;
    }

    function makeDetailRow(label, value) {
      if (!value) {
        return null;
      }

      const dt = document.createElement("dt");
      dt.textContent = label;

      const dd = document.createElement("dd");
      dd.className = "mono";
      dd.textContent = value;

      return [dt, dd];
    }

    function renderTable() {
      const allPages = filteredPages();
      const totalPages = Math.max(1, Math.ceil(allPages.length / state.pageSize));
      state.page = Math.min(state.page, totalPages);

      const start = (state.page - 1) * state.pageSize;
      const pageItems = allPages.slice(start, start + state.pageSize);

      els.resultsCount.textContent = `${allPages.length} matching page entries`;
      els.pageCount.textContent = `Page ${state.page} of ${totalPages}`;
      els.prevButton.disabled = state.page <= 1;
      els.nextButton.disabled = state.page >= totalPages;

      if (!pageItems.length) {
        els.tableWrap.innerHTML = '<div class="empty-state">No report entries match the current filters.</div>';
        return;
      }

      const table = document.createElement("table");
      table.innerHTML = `
        <thead>
          <tr>
            <th>Status</th>
            <th>URL</th>
            <th>Issues</th>
            <th>Similarity</th>
            <th>Details</th>
          </tr>
        </thead>
      `;

      const tbody = document.createElement("tbody");

      pageItems.forEach((page) => {
        const row = document.createElement("tr");

        const statusCell = document.createElement("td");
        statusCell.appendChild(badge(page.status_label, page.tone, "status-badge"));

        const urlCell = document.createElement("td");
        const link = document.createElement("a");
        link.className = "url-link";
        link.href = page.url;
        link.target = "_blank";
        link.rel = "noreferrer";
        link.textContent = page.url;

        const path = document.createElement("div");
        path.className = "path-text";
        path.textContent = page.path;

        urlCell.append(link, path);

        const issuesCell = document.createElement("td");
        const issueStack = document.createElement("div");
        issueStack.className = "issue-stack";
        if (page.is_clean) {
          issueStack.appendChild(badge("No issues", "clean", "issue-badge"));
        } else {
          page.issue_labels.forEach((issue) => {
            issueStack.appendChild(badge(issue.label, issue.tone, "issue-badge"));
          });
        }
        issuesCell.appendChild(issueStack);

        const similarityCell = document.createElement("td");
        similarityCell.textContent = formatSimilarity(page.text_similarity);

        const detailCell = document.createElement("td");
        const details = document.createElement("details");
        const summary = document.createElement("summary");
        summary.textContent = "Inspect";
        details.appendChild(summary);

        const grid = document.createElement("dl");
        grid.className = "detail-grid";

        [
          ["Local file", page.local_file],
          ["Matched local file", page.matched_local_file],
          ["Matched local URL", page.matched_local_url],
          ["Source file", page.source_file],
          ["Alias content file", page.alias_content_file],
          ["Source type", page.source_type],
        ].forEach(([label, value]) => {
          const pair = makeDetailRow(label, value);
          if (pair) {
            grid.append(pair[0], pair[1]);
          }
        });

        details.appendChild(grid);
        detailCell.appendChild(details);

        row.append(statusCell, urlCell, issuesCell, similarityCell, detailCell);
        tbody.appendChild(row);
      });

      table.appendChild(tbody);
      els.tableWrap.innerHTML = "";
      els.tableWrap.appendChild(table);
    }

    function renderFooterMeta() {
      els.footerMeta.innerHTML = "";
      [
        ["Total URLs in sitemap", String(data.total_urls_in_sitemap)],
        ["Total URLs checked", String(data.total_urls_checked)],
        ["Average similarity", data.average_similarity],
      ].forEach(([label, value]) => {
        els.footerMeta.appendChild(makePanel(label, value));
      });
    }

    function render() {
      renderIssueControls();
      renderTable();
      els.problemsOnlyButton.textContent = `Problems only: ${state.problemsOnly ? "on" : "off"}`;
    }

    els.searchInput.addEventListener("input", (event) => {
      state.query = event.target.value;
      state.page = 1;
      render();
    });

    els.issueSelect.addEventListener("change", (event) => {
      state.issue = event.target.value;
      state.page = 1;
      render();
    });

    els.sortSelect.addEventListener("change", (event) => {
      state.sort = event.target.value;
      state.page = 1;
      render();
    });

    els.problemsOnlyButton.addEventListener("click", () => {
      state.problemsOnly = !state.problemsOnly;
      state.page = 1;
      render();
    });

    els.prevButton.addEventListener("click", () => {
      state.page = Math.max(1, state.page - 1);
      renderTable();
    });

    els.nextButton.addEventListener("click", () => {
      state.page += 1;
      renderTable();
    });

    els.themeToggle.addEventListener("click", () => {
      const current = document.documentElement.getAttribute("data-theme") === "dark" ? "dark" : "light";
      setTheme(current === "dark" ? "light" : "dark");
    });

    initTheme();
    renderMeta();
    renderSummary();
    renderFooterMeta();
    render();
  </script>
</body>
</html>
"""


def derive_html_output_path(json_report_path: Path) -> Path:
    if json_report_path.suffix.lower() == ".json":
        return json_report_path.with_suffix(".html")
    return Path(f"{json_report_path}.html")


def _format_datetime(value: str | None) -> str:
    if not value:
        return "Unknown"

    try:
        parsed = datetime.fromisoformat(value)
    except ValueError:
        return value

    return parsed.strftime("%Y-%m-%d %H:%M:%S %Z")


def _format_count(value: object) -> str:
    if isinstance(value, int):
        return f"{value:,}"
    return str(value)


def _format_average_similarity(summary: dict[str, object]) -> str:
    value = summary.get("average_similarity")
    if isinstance(value, (int, float)):
        return f"{value * 100:.1f}%"
    return "-"


def _issue_descriptor(issue_key: str) -> dict[str, object]:
    issue = ISSUE_META.get(issue_key)
    if issue:
        return issue
    return {
        "label": issue_key.replace("_", " ").title(),
        "severity": 1,
        "tone": "muted",
    }


def _page_status(page: dict[str, object]) -> dict[str, object]:
    issues = page.get("issues") or []
    if not issues:
        return {"label": "Clean", "severity": 0, "tone": "clean"}

    descriptors = [_issue_descriptor(str(item)) for item in issues]
    descriptors.sort(key=lambda item: int(item["severity"]), reverse=True)
    top = descriptors[0]
    return {
        "label": top["label"],
        "severity": int(top["severity"]),
        "tone": str(top["tone"]),
    }


def build_view_model(report: dict[str, object], report_label: str) -> dict[str, object]:
    pages = report.get("pages") or []
    summary = report.get("summary") or {}

    issue_counts: dict[str, int] = {}
    transformed_pages: list[dict[str, object]] = []
    clean_pages = 0

    for raw_page in pages:
        issues = [str(item) for item in raw_page.get("issues") or []]
        if issues:
            for issue in issues:
                issue_counts[issue] = issue_counts.get(issue, 0) + 1
        else:
            clean_pages += 1

        status = _page_status(raw_page)
        issue_labels = [
            {
                "label": str(_issue_descriptor(issue)["label"]),
                "tone": str(_issue_descriptor(issue)["tone"]),
            }
            for issue in issues
        ]

        search_parts = [
            str(raw_page.get("url") or ""),
            str(raw_page.get("path") or ""),
            str(raw_page.get("local_file") or ""),
            str(raw_page.get("matched_local_url") or ""),
            str(raw_page.get("matched_local_file") or ""),
            str(raw_page.get("alias_content_file") or ""),
            " ".join(issues),
        ]

        transformed_pages.append(
            {
                "url": raw_page.get("url"),
                "path": raw_page.get("path"),
                "issues": issues,
                "issue_labels": issue_labels,
                "status_label": status["label"],
                "severity": status["severity"],
                "tone": status["tone"],
                "is_clean": not issues,
                "text_similarity": raw_page.get("text_similarity"),
                "local_file": raw_page.get("local_file"),
                "matched_local_url": raw_page.get("matched_local_url"),
                "matched_local_file": raw_page.get("matched_local_file"),
                "alias_content_file": raw_page.get("alias_content_file"),
                "source_file": raw_page.get("source_file"),
                "source_type": raw_page.get("source_type"),
                "search_text": " ".join(search_parts).lower(),
            }
        )

    summary_cards = []
    for key, label in SUMMARY_KEYS:
        value = summary.get(key, issue_counts.get(key, 0))
        summary_cards.append({"label": label, "value": _format_count(value)})
    summary_cards.append(
        {
            "label": "Average similarity",
            "value": _format_average_similarity(summary),
        }
    )

    ordered_issue_counts = []
    for issue, count in sorted(
        issue_counts.items(),
        key=lambda item: (
            int(_issue_descriptor(item[0])["severity"]),
            item[1],
            item[0],
        ),
        reverse=True,
    ):
        descriptor = _issue_descriptor(issue)
        ordered_issue_counts.append(
            {
                "key": issue,
                "label": str(descriptor["label"]),
                "count": count,
                "tone": str(descriptor["tone"]),
            }
        )

    return {
        "report_label": report_label,
        "generated_at": _format_datetime(str(report.get("generated_at_utc") or "")),
        "source_sitemap_url": report.get("source_sitemap_url") or "-",
        "local_public_dir": report.get("local_public_dir") or "-",
        "offline_dir": report.get("offline_dir") or "-",
        "allowed_domains": report.get("allowed_domains") or [],
        "total_urls_in_sitemap": report.get("total_urls_in_sitemap") or 0,
        "total_urls_checked": report.get("total_urls_checked") or len(transformed_pages),
        "total_pages": len(transformed_pages),
        "clean_pages": clean_pages,
        "average_similarity": _format_average_similarity(summary),
        "summary_cards": summary_cards,
        "issue_counts": ordered_issue_counts,
        "pages": transformed_pages,
    }


def render_html(view_model: dict[str, object]) -> str:
    payload = json.dumps(view_model, ensure_ascii=True, separators=(",", ":")).replace("</", "<\\/")
    return HTML_TEMPLATE.replace("__VIEWER_DATA__", payload)


def write_html_report(
    report: dict[str, object],
    *,
    json_report_path: Path,
    html_output_path: Path,
) -> None:
    html_output_path.parent.mkdir(parents=True, exist_ok=True)
    view_model = build_view_model(report, json_report_path.name)
    html_output_path.write_text(render_html(view_model), encoding="utf-8")


def load_report(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render a standalone HTML viewer for sitemap audit JSON reports."
    )
    parser.add_argument(
        "--input",
        default="reports/sitemap_audit_report.json",
        help="Path to the JSON sitemap audit report.",
    )
    parser.add_argument(
        "--output",
        default="",
        help="Output HTML path. Defaults to the JSON path with a .html suffix.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else derive_html_output_path(input_path)

    report = load_report(input_path)
    write_html_report(report, json_report_path=input_path, html_output_path=output_path)

    print(
        json.dumps(
            {
                "input": str(input_path),
                "output": str(output_path),
                "pages": len(report.get("pages") or []),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
