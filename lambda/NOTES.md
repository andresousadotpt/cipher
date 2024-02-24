# How to install python packages into lambda functions
```bash
$ pip install --platform manylinux2014_x86_64 \ 
    --target=<folder_for_function> \ 
    --implementation cp \
    --python-version 3.9 \
    --only-binary=:all: --upgrade <package>
```
then zip it and send to lambda function, or through github actions to deploy the lambda function