# 研究方針　非可換三次元多様体の双有理幾何と非可換有理性

2026年11月10日（日本標準時）・現行第14版（最大 pencil の一次 corner 比較）

## 目標と達成基準

再開時は本ファイルを最初に読む。対象は複素数上の X3=P3、X12=P1×P2、X111=(P1)^3 であり、成分は自己同型群とスカラー倍で割る前の Poisson 概型の既約成分を指す。

各成分の一般元について、古典的ファイバーと一次 Poisson 括弧を固定した代数的量子化を構成し、その非可換関数体の同型、不変量、共通 blow-up、contraction、および SOD を決定する。高次の量子化係数は比較に適合するよう選ぶ。具体的に選んだ量子化の同型と、任意の量子化を分類する問題では、それぞれ仮定を指定する。

主要な達成基準は、有限表示と平坦性を持つ射影斉次環、次数零分数体の同型、半古典極限の同定を同時に与えることである。blow-up による比較では、中心と例外対象、fully faithful functor、generic localization との両立性まで指定する。元の偏極を持つ射影模型への延長が未完成の場合は、有理量子化として明記する。

## 現行版と再開の入口

現在有効な公表用原稿は **`monograph/poisson_threefolds_monograph.tex`** を入口とする1冊だけである。PDFは `latexmk` により `monograph/build/poisson_threefolds_monograph.pdf` に再生成し、Gitでは追跡しない。2026年11月10日の現行第14版（最大 pencil の一次 corner 比較）。旧版の参照を前提とせず、必要なソース・証明・実装・文献を同梱した。

研究の理解と再開に必要な情報は、この研究方針、`01-research-notes.md`、モノグラフ、依存TeX断片、計算コードに整理した。量子化の存在結果もモノグラフ前半に統合しているため、別の独立した量子化原稿は不要である。

**直接証明・拡張した結果**：任意の有限積 $X=\prod_i\mathbb P^{n_i}$ と Poisson $\pi$ について、有限型滑らかな曲線上の有限階数 tilting 代数族が存在し、任意の指定有限 jet を代数化できる。Van den Bergh の formality、tilting の変形理論、Artin 近似に依存（`restored_finite_products.tex`）。中央正則列 $(s,t)$ の Rees 環と随伴次数環の表示を直接証明した。指定した perfect な制限 bimodule から categorical gluing を作り、滑らかな余次元2の可換 blow-up の圏と同型になることを証明した（`restored_rees_gluing.tex`）。**Rees のアフィン相対 Proj と categorical gluing の同値は `central_pencil_basechange.tex` で証明。元の非可換射影圏への導来局所化・降下は未証明。**

**条件付きの圏復元**：反標準自己同値がある noetherian heart 上で t-exact で、Artin--Zhang の ample pair 条件と bounded derived comparison が成り立つとき、反標準環の qgr から共通圏を復元できる。無条件で主張することはできず、infinitely-near 二点の可換 weak del Pezzo における $(-2)$ 曲線の収縮を障害として記した（`restored_anticanonical_criterion.tex`）。五個の section module の full dg Hom と生成性の同定は今後の課題。可換二点 blow-up では、相異なる二点なら $-K$ ample、infinitely-near なら $(-2)$ 曲線を収縮する。両場合で $h^0(-nK)=1+7n(n+1)/2$ は一致するため、Hilbert 関数だけでは ample 性を判定できない（`central_pencil_basechange.tex`）。

**確認済みの一次資料**：Mori--Ueyama--Wu arXiv:2606.24606 定理1.3／5.17 は smooth な central Sklyanin quadric の standardness。De Deyn arXiv:2606.05137v2 定理1.1 は標数零の order の stacky Azumaya 解消。両者の適用範囲は `restored_literature_scope.tex` に整理した。

## 主要な到達点と主張の状態

### 成分分類と古典的幾何

