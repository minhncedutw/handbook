
## Install
- Download at [source](https://hub.docker.com/editions/community/docker-ce-desktop-windows). Then install normally.
- Start docker
- Change image storage location by the way:
    - Open `Settings` > `Daemon`
    - Switch to `Advanced`
    - Add new location to the end of the editor such as:
    ```json
    {
    "registry-mirrors": [],
    "insecure-registries": [],
    "debug": true,
    "experimental": false,
    "graph": "E:\\WORKSPACES\\Docker"
    }
    ```
    - Docker will auto restart. Then, enjoy it.