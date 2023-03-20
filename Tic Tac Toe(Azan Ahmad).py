import random

current_player=0
symbol=0
play_again=str("y")





def menu():
    print("Enter 1 for single player mode(with computer)")
    print("Enter 2 for double player mode")
    print("Enter 3 for tournament mode double player of 5 games")
    global game_mode
    game_mode=int(input())
    
    
    return game_mode


def main():
    menu()
    if game_mode==1:
        single_player()

    elif game_mode==2:
        double_player()

    elif game_mode==3:
        tournament()
        
    else:
        print("Enter a number between(1-3)")
        
    
        

def double_player():
        
    
        
        
        play_again=str("y")
        current_player=0
        symbol=0

        while play_again==str("y"):
            

            p1=str(input("Enter player 1 name: "))
            print("Sign for", p1 ,"is 'o'")
            p2=str(input("Enter player 2 name: "))
            print("Sign for",p2,"is 'x'")

            toss=random.randint(0,1)
            
            if toss==0:
                print(p1, " won the toss")
                current_player=p1
                symbol='o'

            elif toss==1:
                print(p2, "won the toss")
                current_player=p2
                symbol='x'

            else:
                print("Please enter valid information")
               
            n=[1,2,3,4,5,6,7,8,9]
            print(n[0],"|",n[1],"|",n[2])
            print("__________")
            print(n[3],"|",n[4],"|",n[5])
            print("__________")
            print(n[6],"|",n[7],"|",n[8])
            
            for z in range(1,10):
                print("turn",z)
                num=eval(input("Enter your desired box: "))

                


                if num==1 and n[0]==1:
                    n[0]=symbol
                   

                elif num==2 and n[1]==2:
                    n[1]=symbol
                   
                elif num==3 and n[2]==3:
                    n[2]=symbol 

                elif num==4 and n[3]==4:
                    n[3]=symbol

                elif num==5 and n[4]==5:
                    n[4]=symbol
                   

                elif num==6 and n[5]==6:
                    n[5]=symbol
                   
                   
                elif num==7 and n[6]==7:
                    n[6]=symbol
                    

                elif num==8 and n[7]==8:
                    n[7]=symbol
                   
                elif num==9 and n[8]==9:
                    n[8]=symbol

                else:
                    print("This spot is already taken!Play again")
                    break 


                

               
                   
                  
                                  

                print(n[0],"|",n[1],"|",n[2])
                print("__________")
                print(n[3],"|",n[4],"|",n[5])
                print("__________")
                print(n[6],"|",n[7],"|",n[8])

                




                if symbol=='o':
                    symbol='x'
                    
                elif symbol=='x':
                    symbol='o'






                if n[0]==n[1] and n[1]==n[2]:
                    print("Congratulations",current_player,"has won")
                    break

                elif n[0]==n[3] and n[0]==n[6]:
                    print("Congratulations",current_player,"has won")
                    break


                elif n[1]==n[4] and n[1]==n[7]:
                    print("Congratulations",current_player,"has won")
                    break 

                elif n[2]==n[5] and n[2]==n[8]:
                    print("Congratulations",current_player,"has won")
                    break

                elif n[3]==n[4] and n[3]==n[5]:
                    print("Congratulations",current_player,"has won")
                    break
                    
                elif n[6]==n[7] and n[6]==n[8]:
                    print("Congratulations",current_player,"has won")
                    break

                elif n[0]==n[4] and n[0]==n[8]:
                    print("Congratulations",current_player,"has won")
                    break

                elif n[2]==n[4] and n[2]==n[6]:
                    print("Congratulations",current_player,"has won")
                    break
                elif n[0]!=1 and n[1]!=2 and n[2]!=3 and n[3]!=4 and n[4]!=5 and n[5]!=6 and n[6]!=7 and n[7]!=8 and n[8]!=9:
                    print("Its a draw")  
                
                    
                           
                if current_player==p1:
                    current_player=p2
                    
                elif current_player==p2:
                    current_player=p1
            
            
            play_again=str(input("Do you want to play again.(Reply with 'y' for yes or 'n' for no): "))
        
            if play_again==str("n"):
                go_back=str(input("Press m to go to main menu or e to exit: "))
                if go_back==str("m"):
                    main()
                else:
                    break
            elif play_again==str("y"):
                play_again==str("y")

            else:
                break
                             
                


        print("Thanks for Playing with us")



