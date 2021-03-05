#=========================================================================
# RegIncr
#=========================================================================
# This is a simple model for a registered incrementer. An eight-bit value
# is read from the input port, registered, incremented by one, and
# finally written to the output port.

from pymtl3 import *

class RegIncr( Component ):

  # Constructor

  def construct( s ):

    # Port-based interface

    s.in_ = InPort ( Bits8 )
    s.out = OutPort( Bits8 )

    # Sequential logic

    s.reg_out = Wire( 8 ) #

    @update_ff
    def block1():
      if s.reset:
        s.reg_out <<= 0
      else:
        s.reg_out <<= s.in_

    # ''' TUTORIAL TASK ''''''''''''''''''''''''''''''''''''''''''''''''''
    # This model is incomplete. As part of the tutorial you will insert a
    # combinational concurrent block here to model the incrementer logic,
    # and later you will insert a line tracing function to compactly
    # output the input, register, and output values.
    # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

