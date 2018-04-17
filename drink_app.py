
from tkinter import ttk
from tkinter import *
import tkinter as tk
from drink_helper import State, Recipe
from pubnub_interface import Message_Handler

class DrinkApp():
    def __init__(self):
        self.message_handler = Message_Handler("client", "server")
        # Setup main window
        self.root = tk.Tk()
        self.root.title("The Drinkinator")
        #self.root.geometry("500x500")
        self.root.resizable(height=False)
        self.notebook = ttk.Notebook(self.root)
        
        # Setup main pages
        self.home = ttk.Frame(self.notebook)
        self.settings = ttk.Frame(self.notebook)
        
        self.home.grid_rowconfigure(0, weight=1)
        self.home.grid_rowconfigure(1, weight=1)
        self.home.grid_rowconfigure(2, weight=1)
        self.home.grid_columnconfigure(0, weight=1)
    
        
        self.settings.grid_rowconfigure(0, weight=1)
        self.settings.grid_rowconfigure(1, weight=1)
        self.settings.grid_rowconfigure(2, weight=1)
        self.settings.grid_columnconfigure(0, weight=1)
        
        # Setup home page
        
        ######################## Setup drink name frame
        self.home_drink_name_frame = tk.Frame(self.home,  bg="light cyan", padx=20, pady=20)
        self.home_drink_name_frame.grid(sticky = "nsew", row=0)
        
        self.home_drink_name_frame.grid_rowconfigure(0, weight=1)
        self.home_drink_name_frame.grid_rowconfigure(1, weight=1)
        self.home_drink_name_frame.grid_rowconfigure(2, weight=1)
        self.home_drink_name_frame.grid_columnconfigure(0, weight=1)
        self.home_drink_name_frame.grid_columnconfigure(1, weight=1)
        
        # setup drink discription
        self.home_current_bottles = tk.Label(self.home_drink_name_frame, bg = "light cyan", text="The current bottles in the Drinkinator are set to:")
        self.home_current_bottles.grid(row = 0, columnspan = 2, pady = 2, padx = 2, sticky = "nsew")
        
        # Setup drink labels
        self.home_drink_one = tk.Label(self.home_drink_name_frame, text="Slot 1: " + "Drink 1", bg = "light cyan", anchor = "w")
        self.home_drink_one.grid(row = 1,  pady = 2, padx = 2, sticky = "nsew")
        self.home_drink_two = tk.Label(self.home_drink_name_frame, text="Slot 2: " + "Drink 2", bg = "light cyan", anchor = "w")
        self.home_drink_two.grid(row = 1, column = 1,  pady = 2, padx = 2, sticky = "nsew")
        self.home_drink_three = tk.Label(self.home_drink_name_frame, text="Slot 3: " + "Drink 3", bg = "light cyan", anchor = "w")
        self.home_drink_three.grid(row = 2,  pady = 2, padx = 2, sticky = "nsew")
        self.home_drink_four = tk.Label(self.home_drink_name_frame, text="Slot 4: " + "Drink 4", bg = "light cyan", anchor = "w")
        self.home_drink_four.grid(row = 2, column = 1,  pady = 2, padx = 2, sticky = "nsew")
        
        ##################### Setup drink select frame
        self.home_drink_select_frame = tk.Frame(self.home,  bg="light cyan", padx=20, pady=20)
        self.home_drink_select_frame.grid(sticky = "nsew", row=1)
        
        self.home_drink_select_frame.grid_rowconfigure(0, weight=1)
        self.home_drink_select_frame.grid_columnconfigure(0, weight=1)
        
        
        # Setup drink select
        self.home_drink_options = ["Choose a drink"]
        self.home_drink_selected = tk.StringVar(self.home_drink_select_frame)
        self.home_drink_selected.set("Select drink")        
        
        self.home_drink_select = tk.OptionMenu(self.home_drink_select_frame, self.home_drink_selected, "select a value")
        self.home_drink_select.grid(pady = 2, padx = 2, sticky = "nsew")
        
        
        ############3 Setup drink slider frame
        self.home_drink_slider_frame = tk.Frame(self.home, bg="light cyan", padx=20, pady=20)
        self.home_drink_slider_frame.grid(sticky = "nsew", row=2)
        
        self.home_drink_slider_frame.grid_rowconfigure(0, weight=1)
        self.home_drink_slider_frame.grid_rowconfigure(1, weight=1)
        self.home_drink_slider_frame.grid_rowconfigure(2, weight=1)
        self.home_drink_slider_frame.grid_rowconfigure(3, weight=1)
        self.home_drink_slider_frame.grid_rowconfigure(4, weight=1)
        self.home_drink_slider_frame.grid_columnconfigure(0, weight=1)
        
        # setup slider discription
        self.home_sliders = tk.Label(self.home_drink_slider_frame, text="Slide to select the ratios below")
        self.home_sliders.grid(row = 0, columnspan = 2, pady = 2, padx = 2, sticky = "nsew")
        
        # Setup drink sliders
        self.home_slider_one = Scale(self.home_drink_slider_frame, label = "none",  bg = "white", from_=0, to=10, orient=HORIZONTAL)
        self.home_slider_one.grid(sticky = "nsew", row = 1)
        self.home_slider_two = Scale(self.home_drink_slider_frame, label = "none", bg = "white", from_=0, to=10, orient=HORIZONTAL)
        self.home_slider_two.grid(sticky = "nsew", row = 2)
        self.home_slider_three = Scale(self.home_drink_slider_frame, label = "none", bg = "white", from_=0, to=10, orient=HORIZONTAL)
        self.home_slider_three.grid(sticky = "nsew", row = 3)
        self.home_slider_four = Scale(self.home_drink_slider_frame, label = "none", bg = "white", from_=0, to=10, orient=HORIZONTAL)
        self.home_slider_four.grid(sticky = "nsew", row = 4)
        
        ##############3 Setup start frame
        
        self.home_start_frame = tk.Frame(self.home, bg="light cyan", padx=20, pady=20)
        self.home_start_frame.grid(sticky = "nsew", row=4)
        
        self.home_start_frame.grid_rowconfigure(0, weight=1)
        self.home_start_frame.grid_columnconfigure(0, weight=1)
        
        # Setup start button
        self.home_start_button = tk.Button(self.home_start_frame, bg = "white", fg = "black", text = "!START!", command = self.start_activated)
        self.home_start_button.grid()
        
        
        
        
        # Setup settings page
        
        ######################################### Setup drink select frame
        self.settings_drink_select_frame = tk.Frame(self.settings, bg="light cyan", padx=20, pady=20)
        self.settings_drink_select_frame.grid(sticky = "nsew", row=0)
        
        self.settings_drink_select_frame.grid_rowconfigure(0, weight=1)
        self.settings_drink_select_frame.grid_rowconfigure(1, weight=1)
        self.settings_drink_select_frame.grid_columnconfigure(0, weight=1)
        self.settings_drink_select_frame.grid_columnconfigure(1, weight=1)
        
        # Setup new drink directions
        self.w = Label(self.settings_drink_select_frame, bg = "light cyan", text="Setup the bottles below, matching the Drinkinator slots")
        self.w.grid(columnspan = 2, sticky = "nsew")
        
        # Setup drink slot 1
        self.settings_ingredient_selected_one = tk.StringVar(self.settings_drink_select_frame)
        self.settings_ingredient_selected_one.set("Empty Slot")
        
        self.settings_ingredient_select_one = tk.OptionMenu(self.settings_drink_select_frame, self.settings_ingredient_selected_one, "Empty Slot")
        self.settings_ingredient_select_one.grid(row = 1, pady = 2, padx = 2, sticky = "nsew")
        
        # Setup drink slot 2
        self.settings_ingredient_selected_two = tk.StringVar(self.settings_drink_select_frame)
        self.settings_ingredient_selected_two.set("Empty Slot")
        
        self.settings_ingredient_select_two = tk.OptionMenu(self.settings_drink_select_frame, self.settings_ingredient_selected_two, "Empty Slot")
        self.settings_ingredient_select_two.grid(column = 1, row = 1, pady = 2, padx = 2, sticky = "nswe")

        
        # Setup drink slot 3
        self.settings_ingredient_selected_three = tk.StringVar(self.settings_drink_select_frame)
        self.settings_ingredient_selected_three.set("Empty Slot")
        
        self.settings_ingredient_select_three = tk.OptionMenu(self.settings_drink_select_frame, self.settings_ingredient_selected_three, "Empty Slot")
        self.settings_ingredient_select_three.grid(row =2, pady = 2, padx = 2, sticky = "nsew")

        
        # Setup drink slot4
        self.settings_ingredient_selected_four = tk.StringVar(self.settings_drink_select_frame)
        self.settings_ingredient_selected_four.set("Empty Slot")
        
        self.settings_ingredient_select_four = tk.OptionMenu(self.settings_drink_select_frame, self.settings_ingredient_selected_four, "Empty Slot")
        self.settings_ingredient_select_four.grid(row = 2, column = 1, pady = 2, padx = 2, sticky = "nsew")


        
        ################################################## Setup new drink slider frame
        self.settings_drink_slider_frame = tk.Frame(self.settings, bg="light cyan", padx=20, pady=20)
        self.settings_drink_slider_frame.grid( sticky = "nsew", row=2)
        
        self.settings_drink_slider_frame.grid_rowconfigure(0, weight=1)
        self.settings_drink_slider_frame.grid_rowconfigure(1, weight=1)
        self.settings_drink_slider_frame.grid_rowconfigure(2, weight=1)
        self.settings_drink_slider_frame.grid_rowconfigure(3, weight=1)
        self.settings_drink_slider_frame.grid_rowconfigure(4, weight=1)
        self.settings_drink_slider_frame.grid_rowconfigure(5, weight=1)
        self.settings_drink_slider_frame.grid_columnconfigure(0, weight=1)
        self.settings_drink_slider_frame.grid_columnconfigure(1, weight=1)
        self.settings_drink_slider_frame.grid_columnconfigure(2, weight=1)
        
        
        # Setup new drink directions
        self.w = Label(self.settings_drink_slider_frame, bg = "light cyan" , text="Add a new recipe. Select Bottles and Ratios below.")
        self.w.grid(sticky = "nsew", column = 0, columnspan = 3)

        
        # Setup drink 1 sliders
        self.settings_slider_one = Scale(self.settings_drink_slider_frame, bg = "white", from_=0, to=10, orient=HORIZONTAL)
        self.settings_slider_one.grid(row = 1, pady = 3, sticky = "nsew",  padx = 3,  column = 1, columnspan = 2)
        
        # Setup drink 1 select
        self.settings_drink_selected_one = tk.StringVar(self.settings_drink_slider_frame)
        self.settings_drink_selected_one.set("Empty Slot")
        self.settings_drink_select_one = tk.OptionMenu(self.settings_drink_slider_frame, self.settings_drink_selected_one, "Empty Slot")
        self.settings_drink_select_one.config(bg = "white", bd = 0)
        self.settings_drink_select_one.grid(row = 1, column = 0,  pady = 3, padx = 3, sticky = "nsew")
        
        # Setup drink 2 slider 
        self.settings_slider_two = Scale(self.settings_drink_slider_frame, bg = "white", from_=0, to=10, orient=HORIZONTAL)
        self.settings_slider_two.grid(row = 2, pady = 3, padx = 3, sticky = "nsew",  column = 1, columnspan = 2)
        
        # Setup drink 2 select
        self.settings_drink_selected_two = tk.StringVar(self.settings_drink_slider_frame)
        self.settings_drink_selected_two.set("Empty Slot")
        self.settings_drink_select_two = tk.OptionMenu(self.settings_drink_slider_frame, self.settings_drink_selected_two, "Empty Slot")
        self.settings_drink_select_two.config(bg = "white", bd = 0)
        self.settings_drink_select_two.grid(row = 2, pady = 3, column = 0,padx = 3, sticky = "nsew")
    
        
        # Setup drink 3 slider
        self.settings_slider_three = Scale(self.settings_drink_slider_frame,  bg = "white", from_=0, to=10, orient=HORIZONTAL)
        self.settings_slider_three.grid(row = 3, pady = 3,padx = 3, sticky = "nsew",  column = 1, columnspan = 2)
        
        # Setup drink 3 select
        self.settings_drink_options = ["Slot ...", "some good drinks here", "this one looks pretty good huh?", "nice"]
        self.settings_drink_selected_three = tk.StringVar(self.settings_drink_slider_frame)
        self.settings_drink_selected_three.set("Empty Slot")
        self.settings_drink_select_three = tk.OptionMenu(self.settings_drink_slider_frame, self.settings_drink_selected_three, "Empty Slot")
        self.settings_drink_select_three.config(bg = "white", bd = 0)
        self.settings_drink_select_three.grid(row = 3, pady = 3, column = 0, padx = 3, sticky = "nsew")
        
        
        # Setup drink4 slider
        self.settings_slider_four = Scale(self.settings_drink_slider_frame,  bg = "white", from_=0, to=10, orient=HORIZONTAL)
        self.settings_slider_four.grid(row = 4, pady = 3, padx = 3, sticky = "nsew", column = 1, columnspan = 2)
        
        # Setup drink4 select
        self.settings_drink_selected_four = tk.StringVar(self.settings_drink_slider_frame)
        self.settings_drink_selected_four.set("Empty Slot")
        self.settings_drink_select_four = tk.OptionMenu(self.settings_drink_slider_frame, self.settings_drink_selected_four, "Empty Slot")
        self.settings_drink_select_four.config(bg = "white", bd = 0)
        self.settings_drink_select_four.grid(row = 4, pady = 3, column = 0, padx = 3, sticky = "nsew")
    
        
        
        # Setup save drink button/name
        self.setting_new_drink_frame_drink = tk.Entry(self.settings_drink_slider_frame)
        self.setting_new_drink_frame_drink.grid(row=5, column=0, columnspan = 2, sticky = 'nsew')
        self.setting_new_drink_frame_drink.insert(0, "New Drink Name")
        
        self.settings_save_button = tk.Button(self.settings_drink_slider_frame, bg = "white", fg = "black", text = "Save", command = self.save_new_drink)
        self.settings_save_button.grid(row = 5, column = 2)
        
        
        ######################################################### Setup add drink frame
        self.settings_new_drink_frame = tk.Frame(self.settings, bg="light cyan", padx=20, pady=20)
        self.settings_new_drink_frame.grid(sticky = "nsew", row=1)
        
        self.settings_new_drink_frame.grid_rowconfigure(0, weight=1)
        self.settings_new_drink_frame.grid_rowconfigure(1, weight=1)
        self.settings_new_drink_frame.grid_columnconfigure(0, weight=1)
        self.settings_new_drink_frame.grid_columnconfigure(1, weight=1)
        self.settings_new_drink_frame.grid_columnconfigure(2, weight=1)
        self.settings_new_drink_frame.grid_columnconfigure(3, weight=1)
        
        # Setup new drink directions
        self.w = Label(self.settings_new_drink_frame, bg = "light cyan", text="This will add the mixer type to possible bottle options")
        self.w.grid(columnspan = 4, sticky = "nsew", pady = 10)
        
        # Setup add drink
        
        self.setting_new_drink_frame_ingredient = tk.Entry(self.settings_new_drink_frame)
        self.setting_new_drink_frame_ingredient.grid(row=1, column=0, columnspan =3, sticky = "nswe")
        self.setting_new_drink_frame_ingredient.insert(0, "new ingredient")
        
        
        self.settings_add_button = tk.Button(self.settings_new_drink_frame, bg = "white", fg = "black", text = "Add", command = self.add_ingredient)
        self.settings_add_button.grid(row = 1, column = 3, columnspan = 1, sticky = "sne")
        
        
        
        
        
        # Add tabs to notebook
        self.notebook.add(self.home, text="Home")
        self.notebook.add(self.settings, text="Settings")
        self.notebook.pack(expand=1, fill="both")
        
        # Start main loop
        self.full_update()
        self.root.mainloop()
        
    def full_update(self):
        avalible_ingrediants = []
        # Remove buttons/slders to start with
        self.home_drink_one.grid_remove()
        self.home_drink_two.grid_remove()
        self.home_drink_three.grid_remove()
        self.home_drink_four.grid_remove()
        self.home_slider_one.grid_remove()
        self.home_slider_two.grid_remove()
        self.home_slider_three.grid_remove()
        self.home_slider_four.grid_remove()
        # Update and re-add buttons/slders if necessary 
        if (State.inventory["slot_one"] != None):
            self.home_drink_one.config(text=("Slot #1: "+State.inventory["slot_one"]))
            self.home_drink_one.grid()
            self.home_slider_one.config(label=State.inventory["slot_one"])
            self.home_slider_one.grid()
            avalible_ingrediants.append(State.inventory["slot_one"])
        if (State.inventory["slot_two"] != None):
            self.home_drink_two.config(text=("Slot #2: "+State.inventory["slot_two"]))
            self.home_drink_two.grid()
            self.home_slider_two.config(label=State.inventory["slot_two"])
            self.home_slider_two.grid()
            avalible_ingrediants.append(State.inventory["slot_two"])
        if (State.inventory["slot_three"] != None):
            self.home_drink_three.config(text=("Slot #3: "+State.inventory["slot_three"]))
            self.home_drink_three.grid()
            self.home_slider_three.config(label=State.inventory["slot_three"])
            self.home_slider_three.grid()
            avalible_ingrediants.append(State.inventory["slot_three"])
        if (State.inventory["slot_four"] != None):
            self.home_drink_four.config(text=("Slot #4: "+State.inventory["slot_four"]))
            self.home_drink_four.grid()
            self.home_slider_four.config(label=State.inventory["slot_four"])
            self.home_slider_four.grid()
            avalible_ingrediants.append(State.inventory["slot_four"])
            
        # Figure out which recipies are currently avalible
        self.home_drink_options = []
        for recipe_name, recipe in State.recipes.items():
            avalible = True
            for value in recipe.ingredients:
                if (value != "recipe_name"):
                    if not (value in avalible_ingrediants):
                        avalible = False
            if (avalible == True):
                self.home_drink_options.append(recipe.recipe_name)
        self.home_drink_selected.set("Select a drink")
        # Clear dropdown values
        self.home_drink_select["menu"].delete(0, 'end')
        # Add new values that call set selection
        for name in self.home_drink_options:
            self.home_drink_select["menu"].add_command(label=name, command = lambda name = name: self.set_selection(name))
        # Setup drink setup drop downs
        self.settings_ingredient_select_one["menu"].delete(0, 'end')
        self.settings_ingredient_select_two["menu"].delete(0, 'end')
        self.settings_ingredient_select_three["menu"].delete(0, 'end')
        self.settings_ingredient_select_four["menu"].delete(0, 'end')
        for ingredient in State.ingredients:
            self.settings_ingredient_select_one["menu"].add_command(label=ingredient, command = lambda ingredient = ingredient: self.set_ingredient(self.settings_ingredient_selected_one, ingredient, "slot_one"))
            self.settings_ingredient_select_two["menu"].add_command(label=ingredient, command = lambda ingredient = ingredient: self.set_ingredient(self.settings_ingredient_selected_two, ingredient, "slot_two"))
            self.settings_ingredient_select_three["menu"].add_command(label=ingredient, command = lambda ingredient = ingredient: self.set_ingredient(self.settings_ingredient_selected_three, ingredient, "slot_three"))
            self.settings_ingredient_select_four["menu"].add_command(label=ingredient, command = lambda ingredient = ingredient: self.set_ingredient(self.settings_ingredient_selected_four, ingredient, "slot_four"))
        self.settings_ingredient_select_one["menu"].add_command(label="Empty Slot", command = lambda: self.set_ingredient(self.settings_ingredient_selected_one, "Empty Slot", "slot_one"))
        self.settings_ingredient_select_two["menu"].add_command(label="Empty Slot", command = lambda: self.set_ingredient(self.settings_ingredient_selected_two, "Empty Slot", "slot_two"))
        self.settings_ingredient_select_three["menu"].add_command(label="Empty Slot", command = lambda: self.set_ingredient(self.settings_ingredient_selected_three, "Empty Slot", "slot_three"))
        self.settings_ingredient_select_four["menu"].add_command(label="Empty Slot", command = lambda: self.set_ingredient(self.settings_ingredient_selected_four, "Empty Slot", "slot_four"))
        self.settings_ingredient_selected_one.set(State.inventory["slot_one"])
        self.settings_ingredient_selected_two.set(State.inventory["slot_two"])
        self.settings_ingredient_selected_three.set(State.inventory["slot_three"])
        self.settings_ingredient_selected_four.set(State.inventory["slot_four"])
        
        self.settings_drink_select_one["menu"].delete(0, 'end')
        self.settings_drink_select_two["menu"].delete(0, 'end')
        self.settings_drink_select_three["menu"].delete(0, 'end')
        self.settings_drink_select_four["menu"].delete(0, 'end')
        for ingredient in State.ingredients:
            self.settings_drink_select_one["menu"].add_command(label=ingredient, command = lambda ingredient = ingredient: self.set_recipe_ingredient(self.settings_drink_selected_one, ingredient))
            self.settings_drink_select_two["menu"].add_command(label=ingredient, command = lambda ingredient = ingredient: self.set_recipe_ingredient(self.settings_drink_selected_two, ingredient))
            self.settings_drink_select_three["menu"].add_command(label=ingredient, command = lambda ingredient = ingredient: self.set_recipe_ingredient(self.settings_drink_selected_three, ingredient))
            self.settings_drink_select_four["menu"].add_command(label=ingredient, command = lambda ingredient = ingredient: self.set_recipe_ingredient(self.settings_drink_selected_four, ingredient))
        self.settings_drink_select_one["menu"].add_command(label="Empty Slot", command = lambda: self.set_recipe_ingredient(self.settings_drink_selected_one, "Empty Slot"))
        self.settings_drink_select_two["menu"].add_command(label="Empty Slot", command = lambda: self.set_recipe_ingredient(self.settings_drink_selected_two, "Empty Slot"))
        self.settings_drink_select_three["menu"].add_command(label="Empty Slot", command = lambda: self.set_recipe_ingredient(self.settings_drink_selected_three, "Empty Slot"))
        self.settings_drink_select_four["menu"].add_command(label="Empty Slot", command = lambda: self.set_recipe_ingredient(self.settings_drink_selected_four, "Empty Slot"))
        print(State.to_string())
    def set_ingredient(self, dropdown, name, slot):
        dropdown.set(name)
        if (name == "Empty Slot"):
            State.set_inventory(slot, None)
        else:
            State.set_inventory(slot, name)
        self.message_handler.fireMessage(request_type="set_inventory", receiver='server', jsonable_obj=State.inventory)
        self.full_update()
    def set_recipe_ingredient(self, dropdown, name):
        dropdown.set(name)
    def set_selection(self, value):
        # Update what the dropdown shows
        self.home_drink_selected.set(value)
        recipe_value = State.recipes[value]
        # Update slider amounts
        self.home_slider_one.set(0)
        self.home_slider_two.set(0)
        self.home_slider_three.set(0)
        self.home_slider_four.set(0)
        if (State.inventory["slot_one"] in recipe_value.ingredients):
            self.home_slider_one.set(recipe_value.ingredients[State.inventory["slot_one"]])
        if (State.inventory["slot_two"] in recipe_value.ingredients):
            self.home_slider_two.set(recipe_value.ingredients[State.inventory["slot_two"]])
        if (State.inventory["slot_three"] in recipe_value.ingredients):
            self.home_slider_three.set(recipe_value.ingredients[State.inventory["slot_three"]])
        if (State.inventory["slot_four"] in recipe_value.ingredients):
            self.home_slider_four.set(recipe_value.ingredients[State.inventory["slot_four"]])

    def start_activated(self):
        # Create a new recipe object and send it too the server
        send_ingredients = []
        if (State.inventory["slot_one"] != None) and (self.home_slider_one.get() > 0):
            send_ingredients.append((State.inventory["slot_one"], self.home_slider_one.get()))
        if (State.inventory["slot_two"] != None) and (self.home_slider_two.get() > 0):
            send_ingredients.append((State.inventory["slot_two"], self.home_slider_two.get()))
        if (State.inventory["slot_three"] != None) and (self.home_slider_three.get() > 0):
            send_ingredients.append((State.inventory["slot_three"], self.home_slider_three.get()))
        if (State.inventory["slot_four"] != None) and (self.home_slider_four.get() > 0):
            send_ingredients.append((State.inventory["slot_four"], self.home_slider_four.get()))
        send_recipe = Recipe("Outgoing Drink", send_ingredients)
        self.message_handler.fireMessage(request_type="make_drink", receiver="server", jsonable_obj=send_recipe.dict_obj())
    def add_ingredient(self):
        print("Added drink ingredient")
        print(self.setting_new_drink_frame_ingredient.get())
        State.add_ingredient(self.setting_new_drink_frame_ingredient.get())
        self.message_handler.fireMessage(request_type="add_ingredients",receiver='server',jsonable_obj=State.ingredients)
        self.full_update()
    def save_new_drink(self):
        print("Saved new Drink")
        name = self.setting_new_drink_frame_drink.get()
        print(name)
        ingredient_amounts = {}
        if (self.settings_drink_selected_one.get() != "Empty Slot") and (self.settings_slider_one.get() > 0):
            ingredient_amounts[self.settings_drink_selected_one.get()] = self.settings_slider_one.get()
        if (self.settings_drink_selected_two.get() != "Empty Slot") and (self.settings_slider_two.get() > 0):
            ingredient_amounts[self.settings_drink_selected_two.get()] = self.settings_slider_two.get()
        if (self.settings_drink_selected_three.get() != "Empty Slot") and (self.settings_slider_three.get() > 0):
            ingredient_amounts[self.settings_drink_selected_three.get()] = self.settings_slider_three.get()
        if (self.settings_drink_selected_four.get() != "Empty Slot") and (self.settings_slider_four.get() > 0):
            ingredient_amounts[self.settings_drink_selected_four.get()] = self.settings_slider_four.get()
        options = []
        for key, value in ingredient_amounts.items():
            options.append((key,value))
        newRecipe = Recipe(name, options)
        State.add_recipe(newRecipe)
        jsonable_recipes = [recipe.dict_obj() for name, recipe in State.recipes.items()]
        self.message_handler.fireMessage(request_type="add_recipes", receiver='server', jsonable_obj=jsonable_recipes)
        self.full_update()
        
if __name__== "__main__":
    State.load_state()
    app = DrinkApp()
