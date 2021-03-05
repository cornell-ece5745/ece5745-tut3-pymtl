#=========================================================================
# RegIncrNstage
#=========================================================================
# Registered incrementer that is parameterized by the number of stages.

from pymtl3   import *
from .RegIncr import RegIncr

class RegIncrNstage( Component ):

  # Constructor

  def construct( s, nstages=2 ):

    # Port-based interface

    s.in_ = InPort (8)
    s.out = OutPort(8)

    # Instantiate the registered incrementers

    s.reg_incrs = [ RegIncr() for _ in range(nstages) ]

    # Connect input port to first reg_incr in chain

    s.in_ //= s.reg_incrs[0].in_

    # ''' TUTORIAL TASK ''''''''''''''''''''''''''''''''''''''''''''''''''
    # This model is incomplete. As part of the tutorial you will insert
    # code here to connect the stages together.
    # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    # Connect last reg_incr in chain to output port

    s.out //= s.reg_incrs[-1].out

  # Line tracing

  def line_trace( s ):
    return f"{s.in_} " \
           f"({'|'.join([ str(x.out) for x in s.reg_incrs ])}) " \
           f"{s.out}"
