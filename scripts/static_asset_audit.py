#!/usr/bin/env python3
"""Audit built site HTML/CSS for internal asset links and uploaded-file coverage."""

from __future__ import annotations

import argparse
import json
import posixpath
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlparse

ALLOWED_DOMAINS = {"opengis.ch", "www.opengis.ch"}
UPLOAD_ROOTS = (
    "/wp-content/uploads/",
    "/i0.wp.com/www.opengis.ch/wp-content/uploads/",
)
ASSET_EXTENSIONS = {
    ".apng",
    ".avif",
    ".avi",
    ".css",
    ".eot",
    ".gif",
    ".ico",
    ".jpeg",
    ".jpg",
    ".js",
    ".json",
    ".m4a",
    ".m4v",
    ".map",
    ".mov",
    ".mp3",
    ".mp4",
    ".ogg",
    ".ogv",
    ".pdf",
    ".png",
    ".svg",
    ".ttf",
    ".txt",
    ".wav",
    ".webm",
    ".webp",
    ".woff",
    ".woff2",
    ".xml",
    ".zip",
}
CSS_URL_RE = re.compile(r"url\((.*?)\)", re.IGNORECASE)

HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Static Asset Audit</title>
  <style>
    :root {
      color-scheme: light dark;
      --bg: #f4f7f4;
      --bg-accent: #dce7d2;
      --panel: rgba(255, 255, 255, 0.92);
      --panel-strong: #ffffff;
      --text: #152018;
      --muted: #5d6c60;
      --border: rgba(21, 32, 24, 0.12);
      --shadow: 0 18px 50px rgba(33, 50, 31, 0.12);
      --brand: #5f9d15;
      --brand-strong: #407010;
      --critical: #a52b2b;
      --critical-bg: rgba(165, 43, 43, 0.12);
      --warning: #946200;
      --warning-bg: rgba(148, 98, 0, 0.12);
      --clean: #20643a;
      --clean-bg: rgba(32, 100, 58, 0.12);
      --info: #0f5c8a;
      --info-bg: rgba(15, 92, 138, 0.12);
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
      --warning-bg: rgba(255, 211, 94, 0.14);
      --clean-bg: rgba(100, 216, 140, 0.14);
      --info-bg: rgba(118, 201, 255, 0.14);
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
    .page {
      width: min(1400px, calc(100vw - 2rem));
      margin: 0 auto;
      padding: 1.25rem 0 2.5rem;
    }
    .hero, .panel {
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
    .lede, .muted, .results-count { color: var(--muted); }
    .grid {
      display: grid;
      gap: 1rem;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    }
    .panel { padding: 1rem 1.1rem; }
    .label {
      margin: 0;
      color: var(--muted);
      font-size: 0.84rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-weight: 700;
    }
    .value {
      margin: 0.35rem 0 0;
      font-weight: 700;
      font-size: 1.9rem;
      line-height: 1;
      letter-spacing: -0.04em;
    }
    .toolbar, .results { margin-top: 1rem; }
    .toolbar { display: grid; gap: 1rem; }
    .controls {
      display: grid;
      gap: 1rem;
      grid-template-columns: 1.6fr 1fr 1fr auto;
      align-items: end;
    }
    .field { display: grid; gap: 0.4rem; }
    .field input, .field select, .button {
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
    .results-switch {
      display: flex;
      gap: 0.7rem;
      flex-wrap: wrap;
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
    .table-wrap {
      overflow: auto;
      border-radius: 18px;
      border: 1px solid var(--border);
      margin-top: 1rem;
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
    .mono { font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace; }
    .badge {
      display: inline-flex;
      padding: 0.28rem 0.6rem;
      border-radius: 999px;
      font-size: 0.78rem;
      font-weight: 700;
      white-space: nowrap;
    }
    .critical { color: var(--critical); background: var(--critical-bg); }
    .warning { color: var(--warning); background: var(--warning-bg); }
    .clean { color: var(--clean); background: var(--clean-bg); }
    .info { color: var(--info); background: var(--info-bg); }
    .theme-toggle { width: auto; min-width: 8.5rem; }
    @media (max-width: 980px) {
      .controls { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>
  <div class="page">
    <section class="hero">
      <div class="hero-top">
        <div>
          <p class="eyebrow">Static asset report</p>
          <h1>Static Asset Audit</h1>
          <p class="lede">Checks built HTML and CSS for internal asset references, missing files, and unreferenced uploaded files.</p>
        </div>
        <button class="button secondary theme-toggle" id="themeToggle" type="button">Toggle theme</button>
      </div>
      <div class="grid" id="summaryGrid"></div>
    </section>
    <section class="panel toolbar">
      <div class="controls">
        <label class="field">
          <span class="label">Search</span>
          <input id="searchInput" type="search" placeholder="Filter by source file, URL, or asset path">
        </label>
        <label class="field">
          <span class="label">View</span>
          <select id="viewSelect">
            <option value="missing">Missing references</option>
            <option value="unreferenced">Unreferenced uploads</option>
            <option value="all">All findings</option>
          </select>
        </label>
        <label class="field">
          <span class="label">Sort by</span>
          <select id="sortSelect">
            <option value="severity">Severity</option>
            <option value="path">Path</option>
            <option value="source">Source file</option>
          </select>
        </label>
        <button class="button secondary" id="cleanToggle" type="button">Show clean summary</button>
      </div>
      <div class="results-switch" id="quickFilters"></div>
    </section>
    <section class="panel results">
      <p class="label" id="resultsTitle">Findings</p>
      <p class="results-count" id="resultsCount"></p>
      <div class="table-wrap" id="tableWrap"></div>
    </section>
  </div>
  <script id="audit-data" type="application/json">__ASSET_AUDIT_DATA__</script>
  <script>
    const data = JSON.parse(document.getElementById("audit-data").textContent);
    const state = { query: "", view: "missing", sort: "severity" };

    function setTheme(theme) {
      document.documentElement.setAttribute("data-theme", theme);
      localStorage.setItem("static-asset-audit-theme", theme);
    }
    function initTheme() {
      const savedTheme = localStorage.getItem("static-asset-audit-theme");
      if (savedTheme === "light" || savedTheme === "dark") {
        setTheme(savedTheme);
        return;
      }
      setTheme(window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    }
    function card(label, value) {
      const article = document.createElement("article");
      article.className = "panel";
      const title = document.createElement("p");
      title.className = "label";
      title.textContent = label;
      const body = document.createElement("p");
      body.className = "value";
      body.textContent = value;
      article.append(title, body);
      return article;
    }
    function filteredRows() {
      const query = state.query.trim().toLowerCase();
      let rows = data.findings.filter((row) => {
        if (state.view === "missing" && row.kind !== "missing_reference") return false;
        if (state.view === "unreferenced" && row.kind !== "unreferenced_upload") return false;
        if (!query) return true;
        return row.search_text.includes(query);
      });
      rows = rows.slice().sort((a, b) => {
        if (state.sort === "path") {
          return a.asset_path.localeCompare(b.asset_path);
        }
        if (state.sort === "source") {
          return a.source_file.localeCompare(b.source_file);
        }
        if (a.severity !== b.severity) {
          return b.severity - a.severity;
        }
        return a.asset_path.localeCompare(b.asset_path);
      });
      return rows;
    }
    function renderSummary() {
      const grid = document.getElementById("summaryGrid");
      grid.innerHTML = "";
      data.summary_cards.forEach((item) => grid.appendChild(card(item.label, item.value)));
    }
    function renderQuickFilters() {
      const target = document.getElementById("quickFilters");
      target.innerHTML = "";
      [
        ["missing", `Missing references (${data.summary.missing_reference_count})`],
        ["unreferenced", `Unreferenced uploads (${data.summary.unreferenced_upload_count})`],
        ["all", `All findings (${data.findings.length})`],
      ].forEach(([key, label]) => {
        const button = document.createElement("button");
        button.type = "button";
        button.className = `chip${state.view === key ? " active" : ""}`;
        button.textContent = label;
        button.addEventListener("click", () => {
          state.view = key;
          document.getElementById("viewSelect").value = key;
          renderTable();
          renderQuickFilters();
        });
        target.appendChild(button);
      });
    }
    function badge(text, className) {
      const span = document.createElement("span");
      span.className = `badge ${className}`;
      span.textContent = text;
      return span;
    }
    function renderTable() {
      const rows = filteredRows();
      document.getElementById("resultsCount").textContent = `${rows.length} matching findings`;
      const wrap = document.getElementById("tableWrap");
      if (!rows.length) {
        wrap.innerHTML = '<div class="panel muted">No findings match the current filters.</div>';
        return;
      }
      const table = document.createElement("table");
      table.innerHTML = `
        <thead>
          <tr>
            <th>Status</th>
            <th>Asset</th>
            <th>Source file</th>
            <th>Reference</th>
            <th>Count</th>
          </tr>
        </thead>
      `;
      const tbody = document.createElement("tbody");
      rows.forEach((row) => {
        const tr = document.createElement("tr");
        const status = document.createElement("td");
        status.appendChild(
          badge(
            row.kind === "missing_reference" ? "Missing reference" : "Unreferenced upload",
            row.kind === "missing_reference" ? "critical" : "warning"
          )
        );
        const asset = document.createElement("td");
        asset.className = "mono";
        asset.textContent = row.asset_path;
        const source = document.createElement("td");
        source.className = "mono";
        source.textContent = row.source_file || "-";
        const ref = document.createElement("td");
        ref.className = "mono";
        ref.textContent = row.reference_url || "-";
        const count = document.createElement("td");
        count.textContent = String(row.count);
        tr.append(status, asset, source, ref, count);
        tbody.appendChild(tr);
      });
      table.appendChild(tbody);
      wrap.innerHTML = "";
      wrap.appendChild(table);
    }
    document.getElementById("searchInput").addEventListener("input", (event) => {
      state.query = event.target.value;
      renderTable();
    });
    document.getElementById("viewSelect").addEventListener("change", (event) => {
      state.view = event.target.value;
      renderQuickFilters();
      renderTable();
    });
    document.getElementById("sortSelect").addEventListener("change", (event) => {
      state.sort = event.target.value;
      renderTable();
    });
    document.getElementById("themeToggle").addEventListener("click", () => {
      const current = document.documentElement.getAttribute("data-theme") === "dark" ? "dark" : "light";
      setTheme(current === "dark" ? "light" : "dark");
    });
    initTheme();
    renderSummary();
    renderQuickFilters();
    renderTable();
  </script>
</body>
</html>
"""


class AssetReferenceParser(HTMLParser):
    """Extract internal-looking asset references from HTML."""

    REFERENCE_ATTRS = {
        "href",
        "poster",
        "src",
        "srcset",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.references: list[tuple[str, str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for attr_name, raw_value in attrs:
            if raw_value is None:
                continue

            attr_name = attr_name.lower()
            if attr_name in self.REFERENCE_ATTRS:
                if attr_name == "srcset":
                    for candidate in extract_srcset_urls(raw_value):
                        self.references.append((tag, attr_name, candidate))
                else:
                    self.references.append((tag, attr_name, raw_value))
            elif attr_name == "style":
                for candidate in extract_css_urls(raw_value):
                    self.references.append((tag, attr_name, candidate))


def extract_srcset_urls(value: str) -> list[str]:
    urls: list[str] = []
    for item in value.split(","):
        candidate = item.strip()
        if not candidate:
            continue
        urls.append(candidate.split()[0])
    return urls


def extract_css_urls(value: str) -> list[str]:
    urls: list[str] = []
    for match in CSS_URL_RE.finditer(value):
        candidate = match.group(1).strip().strip("'").strip('"')
        if candidate:
            urls.append(candidate)
    return urls


def is_internal_asset_path(path: str) -> bool:
    suffix = PurePosixPath(path).suffix.lower()
    if suffix in ASSET_EXTENSIONS:
        return True
    return any(path.startswith(root) for root in UPLOAD_ROOTS)


def normalize_reference_url(raw_url: str, *, source_file: Path, public_dir: Path) -> str | None:
    raw = raw_url.strip()
    if not raw or raw.startswith("#"):
        return None
    lowered = raw.lower()
    if lowered.startswith(("data:", "javascript:", "mailto:", "tel:")):
        return None

    parsed = urlparse(raw)
    if parsed.scheme and parsed.scheme not in {"http", "https"}:
        return None

    if parsed.netloc and parsed.hostname and parsed.hostname.lower() not in ALLOWED_DOMAINS:
        return None

    path = parsed.path or ""
    if parsed.netloc:
        normalized_path = posixpath.normpath(unquote(path if path.startswith("/") else f"/{path}"))
    elif raw.startswith("//"):
        if parsed.hostname and parsed.hostname.lower() in ALLOWED_DOMAINS:
            normalized_path = posixpath.normpath(unquote(path if path.startswith("/") else f"/{path}"))
        else:
            return None
    elif raw.startswith("/"):
        normalized_path = posixpath.normpath(unquote(raw.split("?", 1)[0].split("#", 1)[0]))
    else:
        source_dir = source_file.relative_to(public_dir).parent.as_posix()
        normalized_path = posixpath.normpath(
            unquote(f"/{source_dir}/{raw.split('?', 1)[0].split('#', 1)[0]}")
        )

    if not normalized_path.startswith("/"):
        normalized_path = f"/{normalized_path}"

    if normalized_path == "/livereload.js":
        return None

    if not is_internal_asset_path(normalized_path):
        return None

    return normalized_path


def public_path_for_asset(asset_path: str, public_dir: Path) -> Path:
    return public_dir / asset_path.lstrip("/")


def public_url_for_file(public_dir: Path, file_path: Path) -> str:
    return f"/{file_path.relative_to(public_dir).as_posix()}"


def gather_references(public_dir: Path) -> list[dict[str, str]]:
    references: list[dict[str, str]] = []

    for html_file in sorted(public_dir.rglob("*.html")):
        parser = AssetReferenceParser()
        parser.feed(html_file.read_text(encoding="utf-8", errors="replace"))
        parser.close()

        for tag, attr_name, raw_url in parser.references:
            normalized = normalize_reference_url(raw_url, source_file=html_file, public_dir=public_dir)
            if normalized is None:
                continue
            references.append(
                {
                    "source_file": html_file.relative_to(public_dir).as_posix(),
                    "source_type": "html",
                    "tag": tag,
                    "attribute": attr_name,
                    "raw_url": raw_url,
                    "asset_path": normalized,
                }
            )

    for css_file in sorted(public_dir.rglob("*.css")):
        css_text = css_file.read_text(encoding="utf-8", errors="replace")
        for raw_url in extract_css_urls(css_text):
            normalized = normalize_reference_url(raw_url, source_file=css_file, public_dir=public_dir)
            if normalized is None:
                continue
            references.append(
                {
                    "source_file": css_file.relative_to(public_dir).as_posix(),
                    "source_type": "css",
                    "tag": "css",
                    "attribute": "url()",
                    "raw_url": raw_url,
                    "asset_path": normalized,
                }
            )

    return references


def uploaded_files(public_dir: Path) -> list[str]:
    found: list[str] = []
    for root in UPLOAD_ROOTS:
        candidate_root = public_dir / root.lstrip("/")
        if not candidate_root.exists():
            continue
        for file_path in candidate_root.rglob("*"):
            if file_path.is_file():
                found.append(public_url_for_file(public_dir, file_path))
    return sorted(set(found))


def audit_assets(public_dir: Path) -> dict[str, object]:
    references = gather_references(public_dir)
    upload_set = set(uploaded_files(public_dir))

    missing_reference_counter: Counter[tuple[str, str, str]] = Counter()
    referenced_assets: set[str] = set()
    referenced_uploads: set[str] = set()

    for reference in references:
        asset_path = reference["asset_path"]
        referenced_assets.add(asset_path)
        if asset_path in upload_set:
            referenced_uploads.add(asset_path)

        if not public_path_for_asset(asset_path, public_dir).exists():
            missing_reference_counter[(asset_path, reference["source_file"], reference["raw_url"])] += 1

    missing_reference_rows = [
        {
            "kind": "missing_reference",
            "severity": 2,
            "asset_path": asset_path,
            "source_file": source_file,
            "reference_url": raw_url,
            "count": count,
            "search_text": " ".join((asset_path, source_file, raw_url)).lower(),
        }
        for (asset_path, source_file, raw_url), count in sorted(missing_reference_counter.items())
    ]

    unreferenced_upload_rows = [
        {
            "kind": "unreferenced_upload",
            "severity": 1,
            "asset_path": asset_path,
            "source_file": "",
            "reference_url": "",
            "count": 1,
            "search_text": asset_path.lower(),
        }
        for asset_path in sorted(upload_set - referenced_uploads)
    ]

    summary = {
        "scanned_html_files": len(list(public_dir.rglob("*.html"))),
        "scanned_css_files": len(list(public_dir.rglob("*.css"))),
        "total_asset_references": len(references),
        "unique_asset_references": len(referenced_assets),
        "missing_reference_count": len(missing_reference_rows),
        "total_uploaded_files": len(upload_set),
        "referenced_uploaded_files": len(referenced_uploads),
        "unreferenced_upload_count": len(unreferenced_upload_rows),
    }

    findings = missing_reference_rows + unreferenced_upload_rows

    return {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "public_dir": str(public_dir),
        "upload_roots": list(UPLOAD_ROOTS),
        "summary": summary,
        "references": references,
        "missing_references": missing_reference_rows,
        "unreferenced_uploads": unreferenced_upload_rows,
        "findings": findings,
    }


def derive_html_output_path(json_report_path: Path) -> Path:
    return json_report_path.with_suffix(".html") if json_report_path.suffix.lower() == ".json" else Path(
        f"{json_report_path}.html"
    )


def build_view_model(report: dict[str, object], report_label: str) -> dict[str, object]:
    summary = report["summary"]
    return {
        "report_label": report_label,
        "summary": summary,
        "summary_cards": [
            {"label": "HTML files", "value": f"{summary['scanned_html_files']:,}"},
            {"label": "CSS files", "value": f"{summary['scanned_css_files']:,}"},
            {"label": "Asset references", "value": f"{summary['total_asset_references']:,}"},
            {"label": "Unique assets", "value": f"{summary['unique_asset_references']:,}"},
            {"label": "Missing refs", "value": f"{summary['missing_reference_count']:,}"},
            {"label": "Unreferenced uploads", "value": f"{summary['unreferenced_upload_count']:,}"},
            {"label": "Uploaded files", "value": f"{summary['total_uploaded_files']:,}"},
            {"label": "Referenced uploads", "value": f"{summary['referenced_uploaded_files']:,}"},
        ],
        "findings": report["findings"],
    }


def render_html_report(report: dict[str, object], *, json_report_path: Path, html_output_path: Path) -> None:
    view_model = build_view_model(report, json_report_path.name)
    payload = json.dumps(view_model, ensure_ascii=True, separators=(",", ":")).replace("</", "<\\/")
    html_output_path.parent.mkdir(parents=True, exist_ok=True)
    html_output_path.write_text(
        HTML_TEMPLATE.replace("__ASSET_AUDIT_DATA__", payload),
        encoding="utf-8",
    )


def write_json_report(output_path: Path, report: dict[str, object]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2, ensure_ascii=True), encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit built HTML/CSS for internal asset links and uploaded-file coverage."
    )
    parser.add_argument(
        "--public-dir",
        default="public",
        help="Path to built Hugo output.",
    )
    parser.add_argument(
        "--output",
        default="reports/static_asset_audit_report.json",
        help="JSON report output path.",
    )
    parser.add_argument(
        "--html-output",
        default="",
        help="Optional HTML report output path. Defaults to the JSON output path with a .html suffix.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    public_dir = Path(args.public_dir)
    output_path = Path(args.output)
    html_output_path = Path(args.html_output) if args.html_output else derive_html_output_path(output_path)

    if not public_dir.exists() or not public_dir.is_dir():
        raise FileNotFoundError(f"Public directory not found: {public_dir}")

    report = audit_assets(public_dir)
    write_json_report(output_path, report)
    render_html_report(report, json_report_path=output_path, html_output_path=html_output_path)

    print(
        json.dumps(
            {
                "report": str(output_path),
                "html_report": str(html_output_path),
                "summary": report["summary"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
