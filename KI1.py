import matplotlib.pyplot as plt
from random import gauss as gi
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#Funktion für die Funktions-approximation aufgrund der Input Daten
def test(N, NOISE, A, B):	
	FUN = lambda x : A*x+B
	
	data_x = [i for i in range(N)]
	data_y = [FUN(i)+gi(0,NOISE) for i in range(N)]

	mid_x = sum(data_x)/N
	mid_y = sum(data_y)/N
	
	a = sum((data_x[i]-mid_x)*(data_y[i]-mid_y) for i in range(N))/sum((x-mid_x)**2 for x in data_x)
	b = mid_y-a*mid_x
	
	#Auszuwertender Fehler als return
	#return a-A
	return b-B
	


#Anzahl Input Daten bzw. Punkte
KNOTEN = 15
#Maximale Abweichung der Punkte zur Richtigen Funktion
ABWEICHUNG = 1
#genauigkeit der abweichungs Berechnungen
STEP = 0.1
#Genauigkeit der Simulation
GENAUIGKEIT = 100
#Lineare Funktion: A = Steigungsfaktor, B = Schnittpunkt mit Y-Achse
A = 1.5
B = 3

dataKnoten = np.arange(2,KNOTEN+1,1)
dataAbweichung = np.arange(0,ABWEICHUNG+STEP, STEP)
dataKnoten, dataAbweichung = np.meshgrid(dataKnoten,dataAbweichung)
dataFehler = []

for j in dataAbweichung:
	val = []
	for i in range(2,KNOTEN+1):
		temp = 0
		for _ in range(GENAUIGKEIT):
			temp += abs(test(i, j[0], A, B))
		val.append(temp/GENAUIGKEIT)
	dataFehler.append(val)

dataFehler = np.array(dataFehler)
	
#Plotzuegs
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(dataKnoten, dataAbweichung, dataFehler, rstride=1, cstride=1, cmap='hot')
plt.xlim(2,KNOTEN)
plt.ylim(0,ABWEICHUNG)
#plt.xticks([i for i in range(2,KNOTEN+1,KNOTEN//10)])
plt.title('Knoten-Unschärfe Verhältnis')
plt.xlabel('Knoten Anzahl')
plt.ylabel('Maximale Unschärfe der Funktion')
plt.show()