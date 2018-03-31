from tkinter import ttk
from tkinter import *
import tkinter as tk

class DrinkApp():
	def __init__(self): #self, *args, **kwargs
		#tk.Tk.__init__(self, *args, **kwargs)
		# Setup main window
		self.root = tk.Tk()
		self.root.title("The Drinkinator")
		self.root.geometry('{}x{}'.format(500, 500))
		self.notebook = ttk.Notebook(self.root)
		
		# Setup main pages
		self.home = ttk.Frame(self.notebook)
		self.settings = ttk.Frame(self.notebook)
		
		self.home.grid_rowconfigure(1, weight=1)
		self.home.grid_columnconfigure(0, weight=1)
		
		# Setup home page
		
		# Setup drink name frame
		self.home_drink_name_frame = tk.Frame(self.home, bg="cyan", padx=5, pady=5)
		self.home_drink_name_frame.grid(row=0, pady = 10, padx = 20)
		
		# Setup drink labels
		self.home_drink_one = tk.Label(self.home_drink_name_frame, text="Drink one")
		self.home_drink_one.pack()
		self.home_drink_two = tk.Label(self.home_drink_name_frame, text="Drink two")
		self.home_drink_two.pack()
		self.home_drink_three = tk.Label(self.home_drink_name_frame, text="Drink three")
		self.home_drink_three.pack()
		self.home_drink_four = tk.Label(self.home_drink_name_frame, text="Drink four")
		self.home_drink_four.pack()
		
		# Setup drink select frame
		self.home_drink_select_frame = tk.Frame(self.home, bg="lavender", padx=5, pady=5)
		self.home_drink_select_frame.grid(row=1)
		
		# Setup drink select
		self.home_drink_options = ["Wow", "some good drinks here", "this one looks pretty good huh?", "nice"]
		self.home_drink_selected = tk.StringVar(self.home_drink_select_frame)
		self.home_drink_selected.set(self.home_drink_options[0])
		
		self.home_drink_select = tk.OptionMenu(self.home_drink_select_frame, self.home_drink_selected, *self.home_drink_options)
		self.home_drink_select.pack()
		
		# Setup drink slider frame
		self.home_drink_slider_frame = tk.Frame(self.home, bg="white", padx=5, pady=5)
		self.home_drink_slider_frame.grid(row=2)
		
		# Setup drink sliders
		self.home_slider_one = Scale(self.home_drink_slider_frame, from_=0, to=100, orient=HORIZONTAL)
		self.home_slider_one.pack()
		self.home_slider_two = Scale(self.home_drink_slider_frame, from_=0, to=100, orient=HORIZONTAL)
		self.home_slider_two.pack()
		self.home_slider_three = Scale(self.home_drink_slider_frame, from_=0, to=100, orient=HORIZONTAL)
		self.home_slider_three.pack()
		self.home_slider_four = Scale(self.home_drink_slider_frame, from_=0, to=100, orient=HORIZONTAL)
		self.home_slider_four.pack()
		
		# Setup start frame
		self.home_start_frame = tk.Frame(self.home, bg="white", padx=5, pady=5)
		self.home_start_frame.grid(row=3)
		
		# Setup start button
		self.home_start_button = tk.Button(self.home_start_frame, text = "!START!", command = self.start_activated)
		self.home_start_button.pack()
		
		# Add tabs to notebook
		self.notebook.add(self.home, text="Home")
		self.notebook.add(self.settings, text="Settings")
		self.notebook.pack(expand=1, fill="both")
		
		# Start main loop
		self.root.mainloop()
	def full_update(self):
		pass
	def start_activated(self):
		print("DRINK UP BABY")


if __name__== "__main__":
    app = DrinkApp()
    app.full_update()
