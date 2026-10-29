import time
passcode = input("what is your password")
dock_ships = ["enterprise", "light breaker"]
while True:
 password = input("what is the passcode")
 if password == passcode:
  print("passcode correct")
  dock_ships.append ("light smasher")
  print(dock_ships)
  print("do you want to change your passcode?")
  if input() == ("yes"):
   passcode = input("whats your new passcode ?")
 else:
     print("wrong passcode access denied wait 5 seconds")
     time.sleep(5)
