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
        self._name = None
        self._species = None
        self._gender = None
        self._color = None
        self._edible_items = None
        self._drinkable_items = None

        self._hunger = None
        self._thirst = None
        self._smell = None
        self._loneliness = None
        self._energy = None

        self._name = name.capitalize()
        self._species = species.capitalize()
        self._gender = gender.capitalize()
        self._color = color.capitalize()
        self._edible_items = []
        self._drinkable_items = []

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

    def get_hunger_level(self):
        # return hunger
        return self._hunger
    
    def get_thirst_level(self):
        # return thirst
        return self._thirst
    
    def get_energy_level(self):
        # return energy
        return self._energy
    
    def drink(self, liquid):
	# insert docstring
        if not isinstance(liquid, tuple(self._drinkable_items)):
            return
        if self._thirst < 1:
            print("Your pet is satisfied, no desire for sustenance now.")
            self._time_pass_by()
            return
        self._time_pass_by()
        self._hunger = min(MAX,self._hunger)
        self._thirst = min(MAX,self._thirst)
        self._smell = min(MAX,self._smell)
        self._loneliness = min(MAX,self._loneliness)
        self._energy = max(MIN, self._energy)
        self._thirst = max(MIN,self._thirst-liquid.get_quantity())
        self._reply_to_master('drink')
    
        self._update_status()

    def feed(self, food):
	# insert docstring
        if not isinstance(food, tuple(self._edible_items)):
            return
        if self._hunger < 1:
            print("Your pet is satisfied, no desire for sustenance now.")
            self._time_pass_by()
            return
        self._time_pass_by()
        self._hunger = min(MAX,self._hunger)
        self._thirst = min(MAX,self._thirst)
        self._smell = min(MAX,self._smell)
        self._loneliness = min(MAX,self._loneliness)
        self._energy = max(MIN, self._energy)
        self._hunger = max(MIN,self._hunger-food.get_quantity())
        self._reply_to_master('feed')
        
        self._update_status()


    def shower(self):
	# insert docstring
        time = 4
        self._time_pass_by(time)
        self._hunger = min(MAX,self._hunger)
        self._thirst = min(MAX,self._thirst)
        self._smell = min(MAX,self._smell)
        self._loneliness = min(MAX,self._loneliness)
        self._energy = max(MIN, self._energy)
        
        self._smell = 0
        self._loneliness = max(MIN, self._loneliness - time)

        self._reply_to_master('shower')
        self._update_status()


    def sleep(self):
	# insert docstring
        time = 7
        self._time_pass_by(time)
        self._hunger = min(MAX,self._hunger)
        self._thirst = min(MAX,self._thirst)
        self._smell = min(MAX,self._smell)
        self._loneliness = min(MAX,self._loneliness)
        self._energy = max(MIN, self._energy)
        
        self._energy = min(MAX, self._energy+time)
        
        self._reply_to_master('sleep')
        self._update_status()

    def play_with(self):
	# insert docstring
        time = 4
        self._time_pass_by(time)
        self._hunger = min(MAX,self._hunger)
        self._thirst = min(MAX,self._thirst)
        self._smell = min(MAX,self._smell)
        self._loneliness = min(MAX,self._loneliness)
        self._energy = max(MIN, self._energy)
        
        self._smell = min(MAX,self._smell+time)
        self._loneliness = max(MIN, self._loneliness-time)
        self._energy = max(MIN, self._energy-time)
        
        self._reply_to_master('play')
        self._update_status()

    def _reply_to_master(self, event='newborn'):
	# insert docstring
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
        # partially formatted string for your guidance
        #s = "{:<12s}: [{:<20s}]".format() + "{:5.2f}/{:2d}".format()
        f_energy = float(self._energy)
        f_hunger = float(self._hunger)
        f_loneliness = float(self._loneliness)
        f_smell = float(self._smell)
        f_thirst = float(self._thirst)
        energy = int(round(f_energy,0))
        hunger = int(round(f_hunger,0))
        loneliness = int(round(f_loneliness,0))
        smell = int(round(f_smell,0))
        thirst = int(round(f_thirst,0))
        energy_bar = energy*2*'#'
        hunger_bar = hunger*2*'#'
        loneliness_bar = loneliness*2*'#'
        smell_bar = smell*2*'#'
        thirst_bar = thirst*2*'#'
        print("{:<12s}: [{:<20s}]".format('Energy',energy_bar) + "{:5.2f}/{:2d}".format(f_energy,10))
        print("{:<12s}: [{:<20s}]".format('Hunger',hunger_bar) + "{:5.2f}/{:2d}".format(f_hunger,10))
        print("{:<12s}: [{:<20s}]".format('Loneliness',loneliness_bar) + "{:5.2f}/{:2d}".format(f_loneliness,10))
        print("{:<12s}: [{:<20s}]".format('Smell',smell_bar) + "{:5.2f}/{:2d}".format(f_smell,10))
        print("{:<12s}: [{:<20s}]".format('Thirst',thirst_bar) + "{:5.2f}/{:2d}".format(f_thirst,10))
    
        
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
    def __init__(self,name='fluffy',gender='male',color='white'):
        Pet.__init__(self,name,'cat',gender,color)
        self._edible_items = cat_edible_items
        self._drinkable_items = cat_drinkable_items
        
class Dog(Pet):
    def __init__(self,name='fluffy',gender='male',color='white'):
        Pet.__init__(self,name,'dog',gender,color)
        self._edible_items = dog_edible_items
        self._drinkable_items = dog_drinkable_items

def main():
    print("Welcome to this virtual pet game!")
    prompt = "Please input the species (dog or cat), name, gender (male / female), fur color of your pet, seperated by space \n ---Example input:  [dog] [fluffy] [male] [white] \n (Hit Enter to use default settings): "
    Dog_case = True
    while True:
        command = input(prompt).split()
        if command:
            if command[0] in ['dog','cat'] and command[2] in ['male','female']:
                if command[0] == 'cat':
                    Dog_case = False
                break
            else:
                continue
    if Dog_case:
        pet = Dog(command[1],command[2],command[3])
    else:
        pet = Cat(command[1],command[2],command[3])
    intro = "\nYou can let your pet eat, drink, get a shower, get some sleep, or play with him or her by entering each of the following commands:\n --- [feed] [drink] [shower] [sleep] [play]\n You can also check the health status of your pet by entering:\n --- [status]."
    print(intro)
    
    prompt = "\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): "
    while True:
        act = input(prompt)
        if act == 'q':
            break
        elif act == 'status':
            pet.show_status()
        elif act == 'drink':
            while True:
                scale = input("How much drink ? 1 - 10 scale: ")
                if scale.isdigit():
                    scale = int(scale)
                    if scale <= 10 and scale > 0:
                        pet.drink(Water(scale))
                        break
                print('Invalid input.')
        elif act == 'feed':
            while True:
                scale = input("How much food ? 1 - 10 scale: ")
                if scale.isdigit():
                    scale = int(scale)
                    if scale <= 10 and scale > 0:
                        if Dog_case:
                            pet.feed(DogFood(scale))
                        else:
                            pet.feed(CatFood(scale))
                        break
                print('Invalid input.')
        elif act == 'play':
            pet.play_with()
        elif act == 'sleep':
            pet.sleep()
        elif act == 'shower':
            pet.shower()
        else:
            print('Invalid command.')




            
    # error checking for user input
    # your code goes here #

    # create a pet object
    # your code goes here #



    # your code to handle commands goes here

    print("Bye ~")

if __name__ == "__main__":
    main()
