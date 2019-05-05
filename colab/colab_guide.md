
#### Connect google drive
```python
from google.colab import drive
drive.mount('/content/drive')
%cd PATH
```

#### Upload local files to colab
```python
from google.colab import files
uploaded = files.upload()
for file in uploaded.keys():
    print('Uploaded file "{name}" with length {length} bytes'.format(name=file, length=len(uploaded[file])))
```

#### Google Colab hotkeys
```
ctrl m a     # insert cell above
ctrl m b     # insert cell below
ctrl m d     # delete cell
ctrl m c     # copy cell
ctrl m x     # cut cell
ctrl m v     # paste cell
```

#### Colab command line
```commandline
!ls
!mkdir 
!git clone [git clone url]
!wget [url] -p drive/[Folder Name]
!pip install [package name]
!apt-get install [package name]
!python3 /content/drive/Project/script.py
```
Check CPU and RAM specifications
```commandline
!cat /proc/cpuinfo
!cat /proc/meminfo
```

