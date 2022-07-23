# 27_A
f = list(map(int, open('27_A.txt').readlines()[1:]))  # Считываем все значения, кроме первого, в список
n = len(f)
res = 10 ** 10
r = 0
for i in range(n):
    s = 0
    for j in range(1, n // 2 + 1):  # проходимся по всем значениям в списке от первого элемента до середины
        s += f[(j + i) % n] * j + f[(i - j + n) % n] * j  # считаем сумму с двух сторон
    if s < res:
        res = s
        r = i + 1
print(r)  # ответ 160
