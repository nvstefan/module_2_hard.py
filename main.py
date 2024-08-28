# Дополнительное практическое задание
# по модулю: "Основные операторы"

def password_gen(m):
    password = ''
    for i in range(1, m):
        for j in range(i + 1, m):
            if m % (i + j) == 0:
                password += str(i) + str(j)
    return password

m = int(input('Введите число :'))
while (20 < m or m < 3):
    m = int(input('Число должно быть от 3 до 20, введите снова :'))

result = password_gen(m)
print('Пароль:', result)