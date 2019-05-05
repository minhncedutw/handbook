#### Jupyter access remote server through ssh
```commandline
ssh -L 8000:localhost:8888 sammy@your_server_ip
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
# !conda list
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
