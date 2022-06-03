from drinks import *

generic_drink = Drink()
coke = CocaCola()
milk = Milk( 2 )
choc_milk = ChocolateMilk()

print( "type( generic_drink ) == Drink:", end=" " )
print( type( generic_drink ) == Drink )     # Prints:__________________

print( "type( coke ) == Drink:", end=" " )
print( type( coke ) == Drink )              # Prints:__________________

print( "type( milk ) == Milk:", end=" " )
print( type( milk ) == Milk )               # Prints:__________________

print( "type( choc_milk ) == Milk:", end=" " )
print( type( choc_milk ) == Milk )          # Prints:__________________

print( "isinstance( generic_drink, Drink):", end=" " )
print( isinstance(generic_drink, Drink) )        # Prints:________

print( "isinstance( coke, Drink ):" , end=" ")
print( isinstance( coke, Drink ) )               # Prints:________

print( "isinstance( generic_drink, CocaCola ):", end=" " )
print( isinstance( generic_drink, CocaCola ) )   # Prints:________

print( "isinstance( choc_milk, Drink ):", end=" " )
print( isinstance( choc_milk, Milk ) )           # Prints:________

print( "isinstance( milk, ChocolateMilk ):", end=" " )
print( isinstance( milk, ChocolateMilk ) )       # Prints:________

print( "isinstance( choc_milk, CocaCola ):", end=" " )
print( isinstance( choc_milk, CocaCola ) )       # Prints:________

print( "isinstance( choc_milk, WhiteMilk ):", end=" " )
print( isinstance( choc_milk, WhiteMilk ) )      # Prints:________

print( "isinstance( choc_milk, object ):", end=" " )
print( isinstance( choc_milk, object ) )         # Prints:________

print( "isinstance( Milk, Drink ):", end=" " )
print( isinstance( Milk, Drink ) )               # Prints:________

print( "isinstance( Milk, type ):", end=" " )
print( isinstance( Milk, type ) )                # Prints:________








