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
food="Python's favorite food is perl"

"Python is very easy." he says.
say='"Python is very easy." he says.'

#여러줄을 문자열에 대입
#여러줄을 문자열에 대입하고 싶을 때 백슬래시(\)n을 사용할 수 있다. 또는 ''', """으로도 가능하다.
multiline="Life is too short\nYou need python"
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

#문자열 연산
#연산은 숫자만 가능한 것이 아니다. 문자열을 연산하는 것도 가능하다.
head="Python"
tail=" is fun!"
head+tail
'Python is fun!'

a="python"
a*2
'pythonpython'

#문자열 길이 구하기
#문자열의 글자 수를 구할 수 있다.
a="Life is too short"
len(a)
17

#문자열 인덱싱
a="Life is too short, You need Python"
 Life is too short, You need Python
#0         1         2         3
#0123456789012345678901234567890123
#위처럼 문자열의 각 문자마다 번호를 매겨볼 수 있다. *파이썬은 숫자를 0부터 센다.
#따라서 아래와 같이 인덱싱을 해보면(3번째 글자를 검색해 보면) f가 아닌 e가 나오는 것을 알 수 있다. 또, 문자열을 뒤에서부터 읽고 싶으면 마이너스를 붙이면 된다.(a[-1]은 뒤에서 첫 번째를 의미한다.
a="Life is too short, You need Python"
a[3]
'e'
a[-1]
'n'

#문자열 슬라이싱
#문자열 인덱싱은 글자를 뽑아내는 코드였다. 하지만 단어를 뽑아내고 싶으면 대괄호 안에 시작과 끝을 지정해 주면 된다.(꼭 시작번호를 0으로 하지 않아도 된다.)
a="Life is too short, You need Python"
a[0:4]
'Life'
#근데 한 가지 이상한 점이 있다. 'Life'는 0123인데 왜 [0:4]라고 하는가? 이유는 다음과 같다.
#0은 a보다 크거나 같고, 3은 a보다 작기 때문에 a[0:3]로 했을 때 012만 출력되는 것이다. 이때 띄어쓰기도 포함되니 주의하자.

#a[시작번호:끝 번호]에서 시작번호와 끝 번호 둘 중 하나를 생략할 수도 있다.([:8]=처음부터~8, [8:]=8~끝까지)
a="20010331Rainy"
date=a[:8]
weather=a[8:]
date
'20010331'
weather
'Rainy'

#문자열 포매팅
#문자열 안에 숫자, 문자열을 삽입할 수 있다.
"I eat %d apples." %3
'I eat 3 apples.'

"I eat %s apples." %"five"
'I eat five apples.'

number=3
"I eat %d apples." %number
'I eat 3 apples.'

number=10
day = "three"
"I ate %d apples. so I was sick for %s days." %(number, day)
'I ate 10 apples. so I was sick for three days.'

#%를 삽입하고 싶다면 "Error is %d%." %98가 아닌
"Error is %d%%." %98
'Error is 98%.'
#로 해야 된다.

#문자열 포매팅 응용
#1. 정렬과 공백
"%10s"%"hi"
'        hi'
#여기서 %10s는 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 그 앞의 나머지는 공백으로 남겨두라는 의미이다.
"%-10sjane."%'hi'
'hi        jane.'
#반대쪽인 왼쪽 정렬은 %-10s을 해주면 된다.
"{0:^10}".format("hi")
'    hi    '
#가운데 정렬은 :^로 정렬 가능하다.

#2. 소수점 표현하기
"%0.4f"%3.42134234
'3.4213'
#3.42134234를 소수점 네 자리까지만 나타내고 싶을 때 0.4를 사용한 것이다.

#문자열 관련 함수들
#1. 문자 개수 세기
a="hobby"
a.count('b')
2
#문자열 중 b의 개수를 돌려준다.

#2. 위치 알려주기(find)
a="Python is the best choice"
a.find('b')
14
a.find('k')
-1
#찾는 문자나 문자열이 존재하지 않는다면 -1을 반환한다.

#2-1. 위치 알려주기(index)
a="Life is too short"
a.index('t')
8
#위와 같이 t가 두 번 들어간 경우 index를 통해 가장 처음으로 나온 t를 반환한다.

#3. 문자열 삽입
",".join('abcd')
'a,b,c,d'

#4. 소문자를 대문자로 바꾸기
a="hi"
a.upper()
'HI'

#4-1. 대문자를 소문자로 바꾸기
a="HI"
a.lower()
'hi'

#5. 문자열 바꾸기
a="Life is too short"
a.replace("Life", "Your leg")
'Your leg is too short'

#6. 문자열 나누기
a="Life is too short"
a.split()
['Life', 'is', 'too', 'short']