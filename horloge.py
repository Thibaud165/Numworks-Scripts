from time import *

seconde=0
minute=0
heure=0

while True:
  mono = monotonic()
  
  while mono > 60:
    mono -= 60
    minute += 1 
  
  while minute > 60:
    minute -= 60
    heure += 1
  
  seconde = mono
  print(heure, ":", minute, ":", seconde)
