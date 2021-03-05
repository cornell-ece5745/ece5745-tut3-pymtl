#=========================================================================
# RegIncr2stage
#=========================================================================
# Two-stage registered incrementer that uses structural composition to
# instantitate and connect two instances of the single-stage registered
# incrementer.

from pymtl3  import *
from .RegIncr import RegIncr

class RegIncr2stage( Component ):

  # Constructor

  def construct( s ):

    # Port-based interface

    s.in_ = InPort (8)
    s.out = OutPort(8)

    # First stage

    s.reg_incr_0 = RegIncr()

    connect( s.in_, s.reg_incr_0.in_ )

    # ''' TUTORIAL TASK ''''''''''''''''''''''''''''''''''''''''''''''''''
    # This model is incomplete. As part of the tutorial you will insert
    # code here to instantiate and then connect the second stage of this
    # two-stage registered incrementer.
    # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

  # Line tracing

  def line_trace( s ):
    return "{} ({}|{}) {}".format(
      s.in_,
      s.reg_incr_0.line_trace(),
      s.reg_incr_1.line_trace(),
      s.out
    )
