#문자열
#문자열은 문자, 단어 등으로 구성된 문자들의 집합을 말한다.
"Life is too short, You need Python"
"a"
"123"

#문자열의 사용
#", ', """, '''
"Hello World"
'Python is fun'
"""Life is too short, You need python"""
'''Life is too short, You need python'''

#문자열 안에 작은따옴표나 큰따옴표를 추가하고 싶을 때
#Python's favorite food is perl과 같이 문자에 작은따옴표가 있을 때 문자열을 큰따옴표로 둘러싸이면 문자열로 만들 수 있다.
Python's favorite food is perl
food = "Python's favorite food is perl"

"Python is very easy." he says.
say = '"Python is very easy." he says.'

#여러줄을 문자열에 대입
#여러줄을 문자열에 대입하고 싶을 때 백슬래시(\)n을 사용할 수 있다. 또는 ''', """으로도 가능하다.
multiline = "Life is too short\nYou need python"
print(multiline)
Life is too short
You need python

multiline='''
... Life is too short
... You need python
... '''
multiline="""
... Life is too short
... You need python
... """
print(multiline)
Life is too short
You need python