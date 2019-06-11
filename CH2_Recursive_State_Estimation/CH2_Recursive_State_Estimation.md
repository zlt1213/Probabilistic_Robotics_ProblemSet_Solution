# CH2 Recursive State Estimation

## Problem 1.

**1. Known:**

Let $f_t$ be a random virable such that:
$F_t = 0 $ represent the event that the sensor  is faulty at measurement t.
$F_t = 1 $ represent the event that the sensor  is functional at measurement t.

$P(F_t = 0) = 0.01 $
$P(F_t = 1) = 1- P(F_t = 0) = 0.99$

Let $Z_t$ represent the measurement at time t.
$ P(Z_t &lt; 1 | F_t = 0) = 1.0 $
and(uniformly distributed)
$ P(Z_t &lt; 1 | F_t = 1) = 1/3$

**2. Goal**
Solve for $P(F_9 = 0 | Z_{0:9} &lt; 1)$

**3. Answer:**
Total probability theorem:
$
\\begin{aligned}
P(Z_t &lt; 1)
&= P(Z_t &lt; 1 | F_t = 0) P(F_t = 0) + P(Z_t &lt; 1 | F_t = 1) P(F_t = 1)\\
&= 1 \\times 0.01 + 1/3 \\times 0.99\\
&= 0.34
\\end{aligned}
$

Bayes rule:
$
\\begin{aligned}
P(F_n = 0 | Z_{0:n} &lt; 1)&= P(F_n = 0 | Z_{n} &lt; 1, Z_{0:n-1} &lt; 1)\\
& = \\frac{P(Z_{n} &lt; 1 | F_n = 0, Z_{0:n-1} &lt; 1)P(F_n = 0|Z_{0:n-1} &lt; 1)}
{P(Z_{n} &lt; 1|Z_{0:n-1} &lt; 1)}
\\end{aligned}
$

Indenpendence:
$\\begin{aligned}P(Z_{n} &lt; 1|Z_{0:n-1} &lt; 1) = P(Z\_{n} &lt; 1)\\end{aligned}$

If the sensor is faulty at time $t-1$, it will also be faulty at time $t$.
$P(F_n = 0|Z_{0:n-1} &lt; 1) = P(F_{n-1} = 0|Z_{0:n-1} &lt; 1)$

thus:
$
\\begin{aligned}
P(F_n &lt; 0 | Z_{0:n} &lt; 1)
& = \\frac{P(Z_{n} &lt; 1 | F_n = 0, Z_{0:n-1} &lt; 1)P(F_n &lt; 0)}
{P(Z_{n} &lt; 1)}\\
& = \\frac{P(F_n &lt; 0)}{P(Z_{n} &lt; 1)} \\
& = \\frac{0.01}{0.34} \\
& = 0.0294117
\\end{aligned}
$

## Problem 2.

**Known**
Let $X_n$ represents the random variable which stand for the weather of Day n. Let s,c,r represent the event of sunny, cloudy and rainy.
$P(D_{n+1} = s | D_n = s ) = 0.8$
$P(D_{n+1} = s | D_n = c ) = 0.4$
$P(D_{n+1} = s | D_n = r ) = 0.2$
$P(D_{n+1} = c | D_n = s ) = 0.2$
$P(D_{n+1} = c | D_n = c ) = 0.4$
$P(D_{n+1} = c | D_n = r ) = 0.6$
$P(D_{n+1} = r | D_n = s ) = 0.0$
$P(D_{n+1} = r | D_n = c ) = 0.2$
$P(D_{n+1} = r | D_n = r ) = 0.2$

**Goal**
(a). If $P(D_1 = s) = 1.0$, get $P(D_2=c), P(D_3=c), P(D_4=r)$

(b).  Write a simulator

(c). Calculate Stationary distribution of weather.

(d). Derive closed-form soultion to calculate stationary distribution.

(e). Calcualte the entropy of the stationary distribution.

(f). Calculate with Bayes rule.

(g). What if add season to our model.

**Answer**

* * *

Goal (a)

-   Day 2

$
\\begin{aligned}
P(D_2 = c) = &P(D_2 = c|D_1 = s)P(D_1 = s) + \\
&P(D_2 = c|D_1 = c)P(D_1 = c) + \\
&P(D_2 = c|D_1 = c)P(D_1 = c)
\\end{aligned}
$

If
$P(D_1 = s) = 1$
then
$P(D_1 = c) = 0$ and $P(D_1 = r) = 0$
thus
$
P(D_2 = c) = P(D_2 = c|D_1 = s)P(D_1 = s) = 0.2
$

-   Day 3

The weather fo Day 3 depends on the weather of Day 2.

$
P(D_2 = s) = P(D_2 = s|D_1 = s)P(D_1 = s) = 0.8
$
$
P(D_2 = c) = P(D_2 = c|D_1 = s)P(D_1 = s) = 0.2
$
$
P(D_2 = r) = P(D_2 = r|D_1 = s)P(D_1 = s) = 0.0
$

so

$
\\begin{aligned}
P(D_3 = c) &= P(D_3 = c|D_2 = s)P(D_2 = s) +
P(D_3 = c|D_2 = c)P(D_2 = c) +
P(D_3 = c|D_2 = r)P(D_2 = r) \\
&=0.2 \\times 0.8 + 0.4 \\times 0.2 + 0.6 \\times 0.0 \\
&= 0.24
\\end{aligned}
$

