```python
logs = ["dig1 8 1 5 1","let1 art can", "dig2 3 6", "let2 own kit dig","let3 art zero"]
letters , digits =[],[]

for log in logs:
       if log.split()[1].isdigit():
              digits.append(log)

       else:
              letters.append(log)


letters.sort(key=lambda x:(x.split()[1:],x.split()[0]))


print(letters + digits)

>>> ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']
```

# 주요함수
1) isdigit : 문자열이 숫자로 구성되어 있는지 판별해줌
2) sort와 key 인수
