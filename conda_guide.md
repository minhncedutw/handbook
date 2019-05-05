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

#### Install Fastai env
```yaml
# conda create --name fastai python=3.6 -y
# conda install cudatoolkit=9.0 pytorch=1.0.0 torchvision -c pytorch -y
# conda install fastai pillow-simd -c fastai -c scw -y
# conda env update -f env-fastai.yml --freeze-installed
name: fastai
channels:
  - pytorch
  - scw
  - fastai
  - conda-forge
  - defaults
dependencies:
  - bcolz
  - beautifulsoup4
  - bokeh
  - cudatoolkit=9.0
  - cython
  - decorator
  - dill
  - fastai
  - fastprogress
  - hdf5
  - ipykernel
  - ipython
  - jupyter
  - jupyterlab
  - matplotlib
  - notebook
  - numpy
  - pandas
  - pillow
  - pip
  - python
  - pytorch=1.0.0
  - requests
  - scipy
  - seaborn
  - statsmodels
  - torchvision
  - tqdm
```

#### EXPORT environment
```commandline
conda env export | cut -f 1 -d '=' | grep -v "^prefix: " > environment.yml
```
```commandline
conda list -e > requirements.txt
```

#### CREATE environment from SHARED environment file
```commandline
conda env create -f environment.yml
```
```commandline
pip install -r requirements.txt
```

#### REMOVE package in environment
`conda remove --name ENV_NAME PACKAGE_NAME`

#### REMOVE environment
`conda remove --name ENV_NAME --all`

#### UPDATE in conda
```commandline
conda update python
conda update conda
```

#### CLONE environment
```commandline
conda create --name NEW_ENV --clone OLD_ENV
```

#### CLEAN trash packages
```commandline
conda clean -a -y
conda clean -pt # removes any unextracted tarballs, and any extracted packages that are not currently linked into an environment
# or
conda clean -a --dry-run # If you want to know what files would be deleted before actually deleting
```

#### Symbol link for conda's python to avoid CONFLICTION with system python (UBUNTU)
```commandline
mkdir .symlinks
cd .symlinks

ln -s /home/user/miniconda3/bin/conda conda
ln -s /home/user/miniconda3/bin/activate activate
ln -s /home/user/miniconda3/bin/deactivate deactivate

export PATH="/home/user/.symlinks:$PATH"
```
