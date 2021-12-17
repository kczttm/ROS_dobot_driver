from DoBot_IK import *
import numpy as np

def IK_Processing(qsol):

    # *** Because of the way DoBot reads q3**
    qsol[2, :] = qsol[2, :] + qsol[1, :]
    # re-wrap to pi
    qsol = np.arctan2(np.sin(qsol), np.cos(qsol))
    # DoBot reads angles in degrees
    qsol = np.rad2deg(qsol)
    # print(qsol)
    # find the limits of the dobot
    for i in [0,1,2,3]:
        # ending loop as soon as it finds an acceptable solution, deleating all other solutions

        q1 = qsol[0, 0]
        q2 = qsol[1, 0]
        q3 = qsol[2, 0]


        q3_lim = q3lim(q2)
        # print("***********")
        # print(q3_lim[0])
        # print(q3)
        # print(q3_lim[1])
        if q3 > q3_lim[0] or q3 < q3_lim[1]:
           qsol = np.delete(qsol, 0, 1)
           continue
        if q1 > 135 or q1 < -135:
            qsol = np.delete(qsol, 0, 1)
            continue
        if q2 > 85 or q2 < -5:
            qsol = np.delete(qsol, 0, 1)
            continue
        return qsol[:,0] # returns first solution if many are available

def q3lim(q2):
    # Takes q2 in degrees
    """Line encoded as l=(x,y)."""
    l1_up = (0,62)
    l2_up = (40, 94)
    m_up = ((l2_up[1] - l1_up[1])) / (l2_up[0] - l1_up[0])
    b_up = (l2_up[1] - (m_up * l2_up[0]))
    if q2 >= 40:
        q3_lim_up =  94
    else:
        q3_lim_up = m_up * q2 + b_up

    l1_dn = (34, 0)
    l2_dn = (80, 44)
    m_dn = ((l2_dn[1] - l1_dn[1])) / (l2_dn[0] - l1_dn[0])
    b_dn = (l2_dn[1] - (m_dn * l2_dn[0]))
    if q2 <= 30:
        q3_lim_dn = 0
    else:
        q3_lim_dn = m_dn * q2 + b_dn
    return (q3_lim_up, q3_lim_dn)