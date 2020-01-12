import stepik67

print("Все в рамках одних суток")
print("Введите количество часов и минут. В ответ получите общее количество минут")
x = int(input())
y = int(input())
print(stepik67.minutes_from_hm(x, y))

print("Введите количество минут. В ответ получите количество часов и минут")
m = int(input())
for x in stepik67.minutes_to_hm(m):
    print(x)


print("Введите количество минут, затем часы и минуты, к которым их нужно прибавить. Ответ - часы, минуты")
X = int(input())
H = int(input())
M = int(input())

for x in stepik67.hm_plus_minutes_to_hm(X, H, M):
    print(x)
