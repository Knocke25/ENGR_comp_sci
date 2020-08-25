#Alyssa Crain
#MAE 3403 Homework 8
#7 Nov 2017

import numpy as np
from scipy.interpolate import griddata
from scipy.optimize import minimize
import matplotlib.pyplot as plt

def Rankine_efficiency(p_high, p_low, t_high=None, p_mid = None, t_mid = None, turbine_efficiency = 1.0, pump_efficiency = 1.0):

    n_T = turbine_efficiency                                                                        #Efficiency of Turbine
    n_P = pump_efficiency                                                                           #Efficiency of Turbine

    sat = np.loadtxt('sat_water_table.txt', skiprows=1, unpack=True)                                #load and format saturated table, skip first row
    tcol = 0; pcol = 1; h_fcol = 2; h_gcol = 3; s_fcol = 4; s_gcol = 5; v_fcol = 6; v_gcol = 7      #specifies what is in each column

    v3 = float(griddata(sat[pcol], sat[v_fcol], p_low/100))                                         #interpolate between grid values in saturated table
    h3 = float(griddata(sat[pcol], sat[h_fcol], p_low/100))

    h4s = h3 + v3 * (p_high - p_low)                                                                #h4 constant because it is subcooled

    W_P = abs((h4s - h3) * n_P)                                                                     #pump work from h3 to h4

    h4 = h3 + (1 / n_P) * (h4s - h3)                                                                #finding enthalpy at 4 with quality (1 / efficiency of pump)

    if t_high == None:                                                                              #fully saturated vapor, quality is 100%
        h1 = float(griddata(sat[pcol], sat[h_gcol], p_high / 100))                                  #interpolate between grid values in saturated table
        s1 = float(griddata(sat[pcol], sat[s_gcol], p_high / 100))

    else:                                                                                                   #not fully saturated, superheated
        tcols, hcols, scols, pcols = np.loadtxt('superheated_water_table.txt', skiprows=1, unpack=True)     #load and format saturated table, skip first row, specifies what is in each row

        h1 = float(griddata((tcols, pcols), hcols, (t_high, p_high)))                                       #interpolate between grid values in superheated table
        s1 = float(griddata((tcols, pcols), scols, (t_high, p_high)))

    if p_mid == None:                                                       #no reheat
        s2s = s1

        s2s_g = float(griddata(sat[pcol], sat[s_gcol], p_low / 100))        #interpolate between grid values in saturated table
        s2s_f = float(griddata(sat[pcol], sat[s_fcol], p_low / 100))
        x = (s2s - s2s_f)/(s2s_g - s2s_f)                                   #find quality using entropy

        if x <= 1.0:                                                        #quality less than 1

            h2s_g = float(griddata(sat[pcol], sat[h_gcol], p_low / 100))    #interpolate between grid values in saturated table
            h2s_f = float(griddata(sat[pcol], sat[h_fcol], p_low / 100))
            h2s = x * (h2s_g - h2s_f) + h2s_f

        else:

            tcols, hcols, scols, pcols = np.loadtxt('superheated_water_table.txt', skiprows=1, unpack=True)     #load and format saturated table, skip first row, specifies what is in each row
            h2s = float(griddata((scols, pcols), hcols, (s2s, p_low)))                                          #interpolate between grid values in superheated table

        RankineEfficiency = (((abs(h2s - h1) * n_T) - W_P) / (abs(h1 - h4))) * 100                              #solving Rankine Efficiency

        return RankineEfficiency

    else:                                                                       #with reheat
        s2s = s1                                                                #isentropic condition from state 1 to state 2s

        s2s_g = float(griddata(sat[pcol], sat[s_gcol], p_mid / 100))            #interpolate between grid values in saturated table
        s2s_f = float(griddata(sat[pcol], sat[s_fcol], p_mid / 100))
        x = (s2s - s2s_f) / (s2s_g - s2s_f)                                     #finding quality using entroypy

        if x <= 1.0:                                                            #quality less than 1

            h2s_g = float(griddata(sat[pcol], sat[h_gcol], p_mid / 100))        #interpolate between grid values in saturated table
            h2s_f = float(griddata(sat[pcol], sat[h_fcol], p_mid / 100))
            h2s = x * (h2s_g - h2s_f) + h2s_f                                   #finding h2 when saturated

            h2 = h1 - n_T * (h1 - h2s)                                          #isentropic h2

        else:

            tcols, hcols, scols, pcols = np.loadtxt('superheated_water_table.txt', skiprows=1, unpack=True)                     #load and format saturated table, skip first row, specifies what is in each row
            h2s = float(griddata((scols, pcols), hcols, (s2s, p_mid)))                                                          #interpolate between grid values in superheated table

            h2 = h1 - n_T * (h1 - h2s)                                                                                          #non-isentropic h2

        if t_mid == None:                                                                                                       #fully saturated vapor , quality is 100%
            h1b = float(griddata(sat[pcol], sat[h_gcol], p_mid / 100))                                                          #interpolate between grid values in superheated table
            s1b = float(griddata(sat[pcol], sat[s_gcol], p_mid / 100))

        else:
            tcols, hcols, scols, pcols = np.loadtxt('superheated_water_table.txt', skiprows=1, unpack=True)                     #load and format saturated table, skip first row, specifies what is in each row
            h1b = float(griddata((tcols, pcols), hcols, (t_mid, p_mid)))                                                        #interpolate between grid values in superheated table
            s1b = float(griddata((tcols, pcols), scols, (t_mid, p_mid)))

        s2bs = s1b

        s2bs_g = float(griddata(sat[pcol], sat[s_gcol], p_low / 100))                                                           #interpolate between grid values in superheated table
        s2bs_f = float(griddata(sat[pcol], sat[s_fcol], p_low / 100))
        x2bs = (s2bs - s2bs_f) / (s2bs_g - s2bs_f)                                                                              #finding quality using entropy

        h2bs_g = float(griddata(sat[pcol], sat[h_gcol], p_low / 100))                                                           #interpolate between grid values in superheated table
        h2bs_f = float(griddata(sat[pcol], sat[h_fcol], p_low / 100))
        h2bs = x2bs * (h2bs_g - h2bs_f) + h2bs_f                                                                                #finding enthalpy using quality

        RankineEfficiency = 100 * ((abs((((h1 - h2s) * n_T + (h1b - h2bs) * n_T))) - W_P) / (abs((h1 - h4) + (h1b - h2))))      #solving Rankine Efficiency

        return RankineEfficiency

