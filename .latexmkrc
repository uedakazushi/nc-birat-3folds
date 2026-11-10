# Run from the repository root:
#   latexmk monograph/poisson_threefolds_monograph.tex
#   latexmk -c monograph/poisson_threefolds_monograph.tex
# Change to the source directory so relative \input files resolve.
$pdf_mode = 4;
$do_cd = 1;
$out_dir = 'build';
$lualatex = 'lualatex -interaction=nonstopmode -file-line-error -halt-on-error %O %S';
$max_repeat = 5;
