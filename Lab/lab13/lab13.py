#
# Demonstrate some of the operations of the Pet classes
#
class PetError( ValueError ):
    
    pass

class Pet( object ):
    
    def __init__( self, species=None, name="" ):
        valid_species = [ 'dog', 'cat', 'horse', 'gerbil', 'hamster', 'ferret']
        
        if species and species.lower() in valid_species:
            
            self.species_str = species.title()
            self.name_str = name.title()
            
        else:
            
            raise PetError()
            
    def __str__( self ):
        
        result_str = "Species of {:s}".format(self.species_str)
        
        if self.name_str:
            
            result_str += ", named {:s}".format(self.name_str)
                
        else:
            result_str += ", unnamed"
        
        return result_str
##
## Class Dog 
##
    
class Dog( Pet ):
    
    def __init__( self, name="", chases = "Cats"):
        
        Pet.__init__(self,"Dog",name)

        self.chases = chases
    
    def __str__(self):
        
        chases_str = Pet.__str__(self)
        
        chases_str += ", chases{:s}".format(self.chases)

        return chases_str
    
##
## Class Cat 
##

class Cat( Pet ):
    
    def __init__( self, name="", hates="Dogs" ):
        
        Pet.__init__(self,"Cat",name)
        
        self.hates = hates
        
    def __str__( self ):
#        
        hates_str = Pet.__str__(self)
  
        hates_str += ", hates {:s}".format(self.hates)
        
        return hates_str



import pets
def main():
    
    try:

        # Hamster
        A = pets.Pet( "Hamster" )
        print( A )       
        
        # Dog named Fido who chases Cats
        B = pets.Dog( "Fido" )
        print( B )

        # Cat named Fluffy who hates everything
        C = pets.Cat( "Fluffy", "everything" )
        print( C )

    except pets.PetError:
        
        print( "Got a pet error." )

main()

