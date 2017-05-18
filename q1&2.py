# -*- coding: utf-8 -*-
"""

@author:Chaka Mofokeng, 217039370
"""

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.animation as animation

from matplotlib import pyplot as plt

#question 1

class nBodySolver:
      def __init__(self,x=0,y=0,m=1):
          self.x=x
          self.y=y
          self.m=m
          
          self.set={'npt':1000, 'G':1, 'soft':0.03}
          
          
      def potentialE(self):
          potential=0
          for n in range(self.conf['npt']):
              dx=self.x[n]-self.x
              dy=self.y[n]-self.y
              r_2=dx**2+dy**2
              soft=self.set['soft']**2
              r_2[r_2<soft]=soft
              r_2=r_2+self.conf['soft']**2
              r=np.sqrt(r_2)
              potential=potential+self.set['G']*np.sum(self.m/r)*self.m[n]
              return -0.5*potential
          
      def initialize(self):
          self.x=np.random.randn(self.set['npt'])
          self.y=np.random.randn(self.set['npt'])
          self.m=np.ones(self.set['npt'])*self.m/self.set['npt']
          self.vx=np.zeros(self.set['npt'])
          self.vy=np.zeros(self.set['npt'])
          self.fx=np.zeros(self.set['npt'])
          self.fy=np.zeros(self.set['npt'])
          
      def Force(self):
          for n in range(self.conf['npt']):
              dx=self.x[n]-self.x
              dy=self.y[n]-self.y
              r_2=dx**2+dy**2
              soft=self.set['soft']**2
              r_2[r_2<soft]=soft
              r_2=r_2+self.conf['soft']**2
              r=np.sqrt(r_2)
              r3=1.0/(r*r_2)
              self.fx[n]=-np.sum(self.m*dx*r3)*self.opts['G']
              self.fy[n]=-np.sum(self.m*dy*r3)*self.opts['G']
         
            
      def update_dt(self,dt):
          self.x+=self.vx*dt
          self.y+=self.vy*dt
          potential=self.potentialE()
          self.Force()
          self.vx+=self.fx*dt
          self.vy+=self.fy*dt
          k_e=0.5*np.sum(self.m*(self.vx**2+self.vy**2))
          return potential+k_e
          
      
        
        
#system=nBodySolver()
#system.initialize()

dt=0.1
oversamp=5
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-8, 8), ylim=(-8, 8))
line, = ax.plot([], [], '*', lw=2)
tot_energy=[]
def animate_points(crud):
    global system,line
    for ii in range(oversamp):
        energy=nBodySolver.update_dt(dt)
        np.append(tot_energy, energy)
    print(energy)
    line.set_data(nBodySolver.x,nBodySolver.y)

ani = animation.FuncAnimation(fig, animate_points, np.arange(30),interval=25, blit=False)
plt.show()

time=np.arange(dt*tot_energy,dt)
plt.plot(time,tot_energy)
plt.set_xlabel("Time(s)")
plt.set_ylabel("Energy")
plt.show()