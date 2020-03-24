# Numpy Matrix Multiplication

You've heard a lot about matrix multiplication in the last few videos – now you'll get to see how to do it with NumPy. However, it's important to know that NumPy supports several types of matrix multiplication.

## Element-wise Multiplication

You saw some element-wise multiplication already. You accomplish that with the `multiply` function or the `*` operator. Just to revisit, it would look like this:

```python
m = np.array([[1,2,3],[4,5,6]])
m
# displays the following result:
# array([[1, 2, 3],
#        [4, 5, 6]])

n = m * 0.25
n
# displays the following result:
# array([[ 0.25,  0.5 ,  0.75],
#        [ 1.  ,  1.25,  1.5 ]])

m * n
# displays the following result:
# array([[ 0.25,  1.  ,  2.25],
#        [ 4.  ,  6.25,  9.  ]])

np.multiply(m, n)   # equivalent to m * n
# displays the following result:
# array([[ 0.25,  1.  ,  2.25],
#        [ 4.  ,  6.25,  9.  ]])
```

## Matrix Product

To find the matrix product, you use NumPy's `matmul` function.

If you have compatible shapes, then it's as simple as this:

```python
a = np.array([[1,2,3,4],[5,6,7,8]])
a
# displays the following result:
# array([[1, 2, 3, 4],
#        [5, 6, 7, 8]])
a.shape
# displays the following result:
# (2, 4)

b = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
b
# displays the following result:
# array([[ 1,  2,  3],
#        [ 4,  5,  6],
#        [ 7,  8,  9],
#        [10, 11, 12]])
b.shape
# displays the following result:
# (4, 3)

c = np.matmul(a, b)
c
# displays the following result:
# array([[ 70,  80,  90],
#        [158, 184, 210]])
c.shape
# displays the following result:
# (2, 3)
```
If your matrices have incompatible shapes, you'll get an error, like the following:

```python
np.matmul(b, a)
# displays the following error:
# ValueError: shapes (4,3) and (2,4) not aligned: 3 (dim 1) != 2 (dim 0)
```

## Numpy dot function

You may sometimes see NumPy's `dot` function in places where you would expect a `matmul`. It turns out that the results of `dot` and `matmul` are the same if the matrices are two dimensional.

So these two results are equivalent:

```python
a = np.array([[1,2],[3,4]])
a
# displays the following result:
# array([[1, 2],
#        [3, 4]])

np.dot(a,a)
# displays the following result:
# array([[ 7, 10],
#        [15, 22]])

a.dot(a)  # you can call `dot` directly on the `ndarray`
# displays the following result:
# array([[ 7, 10],
#        [15, 22]])

np.matmul(a,a)
# array([[ 7, 10],
#        [15, 22]])
```

While these functions return the same results for two dimensional data, you should be careful about which you choose when working with other data shapes. You can read more about the differences, and find links to other NumPy functions, in the `matmul` and `dot` documentation.

# Transpose

Getting the transpose of a matrix is really easy in NumPy. Simply access its `T` attribute. There is also a `transpose()` function which returns the same thing, but you’ll rarely see that used anywhere because typing `T` is so much easier. :)

For example:
```python
m = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
m
# displays the following result:
# array([[ 1,  2,  3,  4],
#        [ 5,  6,  7,  8],
#        [ 9, 10, 11, 12]])

m.T
# displays the following result:
# array([[ 1,  5,  9],
#        [ 2,  6, 10],
#        [ 3,  7, 11],
#        [ 4,  8, 12]])
```

NumPy does this without actually moving any data in memory - it simply changes the way it indexes the original matrix - so it’s quite efficient.

However, that also means you need to be careful with how you modify objects, because **they are sharing the same data**. For example, with the same matrix m from above, let's make a new variable `m_t` that stores `m`'s transpose. Then look what happens if we modify a value in `m_t`:

```python
m_t = m.T
m_t[3][1] = 200
m_t
# displays the following result:
# array([[ 1,   5, 9],
#        [ 2,   6, 10],
#        [ 3,   7, 11],
#        [ 4, 200, 12]])

m
# displays the following result:
# array([[ 1,  2,  3,   4],
#        [ 5,  6,  7, 200],
#        [ 9, 10, 11,  12]])
```

Notice how it modified both the transpose and the original matrix, too! That's because they are sharing the same copy of data. So remember to consider the transpose just as a different view of your matrix, rather than a different matrix entirely.

## A real use case

I don't want to get into too many details about neural networks because you haven't covered them yet, but there is one place you will almost certainly end up using a transpose, or at least thinking about it.

Let's say you have the following two matrices, called `inputs` and `weights`,

```python
inputs = np.array([[-0.27,  0.45,  0.64, 0.31]])
inputs
# displays the following result:
# array([[-0.27,  0.45,  0.64,  0.31]])

inputs.shape
# displays the following result:
# (1, 4)

weights = np.array([[0.02, 0.001, -0.03, 0.036], \
    [0.04, -0.003, 0.025, 0.009], [0.012, -0.045, 0.28, -0.067]])

weights
# displays the following result:
# array([[ 0.02 ,  0.001, -0.03 ,  0.036],
#        [ 0.04 , -0.003,  0.025,  0.009],
#        [ 0.012, -0.045,  0.28 , -0.067]])

weights.shape
# displays the following result:
# (3, 4)
```

I won't go into what they're for because you'll learn about them later, but you're going to end up wanting to find the **matrix product** of these two matrices.

If you try it like they are now, you get an error:

```python
np.matmul(inputs, weights)
# displays the following error:
# ValueError: shapes (1,4) and (3,4) not aligned: 4 (dim 1) != 3 (dim 0)
```

If you did the matrix multiplication lesson, then you've seen this error before. It's complaining of incompatible shapes because the number of columns in the left matrix, `4`, does not equal the number of rows in the right matrix, `3`.

So that doesn't work, but notice if you take the transpose of the `weights` matrix, it will:

```python
np.matmul(inputs, weights.T)
# displays the following result:
# array([[-0.01299,  0.00664,  0.13494]])
```

It also works if you take the transpose of inputs instead and swap their order, like we showed in the video:

```python
np.matmul(weights, inputs.T)
# displays the following result:
# array([[-0.01299],# 
#        [ 0.00664],
#        [ 0.13494]])
```

The two answers are transposes of each other, so which multiplication you use really just depends on the shape you want for the output.