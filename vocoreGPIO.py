'''
This library is public domain. Enjoy!
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

    if mode == True or mode.lower() == "true" or mode.lower() == "1" or mode.lower() == "output" or mode.lower() == "out" or mode == 1 or mode == 1.0: #Any of this parameters leads to put the pin as OUTPUT
        value = "out"
    elif mode == False or mode.lower() == "false" or mode.lower() == "0" or mode.lower() == "input" or mode.lower() == "in" or mode == 0 or mode == 0.0: #Any of this parameters leads to put the pin as INPUT
        value = "in"

    file_direc.write(value)
    file_direc.close()


def digitalWrite(num_pin, state):                                                                                                        
    pin_path = "/sys/class/gpio/gpio%d/" % num_pin                                                                                    
    file_direc = file(pin_path + "direction", "r") #Gets the info if the pin is in OUTPUT mode. We can only use digitalWrite on pins in OUTPUT mode.
    pin_mode = file_direc.read()                                                                                                           
    file_direc.close()                               
                                                  
    if pin_mode == "out" or pin_mode == "out\n" or pin_mode == "out \n":
        value = "1"                                                     
        file_value = file(pin_path + "value", "w") #Opens the file that determinates if the pin is setted as ON or OFF.
                                                                        
        if state == True or state.lower() == "true" or state.lower() == "1" or state.lower() == "high" or state.lower() == "on" or state == 1 or state == 1.0: #Any of this parameters leads to put the pin as "ON"
            value = "1"                                                                                                        
        elif state == False or state.lower() == "false" or state.lower() == "0" or state.lower() == "low"  or state.lower() == "off" or state == 0 or state == 0.0: #Any of this parameters leads to put the pin as "OFF"
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
