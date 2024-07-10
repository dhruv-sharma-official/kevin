import psutil
import os
import vnt_engine
import serial
import serial.tools.list_ports
import subprocess

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math

def speak(audio_file):  # defining speak function
    vnt_engine.speak(audio_file)

class hardinfo():
    class battery():
        def charge():
            battery = psutil.sensors_battery().percent
            return battery
        def power_plug():
            battery = psutil.sensors_battery().power_plugged
            return battery
            

class adjust():
    def brightness_battery():
        if hardinfo.battery.charge()<=50:
            adjust.brightness(30, "percent")
            speak('backup systems activated')
        if hardinfo.battery.charge()>=51 and hardinfo.battery.charge()<=80:
            adjust.brightness(60, "percent")
            speak('battery optimization active')
        if hardinfo.battery.charge()>=81:
            adjust.brightness(80, "percent")
            speak('power is sufficient, no need for power preprocessor')

    def brightness(num,typ):
        command = 'powershell -Command "(Get-CimInstance -Namespace root/WMI -ClassName WmiMonitorBrightness).CurrentBrightness"'
        try:
            output = subprocess.check_output(command, shell=True, text=True)
            current_brightness = int(output.strip())
            print(f"current brightness level {current_brightness}")
        except Exception as e:
            print(f"Error: {e}")
            current_brightness = None
        currentbri = current_brightness
        # print(currentbri, type(currentbri))
        if num == currentbri:
            action = 'already'
        elif num > currentbri:
            action = 'increased to'
        elif num < currentbri:
            action = 'decreased to'
        else:
            action = ""
        if 0<=num<=100:
            os.system(f'powershell -Command "(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{num})"')
            if typ == 'percent':
                speak(f'brightness level is {action} {num} percent')
            elif typ == 'level':
                num = num /10
                speak(f'brightness level is {action} level {int(num)}')
            else:
                speak(f'hardware malfuntioned')
                return SystemError
        else:    
            speak(f"sir, brightness level {num} cannot be achieved, hardware doesnot support it")
            

    def volume(num):
        # Get default audio device using PyCAW
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        # Get current volume 
        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolumeDb - 1.0, None)
        print(currentVolumeDb)
        # NOTE: -6.0 dB = half volume
        
    def power(mode):
        pass


var2 = [True, 'unchanged']
def btrycheck():
    var1 = hardinfo.battery.power_plug()  # to store if charging or not
    if hardinfo.battery.power_plug() != var2[0]:
        print(hardinfo.battery.power_plug())
        var2[0] = hardinfo.battery.power_plug()
        if hardinfo.battery.power_plug() == False and var2[1] == 'changed':
            speak('Charger Disconnected')
            adjust.brightness_battery()
        if hardinfo.battery.power_plug() == True and var2[1] == 'changed':
            speak('Charger Connected')
            adjust.brightness_battery()
        var2[1] = 'changed'
    else:
        pass


def directsend(inp):
    arduinoData = ""
    result = "connection not established"
    print(f'type of inp is {type(inp)}')  #======================
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if ('USB-SERIAL CH340' in port.description):
            port_value = port.device
            arduinoData = serial.Serial(port_value,9600)
            result = "connection established"
            print(f"{result} at {port}")
        else:
            pass
            
    if ('connection established' in result):
        cmd = inp.encode('utf-8')
        arduinoData.write(bytes(cmd))
        print(f'type of cmd is {type(cmd)}')
        print('data sent!')
        arduinoData.close()
    if ('connection not established' in result):
        print("connection failed!")
        
            
# if __name__ == "__main__":
#     directsend('A')
#     print('executed!')