- X12 は九成分。アフィン次元は10が一つ、11が四つ、12が三つ、14が一つ。Riccati 成分の生成点の局所環は長さ2、他は長さ1。モノグラフの `classification_p1p2.tex` に正規形、網羅性、次元、相異性、生成点の構造を全て記載した。三次曲線の全型に対する場合分けと Riccati のモノドロミー論証を読み直し、二次障害の exact certificate を本文に明示した。
- X111 は八成分。次元13が一つ、10が三つ、9が四つで、全成分は生成点で被約。`classification_cube.tex` に全証明がある。判別式条件、非半単純な symplectic 標準形、非一致判別式の階数2の場合を点検した。Jacobi 行列の小行列式を本文の有限体証明書で示す。
- X111 の最大成分の射影化は Gr(2,8)、順序付き因子の射影 GIT 商は P(1,2,2,3)。滑らかな (111) del Pezzo 因子の任意の Poisson 構造は一意に延長する。X12 の固定 (1,2) 因子では延長可能切断が4次元 Segre 錐で延長一意、固定 (1,1) 因子では全14の marked cubic 型の延長ファイバーを記述する。
- `birational_factorizations.tex` と三つの `birational_*_fragment.tex` に楕円基本変換、P3 の二次曲面 pencil、平面と quadric の曲面リンク、対数型、トーラス型の共通 Poisson blow-up の証明がある。曲線中心では π|C=0、点中心ではさらに一次項が Euler ベクトル場と定係数ベクトル場の外積となる条件が必要である。

これらは本文に証明を持ち、主要な場合分けと線形代数は原稿上で点検済みである。計算証明書は現行コードによる厳密計算で照合した。成分の全交叉、embedded associated primes、境界全体の局所環は未決定である。全証明の形式的機械検証は行っていない。分類定理の新規性・優先関係は未確認である。

### 非可換射影模型と関数体

- X12 の七成分は log-canonical 関数体に帰着する。残る二つは垂直楕円型と Riccati 微分 Ore 型。有理逆写像と係数を本文で証明し、記号計算で照合した。
- P3 の一般 L(1,1,2) と X12 の一般 line–conic 型には共通の量子トーラス分数体を持つ射影量子化がある。四次元 AS-regular Ore 環 A_g と対角環 C_pq、および w_g=w_1+(1−g(u))v^{-1} を用いる。
- X111 の一般の対数型は GWA quadric と Ore 型 P1 束で量子化できる。有限次元 Clifford 代数、Orlov の分解、P1 束の補題から各幾何学的ファイバーの dg smooth properness を得る。分数体は一つの交換係数が1の量子トーラスとなる。
- 垂直 X12 と X111 の二因子型には、楕円曲線上の二点を指定する曲面リンクに両立する射影量子化を構成した。Presotto の相対比較に加え、二点 gluing から相対共通圏と二つの SOD を構成し、通常の斉次 quadric 環を復元した。両端点の Hilbert 階数は (n+1)binom(n+2,2) と (n+1)^3。共通圏からの局所化で同じ斜体 D(u) を得る。反標準 orbit 環は平面の二点 blow-up 部分環へ同定した。section functor による共通圏の復元には coherent heart の比較が残る。
- X111 の最大 pencil 成分の一般元にも、元の O(1,1,1) 偏極の通常の斉次環による量子化を構成した。`nc_pencil_projective.tex` の定理 `pencil:thm:native-segre` は、Rains の次数六 filtered deformation の相対 ruling から八生成元・37二次関係式の族を与える。二つの中央元 s,t は正則列で、各次数の階数は (n+1)^3。全次数の PBW 性と任意の基底変換を一つの加群同型で証明した。各幾何学的ファイバーは noetherian Koszul domain。無限位数の楕円平行移動では射影分数斜体の中心は k(t/s)。これにより X111 の八成分すべての一般元に Segre 偏極付き代数的量子化が得られる。
- Riccati 型は根の Möbius 正規化と斉次化により、P3 の S(2,3) 内の特殊族の AS-regular 環と同じ射影分数体を持つ。元の X12 偏極を保つ射影模型との比較は残る。
- Riccati には非零の定数 log-bracket が存在せず、選んだ微分 Ore 量子化の Alev–Dumas 不変量は自明。非自明な量子トーラスとの同型を排除する。Poisson log-coefficient の整数加法群も不変量となる。
- P3 の一般 E(3) は中心変数一つを持つ Weyl 分数体となり、垂直型の三重直線退化に対応する。
- 四次元 Sklyanin pencil は、中心部分体 C(u) の有限拡大後、三次元 Sklyanin 曲面の関数体と比較できる。C(u) 上への下降は未解決。

直接計算の証明はモノグラフにある。AS 正則性、曲面双有理定理、Clifford 判定は記載した一次文献に依存する。無限位数や Q 線形独立性の条件を用いる結果では、その条件を複素閉点の Zariski 開条件として扱わない。

