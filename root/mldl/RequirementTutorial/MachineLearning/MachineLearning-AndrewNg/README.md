# Machine Learning - Andrew Ng, Stanford

## Introduction - What is a machine learning 

1. Machine Learning definition 

**Arthur Samuel(1959). Machine Learning: Field of study that gives computers the ability to learn without being explicity programmed.**

**Tom Mitchell (1998) Well-posed Learning Problem: A computer program is said to learn from expreience E with respect to some task T and some performance measure P, if its performance on T, as measureed by P, improves with experiences E.**

**Machine Learning algorithms:**

- Supervised learning  - teach computer how to do something 
- unsupervised learning - learn by itself 
- Reinforcement learning 
- recommender systems 

```

```

2. Introduction - Supervised Learning 监督学习

- Housing price prediction: Supervised learning {right answers given} 
- Regression: Predict continuous valued output(price)

- Breast cancer (malignant, benign)
- Classification: Discrete valued output (0 or 1)

```
```

3. Introduction - Unsupervised Learning 无监督学习

- Google New(news.google.com): clustering algorithm, Google News is done is looked at tens of thousands of new stories and automatically cluster them together so the new stories that are all about the same topic get to display together it.
- Cocktail party problem: the cocktail party algorithm and (audio separating) 

```
Cocktail party problem algorithm
[W,s,v] = svd((repmat(sum(x.*x,1), size(x,1),1).*x)*x') 

svd: the singular value decomposition 
```

4. Linear regression 线性回归 with one variable [Model representation]

Supervised Learning: Given the "right answer" for each example in the data.
Regression Problem: Predict real-valued output 

```
# some notation:
m = Number of training examples 
x's = "input" variable / features 
y's = "output" variable / "target" variable 
(X,Y) = a single training examples
(X¹,Y¹) = iths training examples 
h = hypothesis 

How do we represent h?
h0(x) = 0₀ + 0₁x  
```

5. Linear regression with one variable - Cost function 

```
Hypothesis: h0(x) = 0₀ + 0₁x 
0₁'s: parameters 
Idea: Choose 0₀, 0₁ so that h0(x) is close to y for our training examples(x,y)

Cost function: called the squared error function is probably the most commonly used one for regression problems. 

Contour plots: also call contour figures.

Gradient descent: for minimizing the cost function 

Have some function J(0₀,0₁)
Want min J(0₀,0₁) 

Outline:
    Start with some 0₀,0₁
    Keep changing 0₀,0₁ to reduce J(0₀,0₁) until we hopefully end up at a minimum
Gradient descent algorithm
    repeat until convergence {
        0j := 0j - α∂J(0₀,0₁)/∂0j  (simultaneously update for j = 0 and j = 1)
        α: is called the learning rate is control how big a step we take downhill, is always a positive number
    Correct: Simulataneous update 
        temp0 := 0₀ - α∂J(0₀,0₁)/∂0₀ 
        temp1 := 0₁ - α∂J(0₀,0₁)/∂0₁ 
        0₀ := temp0
        0₁ := temp1
    partial derivative symbols: 偏导数
    tangent: 切线 
    the slop is the derivative 
    
    If α is too small, gradient descent can be slow. If α is too large, gradient descent can overshoot the minimum, it may fail to converge, or even diverge.
 }

Gradient descent can converge to a local minimum, even with the learning rate α fixed. gradient descent will automatically take smaller steps. So, no need to decrease a over time.

# Gradient descent for linear regression 

Convex function means a bowl-shaped function.

"Batch" Gradient Descent:
    "Batch": Each step of gradient descent uses all the traning examples.

```
6. Linear Algebar Review: 

```
Linear Algebra:线性代数 Notation and set of the things you can do with matrices and vectors.

Topics:
    - What are matrices and vectors 
    - Addition, subtraction, multiplication with matrices and vectors 
    - Matrix inverse, transpose.
Matrix: Rectangular array of numbers; Dimension of matrix: number of rows x number of columns 
Vector: An n x 1 matrix 
Use Uppercase to refer to matrices; 

Matrix Addition:
Scalar Multiplication: 
Combination of Operands: 
Matrix-vector multiplication 
Matrix-matrix multiplication : is really useful since you can pack a lot of computation into just one matrix multiplication operation 

Let A and B be matrices. Then in general, A X B ‡ B X A.(not commutative)

Identity Matrix:特征向量, Denoted I (or I (nxn)): Beacuse Identity times anything is equal to itself.
    for any matrix A, A · I = I · A = A 

Inverse 逆矩阵 and transpose 转制
    Not all numbers have an inverse.
    Matrix inverse:
        If A is an m x m matrix(square matrix), and if it has an inverse. AA⁻¹ = A⁻¹A = I ; 
>>> import numpy as np
>>> a = np.array([[1.0,2.0],[3.0,4.0]])
>>> print(a)
>>> np.linalg.inv(a)
    
    Matrices that don't have an inverse are "singular" or "degenerate"
    
    Matrix Transpose: Let A be an m x n matrix, and let B = A⁻T. Then B is an n x m matrix, and Bij = Aji
```

7. Linear Regression With Multiple Variables

```
    Multiple features (variables)
        Notation:
            M: the number of training examples 
            n = numbers of features 
            x(i) = input (feature) of ith training example 
            xj(i) = value of feature j in ith training example

    h(x) = 0₀ + 0₁x₁ + 0₂x₂ + ... : For convenience of notation, define x₀ = 1 
    h(x) = 0₀x₀ + 0₁x₁ + 0₂x₂ + ... 

    How to use gradient descent for linear regression with multiple features 
```


