## shutil
```python
import shutil

dir(shutil)
```

## shutil.chown
![image](https://user-images.githubusercontent.com/73323188/121682975-b5c12900-caf7-11eb-9cc1-a9166cf7d881.png)

linux 운영체제로 예를 들면,  다음과 같이 각 file은 r,w,x등의 권한을 갖는다. 

shutil.chown은 이러한 권한을 수정해주는 함수다.

## shutil.copy
```python
shutil.copy('Path/filename', 'Path/new filename')
```
filename과 path는 생략 할 수 있다. 


## shutil.copytree
directory는 그냥 copy할 수 없다.
linux의 cp -r과 같다

## os.mkdir

## shutil.retree

오직 directory만 지울수 있음

# linux ls 명령어 구현
```python
for dirName, subDirList, fnames in os.walk('C://Windows//debug'):
       for fname in fnames:
              os.path.join(dirName,fname)
```
## os.walk
dirpath, dirnames, filenames이 들어있는 generator를 생성해준다.

## file directory check
os.path.exist("C")
os.path.isfile
os.path.isdir

## removefile
os.remove => dir는 삭제되지 않는다.

## size check

os.path.getsize
