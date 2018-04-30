'''
Directly connects to the pump relays in PUMP_SETTINGS make sure to have the correct
BCM number of the GPIO pins attached to the relay that control the pump.
'''
from drink_helper import *
import threading
import time
import sys
sys.path.insert(0, '../Adafruit/Adafruit_Python_CharLCD')
import Adafruit_CharLCD as LCD

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()
lcd.blink(True)

class DriveLCD(threading.Thread):
    '''
    Displays list of available recipes to create. Allows the user to select
    them and start creating
    '''
    make_drink_queue = [] # Should contain dictionaries with format: "slot_name": time
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.blink = True

    def run(self):
        buttons = (LCD.SELECT, LCD.UP, LCD.DOWN)
        # Used to keep track of where the user is in the menu
        menu_index = 0 
        write_new = True
        time_of_last_send = time.time()
        while True:
            inventory = [ingredient for slot_name, ingredient in State.inventory.items()]
            #print("inventory is " + str(inventory))
            recipes = State.recipes
            avail_recipes = [] # A list of recipe objects
            display_lines = ["Avail drinks:"]
            
            # Add available recipes to avail_recipes for selection
            for name,recipe in recipes.items():
                possible = True
                for ingredient in recipe.ingredients:
                    if ingredient == "recipe_name":
                        continue
                    # If inventory doesn't contain all of the necessary ingredients don't add
                    if ingredient not in inventory:
                        #print(name + " not possible because " + ingredient + " is missing")
                        possible = False
                if possible:
                    avail_recipes.append(recipe.dict_obj())
            
            if not avail_recipes:
                display_lines = ["No drinks avail"]
            else:
                for avail_rec in avail_recipes:
                    display_lines.append(avail_rec["recipe_name"])
            #
            # Detect button inputs
            # Handle selection of recipe
            if lcd.is_pressed(LCD.SELECT):
                if (time.time() - time_of_last_send) < 10:
                    pass
                if menu_index != 0 and menu_index < len(display_lines):
                    # Shift the menu_index down one to compensate for "Availible drinks" offset
                    converted_index = menu_index -1
                    selected_recipe = avail_recipes[converted_index]
                    self.make_drink_queue.append(selected_recipe)
                    time_of_last_send = time.time()
                    print(self.make_drink_queue)
            
            # Toggle blink with the right arrow
            if lcd.is_pressed(LCD.RIGHT):
                self.blink = not self.blink
                lcd.blink(self.blink)
                
            # Handle up and down scrolling of menu
            if lcd.is_pressed(LCD.UP):
                if menu_index > 0:
                    write_new = True
                    menu_index -= 1
            if lcd.is_pressed(LCD.DOWN):
                if menu_index < (len(display_lines)-1):
                    write_new = True
                    menu_index += 1
            #
            # Print menu to display
            if write_new:
                lcd.clear()
                message = display_lines[menu_index]
                # If there is a line below, display that too
                if (menu_index + 1) < len(display_lines):
                    message += "\n" + display_lines[menu_index+1]
                lcd.message(message)
                write_new = False
            time.sleep(.2)
    
