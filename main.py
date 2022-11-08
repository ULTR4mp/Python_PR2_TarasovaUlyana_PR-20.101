try:
    while True:
        print("Введите название файла : ")
        true: bool = True
        Name: str = input()
        if Name.isalpha() and len(Name) > 3:
            file: str = f"C:\\TarasovaUlyana555\\{Name}.txt"
            with open(file, "w"): #create file
                print("Файл создан")
        else:
            print("Данные введены неккоректно, попробуйте еще раз")
except Exception:
    print("Произошла ошибка")
except KeyboardInterrupt:
    print("Заверешение работы")