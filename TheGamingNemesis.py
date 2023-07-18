import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

df =pd.DataFrame()
csv_file = "D:\\Projects\\The Gaming Nemesis\\highend.csv"
csv_file2 = "D:\\Projects\\The Gaming Nemesis\\lowend.csv"
csv_file3 = "D:\\Projects\\The Gaming Nemesis\\top6games.csv"

def introduction():
    msg='''
                            NAMASTE!!!🙏
                            
Gaming🎮 is just like living a whole different life than your 'usual'.
Thanks to the ever increasing demand , gaming has become a job for many .. a 'gamer job'.
Now there's so much in gaming to tell about .. so many gaming genres
and such contrasting system requirements that it is hard for newbie gamers to cope up with.
In this project i will use the help of Python🐍 (csv and matplotlib) and try to help newbie
gamers and PC enthusiasts to give as much information as i can on gaming.
The whole project is divided into four major parts i.e. reading, analysis, visualization and editing.
All these parts are further divided into menus for easy navigation.

{Nemesis means 'an arch enemy'🦹 .. this project is called nemesis because it was an enemy to my 'gaming time'👾} 
\n\n\n\n'''
    for x in msg:

        print(x,end='')
        time.sleep(0.002)
    wait = input('Press any key to continue.....')         

def made_by():
    msg=''' 
            Gaming Nemesis made by      : Sahil Garje
            Roll No                     : 1
            School Name                 : Army Public School,Ahmednagar
            session                     : 2021-22
            

            Thanks for evaluating my Project.
            \n\n\n
        '''

    for x in msg:
        print(x, end='')
        time.sleep(0.002)
    wait = input('Press any key to continue.....')



def Digital_Games():
    msg='''
            Types of video games

            1.Action games😠
            2.Adventure games🤠
            3.Role-playing games🐉
            4.Simulation games🕹️
            5.Strategy games🤔
            6.Sports games🤺
            7.Puzzle games🧩
        '''
    for x in msg:
        print(x, end='')
        time.sleep(0.002)
    wait = input('Press any key to continue.....')

def clear():
    for x in range(10):
               print()

def read_csv_file():
    df =pd.read_csv(csv_file)
    print(df)
    
def read_csv_file2():
    df2 =pd.read_csv(csv_file2)
    print(df2)    

def developer_highend():
        df = pd.read_csv(csv_file)
        while True:
            clear()
            print('\n\nData Analysis MENU ')
            print('_'*100)
            print('1.  Show Whole DataFrame\n')
            print('2.  Show Columns\n')
            print('3.  Show Top Rows\n')
            print('4.  Row Bottom Rows\n')
            print('5.  Show Specific Column\n')
            print('6.  Add a New Record\n')
            print('7.  Add a New Column\n')
            print('8.  Delete a Column\n')
            print('9.  Delete a Record\n')
            print('10.  Exit (Move to main menu)\n')
            ch = int(input('Enter your choice:'))
            if ch == 1:
                print(df)
                wait = input()
            if ch == 2:
                print(df.columns)
                wait = input()
            if ch == 3:
                n = int(input('Enter Total rows you want to show :'))
                print(df.head(n))
                wait = input()
            if ch == 4:
                n = int(input('Enter Total rows you want to show :'))
                print(df.tail(n))
                wait = input()
            if ch == 5:
                print(df.columns)
                col_name = input('Enter Column Name that You want to print : ')
                print(df[col_name])
                wait = input()
            if ch==6:
                a = input('Enter game title :')
                b = input('Enter release date :')
                c = input(' Enter publisher :')
                d=  input('Enter size :')
                data={'Game Title ':a,'Release Date':b,'Publisher':c,'Size':d}
                df = df.append(data,ignore_index=True)
                print(df)
                wait=input()
            if ch==7:
                col_name = input('Enter new column name :')
                col_value = int(input('Enter default column value :'))
                df[col_name]=col_value
                print(df)
                print('\n\n\n Press any key to continue....')
                wait=input()
            
            if ch==8:
                col_name =input('Enter column Name to delete :')
                del df[col_name]
                print(df)
                print('\n\n\n Press any key to continue....')
                wait=input()
            
            if ch==9:
                index_no =int(input('Enter the Index Number that You want to delete :'))
                df = df.drop(df.index[index_no])
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch == 10:
                break
