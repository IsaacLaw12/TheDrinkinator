'''
    This program should run on startup of the raspberry pi.  IT monitors pubnub for drink requests and
    converts these requests into hardware commands for the raspberry pi.  The raspberry pi is connected
    to pumps which will dispense drinks when activated
'''

class Drink_Server:
    def __init__(self):
        load_state()
        # Load settings from saved file 
        
    def run(self):
        #while (True):
        pass
    def dump_state(self):
        pass
    def load_state(self):
        pass
    def process_request():
        pass
    def send_request():
        pass
    def send_drink_signals():
        pass
    def populate_lcd_screen():
        pass
    def receive_lcd_inputs():
        pass

if __name__ == "__main__":
    server_instance = Drink_Server()
    server_instance.run()
