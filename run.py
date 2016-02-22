
"""
File            run.py
Author          Rafael Silva Quiroz
email           sqrf@icloud.com

License	        educational use

Description     Run the main script. The parameters to introduce are the kind of tissue, the maximum and minimum \\
frequencies and the temperature.
"""


from Epsilon import *
from tissues import *
from parameters import *

tissues = Tissue37()
#brain_grey/brain_white/bone/cornea/retina/water/tongue(just in 37 )

param = Parameters(tissues.bone, 1e7, 1e10)
epsilon = Epsilon(param)
epsilon.run()
