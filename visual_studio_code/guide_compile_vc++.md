
Guide: https://code.visualstudio.com/docs/cpp/config-msvc

### Steps
0. Prepare System Environment Environment:
    - Add to system Path dir of `cl.exe`: `C:/Program Files (x86)/Microsoft Visual Studio 12.0/VC/bin/`
    - Add to system Path dir of `vcvarsall.bat`: `C:/Program Files (x86)/Microsoft Visual Studio 12.0/VC/`

1. Config
    - compiler path(c_cpp_properties.json): press `Ctrl+Shift+P` then type `C/C++: Edit Configurations...`
    - how to build(tasks.json): press `Ctrl+Shift+P` then type `Tasks: Configure Default Build Task` then choose `Others`
    - debug settings(launch.json): Main menu > Debug > Open Configurations(or Add Configuration...)
    
2. Add codes

3. Run
    - `Ctrl+Shift+B`
    - `F5`

### Template:
Source from `pflannery`: https://github.com/Microsoft/vscode-cpptools/issues/1839
(Should try? https://devblogs.microsoft.com/cppblog/building-your-c-application-with-visual-studio-code/)
c_cpp_properties.json
```json
{
    "configurations": [
        {
            "name": "Win32",
            "includePath": [
                "${workspaceFolder}/**",
                "C:/Program Files (x86)/Microsoft Visual Studio 12.0/VC/include"
            ],
            "defines": [
                "_DEBUG",
                "UNICODE",
                "_UNICODE"
            ],
            "intelliSenseMode": "msvc-x64",
            "compilerPath": "cl.exe",
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
    "echoCommand": true,
    "tasks": [
        {
            "label": "full auto-build msvc12",
            "type": "process",
            "command": "cmd",
            "args": ["/C mkdir %OutPath% && %vcvarsall% && cl /Od /Zi /EHsc /Fd:%OutPath%/vc120.pdb /Fo:%OutPath%/%TarName%.obj ${fileBasename} /link /OUT:%OutPath%/%TarName%.%TarExt% /PDB:%OutPath%/%TarName%.pdb"],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "presentation": {
                "reveal": "always"
            },
            "problemMatcher": "$msCompile"
        }
    ],
    "options": {
        "env": {
            "OutPath": "output",
            "TarName": "${fileBasenameNoExtension}",
            "TarExt": "exe",
            "vcvarsall": "vcvarsall.bat x64",
        }
    }
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
            "name": "(Windows) Launch",
            "type": "cppvsdbg",
            "request": "launch",
            "program": "${workspaceFolder}/output/${fileBasenameNoExtension}.exe",
            "args": [],
            "stopAtEntry": false,
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