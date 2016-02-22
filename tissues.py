
"""
File            tissues.py
Author          Rafael Silva Quiroz
email           sqrf@icloud.com

License	        educational use

Description     Creates the classes Tissue20 and Tissue37. They store the numeric values of the variables.
"""
from variables import *
#def __init__(self, name, e_inf, e_s, tau, alpha, sigma):


class Tissue20:
    def __init__(self):
        self.bone = Tejido('Bone', 2.5, 15.3, 12.7e-9, 0.31, 0.093)
        self.brain_grey = Tejido('Brain (grey)', 3.5, 58.3, 9.73e-9, 0.18, 1.13)
        self.brain_white = Tejido('Brain (white)', 3.5, 45.13, 9.49e-9, 0.22, 0.78)
        self.cornea = Tejido('cornea', 3.5, 62.6, 10.8e-9, 0.09, 1.00)
        self.retina = Tejido('retina', 3.5, 67.6, 8.74, 0.09, 1.33)
        self.water = Tejido('water', 3.5, 80.1, 9.2e-9, 0.00, 0.0001)

class Tissue37:
    def __init__(self):
        self.bone = Tejido('Bone', 2.5, 14.9, 13.8e-9, 0.26, 0.092)
        self.brain_grey = Tejido('Brain (grey)', 3.5, 55.5, 7.76e-9, 0.12, 1.03)
        self.brain_white = Tejido('Brain (white)', 3.5, 37.0, 8.04e-9, 0.24, 0.47)
        self.cornea = Tejido('cornea', 3.5, 53.0, 8.72e-9, 0.13, 1.05)
        self.retina = Tejido('retina', 3.5, 67.3, 7.25, 0.05, 1.42)
        self.water = Tejido('water', 3.5, 74.1, 6.2e-9, 0.00, 0.0001)
        self.tongue = Tejido('tongue', 3.5, 57.7, 9.12e-9, 0.08, 0.63)