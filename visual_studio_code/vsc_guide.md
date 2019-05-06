
#### Install
1. Download [Visual Studio Code](https://code.visualstudio.com/)
2. cd to folder of downloaded VSC
3. Run command to install: 
```commandline
sudo dpkg -i code_1.26.0-1534177765_amd64.deb
```
4. Install extensions:
- press: `ctrl shift x`
- install: python, code runner

#### Open a project folder:
```commandline
cd <folder path>
code .
```

#### Show/Hide terminal table, type:
```
ctrl `
```

#### Connect to remote server

Guide:
 - [Guide 1](https://code.visualstudio.com/blogs/2019/05/02/remote-development#_get-started)
 - [Guide 2](https://code.visualstudio.com/docs/remote/ssh)
 - [Video](https://www.youtube.com/watch?v=rh1Ag41J6IA)

#### Run code
Run on terminal, type:
```commandline
python file.py
```

Run on editor: right click, select **Run Python File on Terminal**

#### Debug
```
F5      Start Debugging
F10     Step over
F11     Step into
```

#### Switch interpreter:
- press: `ctrl shift p`
- type: `>Python: Select Interpreter`
- select expected interpreter

#### Create templates
- Go to `File > Preferences > User Snippets`
- Select Python
- In `python.json`, add code this kind:
```json
...
  "Generate docstring": {
		"prefix": "tdoc",
		"body": [
			"\"\"\"",
			"Description: ",
			":param NAME: TYPE, MEAN",
			":return: TYPE, MEAN",
			"\"\"\""
		],
		"description": "Template docstring"
	},
...
```
