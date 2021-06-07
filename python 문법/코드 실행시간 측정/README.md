# 코드 실행시간 측정

__1) ipython %time magic method 활용__ 

%time 명령어를 사용하면 코드가 실행되는 시간을 출력해준다.
```
#ipython enviorment

%time for i in range(10): print(i,end=' ')
0 1 2 3 4 5 6 7 8 9 CPU times: user 0 ns, sys: 0 ns, total: 0 ns
Wall time: 14.3 µs
```

작성되어 있는 모듈파일(.py)이 걸리는 시간도 확인가능하다.
```
%time !python test.py
0 1 2 3 4 5 6 7 8 9 CPU times: user 0 ns, sys: 31.2 ms, total: 31.2 ms
Wall time: 101 ms
```