**最大 pencil の比較に関する今回の直接証明**：`pencil_corner_comparison.tex` で、古典的な八対象の endomorphism algebra を二つの16次元 corner と32次元 cross bimodule に三角分解した。`s=xa+b,t=xc+d` の共通曲面 Poisson 類は `D=bc-ad` であり、HH²(X111)=27 のうち両 corner への共通制限が9次元、残る混合部分が18次元であることを証明した。`restored_finite_products.tex` の一般 tilting 量子化と `nc_pencil_common.tex` の共通圏量子化は、標識を合わせると双対数上で同型となる。ただしこれは Segre 斉次環と共通圏の高次同型ではない。次に Segre 側の八対象、corner 同型、cross の左右作用を高次まで比較する。

### blow-up と SOD

- VdB の曲面一点 blow-up の SOD は既知。dg-enhanced admissible SOD と Perf(P1) の積により、曲線 p×P1 を中心とする三次元積模型の SOD を得る。この tensor 命題は本文で証明した。
- トーラス型の三模型を同じ双指標で変形すると、全ての古典的 blow-up 列が単項式二側イデアルの Rees 環に持ち上がる。`nc_toric_blowup.tex` に全重み Hom の twist、非同変圏の生成性、Orlov 型 SOD、長さ24の共通 exceptional collection、共通量子トーラス分数体の証明がある。q の無限位数仮定は用いない。
- 楕円型の相対共通圏は `nc_relative_blowup.tex` に構成した。階数15の平面 Beilinson 代数へ二点 evaluation を加えた階数23の directed 代数 B を用いる。基底の etale 近傍で四対象の quadric 成分と第三の例外対象を持ち上げ、二周期的な通常の斉次環を再構成する。全 helix の Hom の base change と二次の正規元 g を明記した。`nc_relative_generic.tex` の付値環上の消去と同じ kernel を持つ二つの Verdier 商により共通斜体を証明する。Perf(P1) との積は階数92・十頂点の代数で表示され、二つの SOD に Perf(P1) が二個と一個現れる。
- `nc_quadric_blowup.tex` は cubic Z 表示と中央正規元を持つ quadric の一点 blow-up を切断環と導来同値で比較する。一点上の半単純 restriction に対する消滅補題が核心。固定された無限位数の Sklyanin pencil の非空開集合には、spinor の hereditary fork を用いて同じ証明を適用できる。RSS2023 Thm7.3 の共通環に例外成分二個と一個の SOD、および Perf(P1) 積の SOD を与える。固定ファイバーでのこの環論的同定と、上の古典点を含む相対構成には、それぞれ記載した仮定を用いる。
- 最大 pencil の楕円中心の共通圏は `nc_pencil_common.tex` に構成した。Perf(P1)⊗C_Q と固定 Perf(E) をグラフ ℓ:E→P1 に沿って gluing し、二回の mutation で三重積の量子化と第二の Perf(E) を取り出す。三重積側の有限 directed 代数は階数64、corner は16、cross bimodule は32。両端点の一次 Poisson 類と共通 Verdier quotient Perf(D(u)) を同定した。次数二の被覆の分岐点も構成の範囲に含む。Segre 斉次環とこの有限代数の導来同値・同じ分数斜体を与えるという比較は残る。
- `nc_anticanonical_ring.tex` は階数23の共通圏の反標準 orbit 環を計算する。Serre 三角と spherical restriction、楕円曲線上の正次数消滅により、同じ基底上で全次数の階数1+7n(n+1)/2を得る。中央正則元 g と楕円商 B(E,L3(−τ^{-1}p−τ^{-1}q),τ) を同定し、八生成元・42二次関係式の左右 noetherian な環を得た。generic τ の無限位数を仮定して RSS の Hilbert 定理を使い、相対部分環 R⟨V⟩⊂S^(3) と同定した。各ファイバーの単射性も証明した。ここから section functor で共通圏全体を復元するための heart と ample 性の照合は残る。
- Belmans–Presotto の order blow-up 定理は任意次元。locally free finite-global-dimension order、非分岐な smooth centre、中心上の split 条件を必要とする。三次元で曲線中心は Db(C) 一個、点中心は二個の例外対象となる。標準 Orlov 規約による twist を本文に採用し、原著の符号上の注意を研究ノートに記した。
- Mori–Okawa–Ueda の非可換 P1 束の SOD は曲面を底とする三次元にも適用できる。Kuznetsov–Lunts、Kaledin–Kuznetsov、naive blow-up の適用範囲も主論文に記した。
- 関数斜体は零ランク対象による Serre 商または Ore/Verdier 局所化で回復する。SOD の各成分と個数だけからは回復できない。量子平面 S_q の同じ三項強例外集と、q=1／q≠1 の異なる関数斜体を本文で証明した。

