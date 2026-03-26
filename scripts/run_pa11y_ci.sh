#!/usr/bin/env bash

set -euo pipefail

port="${PA11Y_PORT:-8099}"
host="${PA11Y_HOST:-127.0.0.1}"
base_url="http://${host}:${port}"
chrome_bin="${CHROME_BIN:-$(command -v google-chrome-stable || command -v google-chrome || command -v chromium || command -v chromium-browser || true)}"

if [[ -z "${chrome_bin}" ]]; then
  echo "Unable to find a Chrome/Chromium executable for pa11y-ci." >&2
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
  echo "Timed out waiting for local pa11y test server at ${base_url}" >&2
  exit 1
fi

PA11Y_BASE_URL="${base_url}" CHROME_BIN="${chrome_bin}" ./node_modules/.bin/pa11y-ci --config .pa11yci.js
