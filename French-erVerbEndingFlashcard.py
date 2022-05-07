from asyncore import loop
import random

print


print("\n\n")

def je_func():                              #je function

 print("\033[0;36mwhat is the -er ending for 'Je' (I)\n")
 answerJe = "e"
 answerJeIn = input("\033[1;34m")
 if answerJeIn == answerJe:
  print("\033[1;32mcorrect!\n\n")
 elif answerJeIn != answerJe:
  print("\033[1;31mincorrect, answer is 'e'\n\n")
 
def nous_func():                             #nous function

 print("\033[0;36mwhat is the -er ending for 'Nous' (We)\n")
 answerNous = "ons"
 answerNousIn = input("\033[1;34m")
 if answerNousIn == answerNous:
  print("\033[1;32mcorrect!\n\n")
 elif answerNousIn != answerNous:
  print("\033[1;31mincorrect, answer is 'ons'\n\n")

def tu_func():                              #tu function

 print("\033[0;36mwhat is the -er ending for 'Tu' (You(inf))\n")
 answerTu = "es"
 answerTuIn = input("\033[1;34m")
 if answerTuIn == answerTu:
  print("\033[1;32mcorrect!\n\n")
 elif answerTuIn != answerTu:
  print("\033[1;31mincorrect, answer is 'es'\n\n")

def vous_func():                              #vous function

 print("\033[0;36mwhat is the -er ending for 'Vous' (You(pl/form))\n")
 answerVous = "ez"
 answerVousIn = input("\033[1;34m")
 if answerVousIn == answerVous:
  print("\033[1;32mcorrect!\n\n")
 elif answerVousIn != answerVous:
  print("\033[1;31mincorrect, answer is 'es'\n\n")

def ieo_func():                              #Il/Elle/On function

 print("\033[0;36mwhat is the -er ending for 'Il/Elle/On' (Him/Her/We(inf))\n")
 answerIeo = "e"
 answerIeoIn = input("\033[1;34m")
 if answerIeoIn == answerIeo:
  print("\033[1;32mcorrect!\n\n")
 elif answerIeoIn != answerIeo:
  print("\033[1;31mincorrect, answer is 'e'\n\n")

def ie_func():                              #Ils/Elles function

 print("\033[0;36mwhat is the -er ending for 'Ils/Elles' (they m/f)\n")
 answerIe = "ent"
 answerIeIn = input("\033[1;34m")
 if answerIeIn == answerIe:
  print("\033[1;32mcorrect!\n\n")
 elif answerIeIn != answerIe:
  print("\033[1;31mincorrect, answer is 'ent'\n\n")



class main():
    nous_func()
    je_func()
    tu_func()
    vous_func()
    ieo_func()
    ie_func()

    x = [je_func, nous_func, tu_func, vous_func, ieo_func, ie_func]                 #runs random function
    random.choice(x)()

print("to restart, run the code again.")




print("\n\n")


