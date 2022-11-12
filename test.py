from send2arduino import send_commands
import time

conf = send_commands("12")
time.sleep(2)
print(conf + "1")

conf = send_commands("21")
time.sleep(2)
print(conf + "2")

conf = send_commands("12")
time.sleep(2)
print(conf + "3")

conf = send_commands("21")
time.sleep(2)
print(conf + "4")

conf = send_commands("12")
time.sleep(2)
print(conf + "5")