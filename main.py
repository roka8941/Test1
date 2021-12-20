'''
파이썬 자료형
* 자료형을 확인하는 함수: type() *
1. 숫자
  - 정수(int)
    ex) 
    >>> type(1000000)
    <class 'int'>
  - 부동소수점수(float)
    ex)
    >>> type(2.8)
    <class 'float'>

2. 시퀀스
  - 문자열(str)
    ex)
    >>> type("I love you.")
    <class 'str'>
  - 리스트(list)
    ex)
    >>> type(["I", "love", "you"])
    <class 'list'>
  - 튜플(tuple)
    ex)
    >>> type(('I', 'love', 'you'))
    <class 'tuple'>

3. 매핑
  - 딕셔너리(dict)
    ex)
    >>> type({'one': 1, 'two': 2, 'three': 3})
    <class 'dict'>

4. 불
  - 불(bool)
    ex)
    >>> type(False)
    <class 'bool'>
    >>> type(3 >= 1)
    <class 'bool'>

5. 세트
  - 세트(set)
    ex)
    >>> type({'apple', 'banana', 'orange'})
    <class 'set'>
'''









'''
Your program should prompt the user for a name, and print out a greeting to the name. The output has to match exactly in this case including spaces and newlines and punctuations. Italic characters are what the user entered.

ex)
Enter your name: Emma
Hello, Emma!
Enter your age: 18
You will be 19 next year.
'''

name = input("Enter your name: ")
print("Hello, {}!".format(name))
# print(f"Hello, {name}!")
age = int(input("Enter your age: "))
print("You will be {} next year.".format(age + 1))