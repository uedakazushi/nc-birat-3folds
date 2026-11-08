# 研究ノート　Poisson 成分・非可換関数体・射影模型

2026年11月8日（日本標準時）・現行第10版（復元・再検証）

このノートは現行原稿を補う計算、証明の依存関係、文献上の注意、未解決の構成を整理する。中心原稿は `poisson_threefolds_monograph.tex`、再開の入口は `00-research-plan.md` である。

## 主張の使用範囲

- 成分は固定した多様体上の Poisson 概型の成分を指す。自己同型群とスカラー倍による商は、明記した箇所で取る。
- 今回は指定した一次 Poisson 括弧を持つ量子化を選び、必要な高次パラメーターを対応させる。独立に選んだ任意の量子化同士の分数体同型には別の分類が必要となる。
- 「generic」の代数的な非退化条件と、平行移動の無限位数や係数の Q 線形独立性を区別する。後者を使う主張は幾何学的一般点または指定条件を満たす複素点に限る。
- 元の偏極を持つ射影量子化、別のコンパクト化、アフィン Ore 量子化、標識された分数体、smooth proper dg 圏の代数化について、本文ごとに達成している結論を指定する。
- モノグラフに X12 と X111 の分類の全証明を統合し、主要な場合分け、線形代数、モノドロミーと長さ2の論証を点検した。Riccati の余核汎関数と非零小行列式は本文にも記載した。一般文献の全証明の再検証と、計算コードで確認した恒等式・階数は区別する。

## 非可換双有理比較の要点

十分な証明は中心原稿にあるため、ここでは再開時に必要な入口を記す。

| 結果 | 証明の所在と次の使用方法 |
|---|---|
| Poisson 標識を持つ division ring | `nc_field_fragment.tex` の付値構成。h-adic valuation と剰余体の括弧を保つ同型を使う |
| 三模型のトーラス型 | `nc_toric_blowup.tex` の同じ双指標による Rees 環・Orlov 型 SOD・共通模型。整数行列 M に対し q'ij=∏q_ab^(m_ia m_jb) と高次項まで合わせる |
| P1×P2 の七成分の log-canonical 正規化 | `nc_p1p2_fragment.tex`。有理逆写像と変換後の係数が揃っている |
| 一般 L(1,1,2) と line–conic の射影模型 | 同ファイルの A_g、C_pq。Ω=wv+g(u) と w_g=w_1+(1−g(u))v⁻¹ を用いる |
| 三重積の対数型 | `nc_cube_log_fragment.tex`。L の固有値 ±ν、q=(1−hν)/(1+hν)、p=1+hκ により上の分数体へ移す |
| 楕円曲面リンク | `nc_surface_fragment.tex`。D→checkS の Z-代数包含と index0 corner を使う。選んだ even-periodic Q を通常の S の graded 部分代数と同一視しない |
| 楕円相対共通圏 | `nc_relative_blowup.tex` と `nc_relative_generic.tex`。二点 evaluation、例外集の etale 持上げ、quadric の再構成、同じ kernel を持つ generic quotient を順に使う |
| 最大 pencil の Segre 射影環 | `nc_pencil_projective.tex`。Rains の P1 ruling、二重中央拡大、全次数 PBW、一次括弧と中心を順に使う |
| 最大 pencil の楕円中心の共通圏 | `nc_pencil_common.tex`。二回の mutation、階数32の cross bimodule、両楕円成分を消す局所化を用いる |
| 共通圏の反標準環 | `nc_anticanonical_ring.tex`。Serre 三角、orbit 上の中心性、二点 evaluation 部分環への同定 |
| 固定 Sklyanin quadric の共通環 | `nc_quadric_blowup.tex`。一点消滅補題で VdB の δ の核を消し、RSS 共通環の二つの SOD を得る |
| Riccati の P3 模型 | `nc_riccati_p3_fragment.tex`。左除算 η=(x−r3)⁻¹y、二次導分、divergence zero の斉次化、normal な Z を局所化する |
| E(3) | `nc_p3_fragment.tex`。p,q が可換となる CGG チャートから r=q/p,c=q²/p³,P=r⁻¹s で Weyl 分数体へ移す |
| Sklyanin pencil | 同ファイル。u=Ω1/Ω2 を保って C(u) の有限拡大上で比較する。原体への下降が課題 |

### 不変量と既存の方法の障害

log-canonical 関数体の係数が生成する整数加法群 Γ は Poisson 双有理不変量である。係数を Q 線形独立に取ると、三係数型・二係数型・一係数型は Γ の階数で区別できる。成分を七つまとめて log-canonical に帰着できることから、それらの全ての一般元が互いに同値とは結論しない。

Riccati の K(y) では導分が K を保ち、y の微分が次数を1下げるため、非零定数 λ について {a,b}=λab は不可能である。量子側では微分 Ore 分数体の最高次係数が乗法的で、スカラー交換子不変量 AD は自明になる。log-canonical の対数座標を探す方法は、この障害によって Riccati 型では使えない。

古典的な共通モデルの正則性には中心の条件がある。曲線中心では双ベクトル全体の消失を確認する。三重積の pencil を固定座標の曲面リンクに直接通すと混合項が中心で消えない場合がある。pencil の比を中心変数として用いる楕円基本変換は モノグラフの `birational_cube_fragment.tex`にある。量子側では非可換分数線形変換の左右の順序が重要である。

### Riccati の重み付き模型

通常の P3 模型とは別に、正規化前の全 Riccati 係数を保持する重み付き模型も使える。deg Z=deg X=deg T=1、deg Y=2 とし

    δh(Z)=0,
    δh(X)=Z³ f(X/Z),
    δh(T)=Z³ h(T/Z,X/Z),
    H=C[hbar,Z,X,T][Y;−hbar δh]

と置く。各次数は自由で Hilbert 級数は (1−s)⁻³(1−s²)⁻¹、各ファイバーは大域次元4の AS-regular 環となる。Z=1 の chart は元の Riccati Ore 代数である。古典的 qgr は重み付き射影スタック P(1,1,1,2) の連接層圏で、粗モジュライも同じ重みの射影空間となる。根の選択を避けて全係数を一つの族として扱う場合に使える。通常の P3 への構成は中心原稿に十分な証明がある。

### 射影環の滑らかさと族の範囲

GWA quadric の滑らかさは、AS-regular Ore ambient の central quadric quotient としての表示から得る。有限次元 Clifford 代数 C(G) は階数8で、古典点の M2(C)⊕M2(C) の trace pairing の非退化性を開条件として使う。Orlov の半直交分解と MCM–Clifford の同値から各幾何学的ファイバーの dg smooth properness が従う。これを基底環そのものの上の exceptional collection として主張するには相対的な分裂の追加検証が必要である。

