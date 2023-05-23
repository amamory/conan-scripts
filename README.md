# conan-scripts
Collection of usefull conan scripts in python.

## Requirements

 - conan 1.59
 - python 3

## search_arch

Searchs for packages with a specific architecture name.

Examples of usage:

```bash
python3 search_arch.py protobuf --arch armv8 --remote myremote-name
Remote to be searched: myremote-name
 recipe id: protobuf/3.21.9-xxx myremote-name
  - package id: 37691084913a549db21760184828e74c3afe89fc armv8
  - package id: 62b64e6800f6acd9ea299d62011a3a4502d5a89a armv8
  - package id: 85d9f875d9f2389ee1d949ad8230f9bc1193f31e armv8
  - package id: cc322c1fa59be677b8c4a7a0ddb6eea0e637e8cc armv8
 recipe id: protobuf/3.21.9-yyyyy myremote-name
 recipe id: protobuf/3.21.9-zzzzz myremote-name
```
This mode searchs in all remotes

```bash
python3 search_arch.py protobuf --arch armv8 
Remote to be searched: all
 recipe id: protobuf/3.21.9-xxx myremote-name
  - package id: 37691084913a549db21760184828e74c3afe89fc armv8
  - package id: 62b64e6800f6acd9ea299d62011a3a4502d5a89a armv8
  - package id: 85d9f875d9f2389ee1d949ad8230f9bc1193f31e armv8
  - package id: cc322c1fa59be677b8c4a7a0ddb6eea0e637e8cc armv8
 recipe id: protobuf/3.21.9-yyyyy myremote-name
 recipe id: protobuf/3.21.9-zzzzz myremote-name
```
