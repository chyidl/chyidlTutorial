# Tensorflow Tutorial 

An open source ML framework for everyone, Almost everyone writes tensorflow code in python, tensorflow is powered by a C++ back-end and 

## Tensorflow API styles

- tf.keras 

Keras: a high-level API specification, Build and train neural networks using lego-like building blocks.

```
!pip install keras 
import keras 
```

tf.keras - TensorFlow's implementation, Superset of the Keras API. Adds support for TensorFlow specific functionality, like eager execution.````

```
!pip install tensorflow
from tensorflow import keras 
``` 

- Estimators
- Eager execution 
- Deferred execution 

### Tutorial 

- [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/)
- [MNIST](/root/mldl/RequirementTutorial/TensorFlow/PracticalPythonTensorflow/Fashion_MNIST.py)

The more layers you add to your network the greater the capacity, the larger the number of patterns that your network is capable of learning, so large networks can learn more complex data sets but there's downsides, so when we're training a network and it's in machine learning there's a fundamental tension between memorization and generalization. be careful overfit.

**activation function** 

