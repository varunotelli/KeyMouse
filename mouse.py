import pip
pip.main(['install','pynput'])
from pynput import keyboard
from pynput.mouse import Controller,Button

mouse=Controller()
def on_press(key):

    try:
        if key==keyboard.Key.up:
        	#pyautogui.dragRel(0,-10)
        	mouse.move(0,-20)
        	print('alphanumeric key {0} pressed'.format(key.char))
        if key==keyboard.Key.left:
        	mouse.move(-20,0)
        	print('alphanumeric key {0} pressed'.format(key.char))
        if key==keyboard.Key.down:
        	mouse.move(0,20)
        	print('alphanumeric key {0} pressed'.format(key.char))
        if key==keyboard.Key.right:
        	mouse.move(20,0)
        	print('alphanumeric key {0} pressed'.format(key.char))
        if key==keyboard.Key.ctrl_r:
        	mouse.press(Button.left)
        	mouse.release(Button.left)
        if key.char=='2':
            mouse.scroll(0,-2)
        if key.char=='8':
            mouse.scroll(0,2)
        #pyautogui.dragTo(posx, posy)
        print('alphanumeric key {0} pressed'.format(key.char))

    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    if key==keyboard.Key.esc:
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()