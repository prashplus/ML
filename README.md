# Machine Learning

All the sample Machine Learning codes required during the learning phase

## Getting Started

The instructions will be in the Readme of each directory or it will be in the resepected Python file in form of comments.

### Prerequisites

Look out for the prerequisites dependencies in the import section or will be mentioned in the requirements.txt



## Setup

Setup your Tensorflow or Tensorflow-GPU as the way you want.
Follow the instructions on the official site of tensorflow at: https://www.tensorflow.org/install/

For the easiest way install Anaconda and follow the steps

```
C:> conda create -n tensorflow pip python=3.5
```
Activate your environment

```
C:> activate tensorflow
 (tensorflow)C:>  # Your prompt should change 
```
Install Tensorflow using PIP

```
(tensorflow)C:> pip install --ignore-installed --upgrade tensorflow 
```
or 
```
(tensorflow)C:> pip install --ignore-installed --upgrade tensorflow-gpu
```

### Setting up the GPU Environment (Nvidia GPUs only)

Nvidia has put tremendous efforts to lower down the efforts of the developers like us by making CUDA toolkit and the libraries which works with their CUDA cores. Belive me, an average GPU runs 15-25 times faster in training Neural Networks comparing to a CPU.

If you are installing TensorFlow with GPU support using one of the mechanisms described in this guide, then the following NVIDIA software must be installed on your system:

1. CUDA® Toolkit 9.0. For details, see [NVIDIA's documentation](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/) Ensure that you append the relevant Cuda pathnames to the %PATH% environment variable as described in the NVIDIA documentation. [Link](https://developer.nvidia.com/cuda-toolkit-archive)

2. The NVIDIA drivers associated with CUDA Toolkit 9.0. (Download the latest drivers as per the official site suggestions.)

3. cuDNN v7.0.4 for CUDA® Toolkit 9.0. For details, see [NVIDIA's documentation](https://developer.nvidia.com/cudnn). Note that cuDNN is typically installed in a different location from the other CUDA DLLs. Ensure that you add the directory where you installed the cuDNN DLL to your %PATH% environment variable. [Link](https://developer.nvidia.com/rdp/cudnn-archive)

4. GPU card with CUDA Compute Capability 3.0 or higher for building from source and 3.5 or higher for our binaries. See NVIDIA documentation for a list of supported GPU cards.

If you have a different version of one of the preceding packages, please change to the specified versions. In particular, the cuDNN version must match exactly: TensorFlow will not load if it cannot find cuDNN64_7.dll. To use a different version of cuDNN, you must build from source.

## Running the tests

Invoke the python
```
$ python
```

Run the following lines in python

```python
>>> import tensorflow as tf
>>> hello = tf.constant('Hello, TensorFlow!')
>>> sess = tf.Session()
>>> print(sess.run(hello))
```


## Authors

* **Prashant Piprotar** - - [Prash+](https://github.com/prashplus)
and visit my blog for more Tech Stuff
### http://www.prashplus.com
