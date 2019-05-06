
#### Install and clone google drive to folder `gdrive`

#### Pull from google drive
```commandline
drive pull # downloads data that does not exist locally but does remotely on Google  drive, and may delete local data that is not present on Google Drive. Run it without any arguments to pull all of the files from the current  path
drive pull -force # To force download from paths that otherwise would be marked with no-changes
drive pull photos/img001.png docs # To pull specific files or directories, pass in one or more paths
```

#### Push to google drive
```commandline
drive push -files a1/b2 # To selectively push by type e.g file vs directory/folder, you can use flags
drive push -directories tf1# To selectively push by type e.g file vs directory/folder, you can use flags
```

More infor: https://github.com/odeke-em/drive
