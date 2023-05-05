level_one = ''
level_two = ''
level_three = ''
print('Welcome to the adventure game')
name_player = input('Whats is your name? ')
print()
print('You wake up in a dark forest. You have no memory of how you got here or where you are. You see a path to your left and a river to your right')
response = input('1.- Do you TAKE THE PATH or 2.- FOLLOW THE RIVER?: ')
if response == '1' or response.upper() == 'TAKE THE PATH':
    print()
    print('You walk along the path and eventually come across a small cabin. You hear noises coming from inside.')
    response_one = input('1.- Do you KNOCK ON THE DOOR or 2.- SNEAK AROUND THE BACK?: ')
    if response_one == '1' or response.upper() == 'KNOCK ON THE DOOR':
        print()
        print('An old man opens the door and greets you. He tells you that he is a hermit and has been living alone in the woods for many years. He offers to help you find your way out of the forest.')
        response_two = input('1.- Do you FOLLOW THE HERMIT or 2.- THANK HIM AND LEAVE?: ')
        if response_two == '1' or response_two.upper() == 'FOLLOW THE HERMIT':
            print()
            print('He takes you to a nearby village where you find out that you have been missing for a week. The hermit is a hero for finding you and you are grateful to him.')
            print()
            print('Congratulations, you have completed Level 1!')
            level_one = 'complete'
        elif response_two == '2' or response_two.upper() == 'THANK HIM AND LEAVE':
            print()
            print('you go further into the forest, suddenly a wild black bear attacks you...')
            print('Game over')
        else: 
            print('Incorrect response')
    elif response_one == '2' or response_one.upper() == 'SNEAK AROUND THE BACK':
        print()
        print('You see a group of bandits inside the cabin. They see you and give chase. You manage to escape, but you lose all of your possessions in the process.')
        print()
        print('Congratulations, you have completed Level 1!')
        level_one = 'complete'
    else:
        print('Incorrect response')
elif response == '2' or response.upper() == 'FOLLOW THE RIVER':
    print()
    print('You come across a waterfall. You can see something shiny behind the waterfall.')
    response_one = input('1.- Do you TRY TO REACH THE SHINY OBJECT or 2.- FOLLOW THE RIVER FURTHER?: ') 
    if response_one == '1' or response_one.upper() == 'TRY TO REACH THE SHINY OBJECT':
        print()
        print('You slip and fall on the wet rocks. You hit your head and black out.')
        print('Game over')
    elif response_one == '2' or response_one.upper() == 'FOLLOW THE RIVER FURTHER':
        print()
        print('You eventually find a bridge that takes you across the river. On the other side, you see a sign that says "Welcome to the Enchanted Forest".')
        print()
        print('Congratulations, you have completed Level 1!')
        level_one = 'complete'
    else:
        print('Incorrect response')
else:
    print('Incorrect response')



if level_one == 'complete':
    print('Welcome to the level two')

    print()
    print('You are now in the Enchanted Forest. You see a castle in the distance and a cave to your right.')
    response = input('Do you 1.- HEAD TOWARDS THE CASTLE or 2.- ENTER THE CAVE? ')
    if response == '1' or response.upper() == 'HEAD TOWARDS THE CASTLE':
        print()
        print('You come across a dragon blocking your path. It looks angry.')
        print()
        response_two = input('Do you 1.- ATTACK THE DRAGON or 2.- TRY TO SNEAK PAST IT? ')
        if response_two == '1' or response_two.upper() == 'ATTACK THE DRAGON':
            print()
            print('You manage to defeat the dragon, but you are badly injured in the process.')
            print()
            print('Congratulations, you have completed Level 2!')
            level_two = 'complete'
        elif response_two == '2' or response_two.upper() == 'TRY TO SNEAK PAST IT':
            print()
            print('The dragon sees you and burns you to a crisp.')
            print()
            print('GAME OVER')
        else:
            print('Incorrect response')
    elif response == '2' or response.upper() == 'ENTER THE CAVE':
        print()
        print('You see two tunnels. One on the left and one on the right.')
        print()
        response_two = input('Do you 1.- GO LEFT or 2.- GO RIGHT? ')
        if response_two == '1' or response_two.upper() == 'GO LEFT':
            print()
            print('You come across a treasure chest. You can see that it is booby-trapped.')
            print()
            response_three = input('Do you 1.- OPEN THE CHEST or 2.- LEAVE IT ALONE? ')
            if response_three == '1' or response_three.upper() == 'OPEN THE CHEST':
                print()
                print('You trigger the booby trap and are killed instantly.')
                print()
                print('GAME OVER')
            elif response_three == '2' or response_three.upper() == 'LEAVE IT ALONE':
                print()
                print('You continue through the cave and eventually find your way out.')
                level_two = 'complete'
                print('Congratulations, you have completed Level 2!')
            else:
                print('Incorrect response')
        elif response_two == '2' or response_two.upper() == 'GO RIGHT':
                print()
                print('you found the nest of a basilisk and there are some eggs')
                print()
                response_three = input('Do you 1.- TURN AROUND QUIETLY or do you 2.- TRY TO STEAL ONE? ')
                if response_three == '1' or response_three.upper() == 'TURN AROUND QUIETLY':
                    print()
                    print('You manage to find your way out of the nest and eventually get out of the cave')
                    level_two = 'complete'
                    print('Congratulations, you have completed Level 2!')
                elif response_three == '2' or response_three.upper() == 'TRY TO STEAL ONE':
                    print()
                    print("You stepped on something you shouldn't, the cave collapses!")
                    print()
                    print('GAME OVER')
                else:
                    print('Incorrect response')
        else:
            print('Incorrect response')

