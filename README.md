# TheDrinkinator

Current status of drink_client.py:
GUI is barely there. The only useful functionality is that there are two tabs which 
contain frames.  These frames are where the two different windows need to be built.
 An important thing we need to figure out is what layout manager to use.
All of the commands that use .pack() refer to the pack layout manager, but it is very limited.
Elements can't be positioned around the screen at all, they just fill it up. 

Maybe look into the grid layout manager to help line up elements, or any other layout
manager that looks like it might work.  I'm pretty sure you can only use one layout 
manager at a time though. So if you're working with grid make sure that all the .pack()
commands are gone. 

Also it would be good to figure out how frames work. They're like boxes to store screen 
elements on, and it might be helpful to have several different frames in the window.