#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p monograph/build
(
  cd monograph
  for _ in 1 2 3; do
    lualatex -interaction=nonstopmode -halt-on-error -output-directory=build poisson_threefolds_monograph.tex >/dev/null
  done
  cp build/poisson_threefolds_monograph.pdf poisson_threefolds_monograph.pdf
)
for f in computations/check_*.py computations/p1p2/verify_*.py; do
  echo "checking: $f"
  python "$f"
done
