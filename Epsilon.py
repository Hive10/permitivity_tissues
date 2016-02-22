
"""
File            Epsilon.py
Author          Rafael Silva Quiroz
email           sqrf@icloud.com

License	        educational use

Description     Compute the frequency dependent dielectric function of selected body tissue
"""


from tissues import*
from os.path import join as pjoin
from pylab import*


class Epsilon:
    def __init__(self, parameters):
        self.param = parameters
        self.tejido = self.param.tejido
        self.w_min = self.param.w_min
        self.w_max = self.param.w_max

    def run(self):

        epsilonlist = []
        delta_w = self.w_max - self.w_min
        n = 1000
        resolution = float(delta_w) / n

        freqlist = arange(self.w_min, self.w_max, resolution)
        for i in xrange(len(freqlist)):
            fd = self.tejido.e_inf + (self.tejido.e_s-self.tejido.e_inf) / (1 + freqlist[i] * self.tejido.tau * 1j) ** (1 - self.tejido.alpha) + self.tejido.sigma / (eps_0 * freqlist[i] * 1j)
            eps_real = fd.real
            epsilonlist.append(eps_real)
        eps = epsilonlist

        filename = 'w(Hz)'
        path_to_file = pjoin("./output/", filename)
        filetarget = open(path_to_file, "w")
        filetarget.write("\n".join(map(lambda x: str(x), freqlist)))
        filetarget.close()

        filename = 'E(w)'
        path_to_file = pjoin("./output/", filename)
        filetarget = open(path_to_file, "w")
        filetarget.write("\n".join(map(lambda x: str(x), eps)))
        filetarget.close()

        #print Eps
        print len(freqlist), len(eps), 'it is done!'
        plt.semilogx(freqlist, eps)
        title(' Time domain permitivity of ' + self.param.tejido.name)
        xlabel('$\omega$ (Hz)')
        ylabel('$\epsilon(\omega) $')
        #ylim(3, 7)
        grid()
        show()