'''
Directly connects to the pump relays in PUMP_SETTINGS make sure to have the correct
BCM number of the GPIO pins attached to the relay that control the pump.
'''
import threading
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

PUMP_SETTINGS =  {
    "slot_one" : 17,
    "slot_two" : 27,
    "slot_three": 22,
    "slot_four": 23,    
    }

class DrivePump(threading.Thread):
    '''
    Should run the entire time that the server is running. To create a drink
    Maintains a queue of waiting drink requests, and sends out the signals to
    run the pumps if they are not busy
    '''
    pump_queue = [] # Should contain dictionaries with format: "slot_name": time
    
    def __init__(self):
        threading.Thread.__init__(self)
        # Turn off all the relays
        for slot_name, pin in PUMP_SETTINGS.items():
            GPIO.setup(pin, GPIO.LOW)
            GPIO.setup(pin, GPIO.HIGH)

    def run(self):
        while True:
            # Continually check for pour requests
            if DrivePump.pump_queue:
                current_pour = DrivePump.pump_queue.pop(0)
                print("CURRENT POUR " + str(current_pour))
                time_to_complete = 0
                # Iterate through slot names and times, start a thread to control the pour
                for slot_name, pour_time in current_pour.items():
                    if pour_time > time_to_complete:
                        time_to_complete = pour_time
                    PumpThread(slot_name, pour_time).start()
                # Give pumps time to finish pour
                time.sleep(time_to_complete)
            # Pause to allow new requests to come in / pours to finish
            time.sleep(.1)
                    

class PumpThread(threading.Thread):
    '''
    Starts a thread that turns one GPIO pin on and off to run the
    controlled pump for the correct amount of time.
    '''
    def __init__(self, slot_name, length_run):
        threading.Thread.__init__(self)
        self.slot_name = slot_name
        self.length_run = length_run
        
    def run(self):
        # Turn a pump on for the specified amount of time in seconds
        print("running slot "+str(self.slot_name) +" for "+str(self.length_run)+ " seconds")
        pin_number = PUMP_SETTINGS[self.slot_name]
        
        GPIO.setup(pin_number, GPIO.HIGH)
        GPIO.setup(pin_number, GPIO.LOW)
        time.sleep(self.length_run)
        GPIO.setup(pin_number, GPIO.HIGH)
        print("done with " + str(self.slot_name))


if __name__ == "__main__":
    #pd = PumpThread('slot_one', 3)
    #pd.start()
    DP = DrivePump()
    DP.start()
    time.sleep(1)
    DrivePump.pump_queue.append({"slot_one": 3})
    time.sleep(3)
    DrivePump.pump_queue.append({"slot_one": 2})
