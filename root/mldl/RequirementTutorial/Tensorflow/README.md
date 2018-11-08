# TensorFlow 

**TensorFlow** is an open-source machine learning library for research and production. TensorFlow offers APIs for beginners and experts to develop for desktop, mobile, web, and cloud.

## Learn and use ML 

- [Deep Learning with Python Books]()


## Low Level APIs 

the low-level TensorFlow APIs (TensorFlow Core), Knowing TensorFlow Core is valuable for the follow reasons:

Expermentation and debugging are both more straight forward when you can use low level TensorFlow operations directly. 

It gives you a mental model of how things work internally when using the higher level APIs.

1. tf.Graph     -- Manage TensorFlow program 
2. tf.Session   -- TensorFlow runtime 

- [Setup]()

```
import numpy as np 
import tensorflow as tf 
```

- [Tensor Values]()

The central unit of data in TensorFlow is the **tensor**. A tensor's **rank** is its number of dimensions,while its **shape** is a tuple of integers specifying the array's length along each dimension. 

```
3. # a rank 0 tensor; a scalar with shape []
[1., 2., 3.] # a rank 1 tensor; a vector with shape [3]
[[1., 2., 3.], [4., 5., 6.]] # a rank 2 tensor; a matrix with shape [2, 3]
[[[1., 2., 3.]], [[7., 8., 9.]]] # a rank 3 tensor with shape [2, 1, 3]
```

TensorFlow uses numpy arrays to represent tensor **values**.

- [TensorFlow Core Walkthrough]()

1. Building the computational graph (a tf.Graph)
2. Running the computational graph (Using a tf.Session)

**computational graph** is a series of TensorFlow operations arranged into a graph. The graph is composed of two types of objects.
    a. tf.Operation : The nodes of the graph. Operations describe calculations that consyme and produce tensors.
    b. tf.Tensor : The edges in the graph. These represent the values that will flow through the graph. Most TensorFlow functions return **tf.Tensors** 

    ```
    a = tf.constant(3.0, dtype=tf.float32)
    b = tf.constant(4.0) # also tf.float32 implicitly
    total = a + b 
    print(a)        # Tensor("Const:0", shape=(), dtype=float32)
    print(b)        # Tensor("Const_1:0", shape=(), dtype=float32)
    print(total)    # Tensor("add:0", shape=(), dtype=float32)

    # The above statements only build the computation graph 
    # Each operation in a graph is given a unique name. This name is independent of the names the objects are assigned to in Python. 
    ```

**TensorBoard** TensorFlow provides a utility, is visualizing a computation graph. 

```
writer = tf.summary.FileWriter('.')
writer.add_graph(tf.get_default_graph())
# produce an event file in the current directory with a name "events.out.tfevents.{timestamp}.{hostname}" 
$ tensorboard --logdir . # launch TensorBoard "graphs page" in your browser.
```

**Session** to evaluate tensor, instantiate a **tf.Session** object.

```
# creates a tf.Session object and then invokes its run method to evaluate the total tensor 
sess = tf.Session()
print(sess.run(total)) # 7.0 

vec = tf.random_uniform(shape=(3,)) # to produce a tf.Tensor that generates a random 3-element vector
```

**placeholder** is a promise to provide a value later 

```
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
z = x + y

# evaluate this graph with multiple inputs by using the feed_dict argument 
print(sess.run(z, feed_dict={x: 3, y: 4.5}))
print(sess.run(z, feed_dict={x: [1,3], y:[2,4]}))
```

- [Datasets]()

Placeholders work for simple experiments, but **tf.data** are the preferred method of streaming data into a model. 

```
my_data = [[0, 1,],[2, 3,],[4,5,],[6,7,],]

# To get a runable tf.Tensor from a Dataset you must first convert it to a tf.data.Iterator, and then call the Iterator's tf.data.Iterator.get_next method.

slices = tf.data.Dataset.from_tensor_slice(my_data)
next_item = slices.make_one_iterator().get_next()

while True:
    try:
        print(sess.run(next_item))
    except tf.errors.OutOfRangeError:
        break 
```

- [Layers]()

A trainable model must modify the values in the graph to get new outputs with the same input. **tf.layers** are the preferred way to add trainable parameters to a graph.

```
x = tf.placeholder(tf.float32, shape=[None, 3])
# Creating Layers 
linear_model = tf.layers.Dense(units=1)
y = linear_model(x)

# The layer contains variables that must be initialized before they can be used. 
init = tf.global_variables_initializer() 
sess.run(init)

# Executing Layers 
print(sess.run(y, {x: [[1, 2, 3], [4, 5, 6]]}))
```

- [Feature columns]() 




## Deploy

Distributed TensorFlow, how to create a cluster of TensorFlow servers, and how to distribute a computation graph across that cluster.