Ore 型 P1 束の対角環は直接扱える。PBW と degree1 生成性から双次数の積が全射となり、対角抽出と誘導加群が torsion 商で逆同値になる。対角環の斉次イデアルを Ore 環へ延長し、その有限生成性を対角に戻すことで noetherian 性も得る。Ballard–Farman の通常の tensor product に対する定理を、twisted Ore 型にそのまま適用する必要はない。

## 最大 pencil の二つの量子化

証明は `nc_pencil_projective.tex` の定理 `pencil:thm:native-segre` と `nc_pencil_common.tex` の定理 `pcat:two-contractions`・`pcat:generic` にある。以下は再利用に必要な標識と未比較部分である。

### 楕円データと相対 ruling

s=xa+b、t=xc+d、D=bc−ad とし、E=(D=0) を滑らかな (2,2) 曲線とする。Lx,Ly,Lz は cube の各因子から来る次数二の直線束。行列の階数一の因子化から、pencil の比に対応する ℓ:E→P1 の直線束は M=Ly⊗Lz⊗Lx^{-1} となる。基底曲線の Segre 直線束は L_E=Lx⊗Ly⊗Lz、次数六である。

Rains の period は 3h−Σxi=L_E−6η、deg h=3、deg xi=1。yi=xi−h とすると A2 は yi を置換し、A1 は h↦L_E−6η−h と作用する。h=h0−3η、xi=xi0−η が Weyl-equivariant な相対自明化を与える。古典的 pencil の P2 座標は {−Lx,−Ly,−Lz} で固定される。自然な直線束は ruling 上で O(1) と基底からの直線束の積となる。本文では theta line bundle による実際の下降まで記した。

ℓ の分岐点 p=q では、marked smooth model は infinitely-near blow-up であり、Ep−Eq の (−2)-曲線を反標準環が収縮する。特異な次数六 pencil member と整合する。共通三次元模型の中心はグラフ E' 全体であり、分岐点でも滑らかな codimension two の中心となる。

Rains の THCR は逆 pullback の規約である。本文では B^−(E,L,τ)=B(E,L,τ^{-1}) と明記した。既存の曲面・RSS 節では正 pullback の積 f*g=f ψ^{m*}g を保つ。この差は Poisson 括弧の符号に関わる。

### 有限データと次の比較

Segre 環の表示は六つの楕円生成元と中央 s,t、24個の変形された楕円二次関係と13個の中央可換関係からなる。各 B_j の持上げを用いる S=R[s,t] 加群 N→A は全射であり、generic fiber での PBW と N の torsion-freeness によって同型となる。有限次数のチェックの範囲を越える平坦性は、この本文の証明に依存する。37関係式の一般係数の完全展開は未計算である。

共通圏からの三重積の有限代数の corner は16、cross bimodule は32、全体は64。比較すべき cross bimodule は

\[
 K(F,G)=\operatorname{Fib}\bigl[
 H^0(\mathbf P^1,\mathcal O(1))\otimes\operatorname{RHom}(F,\mathsf sG)
 \longrightarrow\operatorname{RHom}_E(\rho F,M\otimes\rho(\mathsf sG))\bigr].
\]

第二の楕円成分を消す式は W^*jF=s^{-1}ρ^L(M^{-1}F)[1]。ρ^L の像は normal elliptic divisor 上に支持される。一次 Poisson 類の比較では、h-整な局所化の像を有限自由複体の消去で V[0] に簡約し、実際の代数写像 A_R→Mat8(V) を得る。古典的な generic restriction の homological epimorphism により Hochschild 類の通常の制限へ移す。

Segre 斉次環と階数64の有限代数の導来同値、および両者の関数斜体の同定は未完である。前者の exact center が k(t/s)、後者の generic quotient が D(u) であるという結果を使い、三つの次数二直線束と cross bimodule の積を照合する。共通圏自体の HH2(B) における H1(T_B) 成分も未決定である。両端点の一次 Poisson 類は本文で同定した。

### 先行研究の位置付け

Rains, *Filtered deformations of elliptic algebras*, arXiv:2107.13540v2 (2022) の命題2.2–2.3、系2.5、定理2.12、定理3.19、命題5.1、第6節の命題6.1と式(6.13)を確認した。p.14 には filtered deformation の直線から非可換 Fano threefold を構成する方針が既に書かれている。構成された P1×P2 の族は §4 の曲面論と §6 の Weyl 下降に基づく。全 filtered deformation の網羅性は同論文の予想である。今回の具体的な標識付き構成の新規性は未確認。https://arxiv.org/abs/2107.13540

Orlov, *Smooth and proper noncommutative schemes and gluing of DG categories*, Adv.Math.302(2016),59–105 の例3.10が右側 blow-up SOD の cross bimodule を与える。定義3.4–3.5、命題3.7–3.8、命題3.22、定理3.25も確認した。相対性は perfect diagonal と有限 cone で本文中に証明した。https://arxiv.org/abs/1402.7364v5

## 共通圏の反標準環

詳細は `nc_anticanonical_ring.tex` の定理 `thm:relative-anticanonical-ring`・`thm:ac-rss-identification` にある。五対象の restriction は (O_E,N1,N2,kp,kq) である。REnd の H0 が B、H1 が B^∨ となり、θ=S[−2]→id→r^Rr の Serre 三角を得る。F=θ^{-1} とし、orbit の積は ab=F^n(a)∘b、deg b=n とする。

自然変換の自然性だけから g の中心性を結論することはできない。本文では α_Y(α_{θY}−θα_Y)=0 と Ext_E^{-1}(rF^nO,rF^{n+2}O)=0 を合わせ、orbit 上で cancellation を行って必要な可換性を証明した。この手順は他の restriction から反標準環を作る際にも使える。

K0 の計算で δ=T2−2T1+T0、F[Pp]=Pp+δ、F[O]=T0−3T1+3T2−Pp−Pq となる。restriction の ε=(ψ^{-2})^*L⊗((ψ^{-1})^*L)^{-1} が translation ψ³ を決め、商は B(E,L3(−τ^{-1}p−τ^{-1}q),τ)、τ=ψ³ となる。正次数7nの線束の H1 消滅により、同一の基底上で全次数の局所自由性を得る。

