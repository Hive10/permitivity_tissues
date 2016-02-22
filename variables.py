
"""
File            variables.py
Author          Rafael Silva Quiroz
email           sqrf@icloud.com

License	        educational use

Description     Creates the class Tejido, defining the number and kind of variables
"""


eps_0 = 8.8e-12

class Tejido:
    def __init__(self, name, e_inf, e_s, tau, alpha, sigma):
        self.name = name
        self.e_inf = e_inf
        self.e_s = e_s
        self.tau = tau
        self.alpha = alpha
        self.sigma = sigma

