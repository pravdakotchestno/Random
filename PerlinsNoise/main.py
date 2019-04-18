#TODO


from tkinter import *
from math import *

LAYER_WIDTH = 512

def noise(x):
	x = (x<<13) ^ x
	return 1.0 - ((x * (x * x * 15731 + 789221) + 1376312589) & 0x7fffffff) / 1073741824.0

def merge_layers(layer1, layer2):
	layer3 = [[.0] * LAYER_WIDTH] * LAYER_WIDTH
	for y in range(LAYER_WIDTH):
		for x in range(LAYER_WIDTH):
			layer3[y][x] = layer1[y][x] + layer2[y][x]
	return layer3

def return_layer(seed, layer_num):
	field = [[.0] * LAYER_WIDTH] * LAYER_WIDTH
	for y in range(2 ** layer_num):
		for x in range(2 ** layer_num):
			for sy in range(LAYER_WIDTH // (2 ** layer_num)):
				for sx in range(LAYER_WIDTH // (2 ** layer_num)):
					field[y + sy][x + sx] = noise((x * LAYER_WIDTH + y) ^ seed) / 2 ** layer_num
	return field

def return_full(seed):
	full = [[.0] * LAYER_WIDTH] * LAYER_WIDTH
	for i in range(9):
		full = merge_layers(full, return_layer(seed, i))
	return full

def num_to_hex_color(num):
	num = int((num / 4 + 0.5) * 255)
	return '#%02x0000'%num

def draw_noise(canvas, field):
	for y in range(512):
		for x in range(512):
			canvas.create_rectangle(x, y, 1, 1, fill=num_to_hex_color(field[y][x]))
'''
def linear_interpolation(a, b, x):
	return  a * (1 - x) + b * x

def cos_interpolation(a, b, x):
	ft = x * PI
	f = (1 - cos(ft)) * .5
	return  a * (1 - f) + b * f

current_interpolation_algo = None
'''
class App:
	
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		self.canvas = Canvas(master, width=512, height=512)
		self.canvas.pack()
		'''
		self.label = Label(master, text='Which interpolation algorithm use?')
		self.label.pack()
		Radiobutton(master, text="Linear", variable=current_interpolation_algo, value=linear_interpolation).pack(anchor=W)
		Radiobutton(master, text="Cos", variable=current_interpolation_algo, value=cos_interpolation).pack(anchor=W)
		'''
		field = return_full(0)
		draw_noise(self.canvas, field)

root = Tk()
app = App(root)

root.mainloop()