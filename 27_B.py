f = list(map(int, open('27_B.txt').readlines()[1:]))
n = len(f)
s = 0

for i in range(1, n // 2):
    s += (f[i] + f[-i]) * i  # первый раз считаем время, для первого дома
s += f[n // 2] * (n // 2)

change = 0
for i in range(1, n // 2 + 1):
    change -= f[i]  # элементы с 1 до середины отнимаются
for i in range(n // 2 + 1, n + 1):
    change += f[i % n]  # а остальные прибавляются

res = s
r = 0
for i in range(1, n):
    s += change
    if s < res:
        r = i + 1
        res = s
    change += f[i] * 2 - f[(i + n // 2) % n] * 2  # прибавляем 2 * i-й элемент и отнмиаем 2 * противоположнй элемент
print(r)  # ответ 1612820