RSS 環への射は F_H j≅R_{⟨Pp,Pq⟩}jF_pl→jF_pl の反復から作る。c_{m+n}=(c_n F_pl^m)∘F_H^n(c_m) と自然性が乗法を保つ。generic τ の無限位数の下で RSS Thm5.3 の Hilbert 関数により同型となり、torsion-freeness により相対的な単射を得る。中心元を平面の次数三の中心元に合わせると、中心商の THCR の積から全ファイバーの単射性を証明できる。

具体的な42関係式は、S3 の二点 evaluation の核 V を選び、V⊗V→S6 の核を求める有限計算に帰着する。42個の係数行列の具体例は未計算である。平面の反標準関手が (3) となることには、式(S8)の cyclic potential と自己双対 Koszul 分解を用いる。

section functor から Perf(B) 全体を復元する問題では coherent heart の指定が必要である。Rains の heart での root Ep−Eq と点類の組合せは、restriction O_E(p−q)ε^m により effective となる壁を持ち得る。これらの壁は一つの Zariski 開近傍から全て除けるとは限らない。反標準類が nef にとどまる場合を含め、VdB の derived comparison と heart・構造対象・点の表示を照合する。root wall だけから導来同値の不存在を結論することもできない。

一次資料の追加参照箇所は Anno–Logvinenko, *Spherical DG-functors*, JEMS19(2017),2577–2656, Thm1.1=Thm5.1 と §2.1、Keeler, *Ample filters of invertible sheaves*, J.Algebra259(2003),243–283, Thm1.1/1.5、および2018年 corrigendum を含む arXiv v5、Bocklandt, *Graded Calabi Yau algebras of dimension 3*, JPAA212(2008),14–32, Thm4.2–4.3である。書誌と DOI はモノグラフにある。https://arxiv.org/abs/1309.5035v2

RSS の定義5.1、命題5.2、定理5.3は次数制約と無限位数を確認した。Keeler の定理は可換 noetherian 基底上の proper scheme を許し、本文の相対 THCR の noetherian 性に適用できる。https://arxiv.org/abs/math/0108068v5

## 一次文献の参照箇所と注意

中心原稿の bibliography に書誌・DOI・arXiv を集約している。重要な適用箇所を以下に記す。

- Pym, *Quantum deformations of projective three-space*, Adv. Math. 281 (2015), 1216–1241。定理1.1、命題2.9、第3節で六成分と graded 量子化を確認。表1の次元を単一の GL4 軌道の次元として使わない。https://doi.org/10.1016/j.aim.2015.06.005
- Presotto, *Symmetric noncommutative birational transformations*, JNCG 12 (2018), 733–778。刊行版の定理4.1、4.4、§4.2 を使用。arXiv v1 は番号が異なる。平面→quadric の関数体定理に無限位数を追加する必要はなく、本文で ψ³≠id と隣接直線束の非同型性を確認する。https://doi.org/10.4171/JNCG/290
- Presotto–Van den Bergh, JNCG 10 (2016), 221–244。定理1.1の表示と補題5.1・実際の構成で移動の指数が食い違うため、照合は2018年の構成から行う。正しい照合は ψ_plane³=α²、通常の一周期 cubic の移動を σ とするなら ψ_plane³=σ⁴。https://doi.org/10.4171/JNCG/232
- Rogalski–Sierra–Stafford, *Ring-theoretic blowing down II*, JNCG 17 (2023), 1045–1097。定理1.2、7.3 と Basic Facts 7.2。無限位数と smooth quadric の仮定の下で共通 blowup 環を与える。古典点を含む相対 blowup への適用は追加の構成を要する。https://doi.org/10.4171/JNCG/510
- Smith–Van den Bergh, *Noncommutative quadric surfaces*, JNCG 7 (2013), 817–856。補題5.1、命題5.2、定理5.6 の Clifford 判定を使用する。定理5.8の standardness に関する反例は Mori–Ueyama の §5.1 と付録 A.1 にある。今回の smoothness は Clifford 判定と Orlov 分解による。https://doi.org/10.4171/JNCG/136
- Mori–Ueyama, *A categorical characterization of quantum projective spaces*, JNCG 15 (2021), 489–529。§5.1、付録 A.1 の反例を刊行版で確認した。https://doi.org/10.4171/JNCG/403
- Liu–Wang–Wu, *Twisted Calabi–Yau property of Ore extensions*, JNCG 8 (2014), 587–609。定理0.2、§1.2–1.3 を positive connected graded な Ore 拡大に適用する。https://doi.org/10.4171/JNCG/165
- Orlov, arXiv:math/0503632v3。定理2.5の Gorenstein parameter 2 の分解と命題2.17の weighted stack の解釈。https://arxiv.org/abs/math/0503632
- Goodearl–Launois, BSMF 139 (2011), 1–39。命題5.2、系5.3、定理5.5 を Poisson 不変量との比較に用いる。https://doi.org/10.24033/bsmf.2598
- Goodearl–Yakimov, *Twist invariants of graded algebras*, Contemp. Math. 715 (2018), 141–170。定義3.1と命題3.3で Alev–Dumas 不変量と量子トーラスの場合を確認。https://arxiv.org/abs/1706.06957
- Van den Bergh, *Non-commutative quadrics*, IMRN 2011 (17), 3983–4026。§5.2、定義5.3.1、定理5.5.10の geometric quintuple と周期的 Z-代数を相対構成に用いる。https://doi.org/10.1093/imrn/rnq234

新しい具体化と既存文献との優先関係は未確定である。一次文献の PDF や検索結果は bundle に含めない。

一次資料確認：Mori–Ueyama–Wu, *Irreducible noncommutative quadrics*, arXiv:2606.24606, Thm1.3／Thm5.17 は non-degenerate 4D Sklyanin の smooth central quadric が standard であることを証明する。有限位数の平行移動を含むが、一般の normal quotient には適用しない。現行モノグラフ `restored_literature_scope.tex` に引用した。

## 三重積の分類に関する再開情報

### 実際の判定手順

巡回順で w=(A(y,z),B(x,z),C(x,y)) を書く。まず w・curl(w) の27係数を調べる。三頂点で判別二次形式を引いた四次式がすべて零ならモノグラフの命題 `cube:prop:res` により pencil 成分に属する。ある差が非零で全辺が非零なら、反対の辺が階数1になり、共有因子上で同一直線を持つもう一つの辺がある。同じ分類節の中心化代数の核で残る一辺を記述する。これにより全点を覆う。閉包は互いに交わるため、この手順は境界での所属成分を全て列挙するものではない。

### トーラス成分上の判別式と境界

