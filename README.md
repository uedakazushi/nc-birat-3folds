# nc-birat-3folds

**Noncommutative Birational Geometry of Threefolds** — 公開中の数学研究。

研究再開は `00-research-plan.md` から。主要結果とその仮定・未解決問題は `01-research-notes.md`、証明は `monograph/poisson_threefolds_monograph.tex` およびその入力断片にある。

研究内容：`P^3`, `P^1 × P^2`, `(P^1)^3` の Poisson 概型の既約成分、非可換射影量子化、非可換双有理変換、関数斜体とAS-有理性、blow-up と SOD。Poisson分類の新規性など未確認点が残り、公開リポジトリの定理を未査読の結果として扱う。

**最大 pencil の比較の進展（第14版）**：古典的八対象の End を二つの16次元 corner と32次元 cross に分解し、同じ Poisson 一次類を持つ二つの圏量子化の一次同型を証明した（`monograph/pencil_corner_comparison.tex`）。Segre 量子化と共通圏の高次比較・導来同値は未解決。

**研究上の具体的進展**：四次元 Sklyanin の generic quadric pencil で二つの ruling を分離する楕円二次拡大を定め、有限次元 Clifford 型代数の Brauer 類が Tsen により消えることを証明した。ただし関数斜体同型の下降・AS-有理性は未解決。任意の三次元トーリック多様体の同じ双指標による量子化は4次元量子多項式環の関数斜体を持ち、AS-有理的となる。これは既知の量子トーリック構成からの帰結であり、新規性は主張しない。対数正準 Poisson Casimir 体と、中央次数1元を持つ曲面の安定化も証明した。一般の rational 3-fold の全非可換変形に対するAS-有理性は未解決。

## Build & tests

必要環境：latexmk + LuaLaTeX + LuaTeX-ja + AMS-LaTeX、Python 3 + SymPy。GitHub Actions は使用しない。

```bash
bash reproduce.sh
```

生成される主論文PDF（Git追跡外）：`monograph/build/poisson_threefolds_monograph.pdf`。個別に組版するにはリポジトリ直下で `latexmk monograph/poisson_threefolds_monograph.tex`、中間生成物を掃除するには `latexmk -c monograph/poisson_threefolds_monograph.tex` を実行する。設定はルートの `.latexmkrc`。Python検算は `computations/`。コードの成功は数学的な全証明の機械検証を意味しない。

PDFはTeXソースから再生成できる限りGitにcommitせず、`.gitignore` で除外する。数学的内容がPDFにしかない場合に限り、その内容をTeX等の再現可能なソースへ移してから追跡を解除する。リポジトリに古いZIPや変更履歴、TeXの中間ファイルを保存しない。Git履歴は過去版を復元するためではなく共同研究の変更管理のために使用する。
