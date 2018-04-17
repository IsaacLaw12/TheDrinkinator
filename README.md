# TheDrinkinator
Status: 
GUI has all the necessary elements, functionality is in the process of being added.
Drink related requests can successfully be sent between different computers over pubnub.
State can be loaded and saved to a pickle file.  Recipes can be added, edited, and deleted.
Slot inventory can be set and cleared.  Ingredients can be added and deleted.

# Install Dependencies
 Easy way:
 The Pubnub API can be installed with pip install 'pubnub>=4.0.13'
 Pubnub can then just be imported into pubnub_interface.py like the default.

 Harder way:
 The Pubnub API can be downloaded with git clone https://github.com/pubnub/python
 The directory where it is downloaded to then has to be pointed to by the sys.path.insert
 line that is commented out at the top of pubnub_interface.py.

# Install Client
 On the computer that should run the client open up keychain_dist.py.  Add your pubnub keys
 to the file.  Close it and rename the file to keychain.py.  If the default computer name
 of "client" works for you then run the GUI with python3 drink_app.py.
 The computer name can be changed by opening up drink_app.py and changing the name where
 Message_Handler is instantiated.
 
# Install Server
 Server has been tested on a Raspberry Pi.  The setup was to have four relays controlled by 
 GPIO pins: (FILE THIS IN). These relays each control a peristaltic pump for dispensing liquids.
 If you are controlling your relay from different GPIO pins then make sure to open up drink_server.py
 and change the GPIO pins that are used by default.  The tested setup also had a 16x2 lcd display
 with button controls.  
 The tested screen can be found here: https://www.adafruit.com/product/1115?gclid=EAIaIQobChMI57C9tbGa2gIVVp7ACh0y1ACFEAYYASABEgIOrfD_BwE
 This screen is not necessary for running the server, but it provides a way to start drinks directly
  from the Raspberry Pi.
 On the computer that should run the server open up keychain_dist.py.  Add your pubnub keys
 to the file.  Close it and rename the file to keychain.py.  If the default computer name
 of "server" works for you then run the server with python3 drink_server.py
