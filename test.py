from send2arduino import send_commands

conf = send_commands("12")
print(conf + "1")

conf = send_commands("21")
print(conf + "2")

conf = send_commands("12")
print(conf + "3")

conf = send_commands("21")
print(conf + "4")

conf = send_commands("12")
print(conf + "5")