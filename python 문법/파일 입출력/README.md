# shutil
```python
import shutil

dir(shutil)
```

# shutil.chown
![image](https://user-images.githubusercontent.com/73323188/121682975-b5c12900-caf7-11eb-9cc1-a9166cf7d881.png)

linux 운영체제로 예를 들면,  다음과 같이 각 file은 r,w,x등의 권한을 갖는다. 

shutil.chown은 이러한 권한을 수정해주는 함수다.

# shutil.copy
```python
shutil.copy('Path/filename', 'Path/new filename')
```
filename과 path는 생략 할 수 있다. 


# shutil.copytree
directory는 그냥 copy할 수 없다.
linux의 cp -r과 같다




