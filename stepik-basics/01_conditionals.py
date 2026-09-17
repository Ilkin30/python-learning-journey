# ==========================================
# Stepik: Conditional Logic (if / elif / else)
# ==========================================

# 1. Вес боксёра
weight = int(input())

if weight < 60:
    print('Легкий вес')
elif weight < 64:
    print('Первый полусредний вес')
elif weight < 69:
    print('Полусредний вес')


# 2. Количество дней в месяце
month = int(input())

if month == 2:
    print('28')
elif month in (4, 6, 9, 11):
    print('30')
else:
    print('31')


# 3. Серединное число
a, b, c = int(input()), int(input()), int(input())

if a < b < c or c < b < a:
    print(b)
elif c < a < b or b < a < c:
    print(a)
else:
    print(c)


# 4. Ход ладьи
x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')


# 5. Ход короля
x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

if -1 <= x1 - x2 <= 1 and -1 <= y1 - y2 <= 1:
    print('YES')
else:
    print('NO')
