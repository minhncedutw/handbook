
### Build boost lib
- Download boost at: https://www.boost.org/users/history/version_1_68_0.html and Extract boot somewhere
- Afterward, open `Visual Studio Tools` > `Developer Command Prompt for VS2013` (akind: `C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\Tools\Shortcuts`)
- Then cd to extracted boot directory
- Simplest build:
    + type: `bootstrap`
    + then type: `.\b2 --toolset=msvc-12.0 --build-type=complete --prefix=path\to\save\independ\boost --build-dir=build`
      or: `.\b2 variant=debug,release link=static runtime-link=static address-model=64 --prefix=path\to\save\independ\boost --build-dir=build`
- **Better way to build(Recommended)**:
    + type: `bootstramp`
    + then type:
```commandline
.\b2 --with-python --user-config=user-config.jam --toolset=msvc-12.0 --build-type=complete architecture=x86 address-model=64 link=shared
```
