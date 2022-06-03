###############################################################################
#   Project 4
#
#   First we define the values we need
#   We determine the outcome of the game by calculating the sum of the dice
#       and use if-elif-else loop to check them
#       if command == "win" or "loss" or "neither"
#           We think about these processes separately, and we output the results
#               and command == "neither", We need to discuss them separately again.
#                   Finally, we use if to discuss whether the game continues
#                       and whether the balance of the bet is valid 
#
###############################################################################

from cse231_random import randint #from random import randint 

def display_game_rules():
    print('''A player rolls two dice. Each die has six faces. 
          These faces contain 1, 2, 3, 4, 5, and 6 spots. 
          After the dice have come to rest, 
          the sum of the spots on the two upward faces is calculated. 
          If the sum is 7 or 11 on the first throw, the player wins. 
          If the sum is 2, 3, or 12 on the first throw (called "craps"), 
          the player loses (i.e. the "house" wins). 
          If the sum is 4, 5, 6, 8, 9, or 10 on the first throw, 
          then the sum becomes the player's "point." 
          To win, you must continue rolling the dice until you "make your point." 
          The player loses by rolling a 7 before making the point.''')

# star balance
# star wager
#当前资金 大于 卡内余额 减去 消费余额 加上 增加金额

def get_bank_balance():
    star_balance = int(input("Enter an initial bank balance (dollars): "))
    return star_balance 

def add_to_bank_balance(balance):
    add_balance = int(input("Enter how many dollars to add to your balance: "))
    return add_balance

def get_wager_amount():
    star_wager = int(input("Enter a wager (dollars): "))
    return star_wager 

def is_valid_wager_amount(wager, balance):
    if wager <= balance:
        return True
    else:
        return False
      
def roll_die():
    roll_n = randint(1,6) # die roll number
    return roll_n

def calculate_sum_dice(value_die1, value_die2):
    return int(value_die1) + int(value_die2)

def first_roll_result(sum_dice):
    '''If the sum is 7 or 11 on the roll, the player wins and "win" is returned.
    If the sum is 2, 3, or 12 on the first throw (called "craps"),
    the player loses (i.e.the "house" wins) and "loss" is returned.
    If the sum is 4, 5, 6, 8, 9, or 10 on the first throw, 
    then the sum becomes the player's "point" and "point" is returned.'''
    if sum_dice == 7 or sum_dice == 11:
        return "win" #player win
    if sum_dice == 2 or sum_dice == 3 or sum_dice == 12:
        return "loss"   #player loss, house win
    if sum_dice == 4 or 5 or 6 or 7 or 8 or 9 or 10:
        return "point"   
    
def subsequent_roll_result(sum_dice, point_value):
    '''If sum_dice is the point_value, then “point” is returned.
    If sum_dice is 7, then “loss” is returned.
    Otherwise, “neither” is returned.'''
    if sum_dice == point_value:
        return "point"
    elif sum_dice == 7:
        return "loss"
    else:
        return "neither"

def main():
    play_game = True
    display_game_rules()
    int_balance = get_bank_balance()
    count_wager = get_wager_amount()
    while not is_valid_wager_amount(count_wager,int_balance):   #problem
        print("Error: wager > balance. Try again.")
        count_wager = get_wager_amount()
        continue
    while play_game == True:
     #   count_wager = get_wager_amount()
     #   while not is_valid_wager_amount(count_wager,int_balance):   
    #        print("Error: wager > balance. Try again.")
     #       count_wager = get_wager_amount()
      #      continue
    
        value_die1 = roll_die()
        value_die2 = roll_die()
        sums_dice = int(value_die1) + int(value_die2)
        print("Die 1:",value_die1)
        print("Die 2:",value_die2)
        print("Dice sum:",sums_dice)
        
        if first_roll_result(sums_dice) == "win":
            print("Natural winner.")
            print("You WIN!")
            int_balance += count_wager
            print("Balance:",int_balance)
            game_2 = input("Do you want to continue? ")
            if game_2 == "yes":
                add_balance = input("Do you want to add to your balance? ")
                if add_balance == "yes":
                    value_add_balance = input("Enter a wager (dollars):")
                    value_add_balance = int(value_add_balance)
                    int_balance += value_add_balance
                    print("Balance: ",int_balance)
                    continue
                    
                if value_add_balance == "no":
                    if int_balance == 0:
                        print("You don't have sufficient balance to continue.")
                        print("Game is over.")
                        break
                    continue
            elif game_2 == "no":
                print("Game is over.")
                break
        elif first_roll_result(sums_dice) == "loss":
            print("Craps.")
            print("You lose.")
            int_balance -= count_wager
            print("Balance:",int_balance)
            game_2 = input("Do you want to continue? ")
            if game_2 == "yes":
                add_balance = input("Do you want to add to your balance? ")
                if add_balance == "yes":
                    value_add_balance = input("Enter a wager (dollars):")
                    value_add_balance = int(value_add_balance)
                    int_balance += value_add_balance
                    print("Balance: ",int_balance)
                    continue
                    
                if add_balance == "no":
                    if int_balance == 0:
                           print("You don't have sufficient balance to continue.")
                           print("Game is over.")
                           break
                    continue
            elif game_2 == "no":
                print("Game is over.")
                break
        else:
            point_value = sums_dice
            print("*** Point:",point_value)
            break
            if subsequent_roll_result(sums_dice, point_value) == "point":
                print("You matched your Point.")
                print("You WIN")
                int_balance += count_wager
                print("Balance:",int_balance)
                
            elif subsequent_roll_result(sums_dice, point_value) == "loss":
                print("You lose.")
                int_balance += count_wager
                print("Balance:",int_balance)
        
            else:
                game_2 = input("Do you want to continue? ")
                if game_2 == "yes":
                    add_balance = input("Do you want to add to your balance? ")
                    if add_balance == "yes":
                        value_add_balance = input("Enter a wager (dollars): ")
                        value_add_balance = int(value_add_balance)
                        int_balance += value_add_balance
                        print("Balance: ",int_balance)
                        continue
                    
                    if add_balance == "no":
                        if int_balance == 0:
                            print("You don't have sufficient balance to continue.")
                            print("Game is over.")
                            break
                        continue
                elif game_2 == "no":
                    print("Game is over.")
                    break

if __name__ == "__main__":
    main()










    
    