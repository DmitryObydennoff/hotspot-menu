#HOTSPOT MENU
import os 
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear') #Clears the console
os.system('title hotspot-menu v-0.7')

Head = '''
                  _           _                   _
                 | |__   ___ | |_ ___ _ __   ___ | |_   _ __ ___   ___ _ __  _   _
                 | '_ \ / _ \| __/ __| '_ \ / _ \| __| | '_ ` _ \ / _ \ '_ \| | | |
                 | | | | (_) | |_\__ \ |_) | (_) | |_  | | | | | |  __/ | | | |_| |
                 |_| |_|\___/ \__|___/ .__/ \___/ \__| |_| |_| |_|\___|_| |_|\__,_|
                                     |_|'''
Help= '''
Visit github.com/dst0rm/hotspot-menu for help
'''                            
Readme = '''
                  _           _                   _
                 | |__   ___ | |_ ___ _ __   ___ | |_   _ __ ___   ___ _ __  _   _
                 | '_ \ / _ \| __/ __| '_ \ / _ \| __| | '_ ` _ \ / _ \ '_ \| | | |
                 | | | | (_) | |_\__ \ |_) | (_) | |_  | | | | | |  __/ | | | |_| |
                 |_| |_|\___/ \__|___/ .__/ \___/ \__| |_| |_| |_|\___|_| |_|\__,_|
                                     |_|
----------------------------------------------------------------------------------------------------
Version - 0.7 beta
Author - Dmitry Obydennov
Github - github.com/dst0rm/hotspot-menu
More - github.com/dst0rm/hotspot-menu
----------------------------------------------------------------------------------------------------
'''

def get_menu_choice():
    def print_menu():
        print(Fore.GREEN + Head)
        print(Fore.YELLOW + 100 * "-")
        print(Fore.YELLOW + "[ 1 ]",Fore.WHITE + "Start")
        print(Fore.YELLOW + "[ 2 ]",Fore.WHITE + "Stop")
        print(Fore.YELLOW + "[ 3 ]",Fore.WHITE + "Status")
        print(Fore.YELLOW + "[ 4 ]",Fore.WHITE + "Settings")
        print(Fore.YELLOW + "[ 5 ]",Fore.WHITE + "Open ncpa")
        print(Fore.YELLOW + "[ 6 ]",Fore.WHITE + "Help")
        print(Fore.YELLOW + "[ 7 ]",Fore.WHITE + "Readme")
        print(Fore.YELLOW + "[ 8 ]",Fore.WHITE + "Exit")
        print(Fore.YELLOW + 100 * "-")

    loop = True
    int_choice = -1

    while loop:          # While loop which will keep going until loop = False
        print_menu()    # Displays menu
        choice = input(Fore.GREEN + "Enter your choice [1-8]: ")

        if choice == '1': #1. Start
            int_choice = 1
            loop = True
            print(" ")
            cmd = 'netsh wlan start hostednetwork' # cmd input
            os.system(cmd)

        if choice == '2': #1. Stop
            int_choice = 1
            loop = True
            print(" ")
            cmd = 'netsh wlan stop hostednetwork' # cmd input
            os.system(cmd)

        if choice == '3': #3. Status
            int_choice = 1
            loop = True
            os.system('cls' if os.name == 'nt' else 'clear') #Clears the console
            cmd = 'netsh wlan show hostednetwork' # cmd input
            cmd1 = 'netsh wlan show hostednetwork setting=security' # cmd input
            os.system(cmd)
            os.system(cmd1)
            print(" ")
    
        if choice == '4': #4. Settings
            int_choice = 1
            loop = True
            ssid = str( input( 'SSID: ' ) )
            key = str( input( 'Key: ' ) )
            cmd = "netsh wlan set hostednetwork mode=allow ssid="+ssid+" key="+key
            os.system(cmd)

        if choice == '5': #5. Open ncpa
            int_choice = 1
            loop = True
            cmd = 'ncpa.cpl' # cmd input
            os.system(cmd)

        if choice == '6': #6. Help
            int_choice = 1
            loop = True
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Help)

        if choice == '7': #7. abbout
            int_choice = 1
            loop = True
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.RED + Readme)

        if choice == '00': #00!!
            int_choice = 1
            loop = True

        elif choice == '8': #8. Exit
            print("Exiting..")
            int_choice = -1
            loop = False  # This will make the while loop to end
        else:

            input(Fore.RED + "Enter any key to try again...")
            os.system('cls' if os.name == 'nt' else 'clear') #Clears the console
    return [int_choice, choice]

print(get_menu_choice())
#print("1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890")
#os.system("mode con cols=100 lines=55")