def optimize_Rankine(p_high, p_low, t_high, t_mid_max, turbine_efficiency=0.90, pump_efficiency=0.85):

    def eff(vals):
        p_mid, t_mid = vals                                                                                             #setting mid p and t in a vals array
        if p_mid < p_high:                                                                                              #mid p less than high p
            bound = Rankine_efficiency(p_high, p_low, t_high=t_high, p_mid=p_mid, t_mid=t_mid,
                                            turbine_efficiency=turbine_efficiency, pump_efficiency=pump_efficiency)     #solve using Rankine Efficiency function with inputs
        else:
            bound = Rankine_efficiency(p_high, p_low, t_high=t_high, p_mid=p_high, t_mid=t_mid,
                                            turbine_efficiency=turbine_efficiency, pump_efficiency=pump_efficiency)     #solve using Rankine Efficiency function with inputs
        penalty = 0                                                                                                     #start from zero
        if t_mid > t_mid_max:                                                                                           #orig t greater than max
            penalty += (t_mid - t_mid_max) * 10 ** 6
        if p_mid < p_low:                                                                                               #orig p less than low
            penalty += (p_low - p_mid) * 10 ** 6
        if p_mid > p_high:                                                                                              #orig p greater than high
            penalty += (p_mid - p_high) * 10 ** 6

        return -bound + penalty                                                                                         #add together and return

    vals = minimize(eff, (p_low * 100, t_high), method='Nelder-Mead', options={'fatol':0.01, 'xatol':1.0})
    p_mid = vals.x[0]
    t_mid = vals.x[1]
    eff = vals.fun
    count = vals.nfev

    return p_mid, t_mid, eff, count

def main():
    val = Rankine_efficiency(8000, 8, turbine_efficiency=0.85, pump_efficiency=0.9)
    print(val)
    print()

    val = Rankine_efficiency(8000, 8, t_high=480, turbine_efficiency=0.85, pump_efficiency=0.9)
    print(val)
    print()

    val = Rankine_efficiency(8000, 8, t_high=480, p_mid=700, turbine_efficiency=0.85, pump_efficiency=0.9)
    print(val)
    print()

    val = Rankine_efficiency(8000, 8, t_high=480, p_mid=700, t_mid=440, turbine_efficiency=0.85, pump_efficiency=0.9)
    print(val)
    print()

    p = np.linspace(800, 5000, 80)
    eff = np.zeros_like(p)
    for i in range(80):
        eff[i] = Rankine_efficiency(12000, 8, t_high=520, p_mid=p[i], t_mid=500, turbine_efficiency=0.85, pump_efficiency=0.9)
    plt.plot(p, eff)
    plt.show()

    pmid, tmid, e, niter=optimize_Rankine(12000, 8, 520, 500, turbine_efficiency=0.85, pump_efficiency=0.9)
    print(pmid, tmid, e, niter)

    pmid, tmid, e, niter = optimize_Rankine(8000, 8, 480, 440, turbine_efficiency=0.90, pump_efficiency=0.95)
    print(pmid, tmid, e, niter)

main()