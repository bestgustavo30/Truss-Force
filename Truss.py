import re
import numpy as np
import pylab as plt

class Truss:
	def __init__(self,filename):
		fo = open(filename,'r')

		line = fo.readline()
		line = fo.readline()

		self.nodes = []
		while not re.match("BAR",line):
			a = [float(x) for x in line[0:-1].split(',')]
			self.nodes.append(a)
			line = fo.readline()
		self.nodes = np.array(self.nodes)
		print self.nodes	


		line = fo.readline()

		self.bars = []
		while not re.match("REAC",line):
			a = [int(x) for x in line[0:-1].split(',')]
			self.bars.append(a)
			line = fo.readline()

		self.bars = np.array(self.bars)
		print self.bars	


		line = fo.readline()

		self.reac = []
		while not re.match("FORC",line):
			a = [int(x) for x in line[0:-1].split(',')]
			self.reac.append(a)
			line = fo.readline()

		self.reac = np.array(self.reac)
		print self.reac	

		line = fo.readline()

		self.force = []
		while not re.match("END",line):
			a = [float(x) for x in line[0:-1].split(',')]
			self.force.append(a)
			line = fo.readline()

		self.force = np.array(self.force)
		print self.force

		fo.close()
	def plot(self):
		dplotx = (max(self.nodes[:,0])-min(self.nodes[:,0]))*0.1
		dploty = (max(self.nodes[:,1])-min(self.nodes[:,1]))*0.1
		plt.scatter(self.nodes[:,0],self.nodes[:,1])
		for i in range(len(self.bars)):
			plotx=[self.nodes[self.bars[i,0],0],self.nodes[self.bars[i,1],0]]	
			ploty=[self.nodes[self.bars[i,0],1],self.nodes[self.bars[i,1],1]]
			plt.plot(plotx,ploty,'-b')
		
		for i in range(len(self.reac)):
			plotx=[self.nodes[self.reac[i,0],0],self.nodes[self.reac[i,0],0]-self.reac[i,1]*dplotx]
			ploty=[self.nodes[self.reac[i,0],1],self.nodes[self.reac[i,0],1]-self.reac[i,2]*dplotx]
			plt.plot(plotx,ploty,'-k')
		for i in range(len(self.force)):
			print self.force[i,1:2]
			lfuer = np.linalg.norm(self.force[i,1:])
			plotx=[self.nodes[self.force[i,0],0],self.nodes[self.force[i,0],0]-self.force[i,1]*dplotx/lfuer]
			ploty=[self.nodes[self.force[i,0],1],self.nodes[self.force[i,0],1]-self.force[i,2]*dploty/lfuer]
			plt.plot(plotx,ploty,'-r')
		plt.axis('equal')
		plt.show()	
	def write_results(self,results,filename):
		fo = open(filename,'w')
		fo.write("Results, Force\n")
		for i in range(len(self.bars)):
			fo.write("Bar %i: %.2f\n" % (i,results[i]))
		for i in range(len(self.reac)):
			fo.write("Reaction in node %i, components [%i,%i]: %.2f\n" % (self.reac[i,0],self.reac[i,1],self.reac[i,2],results[i+len(self.bars)]))

		fo.close()
	def X(self,i,j):
		x = (self.nodes[i,0]-self.nodes[j,0])/(np.sqrt((self.nodes[i,0]-self.nodes[j,0])**2+(self.nodes[i,1]-self.nodes[j,1])**2))
		return x
	def Y(self,i,j):
		y = (self.nodes[i,1]-self.nodes[j,1])/(np.sqrt((self.nodes[i,0]-self.nodes[j,0])**2+(self.nodes[i,1]-self.nodes[j,1])**2))
		return y
