#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:21:40 2018

@author: yangmiao
"""

if __name__ == "__main__":
    main()


def main():
    print("Welcome to this virtual pet game!")
    prompt = "Please input the species (dog or cat), name, gender (male / female), fur color of your pet, seperated by space \n ---Example input:  [dog] [fluffy] [male] [white] \n (Hit Enter to use default settings): "
    
    dog_data = True
    while True:
        input_answer = input(prompt)
        answer = input_answer.split()
        if answer != None:
            if answer[0] in ['dog','cat']:
                if answer[2] in ['male','female']:
                    if answer[0] == 'cat':
                        dog_data = False
                    else:
                        break
                else:
                    continue
    if dog_data:
        pet = Dog(answer[1],answer[2],answer[3])
    else:
        pet = Cat(answer[1],answer[2],answer[3])
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
#    def drink(self, liquid):
#        # insert docstring
#        self._time_pass_by()
#
#        if isinstance(liquid, tuple(self._drinkable_items)):
#            if self._thirst<2:
#                print("Too much drink to finish. I will leave some for you.")
#                self._thirst = 0
#            else:
#                self._thirst -= liquid.get_quantity()
#                self._reply_to_master("drink")
#
#        else:
#            print('Not drinkable.')
#        self._thirst = max(MIN, self._thirst)
#        self._update_status()
################
#    def drink(self, liquid):
#	# insert docstring
#        if not isinstance(liquid, tuple(self._drinkable_items)):
#            return
#        if self._thirst < 1:
#            print("Your pet is satisfied, no desire for sustenance now.")
#            self._time_pass_by()
#            return
#        self._time_pass_by()
#        self._hunger = min(MAX,self._hunger)
#        self._thirst = min(MAX,self._thirst)
#        self._smell = min(MAX,self._smell)
#        self._loneliness = min(MAX,self._loneliness)
#        self._energy = max(MIN, self._energy)
#        self._thirst = max(MIN,self._thirst-liquid.get_quantity())
#        self._reply_to_master('drink')
#    
#        self._update_status()


#def main():
#    print("Welcome to this virtual pet game!")
#    prompt = "Please input the species (dog or cat), name, gender (male / female), fur color of your pet, seperated by space \n ---Example input:  [dog] [fluffy] [male] [white] \n (Hit Enter to use default settings): "
#
#    while True:
#        answer = input(prompt).split(' ')
#        if len(answer) < 5:
#            if answer[0] == 'cat':
#                dog_data = False
#                break
#            elif answer[0] == 'dog':
#                dog_data = True
#                break
#    if dog_data == True:
#        pet = Dog(answer[1],answer[2],answer[3])
#    elif dog_data == False:
#        pet = Cat(answer[1],answer[2],answer[3])
#
#    intro = "\nYou can let your pet eat, drink, get a shower, get some sleep, or play with him or her by entering each of the following commands:\n --- [feed] [drink] [shower] [sleep] [play]\n You can also check the health status of your pet by entering:\n --- [status]."
#    print(intro)
##
#    while True:
#        prompt = "\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): "
#        result = input(prompt)
#        if result == 'status':
#            pet.show_status()
#        elif result == 'play':
#            pet.play_with()
#        elif result == 'sleep':
#            pet.sleep()
#        elif result == 'shower':
#            pet.shower()
#        elif result == 'feed':
#            while True:
#                food_scale = input("How much food ? 1 - 10 scale: ")
#                if food_scale.isdigit():
#                    if 0 < int(food_scale) < 11:
#                        if pet.species == 'Cat':
#                            pet.feed(CatFood(scale))
#                        else:
#                            pet.feed(DogFood(scale))
#                        break
#                print("Invalid input.")
#            
#        elif result == 'drink':
#            while True:
#                drink_scale = input("How much drink ? 1 - 10 scale: ")
#                if drink_scale.isdigit():
#                    if 0 < int(drink_scale) < 11:
#                        pet.drink(Water(scale))
#                        break
#                print("Invalid input.")
#        elif result == 'q':
#            break
#        else:
#            print("Invalid command.")
#
#    print("Bye ~")
#
#if __name__ == "__main__":
#    main()