-   Day 4

The weather of Day4 depends on the weather of Day 3.
$
\\begin{aligned}
P(D_3 = s) &= P(D_3 = s|D_2 = s)P(D_2 = s) +
P(D_3 = s|D_2 = c)P(D_2 = c) +
P(D_3 = s|D_2 = r)P(D_2 = r) \\
&= 0.8 \\times 0.8 + 0.4 \\times 0.2 + 0.2 \\times 0.0 \\
&= 0.72
\\end{aligned}
$

$
\\begin{aligned}
P(D_3 = r) &= P(D_3 = r|D_2 = s)P(D_2 = s) +
P(D_3 = r|D_2 = c)P(D_2 = c) +
P(D_3 = r|D_2 = r)P(D_2 = r) \\
&=0.0 \\times 0.8 + 0.2 \\times 0.2 + 0.2 \\times 0.0 \\
&= 0.04
\\end{aligned}
$

so

$
\\begin{aligned}
P(D_4 = r) &= P(D_4 = r|D_3 = s)P(D_3 = s) +
P(D_4 = r|D_3 = c)P(D_3 = c) +
P(D_4 = r|D_3 = r)P(D_3 = r) \\
&=0.0 \\times 0.72 + 0.2 \\times 0.24 + 0.2 \\times 0.04 \\
&= 0.056
\\end{aligned}
$

* * *

Goal(b)
Let $X_n$ denote the distribution of weather of Day n.

$
X_n = \\begin{pmatrix}
P(D_n = s) \\
P(D_n = c) \\
P(D_n = r) \\
\\end{pmatrix}
$

$
X_1 = \\begin{pmatrix}
1.0 \\
0.0 \\
0.0 \\
\\end{pmatrix}
$

Transition matrain
$
T = \\begin{pmatrix}
0.8 & 0.2 & 0.0\\
0.4 & 0.4 & 0.2\\
0.2 & 0.6 & 0.2\\
\\end{pmatrix}
$

so

$X\_{n+1} = TX_n$

* * *

Goal (c) and (d)
If
$X_{n+1} = TX_n$
then
$X_{n} = T^{n-1}X_1$

T is diagonalizable
$T = QDQ^{-1}$

where

$
Q = \\begin{pmatrix}
9 & \\sqrt{2}-1 & -\\sqrt{2}-1\\
4 & -\\sqrt{2} & \\sqrt{2}\\
1 & 1 & 1\\
\\end{pmatrix}
$

and

$
D = \\begin{pmatrix}
1 & 0 & 0\\
0 & \\frac{\\sqrt{2}+1}{5} & 0\\
0 & 0 & \\frac{-\\sqrt{2}+1}{5}\\
\\end{pmatrix}
$

so

$
\\begin{aligned}
X\_{n} &= {(QDQ^{-1})}^{n-1}X_1 \\
&= Q{D}^{n-1}Q^{-1}X_1
\\end{aligned}
$

$
\\begin{aligned}
\\lim\_{n \\to \\infty} D =
\\begin{pmatrix}
1.0 & 0.0 & 0.0\\
0.0 & 0.0 & 0.0\\
0.0 & 0.0 & 0.0\\
\\end{pmatrix}
\\end{aligned}
$

$
\\begin{aligned}
\\lim\_{n \\to \\infty} X_n =
\\begin{pmatrix}
9.0/14.0 \\
2.0/7.0 \\
1.0/14.0 \\
\\end{pmatrix}
\\end{aligned}
$

* * *

Goal(f)
$
\\begin{aligned}
P(X_{n-1} | X_n) &= \\frac{P(X_n | X_{n-1}) P(X_{n-1})}{P(X_{n})} \\
&= P(X_n | X_{n-1}) \\frac{P(X_{n-1})}{P(X_{n})}
\\end{aligned}
$

so

$
\\begin{aligned}
P(X_{n-1}) &= \\frac{P(X_{n-1})}{P(X\_{n})}
\\end{aligned}
$

* * *

Goal(g)
The transition matrix will alos depend on weather. It will be time variant.m

* * *

## Problem 3.

**known**
Let $X_t$ denote the random variable of weather condition of Day t. Let $\\hat{X_t}$ denote the random variable of belief of the weather.

Let $T$ denote the transition matrix. The distribution of probability of $X_t$ and $\\hat{X_t}$ are denoted as $P(X_t) and P(\\hat{X_t})$

$P(\\hat{X\_{t+1}}) = TP(X_t)$

where

$
T = \\begin{pmatrix}
0.8 & 0.2 & 0.0\\
0.4 & 0.4 & 0.2\\
0.2 & 0.6 & 0.2\\
\\end{pmatrix}
$

Let $Z_t$ denote the sensored data at Day t, and $M$ denote the measurement matrix.

$P(X_t) = M P(Z_t)$

where

$
M = \\begin{pmatrix}
0.6 & 0.4 & 0.0\\
0.3 & 0.7 & 0.0\\
0.0 & 0.0 & 0.1\\
\\end{pmatrix}
$

And note that you can backslash-escape any punctuation characters
which you wish to be displayed literally, ex.: \`foo\`, \*bar\*, etc.
