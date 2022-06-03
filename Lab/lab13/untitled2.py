#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 16:52:38 2018

@author: yangmiao
"""

##
## Class PetError -- complete
##

class PetError( ValueError ):
  
   pass

##
## Class Pet -- not complete
##

class Pet( object ):
   """
       Pet class
   """
   def __init__( self, species=None, name="" ):
       """
           Constructor
       """
       # Checking for species to be any of the following in the list
       if species.lower() in ['dog', 'cat', 'horse', 'gerbil', 'hamster', 'ferret']:
           # Assigning values
           self.species_str = species.title()
           self.name_str = name.title()
          
       else:
           # Raises pet erro
           raise PetError()
          
   def __str__( self ):
       """
           Method that returns the string format
       """
       # If named
       if len(self.name_str) != 0:
           # Forming result string
           result_str = "Species of: " + self.species_str.title() + ", named " + self.name_str.title();
          
       else:
           # Forming result string
           result_str = "Species of: " + self.species_str.title() + ", unnamed ";
          
       # Return resultant string
       return result_str

##
## Class Dog -- not complete
##

class Dog( Pet ):
   """
       Dog class inherited from Pet class
   """
   def __init__( self, name="", chases="Cats" ):
       """
           Constructor
       """
       # Calling Pet class constructor
       Pet.__init__(self, "Dog", name);
      
       # Storing chases as data attribute
       self.chases = chases;
          
   def __str__( self ):
       """
           Method that returns the string format
       """
          
       # Calling base class __str__ and concatenating with remaining string  
       result_str = Pet.__str__(self)   + ", chases " + self.chases;
          
       # Return resultant string
       return result_str
  
##
## Class Cat -- not complete
##

class Cat( Pet ):
   """
       Cat class inherited from Pet class
   """
   def __init__( self, name="", hates="Dogs" ):
       """
           Constructor
       """
       # Calling Pet class constructor
       Pet.__init__(self, "Cat", name);
      
       # Storing hates as data attribute
       self.hates = hates;
          
   def __str__( self ):
       """
           Method that returns the string format
       """
      
       # Calling base class __str__ and concatenating with remaining string  
       result_str = Pet.__str__(self)   + ", hates " + self.hates;
          
       # Return resultant string
       return result_str
  

#File: lab13.py

##
## Demonstrate some of the operations of the Pet classes
##

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
      
       # For testing pet error, passing string "DEF" as species
       # ABC
       D = pets.Pet( "ABC", "DEF" )
       print( D )     

   except pets.PetError:
      
       print( "Got a pet error." )