三つの半単純ベクトル場に同一の規格化を用い、w=(a yz,b zx,c xy) とする。すると D_x=(c²−b²)x²、D_y=(a²−c²)y²、D_z=(b²−a²)z² となる（巡回する差の順序は論文の定義）。従ってこの三次元パラメーター空間では、三つの差は全て非零、ちょうど一つが零、または全て零という三通りが起こる。全係数が非零かつ三係数の二乗のうち一組だけが一致すれば、対応する対数型にも属する。全ての二乗が等しいとき pencil 成分にも入る。このスライスと交叉の scheme 構造は区別する。頂点の判別式は nilpotent なベクトル場で自動的に零になり得るので、半単純元だけの対角化から全点の分類は得られない。

### 最大成分の偏極

Gaussian 写像が捨てるただ一つの座標は階数8の交代形式の方向である。Plücker 埋め込みの割線と接線の階数は4以下なので、射影化は偏極付き Grassmann 多様体に同型である。原点を含むアフィン像の同次座標環と完全線形系の切断環を同一視してはいけない。次数1ではそれぞれ27次元と28次元である。重み付き射影空間の記述は因子に順序を付けた射影 GIT 商についてであり、さらに因子の有限置換群が作用する。

### 証明・検証の範囲

三重積の網羅性はモノグラフの `classification_cube.tex` における任意の複素点についての代数的証明による。判別式の二次式の次元、シンプレクティック標準形の非半単純部分、反対辺が階数2の場合の二つの Wronskian 恒等式を点検した。一般点の被約性は、一つの型の一点での厳密な接空間計算と既約閉集合の次元を併用する。根基的であること、原点での深さ、全交叉の重複度は未解決。数値的な既約分解や巨大な Gröbner 基底を仮定していない。


## 量子化の証明と検証の範囲

全 Poisson 方向の代数的圏量子化は`poisson_quantization`の第2節に証明した。高次 polyvector cohomology の消失、有限 directed bar 分解、基底変換に横断的な切片、hull の一意性、Artin 近似という順で依存する。既知の global formality と tilting の変形理論を使用する。原稿の証明を点検し、corner と Hilbert 行列の数値、明示的半古典式を計算でも確認した。

quiver 表示の基礎データは P1×P2 で階数60、6頂点、18矢、18二次関係式、最後のシジジー6本、三重積で階数64、8頂点、24矢、24二次関係式、最後のシジジー8本である。相対 Hochschild cochain の次数1,2,3の次元はそれぞれ (336,972,648)、(208,576,384)。次数4以降は零になる。これらは check_tilting.py で再現できる。

X111 の八成分の一般元には Segre 斉次環の代数的量子化がある。X12 の残る成分の斉次座標環の具体化を継続する。一般定理の smooth proper dg 圏の族と、個別の qgr 構成にはそれぞれ本文の仮定を用いる。モノグラフの Poisson 双有理同値を射影量子化へ持ち上げる際には、斉次代数と偏極の同定を別途検証する。

## pencil と geometric quintuple の共通データ

三重積の pencil を生成する二つの (111) 切断は、生成元の二次元空間を第四因子とする四重テンソルを定める。一般には geometric quintuple となり、基底楕円曲線と三つの次数2直線束は非可換 quadric の elliptic quadruple に一致する。GIT商 P(1,2,2,3)=P(2,4,4,6) はこの関係を反映する。`poisson_quantization`第4節と Okawa–Ueda arXiv:1403.0713 を参照する。元の Segre 偏極を持つ三次元 pencil 型の射影環は `nc_pencil_projective.tex` に構成した。`nc_pencil_common.tex` の smooth proper 圏およびその標識された分数斜体 D(u) との比較を次に行う。


## P1×P2 分類の証明と検証の入口

### 全成分の証明の依存関係

| 射影三次式または課題 | 証明箇所 | 結論と証明手段 |
|---|---|---|
| 被約既約・零 | `classification_p1p2.tex` の `p12:th:irreducible-cubic` と `p12:prop:zero-cubic` | meridian の位数3と非対数極の固有値 −1 が両立しない。Polishchuk の安定化 Lie 環の消滅を用いる。零の台は二成分 |
| 直線×滑らかな conic | 同 `p12:sec:conic-stratum` と `p12:sec:tangentgoodline` | どちらか一方は対数的。conic に接する場合は sl₂ の外積表示。残りは割線 xy=1、接線 y=x² として係数を比較 |
| 通常の三角形 | 同 `p12:sec:triangle` | 非対数極の本数 0,1,2 で toric、四因子、5次 del Pezzo 型に入る |
| 共点三直線 | 同 `p12:sec:concurrentfibers` と `p12:th:concurrent-riccati` | 三本とも非対数的なら三本の相異なるべき零方向が必要だがその線形独立性と矛盾。全て対数的な部分は固定した共点三直線上で六次元線形空間 |
| 重複する直線 | 同 `p12:th:double-good`、`p12:prop:doublebad`、`p12:prop:triple-cubic` | 単純直線での対数性で分ける。三重線では平坦性が接続行列の二次部分を強制的に消す。閉包に入れる極限では平面成分と分母払いした混合項をともに比較 |
| 四因子型 | 同 `p12:sec:four` | 分母を払った dlog(F/(UM)) + r dlog(L/M)。一般配置では Jacobian 階数22、族の階数12。例外パラメータ 0, −1, −1/2, 1, −2, ∞ |
| 共点 Riccati 成分の概型 | 同 `p12:th:concurrent-riccati` と `p12:th:double` | 非可換モノドロミーで解析近傍の台を固定し、補間で余分な一次変形を作る。階数 (21,22) の拡大行列が二次障害を証明 |
| 固定 del Pezzo | 同 `p12:th:extension5`、`p12:th:fixed8`、`p12:sec:markedfibers` | 5次では3小行列式、8次では15次元接空間ではなく15次元の線形な接する双ベクトル全体に Jacobi を課す。固定切断の14の marked cubic 軌道で正確なイデアルを比較 |

### 計算に関する注意

非零の平面三次式の係数空間はアフィン10次元。被約三次曲線での分類は、各ファイバー全体が被約スキームだという一般論ではない。共点三直線が一般の Riccati 成分の余分な一次方向は、射影ファイバーの固定方向と区別する必要がある。一次変形の射影には三つの y g(x) 方向があるのに、実際に中心を動かす方向は二つである。

固定8次 del Pezzo の存在判定は、曲面上の零因子の既約性と平面三次式の既約性を区別する。標識点が特異点なら例外曲線が零因子に現れ、法束の第一 Chern 類だけでは排除できない。平面射影の剛性で排除できる。節点と尖点の五つずつの必要係数による独立なチェックは `p1p2/verify_fixed_dp8.py` にも残した。8次の可約三次式の一般点では一意性が成り立つが、重複線や三角形では正次元または非被約のファイバーも現れる。

