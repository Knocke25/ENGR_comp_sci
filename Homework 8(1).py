#MAE 3403- Homework 8- Rankine_effiency and optimize_Rankine- Matthew Mansur- Due 7 Nov., 2017

import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt

def Rankine_efficiency(p_high, p_low, t_high=None, p_mid=None, t_mid=None, turbine_efficiency=1.0, pump_efficiency=1.0):

    nT=turbine_efficiency
    nP=pump_efficiency

    #we need the enthalpy at h4s which is after the isentropic
    sat = np.loadtxt('sat_water_table.txt', skiprows=1, unpack=True)                        # formats the saturated table data
    tcol = 0; pcol = 1; hfcol = 2; hgcol = 3; sfcol = 4; sgcol = 5; vfcol = 6; vgcol = 7

    s3=float(griddata(sat[pcol], sat[sfcol], p_low/100))
    T3=float(griddata(sat[pcol],sat[tcol],p_low/100))

    T4= T3*((p_high/p_low)**(.33/1.33))         #isentropic temperature relation to determine temperature after isentropic process at state 4s

    h4 = float(griddata(sat[tcol], sat[hfcol], T4))                                 # h4--> h4s is the only constant enthalpy throughout the whole process b/c subcooled

    # Quality at state 1=100%-- saturated table
    if t_high==None:
        sat = np.loadtxt('sat_water_table.txt', skiprows=1, unpack=True)  # formats the saturated table data
        tcol = 0; pcol = 1; hfcol = 2; hgcol = 3; sfcol = 4; sgcol = 5; vfcol = 6; vgcol = 7

        h1=float(griddata(sat[pcol], sat[hgcol], p_high/100))                               # h1 when state 1 if fully saturated vapor

        s1 = float(griddata(sat[pcol], sat[sgcol], p_high/100))

        state='Saturated'

    # If h1 is not fully saturated it is super heated
    else:
        tcols, hcols, scols, pcols = np.loadtxt('superheated_water_table.txt', skiprows=1, unpack=True)  # formats the superheated table data

        h1=float(griddata((tcols,pcols), hcols, (t_high,p_high)))                           # h1 when state 1 is super heated

        s1 = float(griddata((tcols, pcols), scols, (t_high, p_high)))

        state='Superheated'

    # NO REHEAT PROCESS
    if p_mid==None:

        sat = np.loadtxt('sat_water_table.txt', skiprows=1, unpack=True)  # formats the saturated table data
        tcol = 0; pcol = 1; hfcol = 2; hgcol = 3; sfcol = 4; sgcol = 5; vfcol = 6; vgcol = 7

        s2s=s1

        s2sg = float(griddata(sat[pcol], sat[sgcol], p_low/100))
        s2sf = float(griddata(sat[pcol], sat[sfcol], p_low/100))
        x= (s2s-s2sf)/(s2sg-s2sf)

        if x<=1.0:

            h2sg = float(griddata(sat[pcol], sat[hgcol], p_low/100))
            h2sf = float(griddata(sat[pcol], sat[hfcol], p_low/100))
            h2s=x*(h2sg-h2sf)+h2sf

        else:

            tcols, hcols, scols, pcols = np.loadtxt('superheated_water_table.txt', skiprows=1, unpack=True)
            h2s= float(griddata((scols, pcols), hcols, (s2s, p_low)))

        RankineEfficiency= (abs(h2s-h1)*nT)/(abs(h1-h4)*nP)

        #print ('Rankine Efficiency (Without Reheating)= ', RankineEfficiency)
        return RankineEfficiency
        #print ()

    # REHEAT PROCESS
    else:
        sat = np.loadtxt('sat_water_table.txt', skiprows=1, unpack=True)  # formats the saturated table data
        tcol = 0; pcol = 1; hfcol = 2; hgcol = 3; sfcol = 4; sgcol = 5; vfcol = 6; vgcol = 7

        s2s = s1                                                                # created isentropic condition from state 1 to state 2s

        s2sg = float(griddata(sat[pcol], sat[sgcol], p_mid / 100))
        s2sf = float(griddata(sat[pcol], sat[sfcol], p_mid / 100))
        x = (s2s - s2sf) / (s2sg - s2sf)                                        # checks quality to determine if state 2s is saturated or superheated

        if x <= 1.0:

            h2sg = float(griddata(sat[pcol], sat[hgcol], p_mid / 100))
            h2sf = float(griddata(sat[pcol], sat[hfcol], p_mid / 100))
            h2s = x * (h2sg - h2sf) + h2sf                                      # h2s when state 2 is saturated

        else:

            tcols, hcols, scols, pcols = np.loadtxt('superheated_water_table.txt', skiprows=1, unpack=True)
            h2s = float(griddata((scols, pcols), hcols, (s2s, p_mid)))          # h2s when state 2 is superheated

        # If t_mid== None-----> quality at reheated max state 1b is 100% (fully staturated)
        if t_mid== None:
            x1b=1.0

            h1b=float(griddata(sat[pcol], sat[hgcol], p_mid / 100))

            s1b=float(griddata(sat[pcol], sat[sgcol], p_mid/100))

        # If t_mid is given----> state 1b is super heated
        else:
            tcols, hcols, scols, pcols = np.loadtxt('superheated_water_table.txt', skiprows=1, unpack=True)
            h1b= float(griddata((tcols,pcols),hcols,(t_mid,p_mid)))

            s1b= float(griddata((tcols,pcols),scols,(t_mid,p_mid)))

        s2bs = s1b

        s2bsg = float(griddata(sat[pcol], sat[sgcol], p_low / 100))
        s2bsf = float(griddata(sat[pcol], sat[sfcol], p_low / 100))
        x2bs = (s2bs - s2bsf) / (s2bsg - s2bsf)

        h2bsg = float(griddata(sat[pcol], sat[hgcol], p_low / 100))
        h2bsf = float(griddata(sat[pcol], sat[hfcol], p_low / 100))
        h2bs = x2bs * (h2bsg - h2bsf) + h2bsf

        RankineEfficiency = ((abs((h2s - h1) + (h2bs - h1b))) * nT) / ((abs((h1 - h4) + (h1b - h2s))) * nP)

        # print ('Rankine Efficiency (With Reheating)', RankineEfficiency)
        # print ()
        return RankineEfficiency

