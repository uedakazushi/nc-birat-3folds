#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

# .latexmkrc selects LuaLaTeX, changes to monograph/, and writes into build/.
# PDFs and other generated files are intentionally not tracked by Git.
latexmk monograph/poisson_threefolds_monograph.tex

for f in computations/check_*.py computations/p1p2/verify_*.py; do
  echo "checking: $f"
  python "$f"
done
