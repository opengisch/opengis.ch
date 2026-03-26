#!/usr/bin/env bash

set -euo pipefail

root_dir="${PWD}"
tmp_dir="$(mktemp -d)"
pages=(
  "public/index.html"
  "public/de/index.html"
  "public/fr/index.html"
  "public/it/index.html"
  "public/jobs/index.html"
  "public/qgis-support/index.html"
  "public/qfield-rapidmapper/index.html"
  "public/core-values/index.html"
  "public/category/qfield/highlights/index.html"
  "public/de/category/qfield-de/highlights/index.html"
  "public/fr/category/qfield/highlights/index.html"
  "public/it/category/qfield-it/highlights/index.html"
)

cleanup() {
  rm -rf "${tmp_dir}"
}

trap cleanup EXIT

for page in "${pages[@]}"; do
  if [[ ! -f "${page}" ]]; then
    echo "Missing expected HTML file: ${page}" >&2
    exit 1
  fi

  relative_page="${page#public/}"
  config_file="${tmp_dir}/$(echo "${relative_page}" | tr '/' '_').yml"

  cat > "${config_file}" <<EOF
DirectoryPath: /work/public
FilePath: ${relative_page}
CheckExternal: false
LogLevel: 3
EOF

  docker run --rm -v "${root_dir}:/work" -v "${config_file}:/tmp/htmltest.yml:ro" wjdp/htmltest -c /tmp/htmltest.yml
done
