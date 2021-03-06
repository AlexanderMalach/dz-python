a = int(input("Введите количество км в первый день пробежки "))
b = int(input("Введите желаемый результат в км "))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print(f"Желаемый результат будет достигнут на %.d день" % result_days)