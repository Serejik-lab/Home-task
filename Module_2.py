def generate_password (n):
    generate = ''

    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                generate += f'{i}{j}'
    return generate

n = int(input("Введите число от 3 до 20: "))
if 3<=n<=20:
    password = generate_password(n)
    print(f"Пароль для числа {n}: {password}")
else:
    print("Введено некорректное число")