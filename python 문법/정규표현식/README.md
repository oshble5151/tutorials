# 정규표현식

정규표현식은 일정한 규칙을 가진 문자열을 표현하는 방법이다.

## 1) re.match 특정 문자열 포함 여부
```python
re.match('regular','regular expression')
>>>
<re.Match object; span=(0, 7), match='regular'>
```
## 2) 문자열이 맨 앞에 오는지 여부 판단
정규 표현식은 특정 문자열이 맨 앞에 오는지 뒤에 오는지 판단할 수 있다.

^ : 문자열이 맨 앞에 오는지 판단
$ : 맨 뒤에 오는지 판단

```python

re.search('^regular','regular expression')
>>>
<re.Match object; span=(0, 7), match='regular'>

re.search('regular$','regular expression')
>>>
<re.Match object; span=(8, 18), match='expression'>
