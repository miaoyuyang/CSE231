
import cards

# Create the deck of cards

the_deck = cards.Deck()
the_deck.shuffle()
#
#"Keep Going: (Nn) to stop:").lower() == 'n'
#"hand1:"
#"hand2:"
#"Player 1 wins!!!"
#"Player 2 wins!!!"
#"Battle was 1: {}, 2: {}. Player 1 wins battle."
#"Battle was 1: {}, 2: {}. Player 2 wins battle."
#"Battle was 1: {}, 2: {}. Battle was a draw."

print("Starting Hands")
player1_list=[]
player2_list=[]
for i in range( 5 ):
    player1_list.append( the_deck.deal() )
    player2_list.append( the_deck.deal() )
    
while len(player1_list) >0 and len(player2_list) >0:
    print( "hand1:",player1_list )
    print( "hand2:",player2_list )
    print()
    
    player1_card = player1_list.pop( 0 )
    player2_card = player2_list.pop( 0 )
    
    if player1_card.rank() == player2_card.rank():
        player1_list.append( player1_card )
        player2_list.append( player2_card )
        print( "Battle was 1:", player1_card, ", 2:", player2_card,"Battle was a draw." )
    elif player1_card.rank() > player2_card.rank():
        player1_list.append( player1_card )
        
        print( "Battle was 1:", player1_card, ", 2:", player2_card,"Player 1 wins battle." )
    else:
        player2_list.append( player2_card )
        print( "Battle was 1:", player2_card, " 2:", player1_card,"Player 2 wins battle." )
        
    if len(player1_list) >0 and len(player2_list) >0:
        game_continue = input("Keep Going: (Nn) to stop: ")   
        if game_continue.lower()=='n':
            break
        else:
            continue
    elif player1_list:
        print( "hand1:",player1_list)
        print("hand2: []")
        print("Player 1 wins!!!")
        break
    else:
        print( "hand1: []")
        print("hand2:",player2_list)
        print("Player 2 wins!!!")
        break

    
    