# try except문 

try except문으로 오류가 발생했을 경우를 컨트롤 할 수 있다. 

except : error가 발생했을 경우의 수행문

else: 예외가 발생하지 않아 except 절을 실행하지 않았을 경우 실행되는 절

finally : 예외 발생여부와 상관없이 수행되는 절


```python

try: 4/0
     
except:
       print('error')
else:
       print('else')
finally:
       print('end')
>>>
error
end
```

except만 적을경우 모든 에러에 대해서 수행되고, error를 명시할 경우 해당 에러에 대해서만 except문을 수행한다.

