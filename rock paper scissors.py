import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice=int(input("type 1 for rock, 2 for paper or 3 for scissors"))
if choice==1:
  print(rock)
if choice==2:
  print(paper)
if choice==3:
  print(scissors)
group=[1 , 2 ,3]#1rock 2paper 3scissors
a=random.choice(group)
print("computer chose")
if a==1:
  print(rock)
if a==2:
  print(paper)
if a==3:
  print(scissors)
if choice==a:
  print("its a draw")
elif choice==1 and a==3:
  print("you win")
elif choice==2 and a==1:
  print("you win")
elif choice==3 and a==2:
  print("you win")
else:
  print("you loose")