四因子型では二つの線形独立な対数微分から来る留数比が有理数に属さなければ、有理第一積分が存在しない。標識 (1,1) 曲面の一意性を調べるには、別の (1,1) グラフ上に dlog を引き戻すとよい。一般配置で x=L/M、g=F/(UM) と置くと、別のグラフ上の g は二次式を二つの一次式で割ったものになる。L に沿う留数から、非自明な別のグラフがありうる有限比は −2,−1,0,1 に限られる。この観察は九成分の証明には使わない。

### 独立検証に有用な別の視点

割線 L と滑らかな Q の場合で L に沿って対数的、Q に沿って非対数的なら、Q の二チャートでの留数を T(x)=c+ax+bx², S(y)=e+dy+fy² と書ける (xy=1)。[S,T−S]=T−S から T+I/2 と S+I/2 は同じ像を持つ冪等行列。正の固有線が定める P¹→P¹ の次数は高々2である。次数0は三角化された d(qt+P) 型、次数1は (1,1) pencil の二切断からの型になる。次数2なら両端で全分岐し、座標変換で (1,x²) になるが、曲率の原点での [a,d]=e−c と矛盾する。P1×P2 分類本文では係数による直接証明を採った。

### 一次文献との対応

- A. Polishchuk, *Algebraic geometry of Poisson brackets* (1997), §6 Thm 6.1, eq. (16)、§15 Prop. 15.1。https://doi.org/10.1007/BF02399197
- J. I. Cogolludo-Agustín, *Braid monodromy of algebraic curves* (2011), §2.3.2 (3a–e), p.182。三次曲線の補集合の基本群。https://doi.org/10.5802/ambp.295
- F. Loray, J. V. Pereira, F. Touzet, *Foliations with trivial canonical bundle on Fano 3-folds* (2013), §9 Thm 9.1。Picard 数1に関する射影化空間の分類。arXiv v3 の定理9.1は P3 の六成分を記す。著者サイトの旧 fano.pdf には九成分の旧記述が残るため、v3を用いる。https://arxiv.org/abs/1112.3871v3
- P. Belmans, E. Fatighenti, F. Tanturri, *Polyvector fields for Fano 3-folds* (2023), §2.2、付録。https://doi.org/10.1007/s00209-023-03261-2
- B. Pym と Gualtieri–Pym は Poisson 葉層と Poisson 加群の背景。Okumura の SNC log symplectic 定理は本例と次元・階数の仮定が異なる。書誌情報は P1×P2 分類本文にある。


## blow-up、SOD、generic localization の適用条件

モノグラフ `nc_blowups.tex` は先行定理と積模型を、`nc_quadric_blowup.tex` は具体的な切断環との比較を、`sod_function_fields.tex` は関数斜体の回復と SOD の貼合せを扱う。相対共通圏とトーリック共通模型には独立の節を置いた。本文にある証明はここで重複させない。

| 文献と参照箇所 | 継続研究で保持する条件 |
|---|---|
| Van den Bergh, *Blowing up of non-commutative smooth surfaces*, §5.1、Thm8.4.1 | 可換 Cohen–Macaulay divisor、有限 injective dimension、生成仮定。exceptional object O_e(-1) と pullback による SOD。原著と本稿で SOD の順序規約をそろえる。https://arxiv.org/abs/math/9809116 |
| RSS, *Noncommutative blowups of elliptic algebras*, Thm1.1、5.3、Prop5.4 | 中心元 g の次数1、楕円平行移動の無限位数、effective D と次数制約。section ring と VdB の blow-up 圏を比較するための ample 条件を確認する。https://arxiv.org/abs/1308.2216 |
| RSS, *Ring-theoretic blowing down I*, Thm1.4、1.5、§10 | line module の自己交点または End(J) の Hilbert 級数条件。反復環論的 blow-up で非 smooth な qgr が生じる例がある。https://doi.org/10.4171/JNCG/11-4-9 |
| Presotto, *Z²-algebras as noncommutative blow-ups*, Thm1.1、3.5 | cubic・quadratic Sklyanin の指定リンクと共通環、diagonal-like 部分 Z-代数の qgr 同値。SOD のためには VdB の射との比較を要する。https://arxiv.org/abs/1701.00413 |
| Belmans–Presotto, Thm30、Remark31、34 | X smooth、order は locally free、有限 global dimension、中心は非分岐、中心上で Mat_n(O)。三次元にも適用可能。分岐中心で pullback の global dimension が無限になる例がある。https://arxiv.org/abs/1705.06943 |
| Mori–Okawa–Ueda, Thm5.1 | X は任意次元 smooth projective、sheaf bimodule は両側 rank2。dual gluing functor が tensor E。曲面を底にする場合を検討できる。掲載誌は今回未確認。https://arxiv.org/abs/1903.06457 |
| Kuznetsov–Lunts, Thm1.4 | separated finite type、標数零。smooth schemes の圏から SOD で作る categorical resolution。https://arxiv.org/abs/1212.6170 |
| Kaledin–Kuznetsov, Def1.7、Prop1.8、(1.9) | noetherian、enough locally free sheaves。refinement parameter Nに応じ Db(Z) がN個現れる。Nは codimension−1 とは別のパラメータ。https://arxiv.org/abs/1410.7121 |
| Keeler–Rogalski–Stafford, Thm1.1 | 任意次元 ≥2、critically dense infinite orbit、σ-ample line bundle。naive blow-up は noetherian でも Ext¹(O,O) が無限次元となり properness を失う。https://arxiv.org/abs/math/0306244 |
| Rogalski, Thm1.3、6.6 | tiny simple object と Ext¹(M,P) の有限次元性により very well-closed point。中心の定義の基盤であり、smoothness と SOD はさらに確認する。https://arxiv.org/abs/1707.07052 |
| Rains 2025, Thm11.12、Cor11.13、Thm15.9 | 曲面 blow-up の SOD と K0 の分解。quasi-ruled の factorization 型結論には共通反復 blow-up の存在を仮定する。全409頁の証明の再検証はしていない。https://arxiv.org/abs/2504.16187 |
| Neeman–Ranicki, Thm0.7 | Tor消滅を伴う universal localization と perfect 圏の Verdier 商。Ore 局所化は平坦性により適用できる。原著は左加群規約なので右加群には反対環で適用する。https://arxiv.org/abs/math/0410620 |

