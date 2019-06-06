
## 
- Firstly build boost by `Developer Command Prompt for VS2013` as Recommended guide in [`./boost/build_boost.md`](./boost/build_boost.md)
```commandline
bootstramp
.\b2 --with-python --user-config=user-config.jam --toolset=msvc-12.0 --build-type=complete architecture=x86 address-model=64 link=shared
```
 - Secondly, 