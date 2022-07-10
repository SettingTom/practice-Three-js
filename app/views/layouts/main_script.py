import os
import eel

def main():

    eel.init('web')
    eel.start('index.html', port=0, size=(800, 600))

    pass


@eel.expose
def run_python():

    files = os.listdir()
    print(files)
    eel.sleep(3)
    return files

if __name__ == '__main__':
    try:
        main()
    except Exception:
        pass