from watchdog.events import FileSystemEventHandler
consonant_letters: list = ['й', 'ц', 'к', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'в', 'п', 'р', 'л', 'д', 'ж', 'ч', 'с' , 'м', 'т', 'б', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

class FileShedule(FileSystemEventHandler):
    def on_created(self, event):
        file_name: str = event.src_path.split("\\")
        name: str = file_name[-1].split(".")
        name_second: str = name[0]
        name_second.lower()
        for w in name_second:
            if w in consonant_letters:
                print(w.upper())
            else:
                print(w.lower())