def optimize_Rankine(p_high,p_low,t_high,t_mid_max,turbine_efficiency=0.90,pump_efficiency=0.85):

    def eff(vals):...
    vals=minimize(eff,(p_low*100,t_high),method='Nelder-Mead',options={'fatol':0.01,'xatol':1.0})
    p_mid=vals.x[0]
    t_mid=vals.x[1]
    eff=vals.fun
    count=vals.nfev

    return p_mid, t_mid, eff, count


def main():
    val=Rankine_efficiency(8000, 8, turbine_efficiency=0.85, pump_efficiency=0.9)
    print(val)
    print()

    val=Rankine_efficiency(8000, 8, t_high=480,turbine_efficiency=0.85, pump_efficiency=0.9)
    print(val)
    print()

    val=Rankine_efficiency(8000, 8, t_high=480, p_mid=700, turbine_efficiency=0.85, pump_efficiency=0.9)
    print(val)
    print()

    val=Rankine_efficiency(8000, 8, t_high=480, p_mid=700, t_mid=440, turbine_efficiency=0.85, pump_efficiency=0.9)
    print(val)
    print()

    p=np.linspace(800,5000,80)
    eff=np.zeros_like(p)
    for i in range(80):
        eff[i]=Rankine_efficiency(12000,8,t_high=520,p_mid=p[i],t_mid=500,turbine_efficiency=0.85,pump_efficiency=0.9)
    plt.plot(p,eff)
    plt.show()

    pmid,tmid,e,niter=optimize_Rankine(12000,8,520,500,turbine_efficiency=0.85,pump_efficiency=0.9)
    print(pmid,tmid,e,niter)

    pmid, tmid, e, niter = optimize_Rankine(8000, 8, 480, 440, turbine_efficiency=0.90, pump_efficiency=0.95)
    print(pmid, tmid, e, niter)

main()