def tournament():

    countp1=0
    countp2=0
    play_again=str("y")
    current_player=0
    symbol=0
    
    
               
    
   
    while play_again==str("y"):
        p1=str(input("Enter player 1 name: "))
        print("Sign for", p1 ,"is 'o'")
        p2=str(input("Enter player 2 name: "))
        print("Sign for",p2,"is 'x'")

        
        for games in range(0,5):
            toss=random.randint(0,1)

            if toss==0:
                print(p1, " won the toss")
                current_player=p1
                symbol='o'

            elif toss==1:
                print(p2, "won the toss")
                current_player=p2
                symbol='x'

            else:
                print("Please enter valid information")
                
            n=[1,2,3,4,5,6,7,8,9]
            print(n[0],"|",n[1],"|",n[2])
            print("__________")
            print(n[3],"|",n[4],"|",n[5])
            print("__________")
            print(n[6],"|",n[7],"|",n[8])
            
            for z in range(1,10):
                print("turn",z)
                num=eval(input("Enter your desired box: "))

                        


                if num==1 and n[0]==1:
                    n[0]=symbol
                   

                elif num==2 and n[1]==2:
                    n[1]=symbol
                   
                elif num==3 and n[2]==3:
                    n[2]=symbol 

                elif num==4 and n[3]==4:
                    n[3]=symbol

                elif num==5 and n[4]==5:
                    n[4]=symbol
                   

                elif num==6 and n[5]==6:
                    n[5]=symbol
                   
                   
                elif num==7 and n[6]==7:
                    n[6]=symbol
                    

                elif num==8 and n[7]==8:
                    n[7]=symbol
                   
                elif num==9 and n[8]==9:
                    n[8]=symbol

                else:
                    print("This spot is already taken!Play again")
                    break 


                        

                       
                print(n[0],"|",n[1],"|",n[2])
                print("__________")
                print(n[3],"|",n[4],"|",n[5])
                print("__________")
                print(n[6],"|",n[7],"|",n[8])


                        




                if symbol=='o':
                    symbol='x'
                            
                elif symbol=='x':
                    symbol='o'






                if n[0]==n[1] and n[1]==n[2]:
                    print("Congratulations",current_player,"has won")
                    if current_player==p1:
                        countp1+=1
                    elif current_player==p2:
                        countp2+=1
                    break

                elif n[0]==n[3] and n[0]==n[6]:
                    print("Congratulations",current_player,"has won")
                    if current_player==p1:
                        countp1+=1
                    elif current_player==p2:
                        countp2+=1
                    break


                elif n[1]==n[4] and n[1]==n[7]:
                    print("Congratulations",current_player,"has won")
                    if current_player==p1:
                        countp1+=1
                    elif current_player==p2:
                        countp2+=1
                    break 

                elif n[2]==n[5] and n[2]==n[8]:
                    print("Congratulations",current_player,"has won")
                    if current_player==p1:
                        countp1+=1
                    elif current_player==p2:
                        countp2+=1
                    break

                elif n[3]==n[4] and n[3]==n[5]:
                    print("Congratulations",current_player,"has won")
                    if current_player==p1:
                        countp1+=1
                    elif current_player==p2:
                        countp2+=1
                    break
                            
                elif n[6]==n[7] and n[6]==n[8]:

                    print("Congratulations",current_player,"has won")
                    if current_player==p1:
                        countp1+=1
                    elif current_player==p2:
                        countp2+=1
                    break

                elif n[0]==n[4] and n[0]==n[8]:

                    print("Congratulations",current_player,"has won")
                    if current_player==p1:
                        countp1+=1
                    elif current_player==p2:
                        countp2+=1
                    break

                elif n[2]==n[4] and n[2]==n[6]:

                    print("Congratulations",current_player,"has won")
                    if current_player==p1:
                        countp1+=1
                    elif current_player==p2:
                        countp2+=1
                    break
                elif n[0]!=1 and n[1]!=2 and n[2]!=3 and n[3]!=4 and n[4]!=5 and n[5]!=6 and n[6]!=7 and n[7]!=8 and n[8]!=9:
                    print("Its a draw")  
                        
                            

                if current_player==p1:
                    current_player=p2
                            
                elif current_player==p2:
                    current_player=p1

        if countp1>countp2:
            print(p1,"has won the tournament")
        elif countp2>countp1:
            print(p2,"has won the tournament")
        else:
            print("The tournament's a draw")

        play_again=str(input("Do you want to play again.(Reply with 'y' for yes or 'n' for no): "))

        if play_again==str("n"):
            go_back=str(input("Press m to go to main menu or e to exit: "))
            if go_back==str("m"):
                main()
            else:
                break
        elif play_again==str("y"):
            play_again==str("y")

        else:
            break
                             
                



    print("Thanks for Playing with us")
                
    
