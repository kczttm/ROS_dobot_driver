from DoBot_IK import DoBot_IK
import numpy as np
p0T = np.transpose(np.array([1,6,3]))
yee = DoBot_IK(p0T)