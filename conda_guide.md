#### Install Keras env
```yaml
# conda create --name keras python=3.6 -y
# conda install cudatoolkit=9.0 tensorflow-gpu keras-gpu -c anaconda -y
# conda update -f env-keras.yml --freeze-installed
name: keras
channels:
  - open3d-admin
  - conda-forge
  - anaconda
  - defaults
dependencies:
  - cudatoolkit=9.0
  - cudnn=7.3.1
  - cython
  - dill
  - flask
  - graphviz
  - h5py
  - hdf5
  - imagehash
  - imageio
  - ipykernel
  - ipython
  - jinja2
  - jpeg
  - jsonschema
  - jupyter
  - jupyter_contrib_nbextensions
  - jupyterlab
  - keras-gpu
  - markdown
  - matplotlib
  - nodejs
  - notebook
  - numpy
  - open3d
  - opencv
  - pandas
  - pillow
  - pip
  - pylint
  - pyscaffold
  - python=3.6
  - python-graphviz
  - qt
  - requests
  - scikit-image
  - scikit-learn
  - scipy
  - scrapy
  - seaborn
  - shapely
  - statsmodels
  - sympy
  - tensorflow-gpu
  - tpot
  - tqdm
  - pip:
    - imgaug
    - mayavi
    - open3d-python
    - primesense
    - vtk
```