def developer_lowend():
        df = pd.read_csv(csv_file2)
        while True:
            clear()
            print('\n\nData Analysis MENU ')
            print('_'*100)
            print('1.  Show Whole DataFrame\n')
            print('2.  Show Columns\n')
            print('3.  Show Top Rows\n')
            print('4.  Row Bottom Rows\n')
            print('5.  Show Specific Column\n')
            print('6.  Add a New Record\n')
            print('7.  Add a New Column\n')
            print('8.  Delete a Column\n')
            print('9.  Delete a Record\n')
            print('10.  Exit (Move to main menu)\n')
            ch = int(input('Enter your choice:'))
            if ch == 1:
                print(df)
                wait = input()
            if ch == 2:
                print(df.columns)
                wait = input()
            if ch == 3:
                n = int(input('Enter Total rows you want to show :'))
                print(df.head(n))
                wait = input()
            if ch == 4:
                n = int(input('Enter Total rows you want to show :'))
                print(df.tail(n))
                wait = input()
            if ch == 5:
                print(df.columns)
                col_name = input('Enter Column Name that You want to print : ')
                print(df[col_name])
                wait = input()
            if ch==6:
                a = input('Enter game title :')
                b = input('Enter release date :')
                c = input(' Enter publisher :')
                d=  input('Enter size :')
                data={'Game Title ':a,'Release Date':b,'Publisher':c,'Size':d}
                df = df.append(data,ignore_index=True)
                print(df)
                wait=input()
            if ch==7:
                col_name = input('Enter new column name :')
                col_value = int(input('Enter default column value :'))
                df[col_name]=col_value
                print(df)
                print('\n\n\n Press any key to continue....')
                wait=input()
            
            if ch==8:
                col_name =input('Enter column Name to delete :')
                del df[col_name]
                print(df)
                print('\n\n\n Press any key to continue....')
                wait=input()
            
            if ch==9:
                index_no =int(input('Enter the Index Number that You want to delete :'))
                df = df.drop(df.index[index_no])
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch == 10:
                break            

def graph():
    df = pd.read_csv(csv_file3)
    g = df.groupby("Name")
    x = df['Name'].unique()
    y = g['Global_Sales'].unique()
    plt.pie(y, labels=x, autopct='% .2f', startangle=90)
    plt.xticks(rotation='vertical')
    plt.title("The 6 Biggest games ever!")
    plt.show()
        
