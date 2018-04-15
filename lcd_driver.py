'''
Directly connects to the pump relays in PUMP_SETTINGS make sure to have the correct
BCM number of the GPIO pins attached to the relay that control the pump.
'''
import threading
import time
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
        while True:
            # This file should be only called from drink_server.py, that's where State is declared
            inventory = State.inventory
            recipes = State.recipes
            avail_recipes = [] # A list of recipe objects
            display_lines = ["Available drinks:"]
            
            # Add available recipes to avail_recipes for selection
            for recipe in recipes:
                possible = True
                for ingredient in recipe.ingredients:
                    # If inventory doesn't contain all of the necessary ingredients don't add
                    if ingredient not in inventory:
                        possible = False
                if possible:
                    avail_recipes.append(recipe)
            
            if not avail_recipes:
                display_lines = ["No drinks avail"]
            else:
                for recipe in avail_recipes:
                    display_lines.append(recipe.recipe_name)
            
            #
            # Detect button inputs
            # Handle selection of recipe
            if lcd.is_pressed(LCD.SELECT):
                if index != 0 and index < len(display_lines):
                    # Shift the index down one to compensate for "Availible drinks" offset
                    converted_index = index -1
                    selected_recipe = avail_recipes[converted_index]
                    make_drink_queue.append(selected_recipe.dict_obj)
            
            # Toggle blink with the right arrow
            if lcd.is_pressed(LCD.RIGHT):
                self.blink = not self.blink
                lcd.blink(self.blink)
                
            # Handle up and down scrolling of menu
            if lcd.is_pressed(LCD.UP):
                if index > 0:
                    index += 1
            if lcd.is_pressed(LCD.DOWN):
                if index < len(display_lines):
                    index -= 1
            #
            # Print menu to display
            lcd.clear()
            message = display_lines[index]
            # If there is a line below, display that too
            if (index + 1) < len(display_lines):
                message += "\n" + display_lines[index+1]
            lcd.message(display_lines[index])            
            

if __name__ == "__main__":
    #pd = PumpThread('slot_one', 3)
    #pd.start()
    DP = DrivePump()
    DP.start()
    time.sleep(1)
    DrivePump.pump_queue.append({"slot_one": 3})
    time.sleep(3)
    DrivePump.pump_queue.append({"slot_one": 2})
