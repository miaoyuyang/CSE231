 #!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Time( object ):
   
    def __init__( self, hour=0, minutes=0, secs=0 ):
       
        """ Construct a Clock using three integers. """
           
        self.__hour = hour
        self.__minutes   = minutes
        self.__secs = secs
        self.__valid = self.__validate()

    def __repr__( self ):

        """ Return a string as the formal representation a Clock. """

        out_str = "Class Time: {:02d}:{:02d}:{:02d}" \
            .format( self.__hour, self.__minutes, self.__secs )

        return out_str

    def __str__( self ):

        """ Return a string (hh/mm/ss) to represent a Date. """

        out_str = "{:02d}:{:02d}:{:02d}" \
            .format( self.__hour, self.__minutes, self.__secs )

        return out_str

    def __validate( self ):

        # Check the hour, minutes and secs for validity

        flag = False

        if (0 <= self.__hour <= 24) and \
           (0 <= self.__minutes <= 60) and \
           (0 <= self.__secs <=60):
           
               flag = True
           
        return flag

    def is_valid( self ):

        """ Return Boolean flag (valid date?) """

        return self.__valid

    def from_str( self, iso_str ):

        """ Convert a string into a Clock. """

        hour, minutes, secs = [ int( n ) for n in iso_str.split( ':' )]
           
        self.__hour = hour
        self.__minutes   = minutes
        self.__secs = secs
        self.__valid = self.__validate()

    def to_iso( self ):

        """ Return a string (hh-mm-ss) to represent a Date. """

        iso_str = "{:02d}:{:02d}:{:02d}" \
            .format( self.__hour, self.__minutes, self.__secs )

        return iso_str

    def to_mdy( self ):

        """ Return a string (hh mm, ) to represent a Date. """

        mdy_str = "{:s} {:d}, {:02d}" \
            .format( Time.__name[self.__hour], self.__miutes, self.__secs )

        return mdy_str
    
A = Time( 12, 25, 30 )

print( A )
print( repr( A ) )
print( str( A ) )
print()

B = Time( 2, 25, 3 )

print( B )
print( repr( B ) )
print( str( B ) )
print()

C = Time( 2, 25 )

print( C )
print( repr( C ) )
print( str( C ) )
print()

D = Time()

print( D )
print( repr( D ) )
print( str( D ) )
print()

D.from_str( "03:09:19" )

print( D )
print( repr( D ) )
print( str( D ) )


