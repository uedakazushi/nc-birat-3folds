# Noncommutative Birational Geometry of Threefolds

日本語研究プロジェクト。非可換射影三次元多様体の関数斜体、Poisson構造、AS-有理性、非可換 blow-up / blow-down、semiorthogonal decomposition を研究する。

**研究再開時は `00_research_plan.md` → `01_research_notes.md` → 論文の順に読む。** 現在の主張には、証明済み・既知結果からの帰結・条件付き・未解決の区別がある。公開リポジトリだが、未検証の主張を確定した定理として引用しないこと。

## Current research

- `\mathbb P^3`, `\mathbb P^1\times\mathbb P^2`, `(\mathbb P^1)^3` の Poisson scheme と非可換双有理模型。
- 関数斜体 `Q_{gr}(A)_0` に基づく AS-rationality の定義案。
- 一般のトーリック量子化の AS-rationality（後述の基礎命題）、楕円 pencil の非可換 blow-up と SOD、中央 Rees 模型の射影化の障害。
- 非可換 `\mathbb P^3` 自身にも非同型な関数斜体がある。したがって「有理性」を一つの量子有理関数体への同型として定義しない。

## Source and reproducibility

直近の研究継続用資料は ChatGPT Library の [モノグラフ第11版および全ソースを含むZIP](https://chatgpt.com/library?file_id=libfile_fde3_f-edb7781d62488191a60a559762595419_49a37d1227488191afb5740001f38c05&account_id=personal) にある。原稿は日本語 LuaLaTeX。新しい計算・証明はリポジトリ内で独立に再現できる形へ順次移す。Libraryリンクは保有者のアクセス権限に依存するため、公開配布可能な複製とは限らない。

`AGENTS.md` を編集・研究継続の規約とする。GitHub Actions は原則使用せず、検算と組版は手元で行う。
