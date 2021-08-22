'''
This library is public domain. Enjoy!
Based on the original C++ commands for pin control in Arduino (https://www.arduino.cc/)
Made by Bryan Barbosa (Github: BryanCMBarbosa) from Federal University of Juiz de Fora and CREA Lab - UC Berkeley
'''

import time

def pinMode(num_pin, mode):
    pin_path = "/sys/class/gpio/gpio%d/" % num_pin
    f_direc = file(pin_path + "direction", "w")
    value = "out"

    if mode == True or mode.lower() == "true" or mode.lower() == "1" or mode.lower() == "output" or mode.lower() == "out" or mode == 1 or mode == 1.0:
        value = "out"
    elif mode == False or mode.lower() == "false" or mode.lower() == "0" or mode.lower() == "input" or mode.lower() == "in" or mode == 0 or mode == 0.0:
        value = "in"

    f_direc.write(value)
    f_direc.close()


def digitalWrite(num_pin, mode):                                                                                                        
    pin_path = "/sys/class/gpio/gpio%d/" % num_pin                                                                                      
    f_direc = file(pin_path + "direction", "r")                                                                                         
    pin_mode = f_direc.read()                                                                                                           
    f_direc.close()                               
                                                  
    if pin_mode == "out" or pin_mode == "out\n" or pin_mode == "out \n":
        value = "1"                                                     
        f_value = file(pin_path + "value", "w")                         
                                                                        
        if mode == True or mode.lower() == "true" or mode.lower() == "1" or mode.lower() == "high" or mode == 1 or mode == 1.0:
            value = "1"                                                                                                        
        elif mode == False or mode.lower() == "false" or mode.lower() == "0" or mode.lower() == "low" or mode == 0 or mode == 0.0:
            value = "0"                                                                                                           
                                                                                                                                  
        f_value.write(value)                                                                                                      
        f_value.close()                                                                                                           
                                                                                                                                  
    else:                                                                                                                         
        print("Pin {} is not in OUTPUT mode.".format(num_pin))                                                                    
                                                                                                                                  
                                                                                                                                  
def digitalRead(num_pin):                                                                                                         
    pin_path = "/sys/class/gpio/gpio%d/" % num_pin                                                                                
    f_value = file(pin_path + "value", "r")                   
    mode = f_value.read()                                     
    f_value.close()                                           
                                                              
    if mode == "1" or mode == "1\n" or mode == "1 \n":        
        return 1                                              
                                                              
    return 0                                                  
                                                      
                                                      
def delay(t):                                         
    time.sleep((t/1000))                              


def delayMicroseconds(t):
    time.sleep((t/1000000))
