# nc-birat-3folds

**Noncommutative Birational Geometry of Threefolds** — 公開中の数学研究。

研究再開は `00_research_plan.md` から。主要結果とその仮定・未解決問題は `01_research_notes.md`、証明は `monograph/poisson_threefolds_monograph.tex` およびその入力断片にある。

研究内容：`P^3`, `P^1 × P^2`, `(P^1)^3` の Poisson 概型の既約成分、非可換射影量子化、非可換双有理変換、関数斜体とAS-有理性、blow-up と SOD。Poisson分類の新規性など未確認点が残り、公開リポジトリの定理を未査読の結果として扱う。

**直近の研究上の新規整理**：任意の三次元トーリック多様体の同じ双指標による量子化は4次元量子多項式環の関数斜体を持ち、AS-有理的となる。これは既知の量子トーリック構成からの帰結であり、新規性は主張しない。対数正準 Poisson Casimir 体と、中央次数1元を持つ曲面の安定化も証明した。一般の rational 3-fold の全非可換変形に対するAS-有理性は未解決。

## Build & tests

必要環境：LuaLaTeX + LuaTeX-ja + AMS-LaTeX, Python 3 + SymPy。GitHub Actions は使用しない。

```bash
bash reproduce.sh
```

主論文PDF：`monograph/poisson_threefolds_monograph.pdf`。Python検算は `computations/`。コードの成功は数学的な全証明の機械検証を意味しない。

リポジトリに古いZIPや変更履歴、TeXの中間ファイルを保存しない。Git履歴は過去版を復元するためではなく共同研究の変更管理のために使用する。
