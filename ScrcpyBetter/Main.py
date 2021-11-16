import subprocess

# usb connection
results = subprocess.run(["adb", "usb"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wireless Connection
def Wireless_Con():
    global Wireless_results
    Wireless_results = subprocess.run(["adb", "tcpip", "5555"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#SCRCPY
def Scrcpy():
    global ScrcpyStart
    ScrcpyStart = subprocess.run(["scrcpy"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# User input
WiredORWirles = input(str("Wired   or     Wireless\nWhat type of connection do you want?: "))

# if Wired has been selected
if WiredORWirles == "Wired":
    print("Ok!, Doing Some Work!\n")
    # if stdout is successful
    if results.stdout == b'restarting in USB mode\r\n':
        print("You USB Connection is Sucessfull!\n")
        Scrcpy()
        
    elif results.stderr == b'* daemon not running; starting now at tcp:5037\r\n* daemon started successfully\r\n':
        results
        if results.stdout == b'restarting in USB mode\r\n':
            print("Your USB Connection is Sucessfull!\n")
        
    elif results.stderr == b'* daemon not running; starting now at tcp:5037\r\n* daemon started successfully\r\nerror: no devices/emulators found\r\n':
        print("The connection is unsucessful :(\n Common fixes to try:\n - Check if your phone if it is charging using the PC")
        print(" - Enable Developer Options in Settings (Go to About Phone > Click the Version button several times.")

    # if stderr occured
    elif results.stderr == b'error: no devices/emulators found\r\n':
        print("The connection is unsucessful :(\nCommon fixes to try:\n - Check if your phone is charging using the PC")
        print(" - Enable Developer Options in Settings (Go to About Phone > Click the Version button several times.")

    else:
        print("nono\n")
    # else:
    #     print("An Error Occured, Please Contact the developer of the project")

# if Wireless has been selected
elif WiredORWirles == "Wireles":
    print("Ok!, Doing Some Work!\n")
    Wireless_Con()
    if Wireless_results.stdout == b'restarting in TCP mode port: 5555\r\n':
        print("Wireless Connection is Successful!")
        Scrcpy()
        
else:
    print("no others")

       

print(results)

