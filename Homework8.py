import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from scipy.optimize import minimize



def Rankine_efficiency(p_high, p_low, t_high=None, p_mid=None, t_mid=None, turbine_efficiency=1.0, pump_efficiency=1.0):
    t_super, h_super, s_super, p_super = np.loadtxt('superheated_water_table.txt', skiprows=1, unpack=True)

    t_sat, p_sat, hf_sat, hg_sat, sf_sat, sg_sat, vf_sat, vg_sat = np.loadtxt('sat_water_table.txt', skiprows=1, unpack=True)
    if t_high == None:
        x = 1
    else:
        if t_mid == None:
            x1b = 1

    if p_mid == None:
        # no reheat process
        if t_high == None:
            # Saturated
            x1 = 1
            h1 = float(griddata(p_sat, hg_sat, p_high / 100))                   # Values at point 1
            s1 = float(griddata(p_sat, sg_sat, p_high / 100))
            t1 = float(griddata(p_sat, t_sat, p_high / 100))
        else:
            # Superheated
            h1 = float(griddata((t_super, p_super), h_super, (t_high, p_high)))
            s1 = float(griddata((t_super, p_super), s_super, (t_high, p_high)))


        sf2 = float(griddata(p_sat, sf_sat, p_low / 100))
        sg2 = float(griddata(p_sat, sg_sat, p_low / 100))

        x2s = (s1 - sf2) / (sg2 - sf2)                                      # Quality at 2S

        hf2 = float(griddata(p_sat, hf_sat, p_low / 100))
        hg2 = float(griddata(p_sat, hg_sat, p_low / 100))
        h2s = hf2 + x2s * (hg2 -hf2)

        h2 = h1 - (turbine_efficiency * (h1 - h2s))
        x2 = (h2 - hf2) / (hg2 - hf2)

        x3 = 0
        h3 = float(griddata(p_sat, hf_sat, p_low / 100))
        v3 = float(griddata(p_sat, vf_sat, p_low / 100))

        h4s = h3 + v3 * (p_high - p_low)
        h4 = h3 + (1/pump_efficiency)*(h4s - h3)

        Turbine_work = h1 - h2
        Pump_work = h4 - h3
        Heat_added = h1-h4

        efficiency = ((Turbine_work - Pump_work) / Heat_added) * 100

        return efficiency

    else:
        # With Reheat

        # no reheat process
        if t_high == None:
            # Saturated
            x1 = 1
            h1 = float(griddata(p_sat, hg_sat, p_high / 100))                   # Values at point 1
            s1 = float(griddata(p_sat, sg_sat, p_high / 100))
            t1 = float(griddata(p_sat, t_sat, p_high / 100))
        else:
            # Superheated
            h1 = float(griddata((t_super, p_super), h_super, (t_high, p_high)))
            s1 = float(griddata((t_super, p_super), s_super, (t_high, p_high)))


        sf2 = float(griddata(p_sat, sf_sat, p_mid / 100))
        sg2 = float(griddata(p_sat, sg_sat, p_mid / 100))

        x2s = (s1 - sf2) / (sg2 - sf2)                                      # Quality at 2S

        hf2 = float(griddata(p_sat, hf_sat, p_mid / 100))
        hg2 = float(griddata(p_sat, hg_sat, p_mid / 100))
        h2s = hf2 + x2s * (hg2 -hf2)

        h2 = h1 - (turbine_efficiency * (h1 - h2s))
        x2 = (h2 - hf2) / (hg2 - hf2)

        if t_mid == None:
            x1b = 1
            h1b = float(griddata(p_sat, hg_sat, p_mid / 100))
            s1b = float(griddata(p_sat, sg_sat, p_mid / 100))

        else:
            h1b = float(griddata((t_super, p_super), h_super, (t_mid, p_mid)))
            s1b = float(griddata((t_super, p_super), s_super, (t_mid, p_mid)))

        sf2b = float(griddata(p_sat, sf_sat, p_low / 100))
        sg2b = float(griddata(p_sat, sg_sat, p_low / 100))

        x2bs = (s1b - sf2b) / (sg2b - sf2b)                                      # Quality at 2S

        hf2b = float(griddata(p_sat, hf_sat, p_low / 100))
        hg2b = float(griddata(p_sat, hg_sat, p_low / 100))
        h2bs = hf2b + x2bs * (hg2b - hf2b)

        h2b = h1b - (turbine_efficiency * (h1b - h2bs))
        x2b = (h2b - hf2b) / (hg2b - hf2b)


        x3 = 0
        h3 = float(griddata(p_sat, hf_sat, p_low / 100))
        v3 = float(griddata(p_sat, vf_sat, p_low / 100))

        h4s = h3 + v3 * (p_high - p_low)
        h4 = h3 + (1/pump_efficiency)*(h4s - h3)

        Turbine_work = (h1 - h2) + (h1b - h2b)
        Pump_work = h4 - h3
        Heat_added = (h1 - h4) + (h1b - h2)

        efficiency = ((Turbine_work - Pump_work) / Heat_added) * 100

        return efficiency


def optimize_Rankine(p_high, p_low, t_high, t_mid_max, turbine_efficiency=0.90, pump_efficiency=0.85):

    def eff(vals):
        fx = 0
    vals = minimize(eff,(p_low*100,t_high),method='Nelder-Mead',options={'fatol':0.01,'xatol':1.0})
    p_mid=vals.x[0]
    t_mid=vals.x[1]
    eff=vals.fun
    count=vals.nfev

    return p_mid, t_mid, eff, count


def main():
    val = Rankine_efficiency(8000, 8, turbine_efficiency=0.85, pump_efficiency=0.9)
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