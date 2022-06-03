###############################################################################
#  Project #11
#
#  Algorithm
#    print headers
#    the player choose the species, name, gender, color of pet
#    print the introduction of pet
#    the player choose the action(feed,drink,shower, sleep, play) of pet
#    use while loop make the pet keep activity
#    use the if statement to make the pet active
#    if the active is vaild, updata the status of pet and show the master
#    if not, report the error and ask the player again
#    calculate the change of energy,hunger,loneliness,smell,thirst
#    updata the newest status of pet
#    if the player enter 'q', game over. print("Bye ~")
###############################################################################
from cse231_random import randint
from edible import *

MIN, MAX = 0, 10
dog_edible_items = [DogFood]
cat_edible_items = [CatFood]
dog_drinkable_items = [Water]
cat_drinkable_items = [Water]

class Pet(object):
    def __init__(self, name='fluffy', species='dog', gender='male',color='white'):
        '''
        This function contains the pet's initial value, which I'll use 
        capitalize() to capitalize the property value. And I will use randint
        to limit the range of values.
        '''
        
        self._name = name.capitalize()
        self._species = species.capitalize()
        self._gender = gender.capitalize()
        self._color = color.capitalize() # translate to capitalize
        self._edible_items = []
        self._drinkable_items = []

        self._hunger = randint(0,5) 
        self._thirst = randint(0,5)
        self._smell = randint(0,5)
        self._loneliness = randint(0,5) # the range bwt 0 and 5
        self._energy = randint(5,10) # the range bwt 5 and 10

        self._reply_to_master('newborn') # the pet will born, shower the master

    def _time_pass_by(self, t=1):
        '''
        These values change as the pet is active. In this function, it will
        recieve the status of pets, and updata pet's status.
        '''
        # this function is complete
        self._hunger = min(MAX, self._hunger + (0.2 * t))
        self._thirst = min(MAX, self._thirst + (0.2 * t))
        self._smell = min(MAX, self._smell + (0.1 * t))
        self._loneliness = min(MAX, self._loneliness + (0.1 * t))
        self._energy = max(MIN, self._energy - (0.2 * t))

    def get_hunger_level(self):
        '''
        This function will get the hunger level of pet, and return the value 
        of the hunger.
        '''
	
        return self._hunger# replace with your code

    def get_thirst_level(self):
        '''
        This function will get the thirst level of pet, and return the value 
        of the thirst.
        '''
        return self._thirst  # replace with your code

    def get_energy_level(self):
        '''
        This function will get the energy level of pet, and return the value 
        of the energy.
        '''
        return self._energy  # replace with your code

    def drink(self, liquid):
        '''
        This function will receive the latest status of the pet, and returns 
        the pet's response after drinking, and updates the pet's status. 
        first, use if-else to check the value liquid if vaild. And if the value
        of thirst less than 2, the pet neednot to drink, also, the value of 
        thirst doesn't go negative.
        '''
        
        if isinstance(liquid, tuple(self._drinkable_items)):
            self._time_pass_by()
            if 0 <= self._thirst < 2: # if the value of thirst is less than 2
                print("Your pet is satisfied, no desire for sustenance now.")
                # the pet need not to drink
            elif self._thirst <=liquid.get_quantity(): 
                # if the fluid value is greater than the thirst value
                # the pet will drink and thirst equal 0
                self._thirst = 0
                self._reply_to_master('drink') # shower the pet's master
            else:
                self._thirst -= liquid.get_quantity()
                self._reply_to_master('drink') # shower the pet's master
                
        else:
            print("Not drinkable") # if the value is vaild
            
        self._thirst = max(MIN,self._thirst) 
        self._update_status() # update the pet's status
    
    def feed(self, food):
        '''
        This function is simlar to last one. It will receive the newest status
        of the pet, and return the pet's response after eating, and updata the
        pet's status.
        '''
        
        if isinstance(food, tuple(self._edible_items)):
            self._time_pass_by()
            if 0 <=self._hunger < 2: # if the value of hunger less than 2
                print("Your pet is satisfied, no desire for sustenance now.")
                #the pet need not to eat food
            elif self._hunger <=food.get_quantity():
                # the hunger not less than 0
                self._hunger = 0
                self._reply_to_master('feed') # show the pet's master
            else:
                self._hunger -= food.get_quantity()
                self._reply_to_master('feed')
                
        else:
            print("Not eatable") # the value of feed is vaild
            
        self._hunger = max(MIN,self._hunger)
        self._update_status() # updata the newest status

    def shower(self):
        '''
        This function will call the _time_pass_by(), and updata the status of
        pet after showing. The shower will take a time =4, and the value of 
        smell,loneliness will change.
        '''
        time =4
        self._time_pass_by(time) #get the status of pet
        self._smell = 0 # After a bath, the value of smell will be zero.
        self._loneliness = max(MIN,self._loneliness-time)  
        # the loneliness of pet will decrease over time
        # and the number will stay between 0 and 10
        
        self._reply_to_master('shower') #shower the master
        self._update_status() # updata
        
    def sleep(self):
        '''
        This function will call the _time_pass_by(), and updata the status of
        pet after sleeping. It will increase energy over time.
        '''
        time = 7 # the time is 7
        self._time_pass_by(time)
        self._energy = min(MAX,self._energy + time) # updata the energy
        
        self._reply_to_master('sleep') # shower the master
        self._update_status() #updata the status

    def play_with(self):
        '''
        This function will call the _time_pass_by(), and updata the status of
        pet after playing. It will increase energy and loneliness and increase
        smell over time.
        '''
        time = 4 # the time is 4
        self._time_pass_by(time) # get the data
        self._loneliness = max(MIN,self._loneliness-time) # updata the new act
        self._smell = min(MAX,self._smell + time)
        self._energy = max(MIN,self._energy - time)
        
        self._reply_to_master('play') # shower the master
        self._update_status() # updata

    def _reply_to_master(self, event='newborn'):
        '''
        This function displays the pet's master after the activity.
        '''
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
        '''
        This function will show the status of pet. It will have an energy bar 
        that USES a well sign to represent the pet. Also, Attribute values will
        be sorted in alphabetical order.
        '''
	
        # partially formatted string for your guidance
        energy = int(round(float(self._energy),MIN)) 
         # round the number of energy and use int to get a integer
        energy_well = energy*"##"
        print("{:<12s}: [{:<20s}]".format('Energy',energy_well) + 
              "{:5.2f}/{:2d}".format(self._energy,MAX))
        # print them
        hunger = int(round(float(self._hunger),MIN))
        hunger_well = hunger*"##"
        print("{:<12s}: [{:<20s}]".format('Hunger',hunger_well) + 
              "{:5.2f}/{:2d}".format(self._hunger,MAX))
        # round the number of loneliness and use int to get a integer
        loneliness = int(round(float(self._loneliness),MIN))
        loneliness_well = loneliness*"##"
        print("{:<12s}: [{:<20s}]".format('Loneliness',loneliness_well) + 
              "{:5.2f}/{:2d}".format(self._loneliness,MAX))
        
        smell = int(round(float(self._smell),MIN))
        smell_well = smell*"##"
        print("{:<12s}: [{:<20s}]".format('Smell',smell_well) + 
              "{:5.2f}/{:2d}".format(self._smell,MAX))

        thirst = int(round(float(self._thirst),MIN))
        thirst_well = thirst*"##"
        print("{:<12s}: [{:<20s}]".format('Thirst',thirst_well) + 
              "{:5.2f}/{:2d}".format(self._thirst,MAX))
        
    def _update_status(self):
        '''
        This function will updata the status of pet.
        '''
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
    '''
    This class inherits the Cat class. I will call the function of __init__ to
    get the data. And updata the attribute of cat.
    '''
    def __init__(self,name='fluffy',gender='male',color='white'):
        Pet.__init__(self,name,'cat',gender,color)
        self._drinkable_items = cat_drinkable_items # updata the attribute
        self._edible_items = cat_edible_items
        
