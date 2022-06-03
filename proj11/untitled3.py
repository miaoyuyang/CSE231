#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:03:55 2018

@author: yangmiao
"""

from cse231_random import randint
from edible import *

MIN, MAX = 0, 10
dog_edible_items = [DogFood]
cat_edible_items = [CatFood]
dog_drinkable_items = [Water]
cat_drinkable_items = [Water]

class Pet(object):
    def __init__(self, name='fluffy', species='dog', gender='male',color='white'):
        # insert docstring
        # modify the following code
        self._name = name.capitalize()
        self._species = species.capitalize()
        self._gender = gender.capitalize()
        self._color = color.capitalize()

        self._drinkable_items = []
        self._edible_items = []

        self._hunger = randint(0,5)
        self._thirst = randint(0,5)
        self._smell = randint(0,5)
        self._loneliness = randint(0,5)
        self._energy = randint(5,10)

        self._reply_to_master('newborn')


    def _time_pass_by(self, t=1):
        # insert docstring
        # this function is complete
        self._hunger += 0.2 * t
        self._thirst += 0.2 * t
        self._smell += 0.1 * t
        self._loneliness +=  0.1 * t
        self._energy -= 0.2 * t

        self._energy = max(MIN, self._energy)
        self._hunger = min(MAX, self._hunger)
        self._thirst = min(MAX, self._thirst)
        self._smell = min(MAX, self._smell)
        self._loneliness = min(MAX, self._loneliness)

    def get_hunger_level(self):
        # insert docstring
        return self._hunger

    def get_thirst_level(self):
        # insert docstring
        return self._thirst

    def get_energy_level(self):
        # insert docstring
        return self._energy

    def drink(self, liquid):
        # insert docstring
        self._time_pass_by()

        if isinstance(liquid, tuple(self._drinkable_items)):
            if self._thirst<2:
                print("Too much drink to finish. I will leave some for you.")
                self._thirst = 0
            else:
                self._thirst -= liquid.get_quantity()
                self._reply_to_master("drink")

        else:
            print('Not drinkable.')
        self._thirst = max(MIN, self._thirst)
        self._update_status()

    def feed(self, food):
        # insert docstring
        self._time_pass_by()

        if isinstance(food, tuple(self._edible_items)):
            if self._hunger<2:
                print("Your pet is satisfied, no desire for sustenance now.")
            else:
                self._hunger-=food.get_quantity()
                self._reply_to_master("feed")

        else:
            print('Not eatable')
        self._hunger = max(MIN, self._hunger)
        self._update_status()

    def shower(self):
        # insert docstring
        time = 4
        self._time_pass_by(time)

        self._smell = 0
        self._loneliness -= time
        self._loneliness = max(MIN,self._loneliness)

        self._reply_to_master('shower')
        self._update_status()



    def sleep(self):
        # insert docstring
        time = 7
        self._time_pass_by(time)

        self._energy += time
        self._energy = min(MAX, self._energy)

        self._reply_to_master('sleep')
        self._update_status()


    def play_with(self):
        # insert docstring
        time = 4
        self._time_pass_by(time)

        self._loneliness -= time
        self._energy -= time
        self._smell += time

        self._loneliness = max(MIN, self._loneliness)
        self._energy = max(MIN, self._energy)
        self._smell = min(MAX, self._smell)

        self._reply_to_master('play')
        self._update_status()


    def _reply_to_master(self, event='newborn'):
        # Print reply message to console
        # this function is complete #
        faces = {}
        talks = {}
        faces['newborn'] = "(๑>◡<๑)"
        faces['feed'] = "(๑´ڡ`๑)"
        faces['drink'] = "(๑´ڡ`๑)"
        faces['play'] = "(ฅ^ω^ฅ)"
        faces['sleep'] = "୧(๑•̀⌄•́๑)૭✧"
        faces['shower'] = "( •̀ .̫ •́ )✧"

        talks['newborn'] = "Hi master, my name is {}.".format(self._name)
        talks['feed'] = "Yummy!"
        talks['drink'] = "Tasty drink ~"
        talks['play'] = "Happy to have your company ~"
        talks['sleep'] = "What a beautiful day!"
        talks['shower'] = "Thanks ~"

        s = "{} ".format(faces[event])  + ": " + talks[event]
        print(s)

    def show_status(self):
        # insert docstring
        prog = int(round(self._energy)/MAX*20)
        print("{:<12s}: [{:<20s}]".format('Energy',"#"*prog) + "{:5.2f}/{:2d}".format(self._energy,MAX))

        prog = int(round(self._hunger)/MAX*20)
        print("{:<12s}: [{:<20s}]".format('Hunger',"#"*prog) + "{:5.2f}/{:2d}".format(self._hunger,MAX))

        prog = int(round(self._loneliness)/MAX*20)
        print("{:<12s}: [{:<20s}]".format('Loneliness',"#"*prog) + "{:5.2f}/{:2d}".format(self._loneliness,MAX))

        prog = int(round(self._smell)/MAX*20)
        print("{:<12s}: [{:<20s}]".format('Smell',"#"*prog) + "{:5.2f}/{:2d}".format(self._smell,MAX))

        prog = int(round(self._thirst)/MAX*20)
        print("{:<12s}: [{:<20s}]".format('Thirst',"#"*prog) + "{:5.2f}/{:2d}".format(self._thirst,MAX))



    def _update_status(self):
        # insert docstring
        # this function is complete #
        faces = {}
        talks = {}
        faces['default'] = "(๑>◡<๑)"
        faces['hunger'] = "(｡>﹏<｡)"
        faces['thirst'] = "(｡>﹏<｡)"
        faces['energy'] = "(～﹃～)~zZ"
        faces['loneliness'] = "(๑o̴̶̷̥᷅﹏o̴̶̷̥᷅๑)"
        faces['smell'] = "(๑o̴̶̷̥᷅﹏o̴̶̷̥᷅๑)"

        talks['default'] = 'I feel good.'
        talks['hunger'] = 'I am so hungry ~'
        talks['thirst'] = 'Could you give me some drinks? Alcohol-free please ~'
        talks['energy'] = 'I really need to get some sleep.'
        talks['loneliness'] = 'Could you stay with me for a little while ?'
        talks['smell'] = 'I am sweaty'

class Cat(Pet):
    def __init__(self, name='fluffy', gender='male', color='white' ):
        super().__init__(name, 'cat', gender, color)
        self._drinkable_items = cat_drinkable_items
        self._edible_items = cat_edible_items

class Dog(Pet):
    def __init__(self, name='fluffy', gender='male', color='white'):
        super().__init__(name, 'dog', gender, color)
        self._drinkable_items = dog_drinkable_items
        self._edible_items = dog_edible_items


def main():
    print("Welcome to this virtual pet game!")
    prompt = "Please input the species (dog or cat), name, gender (male / female), fur color of your pet, seperated by space \n ---Example input:  [dog] [fluffy] [male] [white] \n (Hit Enter to use default settings): "

    # create a pet object
    while True:
        petinput = input(prompt)
        petargs = petinput.split(' ')
        if len(petargs)==4 :
            if petargs[0] == 'cat':
                pet = Cat(*petargs[1:])
                break
            elif petargs[0] == 'dog':
                pet = Dog(*petargs[1:])
                break

    intro = "\nYou can let your pet eat, drink, get a shower, get some sleep, or play with him or her by entering each of the following commands:\n --- [feed] [drink] [shower] [sleep] [play]\n You can also check the health status of your pet by entering:\n --- [status]."
    print(intro)

    while True:
        prompt = "\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): "
        cmd = input(prompt)

        if cmd=='status':
            pet.show_status()
        elif cmd=='sleep':
            pet.sleep()
        elif cmd=='play':
            pet.play_with()
        elif cmd == 'shower':
            pet.shower()
        elif cmd == 'feed':
            scalestr = input('How much food ? 1 - 10 scale: ')
            while True:
                if scalestr.isnumeric() :
                    scale = int(scalestr)
                    if 1<=scale<=10:
                        if pet._species == 'Dog':
                            pet.feed(DogFood(scale))
                            break
                        elif pet._species == 'Cat':
                            pet.feed(CatFood(scale))
                            break
                print('Invalid input.')
                scalestr = input('How much food ? 1 - 10 scale: ')
        elif cmd=='drink':
            scalestr = input('How much drink ? 1 - 10 scale: ')
            while True:
                if scalestr.isnumeric() :
                    scale = int(scalestr)
                    if 1<=scale<=10:
                        pet.drink(Water(scale))
                        break
                print('Invalid input.')
                scalestr = input('How much drink ? 1 - 10 scale: ')
        elif cmd=='q':
            break
        else:
            print('Invalid command.')
    print("Bye ~")

if __name__ == "__main__":
    main()
