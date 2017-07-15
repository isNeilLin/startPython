# 列表推导式

l1 = [x * x for x in range(1,10)]
print(l1)

l2 = [x * x for x in range(1,10) if x % 2 == 0]
print(l2)

l3 = [x + y for x in range(1,10) for y in range(11,13)]
print(l3)

L = ['Hello', 'World', 18, 'Apple', None]
lowerL = [s.lower() for s in L if isinstance(s,str)]
print(lowerL)

# 生成器

g = (x * x for x in range(1,10))
for n in g:
    print(n)

def odd():
    yield('step 1')
    yield('step 2')
    yield('step 3')

o = odd()
for x in o:
    print(x)

# 斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    yield 'done'

for x in fib(6):
    print(x)