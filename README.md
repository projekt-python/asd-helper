# asd-helper
Package containing algorithms and tests required for Algorithm and Data Structures class at AGH University in Kraków


## Setup
### Git hooks
Run this snippet to enable lint checks and automatic formatting before commit/push.
```
cp pre-push ./.git/hooks/
cp pre-commit ./.git/hooks/
chmod +x ./.git/hooks/pre-commit
chmod +x ./.git/hooks/pre-push
```

### Install package
To run tests you can install package in editable state with
```
pip3 install -e .

```
You need to be in proejct root directory when you run above command (i.e. in the directory that conatins setup.py)