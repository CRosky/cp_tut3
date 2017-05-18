#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""


@author: Chaka Mofokeng, 217039370
"""

import numpy as np
from matplotlib import pyplot as plt

def fit(x,npoly,points):
    a=np.zeros([x.shape[0],npoly])
    a[:,0]=1
    for n in range(1,npoly):
        a[:,n]=a[:,n-1]*x
    a=np.matrix(a)
    d=np.matrix(points).transpose()
    lhs=a.transpose()*a
    rhs=a.transpose()*d
    fitp=np.linalg.inv(lhs)*rhs
    p=a*fitp
    return p

n=100
npoly=5


x=np.linspace(0,2*np.pi,n)
xx=np.sin(x)
xxx=np.cos(x)
y=xx+np.random.randn(n)
yy=xxx+np.random.randn(n)


fit_y=fit(x,npoly,y)
fit_z=fit(x,npoly,yy)

plt.plot(x,y,"r",label="sine")
plt.plot(x,fit_y,"-",label="Fit")
plt.legend()
plt.show()

plt.plot(x,yy,"k",label="cosine")
plt.plot(x,fit_z,"-",label="Fit")
plt.legend()
plt.show()