def single_player():


        play_again=str("y")
        current_player=0
        computer='Computer'
        
        while play_again==str("y"):
            n=[1,2,3,4,5,6,7,8,9]
            symbol_comp=0
            p1=str(input("Enter your name: "))
            print("Choose your symbol(o or x): ")
            symbol_player=str(input())
            if symbol_player=='o':
                symbol_comp='x'
            elif symbol_player=='x':
                symbol_comp='o'

            else:
                print("Enter valid informarion")

            
            toss=random.randint(0,1)

            if toss==0:
                print("You won the toss: ")
                current_player=p1
            elif toss==1:
                print("Computer won the toss: ")
                current_player=computer

            else:
                print("Enter valid informarion")

            
            print(n[0],"|",n[1],"|",n[2])
            print("__________")
            print(n[3],"|",n[4],"|",n[5])
            print("__________")
            print(n[6],"|",n[7],"|",n[8])
            


            
            

            for p in range(1,10):
                print("Turn",p)
                
               
                if toss==0:
                    if p==1 or p==3 or p==5 or p ==7 or p==9:
                        turn1=eval(input("Enter your desired position(1-9): "))

                        if turn1==1 and n[0]==1:
                            n[0]=symbol_player
                           

                        elif turn1==2 and n[1]==2:
                            n[1]=symbol_player
                           
                        elif turn1==3 and n[2]==3:
                            n[2]=symbol_player

                        elif turn1==4 and n[3]==4:
                            n[3]=symbol_player

                        elif turn1==5 and n[4]==5:
                            n[4]=symbol_player
                           

                        elif turn1==6 and n[5]==6:
                            n[5]=symbol_player
                           
                           
                        elif turn1==7 and n[6]==7:
                            n[6]=symbol_player
                            

                        elif turn1==8 and n[7]==8:
                            n[7]=symbol_player
                           
                        elif turn1==9 and n[8]==9:
                            n[8]=symbol_player

                        else:
                            print("This spot is already taken play again")
                            break

                    else: #Stopping the corner occupying trick
                        if n[0]==symbol_player and n[1]==2 and n[2]==3 and n[3]==4 and n[4]==5 and n[5]==6 and n[6]==7 and n[7]==8 and n[8]==9:
                            n[4]=symbol_comp

                        elif n[2]==symbol_player and n[0]==1 and n[1]==2 and n[3]==4 and n[4]==5 and n[5]==6 and n[6]==7 and n[7]==8 and n[8]==9:
                            n[4]=symbol_comp

                        elif n[6]==symbol_player and n[0]==1 and n[1]==2 and n[2]==3 and n[3]==4 and n[4]==5 and n[5]==6 and n[7]==8 and n[8]==9:
                            n[4]=symbol_comp

                        elif n[8]==symbol_player and n[0]==1 and n[1]==2 and n[2]==3 and n[3]==4 and n[4]==5 and n[5]==6 and n[6]==7 and n[7]==8:
                            n[4]=symbol_comp
                               #Computer winning conditions                     
                        elif n[1]==symbol_comp and n[2]==symbol_comp and n[0]!=symbol_comp and n[0]!=symbol_player or n[3]==symbol_comp and n[6]==symbol_comp and n[0]!=symbol_comp and n[0]!=symbol_player or n[4]==symbol_comp and n[8]==symbol_comp and n[0]!=symbol_comp and n[0]!=symbol_player:
                            n[0]=symbol_comp

                        elif n[0]==symbol_comp and n[2]==symbol_comp and n[1]!=symbol_comp and n[1]!=symbol_player or n[4]==symbol_comp and n[7]==symbol_comp and n[1]!=symbol_comp and n[1]!=symbol_player:
                            n[1]=symbol_comp

                        elif n[0]==symbol_comp and n[1]==symbol_comp and n[2]!=symbol_comp and n[2]!=symbol_player or n[5]==symbol_comp and n[8]==symbol_comp and n[2]!=symbol_comp and n[2]!=symbol_player or n[4]==symbol_comp and n[6]==symbol_comp and n[2]!=symbol_comp and n[2]!=symbol_player:
                            n[2]=symbol_comp
                            
                        elif n[0]==symbol_comp and n[6]==symbol_comp and n[3]!=symbol_comp and n[3]!=symbol_player or n[4]==symbol_comp and n[5]==symbol_comp and n[3]!=symbol_comp and n[3]!=symbol_player:
                            n[3]=symbol_comp

                        elif n[0]==symbol_comp and n[8]==symbol_comp and n[4]!=symbol_comp and n[4]!=symbol_player or n[1]==symbol_comp and n[7]==symbol_comp and n[4]!=symbol_comp and n[4]!=symbol_player or n[2]==symbol_comp and n[6]==symbol_comp and n[4]!=symbol_comp and n[4]!=symbol_player or n[3]==symbol_comp and n[5]==symbol_comp and n[4]!=symbol_comp and n[4]!=symbol_player:
                            n[4]=symbol_comp

                        elif n[2]==symbol_comp and n[8]==symbol_comp and n[5]!=symbol_comp and n[5]!=symbol_player or n[3]==symbol_comp and n[4]==symbol_comp and n[5]!=symbol_comp and n[5]!=symbol_player:
                            n[5]=symbol_comp

                        elif n[0]==symbol_comp and n[3]==symbol_comp and n[6]!=symbol_comp and n[6]!=symbol_player or n[2]==symbol_comp and n[4]==symbol_comp and n[6]!=symbol_comp and n[6]!=symbol_player or n[7]==symbol_comp and n[8]==symbol_comp and n[6]!=symbol_comp and n[6]!=symbol_player:
                            n[6]=symbol_comp

                        elif n[1]==symbol_comp and n[4]==symbol_comp and n[7]!=symbol_comp and n[7]!=symbol_player or n[6]==symbol_comp and n[8]==symbol_comp and n[7]!=symbol_comp and n[7]!=symbol_player:
                            n[7]=symbol_comp

                        elif n[2]==symbol_comp and n[5]==symbol_comp and n[8]!=symbol_comp and n[8]!=symbol_player or n[0]==symbol_comp and n[4]==symbol_comp and n[8]!=symbol_comp and n[8]!=symbol_player or n[6]==symbol_comp and n[7]==symbol_comp and n[8]!=symbol_comp and n[8]!=symbol_player:  
                            n[8]=symbol_comp

                        else: #blocking player from winning

                            if n[1]==symbol_player and n[2]==symbol_player and n[0]!=symbol_comp and n[0]!=symbol_player or n[3]==symbol_player and n[6]==symbol_player and n[0]!=symbol_comp and n[0]!=symbol_player or n[4]==symbol_player and n[8]==symbol_player and n[0]!=symbol_comp and n[0]!=symbol_player:
                                n[0]=symbol_comp

                            elif n[0]==symbol_player and n[2]==symbol_player and n[1]!=symbol_comp and n[1]!=symbol_player or n[4]==symbol_player and n[7]==symbol_player and n[1]!=symbol_comp and n[1]!=symbol_player:
                                n[1]=symbol_comp

                            elif n[0]==symbol_player and n[1]==symbol_player and n[2]!=symbol_comp and n[2]!=symbol_player or n[5]==symbol_player and n[8]==symbol_player and n[2]!=symbol_comp and n[2]!=symbol_player or n[4]==symbol_player and n[6]==symbol_player and n[2]!=symbol_comp and n[2]!=symbol_player:
                                n[2]=symbol_comp

                            elif n[0]==symbol_player and n[6]==symbol_player and n[3]!=symbol_comp and n[3]!=symbol_player or n[4]==symbol_player and n[5]==symbol_player and n[3]!=symbol_comp and n[3]!=symbol_player:
                                n[3]=symbol_comp

                            elif n[0]==symbol_player and n[8]==symbol_player and n[4]!=symbol_comp and n[4]!=symbol_player or n[1]==symbol_player and n[7]==symbol_player and n[4]!=symbol_comp and n[4]!=symbol_player or n[2]==symbol_player and n[6]==symbol_player and n[4]!=symbol_comp and n[4]!=symbol_player or n[3]==symbol_player and n[5]==symbol_player and n[4]!=symbol_comp and n[4]!=symbol_player:
                                n[4]=symbol_comp

                            elif n[2]==symbol_player and n[8]==symbol_player and n[5]!=symbol_comp and n[5]!=symbol_player or n[3]==symbol_player and n[4]==symbol_player and n[5]!=symbol_comp and n[5]!=symbol_player:
                                n[5]=symbol_comp

                            elif n[0]==symbol_player and n[3]==symbol_player and n[6]!=symbol_comp and n[6]!=symbol_player or n[2]==symbol_player and n[4]==symbol_player and n[6]!=symbol_comp and n[6]!=symbol_player or n[7]==symbol_player and n[8]==symbol_player and n[6]!=symbol_comp and n[6]!=symbol_player:
                                n[6]=symbol_comp

                            elif n[1]==symbol_player and n[4]==symbol_player and n[7]!=symbol_comp and n[7]!=symbol_player or n[6]==symbol_player and n[8]==symbol_player and n[7]!=symbol_comp and n[7]!=symbol_player:
                                n[7]=symbol_comp

                            elif n[2]==symbol_player and n[5]==symbol_player and n[8]!=symbol_comp and n[8]!=symbol_player or n[0]==symbol_player and n[4]==symbol_player and n[8]!=symbol_comp and n[8]!=symbol_player or n[6]==symbol_player and n[7]==symbol_player and n[8]!=symbol_comp and n[8]!=symbol_player:  
                                n[8]=symbol_comp


                            else:#Occupying corner spaces

                                if n[0]==symbol_comp and n[2]!=symbol_player and n[1]!=symbol_comp and n[1]!=symbol_player:
                                    n[1]=symbol_comp

                                elif n[0]==symbol_comp and n[6]!=symbol_player and n[3]!=symbol_comp and n[3]!=symbol_player:
                                    n[3]=symbol_comp

                                elif n[0]==symbol_comp and n[8]!=symbol_player and n[4]!=symbol_comp and n[4]!=symbol_player:
                                    n[4]=symbol_comp

                                elif n[2]==symbol_comp and n[0]!=symbol_player and n[1]!=symbol_comp and n[1]!=symbol_player:
                                    n[1]=symbol_comp

                                elif n[2]==symbol_comp and n[6]!=symbol_player and n[4]!=symbol_comp and n[4]!=symbol_player:
                                    n[4]=symbol_comp

                                elif n[2]==symbol_comp and n[8]!=symbol_player and n[5]!=symbol_comp and n[5]!=symbol_player:
                                    n[5]=symbol_comp

                                elif n[6]==symbol_comp and n[8]!=symbol_player and n[7]!=symbol_comp and n[7]!=symbol_player:
                                    n[7]=symbol_comp

                                elif n[6]==symbol_comp and n[0]!=symbol_player and n[3]!=symbol_comp and n[3]!=symbol_player:
                                    n[3]=symbol_comp

                                elif n[6]==symbol_comp and n[2]!=symbol_player and n[4]!=symbol_comp and n[4]!=symbol_player:
                                    n[4]=symbol_comp

                                elif n[8]==symbol_comp and n[6]!=symbol_player and n[7]!=symbol_comp and n[7]!=symbol_player:
                                    n[7]=symbol_player

                                elif n[8]==symbol_comp and n[2]!=symbol_player and n[5]!=symbol_comp and n[5]!=symbol_player:
                                    n[5]=symbol_comp

                                elif n[8]==symbol_comp and n[0]!=symbol_player and n[4]!=symbol_comp and n[4]!=symbol_player:
                                    n[4]=symbol_comp

                                elif n[0]!=symbol_comp and n[0]!=symbol_player:
                                   n[0]=symbol_comp

                                elif n[2]!=symbol_comp and n[2]!=symbol_player:
                                    n[2]=symbol_comp

                                elif n[6]!=symbol_comp and n[6]!=symbol_player:
                                    n[6]=symbol_comp

                                elif n[8]!=symbol_comp and n[8]!=symbol_player:
                                    n[8]=symbol_comp

                                else:#occupy the centre place

                                    if n[4]!=symbol_comp and n[4]!=symbol_player:
                                        n[4]=symbol_comp

                                    else:

                                        if n[1]!=symbol_comp and n[3]!=symbol_player:
                                            n[1]=symbol_comp

                                        elif n[3]!=symbol_comp and n[3]!=symbol_player:
                                            n[3]=symbol_comp

                                        elif n[5]!=symbol_comp and n[5]!=symbol_player:
                                            n[5]=symbol_comp

                                        elif n[7]!=symbol_comp and n[7]!=symbol_player:
                                            n[7]=symbol_comp
                                


                                        

                                           
                                            

                                                
                        
                        
                
                elif toss==1:
                    if p==2 or p==4 or p==6 or p==8:
                        turn1=eval(input("Enter your desired position(1-9): "))

                        
                        if turn1==1 and n[0]==1:
                            n[0]=symbol_player
                           

                        elif turn1==2 and n[1]==2:
                            n[1]=symbol_player
                           
                        elif turn1==3 and n[2]==3:
                            n[2]=symbol_player

                        elif turn1==4 and n[3]==4:
                            n[3]=symbol_player

                        elif turn1==5 and n[4]==5:
                            n[4]=symbol_player
                           

                        elif turn1==6 and n[5]==6:
                            n[5]=symbol_player
                           
                           
                        elif turn1==7 and n[6]==7:
                            n[6]=symbol_player
                            

                        elif turn1==8 and n[7]==8:
                            n[7]=symbol_player
                           
                        elif turn1==9 and n[8]==9:
                            n[8]=symbol_player

                        else:
                            print("This spot is already taken play again!")
                            break

                        
                    else:
                        if n[0]==symbol_comp and n[2]==symbol_player and n[1]==2 and n[3]==4 and n[4]==5 and n[5]==6 and n[6]==7 and n[7]==8 and n[8]==9:
                            n[4]=symbol_comp

                        elif n[0]==symbol_comp and n[6]==symbol_player and n[1]==2 and n[2]==3 and n[3]==4 and n[4]==5 and n[5]==6 and n[7]==8 and n[8]==9:
                            n[4]=symbol_comp

                        elif n[0]==symbol_comp and n[8]==symbol_player and n[1]==2 and n[2]==3 and n[3]==4 and n[4]==5 and n[5]==6 and n[6]==7 and n[7]==8:
                            n[4]=symbol_comp
                        
                        elif n[1]==symbol_comp and n[2]==symbol_comp and n[0]!=symbol_comp and n[0]!=symbol_player or n[3]==symbol_comp and n[6]==symbol_comp and n[0]!=symbol_comp and n[0]!=symbol_player or n[4]==symbol_comp and n[8]==symbol_comp and n[0]!=symbol_comp and n[0]!=symbol_player:
                            n[0]=symbol_comp

                        elif n[0]==symbol_comp and n[2]==symbol_comp and n[1]!=symbol_comp and n[1]!=symbol_player or n[4]==symbol_comp and n[7]==symbol_comp and n[1]!=symbol_comp and n[1]!=symbol_player:
                            n[1]=symbol_comp

                        elif n[0]==symbol_comp and n[1]==symbol_comp and n[2]!=symbol_comp and n[2]!=symbol_player or n[5]==symbol_comp and n[8]==symbol_comp and n[2]!=symbol_comp and n[2]!=symbol_player or n[4]==symbol_comp and n[6]==symbol_comp and n[2]!=symbol_comp and n[2]!=symbol_player:
                            n[2]=symbol_comp
                            
                        elif n[0]==symbol_comp and n[6]==symbol_comp and n[3]!=symbol_comp and n[3]!=symbol_player or n[4]==symbol_comp and n[5]==symbol_comp and n[3]!=symbol_comp and n[3]!=symbol_player:
                            n[3]=symbol_comp

                        elif n[0]==symbol_comp and n[8]==symbol_comp and n[4]!=symbol_comp and n[4]!=symbol_player or n[1]==symbol_comp and n[7]==symbol_comp and n[4]!=symbol_comp and n[4]!=symbol_player or n[2]==symbol_comp and n[6]==symbol_comp and n[4]!=symbol_comp and n[4]!=symbol_player or n[3]==symbol_comp and n[5]==symbol_comp and n[4]!=symbol_comp and n[4]!=symbol_player:
                            n[4]=symbol_comp

                        elif n[2]==symbol_comp and n[8]==symbol_comp and n[5]!=symbol_comp and n[5]!=symbol_player or n[3]==symbol_comp and n[4]==symbol_comp and n[5]!=symbol_comp and n[5]!=symbol_player:
                            n[5]=symbol_comp

                        elif n[0]==symbol_comp and n[3]==symbol_comp and n[6]!=symbol_comp and n[6]!=symbol_player or n[2]==symbol_comp and n[4]==symbol_comp and n[6]!=symbol_comp and n[6]!=symbol_player or n[7]==symbol_comp and n[8]==symbol_comp and n[6]!=symbol_comp and n[6]!=symbol_player:
                            n[6]=symbol_comp

                        elif n[1]==symbol_comp and n[4]==symbol_comp and n[7]!=symbol_comp and n[7]!=symbol_player or n[6]==symbol_comp and n[8]==symbol_comp and n[7]!=symbol_comp and n[7]!=symbol_player:
                            n[7]=symbol_comp

                        elif n[2]==symbol_comp and n[5]==symbol_comp and n[8]!=symbol_comp and n[8]!=symbol_player or n[0]==symbol_comp and n[4]==symbol_comp and n[8]!=symbol_comp and n[8]!=symbol_player or n[6]==symbol_comp and n[7]==symbol_comp and n[8]!=symbol_comp and n[8]!=symbol_player:  
                            n[8]=symbol_comp

                        else: #blocking player from winning

                            if n[1]==symbol_player and n[2]==symbol_player and n[0]!=symbol_comp and n[0]!=symbol_player or n[3]==symbol_player and n[6]==symbol_player and n[0]!=symbol_comp and n[0]!=symbol_player or n[4]==symbol_player and n[8]==symbol_player and n[0]!=symbol_comp and n[0]!=symbol_player:
                                n[0]=symbol_comp

                            elif n[0]==symbol_player and n[2]==symbol_player and n[1]!=symbol_comp and n[1]!=symbol_player or n[4]==symbol_player and n[7]==symbol_player and n[1]!=symbol_comp and n[1]!=symbol_player:
                                n[1]=symbol_comp

                            elif n[0]==symbol_player and n[1]==symbol_player and n[2]!=symbol_comp and n[2]!=symbol_player or n[5]==symbol_player and n[8]==symbol_player and n[2]!=symbol_comp and n[2]!=symbol_player or n[4]==symbol_player and n[6]==symbol_player and n[2]!=symbol_comp and n[2]!=symbol_player:
                                n[2]=symbol_comp

                            elif n[0]==symbol_player and n[6]==symbol_player and n[3]!=symbol_comp and n[3]!=symbol_player or n[4]==symbol_player and n[5]==symbol_player and n[3]!=symbol_comp and n[3]!=symbol_player:
                                n[3]=symbol_comp

                            elif n[0]==symbol_player and n[8]==symbol_player and n[4]!=symbol_comp and n[4]!=symbol_player or n[1]==symbol_player and n[7]==symbol_player and n[4]!=symbol_comp and n[4]!=symbol_player or n[2]==symbol_player and n[6]==symbol_player and n[4]!=symbol_comp and n[4]!=symbol_player or n[3]==symbol_player and n[5]==symbol_player and n[4]!=symbol_comp and n[4]!=symbol_player:
                                n[4]=symbol_comp

                            elif n[2]==symbol_player and n[8]==symbol_player and n[5]!=symbol_comp and n[5]!=symbol_player or n[3]==symbol_player and n[4]==symbol_player and n[5]!=symbol_comp and n[5]!=symbol_player:
                                n[5]=symbol_comp

                            elif n[0]==symbol_player and n[3]==symbol_player and n[6]!=symbol_comp and n[6]!=symbol_player or n[2]==symbol_player and n[4]==symbol_player and n[6]!=symbol_comp and n[6]!=symbol_player or n[7]==symbol_player and n[8]==symbol_player and n[6]!=symbol_comp and n[6]!=symbol_player:
                                n[6]=symbol_comp

                            elif n[1]==symbol_player and n[4]==symbol_player and n[7]!=symbol_comp and n[7]!=symbol_player or n[6]==symbol_player and n[8]==symbol_player and n[7]!=symbol_comp and n[7]!=symbol_player:
                                n[7]=symbol_comp

                            elif n[2]==symbol_player and n[5]==symbol_player and n[8]!=symbol_comp and n[8]!=symbol_player or n[0]==symbol_player and n[4]==symbol_player and n[8]!=symbol_comp and n[8]!=symbol_player or n[6]==symbol_player and n[7]==symbol_player and n[8]!=symbol_comp and n[8]!=symbol_player:  
                                n[8]=symbol_comp


                            else:#Occupying corner spaces

                                if n[0]==symbol_comp and n[2]!=symbol_player and n[1]!=symbol_comp and n[1]!=symbol_player:
                                    n[1]=symbol_comp

                                elif n[0]==symbol_comp and n[6]!=symbol_player and n[3]!=symbol_comp and n[3]!=symbol_player:
                                    n[3]=symbol_comp

                                elif n[0]==symbol_comp and n[8]!=symbol_player and n[4]!=symbol_comp and n[4]!=symbol_player:
                                    n[4]=symbol_comp

                                elif n[2]==symbol_comp and n[0]!=symbol_player and n[1]!=symbol_comp and n[1]!=symbol_player:
                                    n[1]=symbol_comp

                                elif n[2]==symbol_comp and n[6]!=symbol_player and n[4]!=symbol_comp and n[4]!=symbol_player:
                                    n[4]=symbol_comp

                                elif n[2]==symbol_comp and n[8]!=symbol_player and n[5]!=symbol_comp and n[5]!=symbol_player:
                                    n[5]=symbol_comp

                                elif n[6]==symbol_comp and n[8]!=symbol_player and n[7]!=symbol_comp and n[7]!=symbol_player:
                                    n[7]=symbol_comp

                                elif n[6]==symbol_comp and n[0]!=symbol_player and n[3]!=symbol_comp and n[3]!=symbol_player:
                                    n[3]=symbol_comp

                                elif n[6]==symbol_comp and n[2]!=symbol_player and n[4]!=symbol_comp and n[4]!=symbol_player:
                                    n[4]=symbol_comp

                                elif n[8]==symbol_comp and n[6]!=symbol_player and n[7]!=symbol_comp and n[7]!=symbol_player:
                                    n[7]=symbol_player

                                elif n[8]==symbol_comp and n[2]!=symbol_player and n[5]!=symbol_comp and n[5]!=symbol_player:
                                    n[5]=symbol_comp

                                elif n[8]==symbol_comp and n[0]!=symbol_player and n[4]!=symbol_comp and n[4]!=symbol_player:
                                    n[4]=symbol_comp

                                elif n[0]!=symbol_comp and n[0]!=symbol_player:
                                    n[0]=symbol_comp

                                elif n[2]!=symbol_comp and n[2]!=symbol_player:
                                    n[2]=symbol_comp

                                elif n[6]!=symbol_comp and n[6]!=symbol_player:
                                    n[6]=symbol_comp

                                elif n[8]!=symbol_comp and n[8]!=symbol_player:
                                    n[8]=symbol_comp

                                else:#occupy the centre place

                                    if n[4]!=symbol_comp and n[4]!=symbol_player:
                                        n[4]=symbol_comp

                                    else:

                                        if n[1]!=symbol_comp and n[1]!=symbol_player:
                                            n[1]=symbol_comp

                                        elif n[3]!=symbol_comp and n[3]!=symbol_player:
                                            n[3]=symbol_comp

                                        elif n[5]!=symbol_comp and n[5]!=symbol_player:
                                            n[5]=symbol_comp

                                        elif n[7]!=symbol_comp and n[7]!=symbol_player:
                                            n[7]=symbol_comp

                                            
                                                

                       
                
                print(n[0],"|",n[1],"|",n[2])
                print("__________")
                print(n[3],"|",n[4],"|",n[5])
                print("__________")
                print(n[6],"|",n[7],"|",n[8])

                if n[0]==n[1] and n[1]==n[2]:
                    if current_player=='computer':
                        print("Sorry",current_player,"has won.Try again!")
                        break
                    else:
                        print("Congratulations",current_player,"has won")
                        break

                elif n[0]==n[3] and n[0]==n[6]:
                    if current_player=='computer':
                        print("Sorry",current_player,"has won.Try again!")
                        break
                    else:
                        print("Congratulations",current_player,"has won")
                        break


                elif n[1]==n[4] and n[1]==n[7]:
                    if current_player=='computer':
                        print("Sorry",current_player,"has won.Try again!")
                        break
                    else:
                        print("Congratulations",current_player,"has won")
                        break

                elif n[2]==n[5] and n[2]==n[8]:
                    if current_player=='computer':
                        print("Sorry",current_player,"has won.Try again!")
                        break
                    else:
                        print("Congratulations",current_player,"has won")
                        break

                elif n[3]==n[4] and n[3]==n[5]:
                    if current_player=='computer':
                        print("Sorry",current_player,"has won.Try again!")
                        break
                    else:
                        print("Congratulations",current_player,"has won")
                        break
                    
                elif n[6]==n[7] and n[6]==n[8]:
                    if current_player=='computer':
                        print("Sorry",current_player,"has won.Try again!")
                        break
                    else:
                        print("Congratulations",current_player,"has won")
                        break

                elif n[0]==n[4] and n[0]==n[8]:
                    if current_player=='computer':
                        print("Sorry",current_player,"has won.Try again!")
                        break
                    else:
                        print("Congratulations",current_player,"has won")
                        break

                elif n[2]==n[4] and n[2]==n[6]:
                    if current_player=='computer':
                        print("Sorry",current_player,"has won.Try again!")
                        break
                    else:
                        print("Congratulations",current_player,"has won")
                        break

                elif n[0]!=1 and n[1]!=2 and n[2]!=3 and n[3]!=4 and n[4]!=5 and n[5]!=6 and n[6]!=7 and n[7]!=8 and n[8]!=9:
                    print("Its a draw")
                    

                if current_player==p1:
                    current_player=("computer")
                elif current_player==("computer"):
                    current_player=p1
        
            play_again=str(input("Do you want to play again.(Reply with 'y' for yes or 'n' for no): "))

            if play_again==str("n"):
                go_back=str(input("Press m to go to main menu or e to exit: "))
                if go_back==str("m"):
                    main()
                else:
                    break
            elif play_again==str("y"):
                play_again=str("y")

            else:
                break
                    

        print("Thanks for playing with us")





main()







    