相対共通圏、反標準環、最大 pencil の斉次環と共通圏について証明を記載した。新しい三節は、相対 ruling の下降、全次数の平坦性、Serre と mutation の向き、中心性、局所化および一次類を独立に読み合わせた。有限検算の範囲は研究ノートに記す。先行定理は一次本文の主張と適用条件を確認した。長篇文献の全証明を独立に再検証したという扱いはしない。Rains 2025 の定理15.9には共通反復 blow-up の仮定がある。一般の関数斜体同型から三次元の非可換 blow-up 列を得る主張、および今回の構成の新規性の確定は残る。

### 全方向の圏量子化

モノグラフ前半の存在定理は全 Poisson 方向に有限型基底上の smooth proper dg 圏を与える。`restored_finite_products.tex` では任意の射影空間の有限積に拡張し、任意の指定有限 jet を Artin 近似で代数化する。矩形 tilting 代数の階数は積の二項係数公式、幾何学的ファイバーの大域次元上界は $d=\sum n_i$。偏極付きの非可換 `Proj` の存在までは主張しない。


## 非可換有理性をめぐる新しい研究方針

現行の公開GitHubリポジトリは **`uedakazushi/nc-birat-3folds`**（`main` を正本）である。`nc-rational-threefolds` は研究で問うべき有理性を既に前提にしてしまう。Poisson 分類を超え、AS-regular 三空間、曲線中心の blow-up と SOD、分数斜体の不変量を統合する。

`nc_rationality.tex` で「AS-有理性」を、4次元 AS-regular domain B、Hilbert 級数 (1-z)^(-4) と D(A) ≅ D(B) の存在条件として**定義案**にした。一般の smooth proper dg 圏には必ずしも分数斜体がないので条件の範囲を限定した。Veronese 不変性を直接証明した。量子多項式型と斉次 Weyl 型という二つの異なる非可換 P3 の分数斜体を Alev–Dumas 不変量で区別した。この命題により、非可換 P3 の関数斜体は一意ではない。

変形パラメーターと整格子を保存する同型なら半古典極限は Poisson 双有理同型を与えることを証明した。逆向きは一般には知られない。合理的な研究問題は「古典的に rational な三次元の integral quantization が何らかの非可換 P3 の関数斜体を持つか」であり、**未解決**。特に垂直楕円型から R(2,2) への中心体上の下降、三重積最大 pencil の Segre 環から階数64の共通圏への比較が優先。Poisson 同型を誘導しない任意の斜体同型と、半古典極限に整合する同型を区別する。

### Sklyanin generic quadric の ruling 下降：確立した範囲

`sklyanin_ruling_descent.tex` は、Smith--Van den Bergh (2013) 第5・7・10節の一次本文を確認し、次の帰結を証明する。

- 4次元 Sklyanin 代数の独立な中央二次元 $\Omega_0,\Omega_1$ に対し $u=\Omega_1/\Omega_0$、$K=\mathbb C(u)$ とする。中央な同次数元を持つ一般的な Ore domain について、$\Omega_0\ne0$ チャートの generic pencil quotient の次数零分数体はもとの $D(S)$ と一致する。これは中央局所化と Veronese 不変性による直接証明であり、商全体の smoothness は仮定しない。
- 二つの ruling の標識は $z$ と $-z-2\tau$ であり、ruling の分離体は $K'=\mathbb C(E)$、$K=\mathbb C(E/\langle\iota\rangle)$、$\iota(z)=-z-2\tau$、拡大次数2。四つの固定点は $z+\tau\in E[2]$。Weierstrass 表示では $K'=\mathbb C(x,y)$、$y^2=x^3+ax+b$、$K=\mathbb C(x)$、Galois 元は $y\mapsto-y$。非自明な ruling のモノドロミーは残る。
- generic quadric の8次元 Clifford 型代数 $C_\eta$ は中心が $K'$ となる中心単純代数で、Tsen により $C_\eta\simeq M_2(K')$。**有限次元 Clifford Brauer 類の消滅**は確立。関数斜体の AS-有理性や特定の spinor/ruling の $K$-下降は**未証明**。
- 有限 Galois 拡大後に得た関数斜体同型は、自己同型群係数の非可換 $H^1$ cocycle が自明となることが下降の必要十分条件。今後は具体的な非可換平面との比較同型上で Galois 作用を計算する。
- **古典的注意**：共通楕円基底曲線上の定数点からの射影により、滑らかな一般のquadric は $K$-rational である。ruling の下降不可能だけから AS-有理性の否定を推論しない。