def main_menu():
           clear()
           introduction()
           while True:
                      clear()
                      print('MAIN MENU ')
                      print('_'*100)
                      print()
                      print('1.  Types Of Games\n')
                      
                      print('2.  List of High End Games\n')
                      print('3.  List of Low End Games\n')
                      print('4. Developer options(high end)\n')
                      print('5. Developer options(low end)\n')
                      print('6 Graph of the 6 most selling games\n')
                      print('7.  Exit\n')
                      choice = int(input('Enter your choice :'))
                      if choice==1:
                                 Digital_Games()
                                 wait=input()
                                 ch = int(input('Enter the gaming genre you want to learn more about:' ))
                                 if ch==1:
                                     print('''
Action games are just that—games where the player is in control of and at the center of the action
                                           Subgenres:
                                           I]Platformer
Platformer games get their name from the fact that the game’s character interacts with platforms (usually running, jumping, or falling) throughout the gameplay
                                           II]Shooter
Shooters let players use weapons to engage in the action, with the goal usually being to take out enemies or opposing players
                                           III]Fighting
Fighting games like Mortal Kombat and Street Fighter II focus the action on combat, and in most cases, hand-to-hand combat
                                           IV]Beat-em up
Beat-em up games, or brawlers, also focus on combat, but instead of facing a single opponent, players face wave after wave of enemies
                                           V]Stealth
Stealth games usually encourage players to engage in the action covertly
                                           
                                           ''')
                                           
                                 if ch==2:
                                      print('''
Adventure games are categorized by the style of gameplay, not the story or content.
                                            Subgenres:
                                            I]Visual novels
Extremely popular in Japan, most visual novels require players to build up character traits or statistics to advance the gameplay
                                            II]Interactive movie
Laserdisc and CD-ROM technology allowed for the introduction of the interactive movie. 
                                            III]Real-time 3D
The latest evolution of adventure games is real-time 3D. Instead of pre-rendered scenes, players interact in a real-time 3D video game world
                                            
                                            ''')
                                            
                                 if ch==3:
                                      print('''
Probably the second-most popular game genre, role-playing games, or RPGs, mostly feature medieval or fantasy settings
                                            Subgenres:
                                            I]Action RPG
Action role-playing games take game elements of both action games and action-adventure games
                                            II]MMORPG
MMORPGs involve hundreds of players actively interacting with each other in the same world, and typically, all players share the same or a similar objective.                                            
                                            III]Rouguelikes
The only other game genre based on the name of the game that inspired it, Rogue was a 2D computer game and dungeon crawler from 1980
                                            ''')
                                            
                                 if ch==4:
                                      print('''
Games in the simulation genre have one thing in common—they're all designed to emulate real or fictional reality, to simulate a real situation or event                                            
                                            Subgenres:
                                            I]Construction and management simulation
SimCity is the most popular construction and management simulation of all time.
                                            II]Life simulation
Simulations may allow players to manipulate a character’s genetics or their ecosystem                                            
                                            III]Vehicle simulation
It’s difficult to rank the most popular vehicle simulation games because sales are equally split between flight simulations and racing simulations
                                            ''')
                                            
                                 if ch==5:
                                      print('''
Gameplay is based on traditional strategy board games, strategy games give players a godlike access to the world and its resources.                                            
                                            Subgenres:
                                            I]4X
A 4x is any genre of strategy video game whose four primary goals check these boxes: explore, expand, exploit, and exterminate
                                            II]Artillery
A general name given to two- or three-player turn-based games featuring tanks or other soldiers engaged in combat
                                            III]Multiplayer online battle arena (MOBA)
Players control a single character in one of two teams, working together to try and destroy the other team’s base                                             
                                           ''')
                                           
                                 if ch==6:
                                      print('''
Sports games simulate sports like golf, football, basketball, baseball, and soccer                                            
                                            Subgenres:
                                            I]Team sports
One of the earliest types of video games genres, team sports games simulate playing a sport
                                            II]Competitive
Fictional sport or competitive games fall into this category.
                                            III]Sports-based fighting
Rooted firmly in the fighting game and sports genre, these games include boxing games like Fight Night and wrestling video games
                                            ''')
                                            
                                 if ch==7:
                                      print('''
Puzzle or logic games usually take place on a single screen or playfield and require the player to solve a problem to advance the action.                                            
                                            Subgenres:
                                            I]Logic game
A logic game requires players to solve a logic puzzle or navigate a challenge like a maze
                                            II]Trivia game
Like real trivia games, video trivia game players must answer a question before a timer runs out 
                                            
                                            ''')          
                                 wait=input()           
                      if choice==2:
                                 read_csv_file()
                                 wait=input()    
                      if choice==3:
                                 read_csv_file2()
                                 wait=input()     
                      if choice==4:
                                 developer_highend()
                                 wait=input()
                      if choice==5:
                                 developer_lowend()
                                 wait=input()
                      if choice==6:
                                 graph()
                                 wait=input()           
                      if choice==7:
                                 break
           clear()
           made_by()

main_menu()
