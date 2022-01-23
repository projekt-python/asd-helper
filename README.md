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
You can examine `pre-commit` and `pre-push` file in root directory to see commands being run.

### Install package
To run tests you can install package in editable state with
```
pip3 install -e .

```
You need to be in project root directory when you run above command (i.e. in the directory that conatins setup.py)

