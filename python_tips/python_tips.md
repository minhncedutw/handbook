
#### --------------------------------------------------
#### raise(show error notification)
```python
raise NotImplementedError("error message")

raise Exception('Architecture not supported!')

if len(input_shape) != 2:
    raise ValueError('The input_shape must contains 2 elements')
```

#### --------------------------------------------------
#### assert(show error notification)
Check whether condition is true, if not raise error
```python
assert shape1 == shape2  # else hadamard product isn't possible
```

#### --------------------------------------------------
#### isinstance(check type of variable)
```python
if not isinstance(inputs, list):
    raise ValueError('inputs must be a list')
```

#### --------------------------------------------------
#### path
Declare and type cast
```python
from pathlib import Path
path = Path('/etc') # type casting from `str` to `path`
path.chmod(mode=)
```
Create new path
```python
new_path = path/'abc' # create new path by joining path with string
```
Make directory
```python
path.mkdir(parents=True) # make directory for relative path
path.mkdir(parents=False) # make directory for absolute path

path.mkdir(exist_ok=False) # make and rewrite existed directory
path.mkdir(exist_ok=True) # make new directory, and raise error if directory exists
```
Get directory
```python
print(Path(__file__).resolve()) # get path of current running file
print(Path(__file__).resolve().parent) # get parent directory of current running file
print(Path.cwd()) # get directory of root file(if file `a.py` call func at file `b.py`, `b.py` call `Path.cwd()`, return result is directory of file `a.py`, not file `b.py`
```
Change chmod
```python
path.chmod(mode=0o777) # give full access(More infor at: https://help.ubuntu.com/community/FilePermissions)
path.stat().st_mode # display new access permission of path
```
Source: https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir

#### --------------------------------------------------
#### import
Good practices for importing:
 - https://sweetcode.io/python-file-importation-multi-level-directory-modules-packages/
 - https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
 
#### --------------------------------------------------
#### numpy random
Random integers
```python
arr = np.random.randint(low=1, high=10, size=(2, 3, 4)) # random int value from 1 to 9
```
Random floats (0-1) # 3 below methods are equal
```python
arr = np.random.random_sample(size=(10, 10, 10))
arr = np.random.random(size=(10, 10, 10))
arr = np.random.rand(10, 10, 10)
```
 
#### --------------------------------------------------
#### `sys.path.append('...')` better than `sys.path.insert(0, '...')`
Source: https://stackoverflow.com/questions/31291608/effect-of-using-sys-path-insert0-path-and-sys-pathappend-when-loading-modul

#### --------------------------------------------------
#### Difference between Module & Package
> A package is a collection of Python modules: while a module is a single Python file, a package is a directory of Python modules containing an additional __init__.py file

Source: https://stackoverflow.com/questions/7948494/whats-the-difference-between-a-python-module-and-a-python-package

#### --------------------------------------------------