else:
    print('You lose, try again')


if level_one == 'complete' and level_two == 'complete':
    print()
    print('Welcome to the final level')
    print('LEVEL 3')

    print()
    print('You are now outside of the castle. You see guards patrolling the walls and a moat surrounding the castle.')
    response = input('Do you 1.- TRY TO SNEAK PAST THE GUARDS or 2.- TRY TO SWIM ACROSS THE MOAT? ')
    if response == '1' or response.upper() == 'TRY TO SNEAK PAST THE GUARDS':
        print()
        print('You manage to sneak past the guards and make your way into the castle. You see a room with a large chest in the center.')
        print()
        response_two = input('Do you 1.- OPEN THE CHEST or 2.- CONTINUE EXPLORING THE CASTLE? ')
        if response_two == '1' or response_two.upper() == 'OPEN THE CHEST':
            print()
            print('You open the chest to reveal a large stash of treasure, but as you reach in to grab some, a hidden trap activates and the room starts filling up with poison gas! You need to find a way out quickly')
            response_three = input(' Do you 1.- LOOK FOR A VENTILATION SHAFT or 2.- TRY TO BREAK DOWN THE WALL? ')
            if response_three == '1' or response_three.upper() == 'LOOK FOR A VENTILATION SHAFT':
                print()
                print('You manage to find a ventilation shaft and crawl your way out to safety, treasure in hand')
                print("Congratulations, you've completed the quest!")
                level_three = 'complete'
            elif response_three == '2' or response_three.upper() == 'TRY TO BREAK DOWN THE WALL':
                print()
                print("You attempt to break down the wall, but it's too thick and you quickly run out of breath. As the gas fills your lungs, you collapse to the ground, ending your quest.")
                print()
                print('GAME OVER')
            else: 
                print('Incorrect response')
        elif response_two == '2' or response_two.upper() == 'CONTINUE EXPLORING THE CASTLE':
            print()
            print('You make your way deeper into the castle and come across a group of guards. They catch you and throw you into the dungeon.')
            response_three = input('Do you 1.- ATTEMPT TO ESCAPE or 2.- WAIT FOR RESCUE? ')
            if response_three == '1' or response_three.upper() == 'ATTEMPT TO ESCAPE':
                print()
                print('You manage to escape your cell and sneak your way out of the dungeon, but as you make your way towards the exit, you are caught by the guards and killed')
                print('GAME OVER')
            elif response_three == '2' or response_three.upper() == 'WAIT FOR RESCUE':
                print()
                print("You wait for a few hours until a group of rebels comes to your aid and helps you escape the castle")
                print("Congratulations, you've completed the quest!")
                level_three = 'complete'
            else:
                print('Incorrect response')
    elif response == '2' or response.upper() == 'TRY TO SWIM ACROSS THE MOAT':
        print()
        print('You jump into the moat and start swimming towards the castle. The water is freezing and you start to feel your muscles cramping up. Suddenly, you hear a loud roar and see a giant crocodile swimming towards you.')
        response_two = input('Do you 1.- CONTINUE SWIMMING or 2.- TRY TO SWIM BACK TO SHORE? ')
        if response_two == '1' or response_two.upper() == 'CONTINUE SWIMMING':
            print()
            print("You manage to dodge the crocodile's attacks and make it to the other side of the moat. You climb out of the water and sneak into the castle. Where you find the treasure")
            print("Congratulations, you've completed the quest!")
            level_three = 'complete'
        elif response_two == '2' or response_two.upper() == 'TRY TO SWIM BACK TO SHORE':
            print()
            print('You start swimming back towards the shore, but the crocodile catches up to you and attacks. You are unable to defend yourself and the crocodile drags you underwater.')
            print('GAME OVER')
        else:
            print('Incorrect response')
    else:
        print('Incorrect response')


else:
    print('You lose, try again')


if level_one == 'complete' and level_two == 'complete' and level_three == 'complete':
    print()
    print(f'Congratulations oh brave warrior, your name will be remembered on this earth for all the years, long live the great warrior {name_player.capitalize()}')


#NAME: JOSE ANGEL ARTEAGA
# FOR ADVENTURE ACTIVITY WEEK 3
#FOR THIS ASIGNMENTE I TRY TO MAKE AN ADVENTURE GAME, I USE THE IF, ELIF AND ELSE TO GUIDE THE HISTORY, FOR DO MORE THAT THE MINIMUN #REQUIREMENTS I ADD SOME THINGS, FOR EXAMPLE THE ORIGINAL ACTIVITY THE RESPONSE FROM THE USER WOULD BE A STRING OF WORDS, SO I ACCEPT WORDS OR #ONLY A NUMBER, USING THE OR CONDITION INTO THE IF, I ADD TOO A INDICATOR OF LEVELS COMPLETES, AND A FINAL PRINT ONLY IF THE THREE LEVELS WAS #COMPLETEDS, I ADD THE .UPPER FOR THE WORDS FOR THE COMPARING SITUATIONS.