class Dog(Pet):
    '''
    This class is similar to last one, which wii inherits the Dog class.
    And I will call the function of __init__ to get the data. And updata the 
    attribute of dog.
    ''' 
    def __init__(self,name='fluffy',gender='male',color='white'): # call it
        Pet.__init__(self,name,'dog',gender,color)
        self._drinkable_items = dog_drinkable_items
        self._edible_items = dog_edible_items # # updata the attribute
def main():
    '''
    Run the above function according to the answer of player.
    '''
    print("Welcome to this virtual pet game!") #the header
    prompt = "Please input the species (dog or cat), name, gender (male / female), fur color of your pet, seperated by space \n ---Example input:  [dog] [fluffy] [male] [white] \n (Hit Enter to use default settings): "

    dog_data = True
    while True:
        input_answer = input(prompt)
        answer = input_answer.split() # split the answer
        if answer != {}:
            if answer[0] in ['dog','cat']: #only can choose cat or dog
                if answer[2] in ['male','female']:
                    # the gender of the pet is valid
                    if answer[0] == 'cat': # the player choose cat
                        dog_data = False
                    break
                else:
                    continue
    if dog_data:
        pet = Dog(answer[1],answer[2],answer[3]) # # the player choose dog
    else:
        pet = Cat(answer[1],answer[2],answer[3])# the player choose cat
        
    print("\nYou can let your pet eat, drink, get a shower, get some sleep, or play with him or her by entering each of the following commands:\n --- [feed] [drink] [shower] [sleep] [play]\n You can also check the health status of your pet by entering:\n --- [status].")

    while True:
        prompt = "\n[feed] or [drink] or [shower] or [sleep] or [play] or [status] ? (q to quit): "
        result = input(prompt)
        # the player choose the action of pet
        if result =='status': # show the pet's status
            pet.show_status()

        elif result == 'feed': # the player want to feed to the pet
            
            while True:
                food_scale = input('How much food ? 1 - 10 scale: ')
                # ask the player the number of food to pet
                if food_scale.isdigit() == True:
                    # if the number of food is vaild
                    scale_food = int(food_scale) # this number must be an int
                    if 0 < scale_food < 11:  # only can choose 1-10
                        if pet._species == 'Cat': 
                            pet.feed(CatFood(scale_food))
                            break
                            
                        elif pet._species == 'Dog':
                            pet.feed(DogFood(scale_food))
                            break
                    else: # If not, report an error, and ask the player again
                        print('Invalid input.')
                        continue
                  
                elif food_scale.isdigit() == False: # if the number is invaild
                    print('Invalid input.') 
                    continue # ask the player again
                    
        elif result =='drink': # the pet will have a drink
            
            while True:
                drink_scale = input('How much drink ? 1 - 10 scale: ')
                if drink_scale.isdigit() == True: # the input is digit
                    scale_drink = int(drink_scale) # must be an integer
                    if 0 < scale_drink < 11:
                        if pet._species == 'Cat': # if the species is cat
                            pet.drink(Water(scale_drink))
                            break
                        elif pet._species == 'Dog':
                            pet.drink(Water(scale_drink))
                            break
                    else:
                        print('Invalid input.') # if not, repost the error
                        continue
                   
                elif drink_scale.isdigit() == False: 
                    # If the input is not all digits
                    print('Invalid input.')
                    continue
                    
        elif result =='sleep': # call the sleep function
            pet.sleep()
        elif result =='play': # the answer is play
            pet.play_with()
        elif result == 'shower': # the pet will shower
            pet.shower()
        elif result.lower() == 'q': # the player want to quit this game
            break # game over
        else:
            print('Invalid command.') # if the answer is invaild
            
    print("Bye ~") # the ending scentence

if __name__ == "__main__":
    main()