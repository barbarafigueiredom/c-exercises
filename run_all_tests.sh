#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD_DIR="${ROOT_DIR}/.build"

mkdir -p "${BUILD_DIR}"

for source_file in "${ROOT_DIR}"/exercises/*/solution.c; do
  exercise_dir="$(dirname "${source_file}")"
  exercise_name="$(basename "${exercise_dir}")"
  binary_path="${BUILD_DIR}/${exercise_name}"

  echo "== ${exercise_name} =="
  gcc -Wall -Wextra -std=c11 "${source_file}" -o "${binary_path}"
  "${binary_path}" --test
done
