import numpy as np
from numpy import transpose, cross, arctan2, arcsin
from numpy.linalg import norm
from subprobs import *

def DoBot_FK(q):
    l1 = 103; l2 = 135; l3 = 160; l4 = 50; l5 = 20;
    # ex = np.array([[1,0,0]]).T; ey = np.array([[0, 1,0]]).T; ez = np.array([[0,0,1]]).T;
    # zv = np.array([[0,0,0]]).T
    ex = np.array([1,0,0]); ey = np.array([0, 1,0]); ez = np.array([0,0,1]);
    zv = np.array([0,0,0])
    ex = ex.reshape(-1, 1);  ey = ey.reshape(-1, 1);  ez = ez.reshape(-1, 1);  zv = zv.reshape(-1, 1);

    h1 = ez; h2 = ey; h3 = ey; h4 = ey;
    p01 = l1 * ez; p12 = zv; p23 = l2 * ez; p34 = l3 * ex; p4T = l4 * ex - l5 * ez

    p0T = p01[:,-1][:, np.newaxis]+ rot(h1, q[0]) @ (p12[:,-1][:, np.newaxis]+rot(h2, q[1]) @ (p23[:,-1][:, np.newaxis] + rot(h3, q[2]) @ (p34[:,-1][:, np.newaxis]+ rot(h4, q[3])@p4T)));
    return p0T