Van den Bergh の三次元 flop と NCCR の一次文献も確認した。NCCR の定理6.6.3は三次元 terminal Gorenstein affine domain を仮定し、訂正版 arXiv:math/0211064v2を用いる。A=End_R(M) の generic algebra は Mat_r(Frac R) である。flop の derived equivalence は arXiv:math/0207170 の定理C、4.4.2にある。https://arxiv.org/abs/math/0211064

### 共通楕円環の categorical な比較の所在

RSS 2015 第5節、Definition5.1直後は T(D) が VdB の blow-up の section ring と一致すると明言する。ただし、この比較は同所で独立した証明付きのカテゴリー同値として述べられていない。VdB §9.2 は categorical blow-up と section ring の Proj を射 δ で結ぶ。Thm11.1.3 は楕円量子平面の反復 blow-up で、移動後の点が general position のとき δ が導来同値を誘導する。二点では相異なることが条件となる。

quadric 側の比較は、モノグラフの補題 `blowup:quadric-kernel` と定理 `blowup:quadric-section-equivalence` に証明した。構造層を除いた hereditary fork の制限から、長さ m=2w とファイバー次元 m≤w を同時に得る。一点上の半単純性が本質であり、二点に分かれると m1+m2≤2w となって同じ消滅は出ない。先に D^- 上で δ の核を消し、その後で cohomological dimension 1 の spectral sequence を使い Lδ* の有界性を得る順序を守る。

marked cubic Z 表示への定理には、通常の even rollup Q の central regular g∈Q2 を仮定する。相対二周期性から得る一般の g の正規性だけでは、この中心性を置き換えられない。固定された Sklyanin pencil の一般点には、Mori–Ueyama の spinor helix から同じ fork を直接構成して定理の証明を適用した。non-standard なら N⊗α*N=L となり、Pic²E 上の解は4個である。各 secant class が一つの中央 quadric を定めることを使い、有限個の pencil の元を除く。右加群表示は RSS2023 Basic Facts7.2、左版との移行は Smith–VdB §10.3 による。

系 `blowup:rss-common-sod` は、固定された無限位数パラメーターの共通環 R に二つの SOD を与える。平面側では RSS2015 Prop5.4 と VdB Thm11.1.3 を使う。二点の一般位置は相異なることであり、共通の平行移動後にも保たれる。Rees bimodule と section-ring inclusion が generic quotient の同一視を固定する。

Belmans–Raedschelders, IMRN2020(19),6042–6069 の Prop3.12 を mutation に用いた。Prop3.13/Remark3.14 の geometric square に対する追加の determinant 条件は今回の三頂点の fork には不要である。Mori–Ueyama, JNCG15(2021),489–529 の Lem5.6、5.9、5.13、5.14、Thm5.16 が standard quadric の完全直交性と helix を与える。本文の全 smooth quadric を standard とする主張には付録の反例が関係するため、generic standard 性を独立に証明した。https://doi.org/10.1093/imrn/rny192

Presotto arXiv1701.00413 は v2（2017年7月31日）、20頁、arXiv の Journal-ref は空欄。別論文 JNCG12(2018),733–778 の参考文献[10]でも2017 arXiv preprintとして引用されるため、現行書誌はpreprint表示とした。https://arxiv.org/abs/1701.00413

Van den Bergh, Abstract blowing down, Thm1.1 は coh(tilde S) と O_E(-1) から直交圏の perverse t-structure を使って coh(S) を回復する。SOD から abelian geometry を復元する際には heart の情報も保持する。https://arxiv.org/abs/math/9806046

### 相対共通圏の再利用に必要な規約

`nc_relative_blowup.tex` の B は五頂点・階数23の directed algebra。古典ファイバーの full strong collection は (O,O(H),O(2H),O_Ep,O_Eq)。右側 Orlov 表示を使う。quadric 側の五対象は (O,O(H−Ep),O(2H−Ep−Eq),O(3H−2Ep−Eq),O_Er)。全体の End の階数は29、最初の四対象の corner は24。B と同値な新しい End の階数が異なることは矛盾しない。

例外対象の Ext²=0 により形式的微分を持ち上げ、有限個の d²=0 方程式に Artin 近似を適用する。有限個の Hom 消滅と Morita counit の cone を消して、etale 近傍上の生成性を得る。全 helix の任意の Hom の base change は、四対象から相対 Serre functor で延長し、全ファイバーの AS-regular resolution を使って一斉に確認する。無限個の次数に対して基底を順番に縮小する方法は採らない。

右加群の向きは D_ij=Hom(Q_(3−j),Q_(3−i))。平面の THCR の積を f*g=f ψ^(deg f)*g とすると、restriction の line bundle は N_i=⊗_(a=1)^i ψ^(−a)*L、矢 f:T_i→T_j は ψ^(−j)*f となる。これを逆にすると反対環と Poisson 括弧の符号が混入する。quadric の G_i=N_i^∨N_(i+1) を逆順 H0=G2,H1=G1,H2=G0 にして二周期化する。

Delta=H2 H0^−1 の二分点を基底の etale 近傍で選び、alpha_0=id とする。全 helix は単一の alpha の反復で定義する。Q_n の階数は (n+1)^2。Q→THCR(E,H0 H1,alpha) の二次の核が rank1 であり、その局所生成元 g は正規 regular となる。g の中心性はこの構成では主張していない。geometric quintuple と再構成は VdB, *Non-commutative quadrics*, Thm5.2.2、Cor5.2.3、Thm5.5.10、正規元は Thm5.5.6、noetherian 性は Cor5.5.9、二周期化は Prop5.6.1、Cor5.6.2 に依存する。https://arxiv.org/abs/0807.3753

共通斜体の証明は `nc_relative_generic.tex`。h-付値環上の有限自由複体を unit pivot で消去するため、完備性は不要。第三の例外対象の古典的 generic restriction が零なら、変形後も消える。primitive な helix Hom は非零の古典的切断へ特殊化するため、全ての非零斉次射が共通斜体で可逆になる。斜体埋込みがあるだけでは全射性は出ない。二つの Verdier quotient が同じ kernel を持つことと、斜体拡大の conservative 性を合わせて同値を得る。正規元局所化 chart への projective localization は分母払いで証明し、その後 affine Ore localization に Neeman–Ranicki を使う。

Artin 近似には Stacks Tag07QZ、対象の障害理論の文献には Lowen, Comm.Algebra33(2005),3195–3223 を用いる。Belmans–Okawa–Ricolfi arXiv2002.03303 は v3(2025) を参照した。本文の etale 変形定理は smooth proper schemes を対象にしており、今回の finite directed algebra への適用は上記の直接証明で行う。SOD の非自明性が基底上で open-and-closed という一般結論は同版では予想として扱われる。https://stacks.math.columbia.edu/tag/07QZ

