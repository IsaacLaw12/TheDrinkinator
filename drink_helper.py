'''
This file starts a desktop GUI to interact with the Drinkinator 9000
running on a raspberry pi.  The commands are sent through PubNub.
Authors:
    Alex Undy
    Isaac Law
    Sabrina White
'''
import pickle
import json

class Recipe:
    def __init__(self, recipe_name=None, options=None, recipe_dict=None):
        '''
        Initialize the recipe. A recipe only requires two drinks, the other two are optional
        Options are tuples and have the format (drink_name, amount). Amount is an integer
        value. 1 amount = 10 seconds of pumping or about 15 mL of fluid.
        
        If recipe_name is omitted then a recipe_dict can be passed in to recreate a recipe
        instance from a saved dictionary.  This should be formatted in the same way as returned
        by the dict_obj method.
        Procedure for sending Recipe objects:
        Get jsonifiable version of Recipe by calling:
            Multiple - jsonable_recipes = [recipe.dict_obj() for name, recipe in State.recipes.items()]
            Single - jsonable_recipes = [ recipe.dict_obj() ]
        Receive json version of Recipe:
            # Takes first tuple out of message_queue, and iterates through the recipe list at index 2
            for recipe in Message_Handler.message_queue[0][2]: 
                recreated = Recipe(recipe_dict=recipe)
            
        '''
        if recipe_name:
            # Create new recipe from recipe_name and options
            self.recipe_name = recipe_name
            self.ingredients = {}
            if len(options) < 2:
                raise ValueError("Recipe requires at least two drinks. Not enough given: " + str(options))
            for opt in options:
                if opt:
                    # Set the ingredient name in the dictionary and assign it the amount
                    self.ingredients[opt[0]] = opt[1]
        elif recipe_dict:
            # Recreate Recipe from dictionary representation
            #recipe_dict = json.loads(recipe_dict)[0]
            print("Recipe dict is: " + str(recipe_dict))
            # Create object from dictionary
            if 'recipe_name' not in recipe_dict:
                raise KeyError("Recipe cannot be created from incorrectly formatted dictionary")
            self.recipe_name = recipe_dict['recipe_name']
            self.ingredients = {}
            for key in recipe_dict:
                if key is not "recipe_name":
                    self.ingredients[key] = recipe_dict[key]


    def dict_obj(self):
        # Return a dict representation of Recipe, useful for JSON encoding
        recipe_dict = {
                'recipe_name': self.recipe_name,
            }
        for ingredient in self.ingredients:
            recipe_dict[ingredient] = self.ingredients[ingredient]
        return recipe_dict

    def __repr__(self):
        print_string = "\n" + self.recipe_name + ": \n"
        for ingr in self.ingredients:
            print_string += "    " + ingr + " - " + str(self.ingredients[ingr]) + "\n"
        return print_string


class State:
    '''
    A class to hold the current state of the program.  This class is static
    and not intended to be instantiated.  Reference attributes and methods
    using state.foo or state.bar()
    '''
    saved_state_fn = "state.pkl"
    
    # The only values should be strings that are also found in ingredients
    inventory = {
        "slot_one": None,
        "slot_two": None,
        "slot_three": None,
        "slot_four": None,
        }
    
    # Format: "ingredient name" just a string
    ingredients = []
    # Format "recipe_name":  actual recipe object
    recipes = {}
    
    @staticmethod
    def to_string():
        print_me = ""
        print_me += "Slot Inventory: " + str(State.inventory) + "\n"
        print_me += "Ingredients: " + str(State.ingredients) + "\n"
        print_me += "Recipes: " + str(State.recipes) + "\n"
        return print_me
    
    @staticmethod
    def process_request(request_type, request_data):
        if request_type == "add_ingredients":
            print("setting ingredient")
            for new_in in request_data:
                print("Checking if unique")
                if new_in not in State.ingredients:
                    print("it is unique")
                    State.ingredients.append(new_in)
            State.ingredients = sorted(State.ingredients, key=str.lower)
            State.save_state()
        elif request_type == "set_inventory":
            State.inventory = request_data
            State.save_state()
        elif request_type == "add_recipes":
            for recipe in request_data:
                recipe_obj = Recipe(recipe_dict = recipe)
                # If recipe exists update it, otherwise add to list
                State.add_recipe(recipe_obj)
        else:
            print("Request type: " + request_type + " not recognized")
    
    @staticmethod
    def clear_state():
        # Should only be used for testing, deletes all variables
        State.load_state()
        # Save a copy
        with open("backup"+State.saved_state_fn, "wb") as output:
            pickle.dump(State.inventory, output)
            pickle.dump(State.ingredients, output)
            pickle.dump(State.recipes, output)
        State.inventory = {
            "slot_one": None,
            "slot_two": None,
            "slot_three": None,
            "slot_four": None,
        }
        State.ingredients = []
        State.recipes = {}
    
    @staticmethod
    def load_state():
        try:
            with open(State.saved_state_fn, "rb") as input:
                State.inventory = pickle.load(input)
                State.ingredients = pickle.load(input)
                State.recipes = pickle.load(input)
        except FileNotFoundError:
            pass

    @staticmethod
    def save_state():
        with open(State.saved_state_fn, "wb") as output:
            pickle.dump(State.inventory, output)
            pickle.dump(State.ingredients, output)
            pickle.dump(State.recipes, output)

    @staticmethod
    def set_inventory(slot_name, new_value):
        # Specify which ingredient is in slot_name
        if slot_name in State.inventory:
            State.inventory[slot_name] = new_value
        else:
            print("Error incorrect slot name")
        State.save_state()

    @staticmethod
    def add_recipe(new_recipe):
        recipe_name = new_recipe.recipe_name
        # Add a recipe, if it already exists then update it
        if recipe_name in State.recipes:
            State.recipes[recipe_name] = new_recipe
        else:
            State.recipes[recipe_name] = new_recipe
        State.save_state()

    @staticmethod
    def delete_recipe(recipe_name):
        # Remove the recipe and save changes
        if recipe_name in State.recipes:
            State.recipes.pop(recipe_name)
        State.save_state()

    @staticmethod
    def add_ingredient(ingredient_name):
        # Add an ingredient, should just be a string aka "Orange juice"
        State.ingredients.append(ingredient_name)
        State.save_state()

    @staticmethod
    def delete_ingredient(ingredient_name):
        State.ingredients.remove(ingredient_name)
        State.save_state()


