import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import fsolve
from copy import deepcopy


def sng(x,a,power):
    v = 0

def IntegrateSngEqn(snglist):
    v =0
def SngEqnVal(snglist,x,c1=0,c2=0):
     v= 0
def SngEqnVals(snglist,x,c1=0,c2=0):
    v = 0


def BeamSolver(Loads,L,plotit=True):
    v = 0
    
def HandyDandyBeamPlotter(Vs,Ms,Slopes,Deltas,L,C1,C2,
                          npoints=1000,show=True, save=False,
                          title="Beam1 Characteristics",
                          vtitle="Shear",mtitle="Moment",
                          slopetitle="EISlope", deltatitle="EIDelta"):

    X = np.linspace(L / 100000.0, L, 3000)

        # Four subplots, the axes array is 1-d
    plt.rcParams["figure.figsize"] = [16,16]
    plt.rcParams.update({'font.size': 18})
    fig, axarr = plt.subplots(4, sharex=True)
    plt.suptitle(title,fontsize=36)
    fig.patch.set_facecolor('WhiteSmoke')


    axarr[0].plot(X,Vs,linewidth=3)
    axarr[0].set_title(vtitle)
    axarr[0].locator_params(axis='y',nbins=2)


    axarr[1].plot(X,Ms,linewidth=3)
    axarr[1].set_title(mtitle)
    axarr[1].locator_params(axis='y',nbins=2)


    axarr[2].plot(X,Slopes,linewidth=3)
    axarr[2].set_title(slopetitle)
    axarr[2].locator_params(axis='y',nbins=2)


    axarr[3].plot(X,Deltas,linewidth=3)
    axarr[3].set_title(deltatitle)
    axarr[3].locator_params(axis='y',nbins=2)

    if show == True:
        plt.show()
    if save:
        fig.savefig(title+".pdf")

    return fig,plt





def Beam1():    # a simply supported beam with a distributed load
                # and a point load (Example 4-2 from the notes)
# https://www.dropbox.com/s/une3axzzrvaz4ei/Figure%204-3%20fo%20Singularity.pdf?dl=0
    w=2; F=2500; a=1000;  L =3000.0 # known load and geometry values
    R1=0; R2=0   # initially unknown static reaction values 
                 # due to the supports
    Loads=[[R1,0,-1],[-w,0,0],[-F,a,-1],[w,L,0],[R2,L,-1]]

    BeamSolver(Loads,L,plotit=True)


def Beam2():    # a simply supported beam with a distributed load
                # and a point load
#https://www.dropbox.com/s/p89ek7o5qudtl0t/Figure%204-4%20for%20Singularity.pdf?dl=0

    F=1800; w=300; L=40 ; a=15  # known load and geometry values
    R1=0; R2=0   # initially unknown static reaction values 
                 # due to the supports
    Loads=[[-F,0,-1],[R1,a,-1],[-w,a,0],[R2,L,-1],[w,L,0]]

    BeamSolver(Loads,L,plotit=True)
    

def Beam3():    # a cantilevered beam with a distributed load
                # and a point load
#https://www.dropbox.com/s/p89ek7o5qudtl0t/Figure%204-4%20for%20Singularity.pdf?dl=0

    F=18000; w=300; L=40 ; a=15  # known load and geometry values
    R1=0; M1=0   # initially unknown static reaction values 
                 # due to the supports
    Loads=[[R1,0,-1],[M1,0,-2],[-w,0,0],[-F,a,-1],[w,L,0]]

    Loads, Vs, Ms, EISlopes, EIDeltas, C1, C2 = BeamSolver(Loads,L,plotit=True)
    print(SngEqnVal(Vs,0.0000001))
    print(SngEqnVal(Ms,0.0000001))
    X=np.linspace(0,L,11)
    Y=SngEqnVals(Vs,X)
    print(Y)
    


