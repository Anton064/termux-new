import os
def newMenu():
    print("""
    1. Обновить фон пользователя.
    2. Проверить обновление termux.
    3. Установить обновление termux.
    4. Обновить репозиторий
    5. Выход
    """)
    menu = input("Выберите функцию: ")

    if menu == "1":
        os.system("bash .update.sh")
    elif menu == "2":
        os.system("pkg install update -y")
    elif menu == "3":
        os.system("pkg install upgrade -y")
    elif menu == "4":
        pass
    elif menu == "5":
        os.system("clear && cd && clear")
    else:
        print("Неверно повторите попитку.")
        newMenu()
if __name__ == __name__:
    newMenu()