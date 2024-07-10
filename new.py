import blynklib

# Initialize Blynk with your authentication token
BLYNK_AUTH = '2lh5RXl6w52MxgKyMps_Mjf9d2qQqjYp'  # Replace with your Blynk auth token
blynk = blynklib.Blynk(BLYNK_AUTH)

# Define functions for different actions
def function_0(pin, value):
    print('Function 0 triggered with value:', value[0])

def function_1(pin, value):
    print('Function 1 triggered with value:', value[0])

def function_2(pin, value):
    print('Function 2 triggered with value:', value[0])

def function_3(pin, value):
    print('Function 3 triggered with value:', value[0])

def function_4(pin, value):
    print('Function 4 triggered with value:', value[0])

# Set the handlers using the decorators
@blynk.handle_event('write V0')
def virtual_pin_handler(pin, value):
    function_0(pin, value)

@blynk.handle_event('write V1')
def virtual_pin_handler(pin, value):
    function_1(pin, value)

@blynk.handle_event('write V2')
def virtual_pin_handler(pin, value):
    function_2(pin, value)

@blynk.handle_event('write V3')
def virtual_pin_handler(pin, value):
    function_3(pin, value)

@blynk.handle_event('write V4')
def virtual_pin_handler(pin, value):
    function_4(pin, value)

# Start Blynk background thread
blynk.run()