依存文献：Smith--Van den Bergh, *Noncommutative quadric surfaces* (JNCG 7 (2013), Proposition 5.3, Theorem 5.6, Proposition 10.1, Theorem 10.2), Stacks Project Tag `03RF` (Tsen--Brauer)。この観察の新規性は主張しない。コード `check_sklyanin_ruling_descent.py` は具体的な楕円曲線の分岐数と可換射影写像の式のみを有限検算する。

### 三次元トーリック型に対する証明済みのAS-有理性

`toric_as_rational.tex` に、任意の rank 3 指標格子 M と双指標 c による toric chart の twist の共通分数斜体が、中央一次生成元を持つ4次元量子多項式環 B_q の次数零分数斜体に同型であることを**直接証明**した。したがって任意の射影トーリック三次元多様体の、同じ双指標を用いた**トーリック量子化**は AS-有理的である（fan の滑らかさは不要）。これは Cirio--Landi--Szabo の既知構成に対する簡明な帰結であり、新規性を主張しない。任意の非トーリック・非双指標型変形については何も主張しない。

同節には、対数正準 Poisson 体の Casimir が厳密に Frac(C[L_lambda]) に等しいことを UFD と Newton polytope で証明した。付随して、形式量子トーラス中心の単項式は同じ整数格子で検出される。さらに3次元 AS-regular 曲面座標環 S に非零中央一次元がある場合は、中央多項式拡大 S[v] が AS-regular 4次元で D(S[v]) ≅ D(S)(w) と証明した。**一般の Sklyanin 曲面には中央一次元がないので、この十分条件を直接適用しない。** `check_toric_as_rational.py` は格子変換とHilbert級数の有限検算だけを行い、一般定理の証明ではない。

## 未解決の核心と次の着手方法

1. **最大 pencil の二構成の比較。** 新しい `pencil_corner_comparison.tex` の三角行列代数同型判定を使用し、`nc_pencil_projective.tex` の Segre 斉次環から八対象を作る。二つの16次元 corner の積を比較し、次に `pcat:kernel-bimodule` の階数32の cross bimodule の左右作用・合成を照合する。一次一致は一般 tilting 量子化と共通圏量子化に対して確立したが、Segre 側の lift と二次以降は未証明である。特定の斉次環の smooth properness、階数64の mutation 代数との導来同値、D(u) への generic localization が一致することを達成基準とする。中央 pencil と三つの次数二直線束の標識を固定する。
2. **反標準 section functor と係数。** `restored_anticanonical_criterion.tex` の定理を適用するため、有限代数 B の coherent heart 上で $S^{-1}[2]$ の t-exactness、Artin–Zhang の ample 条件、五個の section module の full dg endomorphism algebra と生成性を照合する。42二次関係式と S3 の二点 evaluation の核 V を入力にし、旧版での証明報告だけを根拠に同値を主張しない。
3. **Sklyanin pencil の下降。** `sklyanin_ruling_descent.tex` の $K' = \mathbb C(E)$ に移り、Smith--Van den Bergh の二つの spinor module の Galois 交換を明示的行列で計算する。Clifford 型代数は $M_2(K')$ に分裂済みなので、次は選んだ非可換曲面の関数斜体同型の cocycle $a_\gamma$ を生成元で計算し、非可換 $H^1$ 類の自明性を判定する。比較同型と平面の具体モデルが揃うまでは AS-有理性を断言しない。
4. **Riccati の射影比較と残る成分。** P3 の S(2,3) 内の像とファイバーを求め、元の X12 偏極を回復する ample sequence または blow-up を構成する。導分の定数体・有理第一積分・monodromy を比較する。R(1,3) の中心拡大 Sklyanin 模型と残る log-canonical 正規形の native compactification も扱う。
5. **Rees の射影降下。** `central_pencil_basechange.tex` に、$A$ の $\mathbb C[s,t]$-自由性、Rees 環の可換 blow-up からの基底変換、$\operatorname{Perf}(Y,\mathscr A)=\langle\operatorname{Perf}(D),\operatorname{Perf}(A)\rangle$ を証明した。$A$ と $D=B(E,M,\tau)$ の vertex では $\operatorname{pd} k=\infty$ なので、単なる perfect torsion による商では `qgr` を回復できない。二重次数付き導来加群圏で真の torsion 局所化を指定し、SOD の projection functors がこれと両立すること、例外成分が $\operatorname{Perf}(E)$ になることを証明する。$\operatorname{Perf}(\operatorname{qgr}A)$ の smoothness と共通斜体局所化の照合も必要。
6. **Poisson 概型の境界。** 全成分交叉、embedded associated primes、原点の深さと一般自己同型商を調べる。まず本文の正規形で成分交叉の小さなスライスを作り、既存の exact Jacobi 実装で局所イデアルを比較する。

