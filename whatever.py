# Brayden Knocke, Gharabet Torossian, Taylor Vazquez


from scipy.optimize import fsolve

from copy import deepcopy

import numpy as np

from BeamPlotter import HandyDandyBeamPlotter


class Beam:
    # initialize variables
    def __init__(self, ):
        self.title = None
        self.dist_unit = None
        self.force_unit = None
        self.Sut = None
        self.Sy = None
        self.E = None
        self.fatigue_factor = None
        self.static_factor = None
        self.shaft_length = None
        self.moment_of_inertia = None

        self.point_load = []
        self.moment_load = []
        self.support = []

        self.loads = None
        self.shear = None
        self.moments = None
        self.slope = None
        self.deflection = None
        self.R1 = None
        self.R2 = None
        self.C1 = None
        self.C2 = None
        self.maxV = None
        self.maxMoment = None
        self.maxSlope = None
        self.maxV_location = None
        self.maxM_location = None
        self.maxSlope_location = None
        self.maxDeflection = None
        self.maxDeflection_location = None

        self.shear_list = None
        self.moment_list = None
        self.slope_list = None
        self.deflection_list = None


    def processBeamData(self, data): # needs to have (self, data)
        # from the array of strings, fill the wing dictionary

            for line in data:  # loop over all the lines
                cells = line.strip().split('')
                keyword = cells[0].lower()

                if keyword == 'title': self.title = cells[1].strip().replace("'", "")
                if keyword == 'distance_unit': self.dist_unit = cells[1].strip().replace("'", "")
                if keyword == 'force_unit': self.force_unit = cells[1].strip().replace("'", "")
                if keyword == 'fatigue_factor': self.fatigue_factor = float(cells[1])
                if keyword == 'static_factor': self.static_factor = float(cells[1])
                if keyword == 'shaft_length': self.shaft_length = float(cells[1])
                if keyword == 'moment_of_inertia': self.moment_of_inertia = float(cells[1])

                if keyword == 'material':
                    self.Sut = float(cells[1])
                    self.Sy = float(cells[2])
                    self.E = float(cells[3])

                if keyword == 'point_load':
                    if cells[1].strip().lower() == 'end':
                        location = -999
                        magnitude = float(cells[2])
                    else:
                        magnitude = float(cells[2])
                        location = float(cells[1])
                    this_load = [magnitude, location, -1]
                    self.point_load.append(this_load)

                if keyword == 'point_moment':
                    if cells[1].strip().lower() == 'end':
                        location = -999
                        magnitude = float(cells[2])
                    else:
                        location = float(cells[1])
                        magnitude = float(cells[2])
                    this_load = [magnitude, location, -2]
                    self.moment_load.append(this_load)

                if keyword == 'support':
                    if cells[1].strip().lower() == 'end': cells[1] = -999
                    self.support.append(float(cells[1]))

            # for the case that shaft lenth is at the bottom of file
            if self.support[0] == -999:
                self.support[0] = self.shaft_length
            if self.support[1] == -999:
                self.support[1] = self.shaft_length
            for load in self.point_load:
                if load[1] == -999:
                    load[1] = self.shaft_length

            for load in self.moment_load:
                if load[1] == -999:
                    load[1] = self.shaft_length


    def print(self):
        print("Title: {}".format(self.title))
        print("Distance Units: {}".format(self.dist_unit))
        print("Force Units: {}".format(self.force_unit))
        print("Sut: {} (ksi)".format(self.Sut))
        print("Sy: {} (ksi)".format(self.Sy))
        print("E: {} (Mpsi)".format(self.E))
        print("Fatigue Factor: {}".format(self.fatigue_factor))
        print("Static Factor: {}".format(self.static_factor))
        print("Shaft Length: {}".format(self.shaft_length))
        print("The shaft length is: {:.2f} {}".format(self.shaft_length, self.dist_unit))
        print("Moment of Inertia: {}".format(self.moment_of_inertia))

    def solve(self):
        q = self.moment_load + self.point_load                          # singularity equation (without R1 and R2)

        def integrate(eqn):                                             # Integration function for singularity fucntions
            for n in range(0, len(eqn)):
                eqn[n][2] = eqn[n][2] + 1
                if eqn[n][2] > 1:
                    eqn[n][0] = eqn[n][0] / (eqn[n][2])
            return eqn

        def find_max_V(eqn):                                            # finds the max shear magnitude and location
            max = eqn[0][0]
            place = eqn[0][1]
            for n in range(0, len(eqn)):
                if abs(eqn[n][0]) > max:
                    max = abs(eqn[n][0])
                    place = eqn[n][1]
            ans = max, place
            return ans

        def find_max_Moment(eqn):                                       # finds max moment magnitude and location
            max = abs(eqn[0][0])
            place = eqn[0][1]
            for n in range(0, len(eqn)):
                if abs(eqn[n][0]) > max:
                    max = abs(eqn[n][0])
                    place = eqn[n][1]
            ans = max, place
            return ans

        def find_max_Slope(eqn):                                        # finds max slope magnitude and location
            max = abs(eqn[0][0])
            place = eqn[0][1]
            for n in range(0, len(eqn)):
                if abs(eqn[n][0]) > max:
                    max = abs(eqn[n][0])
                    place = eqn[n][1]
            ans = max, place
            return ans

        def find_max_Deflection(eqn):                                   # finds max deflection magnitude and location
            max = abs(eqn[0][0])
            place = eqn[0][1]
            for n in range(0, len(eqn)):
                if abs(eqn[n][0]) > max:
                    max = abs(eqn[n][0])
                    place = eqn[n][1]
            ans = max, place
            return ans

        def shear_eqn(eqn):                                             # shear equation for sum of forces in y-dir
            ans = 0
            for n in range(0, len(eqn)):
                if eqn[n][2] == -1:
                    ans = ans + eqn[n][0]
            return ans

        def moment_eqn(eqn):                                            # moment equation for sum of moments and point 0
            ans = 0

            for n in range(0, len(eqn)):
                if eqn[n][2] == -2:
                    ans = ans + eqn[n][0]
                elif eqn[n][2] == -1:
                    ans = ans + (-eqn[n][0] * eqn[n][1])
            return ans

        def equations(p):                                               # equation to then solve for reactions
            R1, R2 = p
            shear = shear_eqn(q)
            moment = moment_eqn(q)
            return (shear + R1 + R2, moment - R1*self.support[0] - R2*self.support[1])


        # Solve for the reaction forces in y-dir for the supports
        self.R1, self.R2 = fsolve(equations, (250, 56))
        r1 = [[self.R1, self.support[0], -1]]
        r2 = [[self.R2, self.support[1], -1]]
        # new singularity function with supports
        q = q + r1 + r2

        def SngEqnVals_shear(snglist, x, c1=0, c2=0):                   # shear values at each time slot
            # x is a list of values and snglist is list of singularity functions
            # get a x long list of values for each time slot
            ans = np.zeros(shape=(len(x), 2))
            i = 0
            for n in x:
                for m in range(0, len(snglist)):
                    if n >= snglist[m][1]:
                        if snglist[m][2] == 0:
                            ans[i][0] = ans[i][0] + snglist[m][0]

                ans[i][1] = n
                i += 1

            return ans

        def SngEqnVals_moment(snglist, x, c1=0, c2=0):                 # moment values at each time slot
            # x is a list of values and snglist is list of singularity functions
            # get a x long list of values for each time slot
            ans = np.zeros(shape=(len(x), 2))

            i = 0
            for n in x:
                for m in range(0, len(snglist)):
                    if n >= snglist[m][1]:
                        if snglist[m][2] == 1:
                            temp = snglist[m][0] * (n - snglist[m][1] )
                            ans[i][0] = ans[i][0] + temp
                        elif snglist[m][2] == 0:
                            ans[i][0] = ans[i][0] + snglist[m][0]
                ans[i][1] = n
                i += 1

            return ans

        def SngEqnVals_slope(snglist, x, c1=0, c2=0):                   # slope values at each time slot
            # x is a list of values and snglist is list of singularity functions
            # get a x long list of values for each time slot
            ans = np.zeros(shape=(len(x), 2))

            i = 0
            for n in x:
                for m in range(0, len(snglist)):
                    if n >= snglist[m][1]:
                        if snglist[m][2] ==2:
                            temp = snglist[m][0] * ((n - snglist[m][1])**2)
                            ans[i][0] = ans[i][0] + temp
                        if snglist[m][2] == 1:
                            temp = snglist[m][0] * (n - snglist[m][1] )
                            ans[i][0] = ans[i][0] + temp
                        elif snglist[m][2] == 0:
                            ans[i][0] = ans[i][0] + snglist[m][0]
                ans[i][1] = n
                ans[i][0] = ans[i][0] / (self.E * 10**6 * self.moment_of_inertia)
                i += 1

            return ans

        def SngEqnVals_Deflection(snglist, x, c1=0, c2=0):              # deflection values at each time slot
            # x is a list of values and snglist is list of singularity functions
            # get a x long list of values for each time slot
            ans = np.zeros(shape=(len(x), 2))

            i = 0
            for n in x:
                for m in range(0, len(snglist) ):
                    if n >= snglist[m][1]:
                        if snglist[m][2] ==3:
                            temp = snglist[m][0] * ((n - snglist[m][1])**3)
                            ans[i][0] = ans[i][0] + temp
                        if snglist[m][2] ==2:
                            temp = snglist[m][0] * ((n - snglist[m][1])**2)
                            ans[i][0] = ans[i][0] + temp
                        if snglist[m][2] == 1:
                            temp = snglist[m][0] * (n - snglist[m][1] )
                            ans[i][0] = ans[i][0] + temp
                        elif snglist[m][2] == 0:
                            ans[i][0] = ans[i][0] + snglist[m][0]
                ans[i][1] = n
                ans[i][0] = (ans[i][0] ) / (self.E * 10**6 * self.moment_of_inertia)
                i += 1

            return ans

        def SngEqnVals_Deflection_constant(snglist, x, c1=0, c2=0):     # deflection values used to then get C1 and C2
            # x is a list of values and snglist is list of singularity functions
            # get a x long list of values for each time slot
            ans = 0

            for m in range(0, len(snglist) ):
                if x >= snglist[m][1]:
                    if snglist[m][2] ==3:
                        temp = snglist[m][0] * ((x - snglist[m][1])**3)
                        ans = ans + temp
                    if snglist[m][2] ==2:
                        temp = snglist[m][0] * ((x - snglist[m][1])**2)
                        ans = ans + temp
                    if snglist[m][2] == 1:
                        temp = snglist[m][0] * (x - snglist[m][1] )
                        ans = ans + temp
                    elif snglist[m][2] == 0:
                        ans = ans + snglist[m][0]
            ans = ans / (self.E * 10 ** 6 * self.moment_of_inertia)
            return ans

        def Constant_things(p):                                         # returns equations to use fsolve to find c1 an c2
            C1, C2 = p
            eqn1 = SngEqnVals_Deflection_constant(Deflection, self.support[0]) + C1 * self.support[0] + C2
            eqn2 = SngEqnVals_Deflection_constant(Deflection, self.support[1]) + C1 * self.support[1] + C2
            return eqn1, eqn2


        # integrate each function to get all equations needed
        q_temp = deepcopy(q)
        V = integrate(q_temp)
        V_temp = deepcopy(V)
        M = integrate(V_temp)
        M_temp = deepcopy(M)
        Slope = integrate(M_temp)
        Slope_temp = deepcopy(Slope)
        Deflection = integrate(Slope_temp)

        # set some variables needed
        L = self.shaft_length
        xxxxx =np.linspace(L / 100000.0, L, 3000)


        # calculate shear values and max point
        sng_vals_V = SngEqnVals_shear(V, xxxxx)
        v_vals = sng_vals_V[:, 0]
        self.maxV, self.maxV_location = find_max_V(sng_vals_V)

        # calculate moment values and max point
        sng_vals_M = SngEqnVals_moment(M, xxxxx)
        m_vals = sng_vals_M[:, 0]
        self.maxMoment, self.maxM_location = find_max_Moment(sng_vals_M)

        # calculate slope values
        sng_vals_Slope = SngEqnVals_slope(Slope, xxxxx)
        S_vals = sng_vals_Slope[:,0]

        # calculate deflection values
        sng_vals_Deflection = SngEqnVals_Deflection(Deflection, xxxxx)
        Deflection_vals = sng_vals_Deflection[:, 0]


        # solve for C1 and C2
        self.C1, self.C2 = fsolve(Constant_things, (1, 2))

        # add c1 to all values in the slope list of values at each time point
        for i in range(0, len(sng_vals_Slope)):
            sng_vals_Slope[i][0] += self.C1

        # find max slope and location
        self.maxSlope, self.maxSlope_location = find_max_Slope(sng_vals_Slope)
        Slope_vals = sng_vals_Slope[:, 0]

        # set up equation for c1 times X and then resolve for each deflection value for each time slot
        c1x = [(self.C1 * (self.E * 10**6 * self.moment_of_inertia)), 0, 1]
        Deflection.extend([c1x])
        sng_vals_Deflection = SngEqnVals_Deflection(Deflection, xxxxx)

        # add c2 value to each deflection value
        for i in range(0, len(sng_vals_Deflection)):
            sng_vals_Deflection[i][0] += self.C2

        # find the max deflection and location
        self.maxDeflection, self.maxDeflection_location = find_max_Deflection(sng_vals_Deflection)
        Deflection_vals = sng_vals_Deflection[:, 0]

        # set varibles for use for graphing
        self.shear_list = v_vals
        self.moment_list = m_vals
        self.slope_list = S_vals
        self.deflection_list = Deflection_vals
        return v_vals, m_vals, S_vals, Deflection_vals



    def plot(self, title = None):
        fig, plt1 = HandyDandyBeamPlotter(self.shear_list, self.moment_list,
                                          self.slope_list, self.deflection_list, self.shaft_length,
                                          self.C1, self.C2,
                                          npoints = 2000, show = True, save = False,
                                          title = title)


def integrate(eqn):
    for n in range(0, len(eqn)):
        eqn[n][2] = eqn[n][2] + 1
        if eqn[n][2] > 1:
            eqn[n][0] = eqn[n][0] / (eqn[n][2])
    return eqn


