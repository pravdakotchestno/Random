from tkinter import *

def noise(a):
	return (1000 - (((a << 17) - a ^ 0xDEADBEEF) ** 24) % 2000) / 1000

def linear_interpolation():
	pass

def cos_interpolation():
	pass

def cubic_interpolation():
	pass

current_interpolation_algo = None

class App:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		self.canvas = Canvas(master, width=512, height=512)
		self.canvas.pack()
		self.label = Label(master, text='Which interpolation algorithm use?')
		self.label.pack()
		Radiobutton(master, text="Linear", variable=current_interpolation_algo, value=linear_interpolation).pack(anchor=W)
		Radiobutton(master, text="Cos", variable=current_interpolation_algo, value=cos_interpolation).pack(anchor=W)
		Radiobutton(master, text="Cubic", variable=current_interpolation_algo, value=cubic_interpolation).pack(anchor=W)
root = Tk()
app = App(root)

root.mainloop()