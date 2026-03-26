#!/usr/bin/env bash

set -euo pipefail

port="${LIGHTHOUSE_PORT:-8100}"
host="${LIGHTHOUSE_HOST:-127.0.0.1}"
base_url="http://${host}:${port}"
chrome_bin="${CHROME_BIN:-$(command -v google-chrome-stable || command -v google-chrome || command -v chromium || command -v chromium-browser || true)}"

if [[ -z "${chrome_bin}" ]]; then
  echo "Unable to find a Chrome/Chromium executable for Lighthouse CI." >&2
  exit 1
fi

if [[ ! -f "public/index.html" ]]; then
  echo "Missing expected Hugo output under public/. Run 'hugo --environment development' first." >&2
  exit 1
fi

server_log="$(mktemp)"
python -m http.server "${port}" --bind "${host}" --directory public >"${server_log}" 2>&1 &
server_pid=$!

cleanup() {
  if kill -0 "${server_pid}" >/dev/null 2>&1; then
    kill "${server_pid}" >/dev/null 2>&1 || true
    wait "${server_pid}" >/dev/null 2>&1 || true
  fi
  rm -f "${server_log}"
}

trap cleanup EXIT

for _ in $(seq 1 20); do
  if curl -fsS "${base_url}/" >/dev/null; then
    break
  fi
  sleep 1
done

if ! curl -fsS "${base_url}/" >/dev/null; then
  echo "Timed out waiting for local Lighthouse CI test server at ${base_url}" >&2
  exit 1
fi

LIGHTHOUSE_BASE_URL="${base_url}" CHROME_PATH="${chrome_bin}" ./node_modules/.bin/lhci autorun --config .lighthouserc.js
