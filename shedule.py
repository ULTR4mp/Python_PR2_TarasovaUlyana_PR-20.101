import time #модуль времени для функции time.sleep()
from watchdog.observers import Observer #для мониторинга событий файловой системы.
from shedule_class import FileShedule  #из файла shedule_class импортируем класс FileShedule
observer = Observer() #Паттерн "Наблюдатель"
event_handler = FileShedule() #передаем в переменную класс
path: str = r"C:\TarasovaUlyana555" #создаем путь к папке
observer.schedule(event_handler, path=path, recursive=True) #наблюдатель следит за нашим путем используя класс
observer.start() #мы получаем фоновый поток, следящий за изменениями
try:
    while True:
        time.sleep(1) #откладывает исполнение текущего потока на 1 секунду
except:
    print("Произошло исключение")
finally:
    observer.stop() #останавливаем поток
    observer.join() #без нее просто не работает