### トーリック Rees 構成と非同変 SOD

`nc_toric_blowup.tex` は同じ M=Z³ 上の双指標 c を全中間模型へ用いる。Cox の Pic 次数と M 重みを保持し、Cox sequence の分裂から重みを選ぶ。滑らかな最大錐の外の変数の Pic 次数は基底になり、局所化は強次数付きとなる。degree-zero charts は同じ量子トーラスの部分環なので貼合せと分裂の選択を照合できる。

twist は全 Hom に適用する。重み m の右加群写像は f^c(p_l)=c(m,l)f(p_l)、合成は g^c f^c=c(n,m)(gf)^c。指標 shift の twist と元の twist の非同変同型は p_l↦c(s,l)p_l。これにより古典的評価三角を使って全 Cox line bundles を生成する。量子 Cox 環の有限 global dimension と graded Nakayama を使い、全 coherent objects の生成性を得る。strong exceptional collection は仮定せず、最小 directed A-infinity 模型の全高次積を変形する。

局所中心 I=(x1,…,xd) に対して単項式の係数が全て単元なので R(I_c)=R(I)^c。x_i t のチャートは x_i、x_j x_i^−1、残りの座標で生成される。各段階の exceptional pieces は点なら二個の Perf(k)、曲線なら一個の Perf(P1)。共通24対象の数は4+2·4+2·6、6+2·1+2·8、8+2·2+2·6で照合する。有限位数の q も含む。

一次資料は Cirio–Landi–Szabo, Adv.Math.246(2013),33–88, §§3–4、Prop4.6、4.15、Elagin, Sb.Math.203(2012),645–676, Thm10.2、Cox, JAG4(1995),17–50, Lem2.2、Thm3.2、Prop3.3、Thm3.11。Cox v3 の訂正は今回用いる第2–3節に影響しない。量子トーリック構成と古典的同変 Orlov を出発点とする今回の非同変 SOD の新規性は未確認。https://arxiv.org/abs/1001.1242

### order 公式の twist の検証

Belmans–Presotto arXiv1705.06943v2 の印刷p.17、Thm30 の式(54)直後には、Lp* の後の成分が O_E(kE)、k=0,…,c−2 と書かれている。PDF画像でも確認した。O_E(E)=O_E(−1) の規約では、三次元の一点 blow-up に対し Ext¹(j_*O_E(−1),O)=k となり、この列の半直交性が成立しない。c=2 の曲面応用では k=0 のため問題が現れない。

モノグラフは標準 Orlov 形で、例外成分に O_E(1−c),…,O_E(−1) を掛けて Lp* の前に置く。order が中心近傍で split する局所計算により半直交性と生成性を確認できる。Lp* の後に置く表示では O_E(0),…,O_E(c−2) を用いる。引用時は生成性の定理と、この規約の補正を区別する。

### 中央 Rees と射影頂点：現在有効な障害と有限入力

- `central_pencil_basechange.tex` に証明をまとめた。次数1の中央正則列 $s,t$ を持つ $A$ は $C=k[s,t]$-次数付き自由。$A/(s,t)=D$ の斉次基底を持ち上げれば自由基底となる。このため Rees は $A\otimes_C\mathcal R_C((s,t))$ であり、チャートは $A[w]/(t-sw)$、$A[v]/(s-tv)$、例外では $D[w]$、$D[v]$。
- **証明済み（アフィン）**：$Y=\operatorname{Bl}_0\mathbb A^2$、$\mathscr A=\mathcal O_Y\otimes_C A$ に対して $\operatorname{Perf}(Y,\mathscr A)=\langle\operatorname{Perf}(D),\operatorname{Perf}(A)\rangle$。混合 Hom は $\operatorname{RHom}_D(M,N\otimes_A^{\mathbf L}D)[-1]$。可換 Orlov の $C$-線形分解を $A$-係数にし、二つのチャート上の導来加群圏を貼り合わせる。
- **未解決（射影）**：元の次数で irrelevant torsion を商にする操作は上記のアフィン SOD に対する自動的な Verdier 商ではない。$D=B(E,M,\tau)$、$\deg M=6$ に対し $H_D=(1+4z+z^2)/(1-z)^2$、$H_A=(1+4z+z^2)/(1-z)^4$。どちらも $1/H$ が Laurent 多項式にならないため、$\operatorname{pd}_D k=\operatorname{pd}_A k=\infty$。通常の torsion は perfect 圏の外にある。これは既に可換 Segre ファイバーでも起きる。
- 証明書 `check_central_rees.py` は二変数 Hilbert 級数 $H_{\mathcal R}=H_A(1-z^2w)/(1-zw)^2$ を有限次数で照合する。局所化と fully faithful functor の証明は計算コードではなく本文に置く。
- **反標準境界**：$\operatorname{Bl}_{p,q}\mathbb P^2$ で $p,q$ が相異なる proper points なら $-K$ ample、infinitely-near なら $-K$ は nef・big だが $(-2)$ 曲線を収縮。両者の反標準 Hilbert 関数は同じ $1+7n(n+1)/2$。したがって数値的な section 計算だけでは Artin--Zhang の ample 条件は検証できない。

### SOD と関数体で保持する追加データ

- qgr の finite-dimensional torsion と generic rank-zero torsion は異なる。関数斜体を回復するのは後者による Serre 商である。
- Ore affine chart の perfect 圏では、局所化先は Verdier 商の冪等完備化となる。一般 dg 圏ではこの局所化自体を指定する必要がある。
- 量子平面の三つの exceptional pieces は全て Perf(C) である。貼合せ代数の xy=qyx と、可逆化する z の矢を保持すれば quantum-plane division ring を回復する。生成元を標識しなければ q↔q^{-1} の交換があるので、qそのものの回復は主張しない。
- 関数斜体の perfect 圏は Hom が無限次元となるため、proper 圏の admissible component としての表示とは両立しない。generic quotient に移ると exceptional line bundles 同士の半直交性も通常失われる。
- 三変数 PBW 環 xy−yx=y、z central の点イデアル I=(x,y,z) は y∈I^m を全mで満たす。gr_I A=C[xbar,zbar] となるため、通常 Rees の exceptional fiber は P1。この例は中心と Rees 構成の条件を検討する際の障害として使える。

### 新しい文献の適用範囲

