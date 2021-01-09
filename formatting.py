# formatting (%로 변수 넣기)
a = "I eat %d apples." % 3
print(a)

b = "I eat %s apples." % "five"
print(b)

number=3
bb = "I eat {0} apples".format(number)
print(bb)

number =10
day="three"
c1 = "I ate %d apples. so I was sick for %s days." % (number, day)
print("c1= "+c1)

c2 = "I ate {number} apples. so I was sick for {day} days.".format(number=10, day="three")
print("c2= "+c2)

d = "Error is %d%%" % 98
print(d)

# %10s: 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 그 앞의 나머지는 공백으로 남겨두라는 의미
e1 = "%10s" % "hi"
print("e1= "+e1)

e2 = "{0:>10}".format("hi")
print("e2= "+e2)

# 위와 반대로 왼쪽으로 정렬
f = "%-10s" % "hi"
g = "%-10sjane" % "hi" # 전체 길이 10인 문자열 공간에서 hi를 맨 왼쪽으로 정렬 후 빈칸 여백 모두 채운 이후 jane
print(f)
print(g)

# 가운데 정렬
i = "{0:^10}".format("hi")+"가운데 정렬 되었는가?"
print("i= "+i)

# 

# 소수(float) 표현 시 소수점 몇째짜리까지 표현하는지
h = "%0.4f" % 3.4543565
print(h)

