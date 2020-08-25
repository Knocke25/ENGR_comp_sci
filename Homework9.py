from scipy import fsolve
#something...











def solvebeam(self)
    z=0 # placeholder for me
    # idk, i think we are given q, and we have to integrate for the V and M
    def integrate(eqn):
        for n in range(0,len(eqn)):
            eqn[n][3] += 1
            if eqn[n][3] > 1:
                eqn[n][1] = eqn[n][1] / n

    def statics(vals)
        R1, R2 = vals
        #v_end = evaluate shear at x = length
        # m_end = evaluate moment at x = length
        # return v_end and m_end
        V[0][0] = R1 ; V[1][0] = R2
        M[0][0] = R1 ; M[1][0] = R2

        e1 = sing_equ_vals(V, L):
        e2 = sing_equ_vals(M, L):
        return e1, e2


        def func(vals)
            x,y = vals




    R1 = 1 # wild guess
    R2 = 5 # Wild Guess


    R1, R2 = fsolve(statics, [R1, R2])



