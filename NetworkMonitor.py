import socket
import time
import sys
import datetime


class NetworkMonitor:

    def __init__(self):

        if(len(sys.argv) > 2):

            print("  _   _      _                      _      __  __             _ _             ")
            print(" | \ | |    | |                    | |    |  \/  |           (_) |            ")
            print(" |  \| | ___| |___      _____  _ __| | __ | \  / | ___  _ __  _| |_ ___  _ __ ")
            print(" | . ` |/ _ \ __\ \ /\ / / _ \| '__| |/ / | |\/| |/ _ \| '_ \| | __/ _ \| '__|")
            print(" | |\  |  __/ |_ \ V  V / (_) | |  |   <  | |  | | (_) | | | | | || (_) | |   ")
            print(" |_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\ |_|  |_|\___/|_| |_|_|\__\___/|_|   ")
            print("")
            print("")


            try:
                self.host = sys.argv[1]
                self.port = int(sys.argv[2])

                while True:
                    self.ping_network(self.host, self.port)
                    time.sleep(10)

            except:
                print("An error occurred")

        else:
            print("Enter valid arguments")
    

    def ping_network(self, host, port):
        self.date = datetime.datetime.now()

        try:
            socket.setdefaulttimeout(3)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
            server_address = (host, port)

            s.connect(server_address)
            print(f"Connection found... - {self.date.year}/{self.date.month}/{self.date.day} - {self.date.hour}:{self.date.minute}:{self.date.second}")
            print("")
    
        except OSError:
            print(f"No connection... - {self.date.year}/{self.date.month}/{self.date.day} - {self.date.hour}:{self.date.minute}:{self.date.second}")
            print("")
            return False
        else:
            s.close()
            return True


NetworkMonitor()