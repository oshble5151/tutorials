# 트리

트리Tree => 하나의 뿌리에서 위로 뻗어나가는 형상.

트리구조는 위 -> 아래 개념을 컴퓨터에서 표현한 구조다.

재귀로 정의된 자기참고의 자료구조를 가지고 있는것이 특징이다.

이는 트리가 서브트리로 구성되어있음을 의미한다.


트리의 구성은 다음과 같다.

![image](https://user-images.githubusercontent.com/73323188/121768360-d42b3100-cb98-11eb-9508-a133e5aa0f70.png)

Degree(차수) : 자식노드의 개수 

Size(크기) : 자신을 포함한 모든 자식노드의 개수

Height(높이) : 현재 위치에서 leaf까지의 거리

Depth(깊이) : 루트에서 부터 현재노드 까지의 거리 

# 트리와 그래프의 차이

트리는 그래프에 포함되며, 트리는 __순환구조를 갖지 않는다.__

# 트리가 아닌 경우

1) 순환구조인 경우
![image](https://user-images.githubusercontent.com/73323188/121768870-89f77f00-cb9b-11eb-8e63-bafb379f54cf.png)

2) 노드의 부모가 2개 일때
![image](https://user-images.githubusercontent.com/73323188/121768881-9c71b880-cb9b-11eb-8043-a12ffb01149e.png)

3) 루트가 2
