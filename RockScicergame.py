import random
rock=''' 
   _______           
---'   ____)       
      (_____)              
      (_____)                
      (____)               
---.__(___)    

'''
paper=''' 
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
Scissors=''''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
game_images=[rock,paper,Scissors]
user_choice=int(input("what do you ?Type 0 for Rock ,1 for Paper or 2 for scissors\n")) 
if user_choice>=3 or user_choice< 0:
    print("You typed an invalid number,you loss!")
print(game_images[user_choice])
computer_choice=random.randint(0,2)
print(f"Computer choise :")
print(game_images[computer_choice])
if user_choice==0 and computer_choice==2:
    print("You lose!")
elif computer_choice==0 and user_choice==2:
    print("You Lose")   
elif computer_choice>user_choice:
    print("You lose")
elif user_choice>computer_choice:
    print("You win!")  
elif computer_choice ==user_choice:
    print("It's a draw")   
