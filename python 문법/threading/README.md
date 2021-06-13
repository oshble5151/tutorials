# thread 란

프로그램이 메모리에서 실행중인 상태를 process라고 한다.

thread는 프로세스의 실행단위를 의미하며, 프로세스는 최소 하나 이상의 thread를 가져야 한다.

비유하자면 process는 일터이고, thread는 일터에서 일하는 기술자에 해당한다.

따라서 한 process에서 여러 thread가 수행되는것, 즉 한 일터에서 여러 기술자가 동시에 작업을 수행하는 것이 병행실행(Concurrent execution) 이다.


![image](https://user-images.githubusercontent.com/73323188/121796903-99d49900-cc57-11eb-8ff2-c8ebd629dfd2.png)



![image](https://user-images.githubusercontent.com/73323188/121796993-30a15580-cc58-11eb-80b1-88722c9b9f3b.png)




# python threding

```python
import threading

class process:
	def __init__(self,name):
		self.process_name = name
	def excution(self):
		for _ in range(0,3):
			print(self.process_name+ 'runiing\n')
			time.sleep(0.3)

process1 = process('process1')
process2 = process('process2')
process3 = process('process3')

process1.excution()
process2.excution()
process3.excution()
>>>
process1runiing

process1runiing

process1runiing

process2runiing

process2runiing

process2runiing

process3runiing

process3runiing

process3runiing
```
