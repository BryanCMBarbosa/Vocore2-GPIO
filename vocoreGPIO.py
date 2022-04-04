'''
library is public domain. Enjoy!
Based on the original C++ commands for pin control in Arduino (https://www.arduino.cc/)
Made by Bryan Barbosa (Github: BryanCMBarbosa) from Federal University of Juiz de Fora and CREA Lab - UC Berkeley
'''

import time

def pinMode(num_pin, mode): #Defines pin mode as OUTPUT or 
    config = file('/sys/class/gpio/export', 'w') #exporting the GPIO%num_pin
    config.write(str(num_pin))
    config.close()

    pin_path = "/sys/class/gpio/gpio%d/" % num_pin #directory where all the files for controlling the pin <num_pin> are stored
    file_direc = file(pin_path + "direction", "w") #Opens the file to write data. If we write "out", the pin goes to OUTPUT mode, if we write "in", the pin goes to INPUT mode.
    value = "out"

    '''
    If mode is setted as True, "true", "1", "output", "out", 1 or 1.0, the pin will be setted as output.
    Else, pin will be setted as input.
    '''
    if type(mode) is bool: #Any of this parameters leads to put the pin as OUTPUT
        if mode:
            value = "out"
        else:
            value = "in"

    elif type(mode) is str:
        mode = mode.lower()
        if mode  == "true" or mode == "1" or mode == "output" or mode == "out":
            value = "out"
        else:
            value = "in"

    elif type(mode) is int or type(mode) is float:
        if mode == 1 or mode == 1.0:
            value = "out"
        else:
            value = "in"

    else:
        value = "in"

    file_direc.write(value)
    file_direc.close()


def digitalWrite(num_pin, state):                                                                                                        
    pin_path = "/sys/class/gpio/gpio%d/" % num_pin                                                                                    
    file_direc = file(pin_path + "direction", "r") #Gets the info if the pin is in OUTPUT mode. We can only use digitalWrite on pins in OUTPUT mode.
    pin_mode = file_direc.read()                                                                                                           
    file_direc.close()                               

    '''
    If state is setted as True, "true", "1", "high", "on", 1 or 1.0, the pin will be setted in high state.
    Else, the pin will be setted in low state. 
    '''                                                  
    if pin_mode == "out" or pin_mode == "out\n" or pin_mode == "out \n":
        value = "0"                                                     
        file_value = file(pin_path + "value", "w") #Opens the file that determinates if the pin is setted as ON or OFF.
        
        if type(state) is bool:                                                                
            if state:
                value = "1"
            else:
                value = "0"

        elif type(state) is str:
            state = state.lower()
            if state == "true" or state == "1" or state == "high" or state == "on":
                value = "1"
            else:
                value = "0"

        elif type(state) is int or type(state) is float:
            if state == 1 or state == 1.0:
                value = "1"
            else:
                value = "0"

        else:
            value = "0"
                                                                                                                                  
        file_value.write(value)                                                                                                      
        file_value.close()                                                                                                           
                                                                                                                                  
    else:                                                                                                                         
        print("Pin {} is not in OUTPUT mode.".format(num_pin))                                                                    
                                                                                                                                  
                                                                                                                                  
def digitalRead(num_pin):                                                                                                         
    pin_path = "/sys/class/gpio/gpio%d/" % num_pin                                                                                
    file_value = file(pin_path + "value", "r") #Gets info about the pin state      
    state = file_value.read()                                     
    file_value.close()                                           
                                                              
    if state == "1" or state == "1\n" or state == "1 \n": #If the pin is setted as ON or is receiving a reading, the return will be 1        
        return 1                                              
                                                              
    return 0                                                  
                                                      
                                                      
def delay(t): #Delay in Milliseconds                                      
    time.sleep((t/1000))                              


def delayMicroseconds(t): #Delay in Microseconds
    time.sleep((t/1000000))