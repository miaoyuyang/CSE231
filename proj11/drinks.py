class Drink (object):
 
    def __init__( self, price=0 ):    
        self.price = price          #1        
        self.kind = "Drink"         #2

    def __str__( self ):
        return "{} @ $ {:0.2f}".\
               format( self.kind,
                       self.price ) #3

    def __repr__( self ):
        return str( self )          #4

    def get_price( self ):      
        return self.price           #5

    def get_kind( self ):             
        return self.kind            #6

    def print_price_sticker( self ): 
        print( self.get_kind() )    #7
        print( "Price: {:0.2f}".format( 
            self.get_price() ) )    #8


class CocaCola (Drink):

    def __init__(self):            
        Drink.__init__(self,1.25)   #9
        self.kind = "Coca-Cola Classic"  #10


class Milk ( Drink ):

    def __init__( self, percent_fat=0 ): 
        Drink.__init__(self, 0.75)       #11
        self.kind = "Milk"               #12
        self.percent_fat = percent_fat   #13

    def __str__( self ):
        milk_str = Drink.__str__( self ) #14
        fat_str = " ({} % fat)".format(
            self.get_fat() )             #15
        return milk_str + fat_str        #16

    def get_fat(self): 
        return self.percent_fat          #17

    def print_price_sticker( self ):    
        print( "{} {}%".format(          #18
            self.get_kind(),
            self.get_fat() ) )
        print( "Price: {:0.2f}".format(
            self.get_price() ) )         #19

class ChocolateMilk( Milk ):

    def __init__( self, percent_fat=0 ):
        Milk.__init__( self, percent_fat) #20
        self.kind = "Chocolate Milk"      #21

class WhiteMilk( Milk ):

    def __init__( self, percent_fat=0 ):
        Milk.__init__( self, percent_fat) #22
        self.kind = "White Milk"          #23


        
        

        
            
    
