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

## pkg_summary

Prints specified fields (options or settings) of all packages of a recipe.

This example prints shared, arch and os for all recipes in all remotes:

```bash
python3 pkg_summary.py openssl --noptions shared --nsettings arch os
Remote to be searched: all
Selected options: ['shared']
Selected settings: ['arch', 'os']
 recipe id: openssl/1.1.1-xxxxx myremote-name 18
0508f825aee0fe3099a5dae626a5316104c6db0a True x86_64 Linux 
1748639999ed79b998e4fe4a6d292ed8e874736a True x86_64 Linux 
30eae4e50fefe0f7b788ed8928ac248681ea6af0 True x86_64 Linux 
39e80bc050aeb2ecadd03cf65e7771e739516fe7 False x86_64 Linux 
3fb49604f9c2f729b85ba3115852006824e72cab False x86_64 Windows 
49811ba046f0d899709dc404026e745db1ef4d8f True x86_64 Linux 
 recipe id: openssl/1.1.1-syyyyy myremote-name 10
30eae4e50fefe0f7b788ed8928ac248681ea6af0 True x86_64 Linux 
3fb49604f9c2f729b85ba3115852006824e72cab False x86_64 Windows 
49811ba046f0d899709dc404026e745db1ef4d8f True x86_64 Linux 
d057732059ea44a47760900cb5e4855d2bea8714 False x86_64 Windows 
...
```