T. De Deyn, *A stacky resolution of singularities for orders by Azumaya algebras*, arXiv:2606.05137v2（2026年10月30日）, Thm1.1 本文確認。標数零の有限型 reduced separated scheme 上の order を smooth DM stack 上の Azumaya へ stacky blow-up によって双有理解消する。一般の qgr や中心が自明な量子分数体には直接適用できず、SOD は主定理の結論ではない。

## 現行の検証範囲と残る障害

本研究の現行版は、`poisson_threefolds_monograph.tex` とこれが読む23個のTeX入力・参考文献断片から再生成できる。第7版の二つの論文は内容を統合したためbundleには重複収録しない。旧版への参照は再開の前提としない。

- **検証された追加結果**：有限積の tilting 束・polyvector 消滅、形式的量子化を指定した有限 jet まで保つ Artin 近似、中央 Rees と随伴次数環の同型、制限 bimodule による categorical blow-up と可換 blow-up の同定（原稿の証明、および formality／Artin 近似／Orlov の引用に依存）。
- **今回組版・静的検査した内容**：LuaLaTeXを3回実行して143頁を出力し、未解決のLaTeX参照・引用は零。数式のはみ出し（overfull hbox）は検出されず、抽出した代表頁を画像で点検した。
- **今回コード実行した内容**：主ディレクトリ11本、`p1p2/verify_*.py` 9本、計20本が正常終了。これはコードに記された整数・有限体・有理数の計算に限る。
- **原稿に証明があるが今回全面再検証していない内容**：X12・X111の分類網羅性、相対gluingの生成性、Sklyaninの環論的同定、全次数PBWおよび相対SOD。その証明は現行原稿に残し、依存する外部文献は本文で引用した。証明が書かれていることと今回確かめたことを区別する。
- **未解決の核心**：最大pencilのSegre環と階数64の圏の導来同値・関数斜体同定、相対反標準section functorからのheart復元、Sklyanin pencilの中心体への下降、Riccatiの元の偏極の復元。全交叉・埋め込まれた素因子・境界の局所環も未決定。37/42二次関係式の一般係数の全展開も未実施。
- **未取得の情報**：先に生成を試みた191頁版は現在利用できず、今回の143頁版は再構成の成果であって逐語的復元ではない。その未取得版にしか記載されていない主張は現行版の証明済み結果には含めない。

注意：中央Rees環の同型だけから非可換 blow-up の導来SODは従わない。添付の既存SODの主張については、実際に使う圏・例外対象・十分な仮定を本文で確認する。非可換曲面の環論的 blow-up と categorical blow-up の比較も、特定の固定ファイバーと仮定を越えて自動的に一般化しない。

## 反標準 section functor と中央 Rees の本質的な障害

- 反標準 orbit 環の同型から $D^b(\operatorname{qgr}R)$ と有限代数模型の同値を得るには、heart 上での反標準自己同値の t-exactness、Artin–Zhang ample pair、bounded derived comparison が必要。可換の二点 blow-up が infinitely near の場合には (-2)-曲線 C に -K・C=0 であり、反標準環の Proj が C を収縮してしまう。この障害は monograph の `restored_anticanonical_criterion.tex` に整理した。
- 中央正則列に対して $\operatorname{gr}_I A=(A/I)[U,V]$ を証明済み。例外モデルの基底が E、法線方向が P1 であることは代数的に明らかになったが、Rees の射影圏と categorical gluing の同値は未証明。
- 制限 bimodule が perfect であれば、dg gluing で SOD を持つ smooth proper categorical blow-up を定義でき、可換 codim2 blow-up の Orlov 分解と一致する。これは Rees 環そのものに SOD を与えたことを意味しない。
- 相対的な五つの section module に関しては全 Hom と合成の照合を実施していない。Euler 行列・Hilbert 関数だけでは検証とならない。

## 非可換有理性の概念的整理（現行）

`nc_rationality.tex` を参照。基準斜体は一つに固定しない。明示的な AS-regular nc P3 の構造環 B について D(B)=Q_gr(B)_0 を扱う。一方で「rational な可換極限を持つ」はファイバーに依存し、単一の斜体の内在的性質ではない。量子トーラス型と Weyl 型の nc P3 の D は不変量 AD_C により分離される。

qgrA の任意の dg 圏変形には Ore division field が付随するとは限らないので、flat integral graded algebra または明示した generic localization を先に固定する。

**新しい比較問題**：斜体同型の存在（弱）と、h-adic 格子を保つ半古典整合な斜体同型（強）を区別する。後者には Poisson birationality が必要。古典 rationality だけでは P3 への正則 Poisson extension は出ず、極の解消と AS-regular なコンパクト化の両方が必要。現在の候補：量子トーラス、Weyl、Riccati、楕円 Sklyanin 斜体、中央 pencil。記載したAS-有理性はまだ一般定理・既存の確立用語ではない。

文献：Pym, *Quantum deformations of projective three-space*, Adv. Math. 281 (2015), 1216–1241, DOI 10.1016/j.aim.2015.06.005（P3の次数付きCY変形の六族。すべてのASregularの分類ではない）；Presotto–Van den Bergh, JNCG 10 (2016), 221–244, DOI 10.4171/JNCG/232（平面/quadricの斜体同型）；Rogalski–Sierra–Stafford, Adv. Math. 369 (2020), 107151, DOI 10.1016/j.aim.2020.107151（曲面の極小模型）；Goodearl–Yakimov, *Twist invariants of graded algebras*, arXiv:1706.06957（スカラー交換子不変量）。

## AS-有理性の新しい正確な十分条件

現行主論文 `toric_as_rational.tex` の定理 `thm:toric-AS-rational` と命題 `prop:toric-Poisson-center`, `prop:central-stabilization` を参照。

- 交代化が q_ij の双指標 twist の分数斜体は、x0 中央で xi xj=qij xj xi の四次元量子多項式環の次数零関数斜体と一致。fan は任意でよい。これは既知の toric cocycle twist と PBW 法の帰結であり、先行研究からの新規性を主張しない。
- Poisson center の完全な証明は k[M] のUFD、既約分数 a/b、Hamiltonian Euler derivation Di について a|Dia, b|Dib、Newton polytope の包含と Minkowski 和から a,b の各Di固有性に帰着する。支持の差は整数 kernel L_lambda。
- 中央一次元 h を持つ3D AS-regular domain S なら S[v] から D(S)(w) を得るが、楕円 Sklyanin への適用は一般にはできない。
- 上記から全ての rational 三次元多様体の全ての非可換変形のAS-有理性を結論することはできない。中央 pencil の native Segre 環と64次元代数の圏比較は未解決のまま。
- 検算コードは unimodular 変換と小範囲の Casimir 指数、Hilbert 級数だけを正確に確認する。
