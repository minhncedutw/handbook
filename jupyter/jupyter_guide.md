#### Jupyter access remote server through ssh
```commandline
ssh -L 8890:localhost:8890 ACCOUNT@SERVER_IP
# then type server's PASSWORD
...
jupyter notebook --ip=8890 --no-browser
```

#### Jupyter lab install extension
```commandline
# Install extension packages for jupyter lab
jupyter labextension install @jupyterlab/shortcutui
jupyter labextension install @jupyterlab/google-drive
jupyter labextension install @jupyterlab/github
jupyter labextension install jupyterlab-drawio

jupyter labextension install @jupyterlab/git
pip install jupyterlab-git
jupyter serverextension enable --py jupyterlab_git
```

#### Jupyter hotkeys:
```
esc a     # insert cell above
esc b     # insert cell below
esc d d   # delete cell
esc c     # copy cell
esc x     # cut cell
esc v     # paste cell
```

## Tip
#### Start with pytorch-based
```python
# !conda list
%reload_ext autoreload
%autoreload 2
%matplotlib inline

import torch
print(torch.cuda.device_count())
print(torch.cuda.current_device())
print(torch.cuda.get_device_name(0))
print(torch.cuda.set_device(0))
```

#### Start with tensorflow-based
```python
# !conda list
%reload_ext autoreload
%autoreload 2
%matplotlib inline

from keras import backend as K
print(K.tensorflow_backend._get_available_gpus())

import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0" # The GPU id to use, usually either "0" or "1"
```

#### Check GPU
```python
import platform
print(platform.python_version())
```

```python
import torch
torch.cuda.device_count()
torch.cuda.current_device()
torch.cuda.get_device_name(0)
```

```python
# check installed fastai framework
python -m fastai.utils.show_install
```

```python
from keras import backend as K
K.tensorflow_backend._get_available_gpus()
```

```python
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
```

```python
import tensorflow as tf
a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
c = tf.matmul(a, b)
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
print(sess.run(c))
```

```python
import tensorflow as tf
a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
c = tf.matmul(a, b)
sess = tf.Session()
print(sess.run(c))
sess.close()
```
