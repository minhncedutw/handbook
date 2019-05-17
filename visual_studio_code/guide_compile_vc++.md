
Source: https://code.visualstudio.com/docs/cpp/config-msvc

**Command hotkeys**: (File > Preferences > Keyboard Shotcuts)
 - Open Terminal: ``Ctrl+` ``
 - Open Command Palette: `Ctrl+Shift+P`
 - Build project: `Ctrl+Shift+B`
 - Debug project: `F5`
 - Debug Step over: `F10`
 - Comment: `Ctrl+/`

### Steps
1. Config
    - compiler path(c_cpp_properties.json): press `Ctrl+Shift+P` then type `C/C++: Edit Configurations...`
    - how to build(tasks.json): press `Ctrl+Shift+P` then type `Tasks: Configure Default Build Task` then choose `Others`
    - debug settings(launch.json): Main menu > Debug > Open Configurations(or Add Configuration...)
    
2. Add codes

3. Run
    - `Ctrl+Shift+B`
    - `F5`

### Template:
c_cpp_properties.json
```json
{
    "configurations": [
        {
            "name": "Win32",
            "defines": [
                "_DEBUG",
                "UNICODE",
                "_UNICODE"
            ],
            "compilerPath": "C:/Program Files (x86)/Microsoft Visual Studio/2017/BuildTools/VC/Tools/MSVC/14.16.27023/bin/Hostx64/x64/cl.exe",
            "windowsSdkVersion": "10.0.17763.0",
            "intelliSenseMode": "msvc-x64",
            "cStandard": "c11",
            "cppStandard": "c++17"
        }
    ],
    "version": 4
}
```

tasks.json
```json
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "msvc 12 build",
            "type": "shell",
            "command": "cl.exe",
            "args": [
                "/EHsc",
                "/Zi",
                "/Fe:",
                "helloworld.exe",
                "helloworld.cpp"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "presentation": {
                "reveal": "always"
            },
            "problemMatcher": "$msCompile"
        }
    ]
}
```

launch.json
```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [

        {
            "name": "(msvc 12) Launch",
            "type": "cppvsdbg",
            "request": "launch",
            "program": "${workspaceFolder}/helloworld.exe",
            "args": [],
            "stopAtEntry": true,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": true
        }
    ]
}
```

helloworld.cpp
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{

    vector<string> msg {"Hello", "C++", "World", "from", "VS Code!"};

    for (const string& word : msg)
    {
        cout << word << " ";
    }
    cout << endl;
}
```