成分分類の元の目標は主論文の全証明に統合した。最大 pencil でも元の Segre 偏極の量子化と、楕円中心の共通圏・二つの収縮・局所化を構成できた。現在はこの二構成の有限データの照合を最優先にする。同じ中心と一次括弧を持つことから、量子化の高次係数まで一致するとは限らないためである。楕円曲面の反標準環は同定でき、残る課題は section functor と coherent heart の対応である。中心体上への下降と、X12 の残る成分の native compactification も引き続き扱う。

## GitHub と Library の運用

GitHub の公開リポジトリ `https://github.com/uedakazushi/nc-birat-3folds` の `main` に、現行の研究方針・研究ノート・モノグラフのLuaLaTeXソース・検算コード・再現手順のみを置く。再生成可能なPDFは原則Gitで追跡せず、PDF固有の数学的内容があれば先にソース化する。未完成結果を含む研究中の内容も、今回のユーザー指示により**追加承諾なく直接mainへpushしてよい**。ただしpublicであることを意識し、主張の状態と検証範囲を明記する。GitHub Actions / PRを使わずローカル検証する。現行bundleの ZIP とPDFは Library にも区切りごとに保存する。Git履歴の存在は研究bundleに旧版を含めることを意味しない。

## 研究全体に共通する運営原則



1. 現状に応じて目標と方針を更新し、数学的重要性、新規性、理解、応用、正確性、実現可能性を併せて判断する。重要な変更時には理由と旧目標の既解決・未解決部分を現行方針に統合する。
2. 証明済み、仮定付き、未完、予想、計算観察を区別し、主要結果の仮定、依存、証明箇所と残課題を示す。既知の事実とこの研究の成果、記述した証明・点検した証明・計算した例を区別する。訂正時は依存する結果も直す。
3. 原稿では一次資料を調査し、Introduction で先行結果の仮定・範囲・本研究との関係を示す。未確認点と新規性の判断を明示し、識別子や参照箇所を残す。
4. 日本語 LuaLaTeX の公表用原稿は、論理的に現在の成果を組み立てる。研究価値に応じて分割・統合する。未完箇所を明記し、軽量化のために有効な証明を削らない。
5. 研究ノートには論文以外で再利用可能な計算、障害、反例、着想および再取得困難な知識を置く。実況、作業履歴や重複する証明を除く。
6. 研究再開は本方針を入口とする。最新 bundle のみで現在の達成基準・依存・優先課題・方法・再現手順が分かるようにする。
7. 方針・ノート・原稿・PDFと検証に必要な最小限のコードを一式とし、旧版・入れ子ZIP・編集履歴・生成中間物・ログを除く。内容や検証可能性を削って容量を抑えない。
8. 各 bundle と主要文書に日付・版番号を付す。区切りごとにユーザーの追加承諾を求めず ChatGPT Library に保存してよい。旧Libraryファイルを明示の指示なく削除しない。生成、検証、保存を別々に扱い、確認できた状態だけを報告する。

## 再生成と検算

必要環境は latexmk と LuaLaTeX（ltjsarticle, LuaTeX-ja, AMS-LaTeX, mathtools, mathrsfs, hyperref）、日本語フォント、Python 3、SymPy。全てのTeX入力とコードは本bundle内にあり、外部データの入力は不要。

```sh
bash reproduce.sh
```

リポジトリ直下で `latexmk monograph/poisson_threefolds_monograph.tex` を実行すれば、PDFが `monograph/build/` 以下に生成される。`bash reproduce.sh` はこの組版とPython検算を実行する。生成物は `.gitignore` により追跡しない。実際に組版・検算を実行した場合にのみ、その結果とPDFの頁数を報告する。有限計算はJacobiの階数、式の恒等性、有限次元不変量を検算するもので、本文の全証明の機械形式化ではない。これまでの原稿に書かれた高度な定理の全証明を今回独立に再検証したわけではない。上記二件の2026年一次文献は本文と定理番号を確認した。新しい構成の文献上の新規性・優先関係は未確定。
