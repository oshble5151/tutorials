# 빅오 표기법이란?

입력값이 무한히 커질때, 함수의 상한선을 설명하는 표기법이다.

빅오 표기법은 알고리즘의 효율성을 분석하는데 매우 유용하게 활용되는 표기법이며 알고리즘의 시간복잡도와 공간복잡도를 분석하는데 사용된다.

__*시간복잡도와 공간복잡도__
- 시간 복잡도: 알고리즘이 수행되는데 걸리는 시간
- 공간 복잡도: 알고리즘의 메모리 점유율

# 빅오(big-O), 빅오메가(big-Ω), 빅세타(big-θ)

__빅오 표기는 기본적으로 특정 함수 실행의 상한과 하한을 의미한다.__

1) 빅오(big-O) : 가장 늦게 실행될때(하한)
2) 빅오메가(big-Ω): 가장 빠르게 실행될때(상한)
3) 빅세타(big-θ): 평균적인 실행속도

# python 주요 자료형 Method의 시간복잡도
참고 및 출처(https://wiki.python.org/moin/TimeComplexity)

# list
![image](https://user-images.githubusercontent.com/73323188/120968137-71eebc80-c7a3-11eb-91d0-ec65a3c6aba4.png)

# collections.deque
![image](https://user-images.githubusercontent.com/73323188/120968262-96e32f80-c7a3-11eb-971f-aca74981968f.png)

# set
![image](https://user-images.githubusercontent.com/73323188/120968430-d3af2680-c7a3-11eb-89da-4f04251ea0e1.png)

# dict
![image](https://user-images.githubusercontent.com/73323188/120968656-15d86800-c7a4-11eb-8af4-85c8c851a953.png)

__*dict는 대부분의 시간복잡도가 O(1)로 처리된다는 장점이 있다.__


