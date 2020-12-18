---
layout: post
title:  "Borde de una triangulación"
date:   2020-12-16 00:30:43 -0500
categories: math
---
Como le decía a mi amigo user89 en mi primer [respuesta aceptada](https://stackoverflow.com/questions/59419537/how-do-i-get-the-boundary-of-a-delaunay-triangulation/65315724#65315724) 
en Stackoverflow, es muy fácil encontrar el borde de una triangulación. 
La observación clave es que un lado de un triángulo está en el borde si no es compartido por ningún otro triángulo. 

Un programa que encuentra el borde necesita conocer qué vecinos tiene cada triángulo, y esa información 
nos la provee scipy.spatial.Delaunay. Un código de ejemplo es entonces:

{% highlight ruby %}
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

# Create triangulation of a rectangle
x = np.linspace(0,1,9)
y = np.linspace(0,1,9)
X,Y = np.meshgrid(x,y)
P = np.array([X.flatten(),Y.flatten()]).T
T = Delaunay(P)

# Find edges at the boundary
boundary = set()
for i in range(len(T.neighbors)):
    for k in range(3):
        if (T.neighbors[i][k] == -1):
            nk1,nk2 = (k+1)%3, (k+2)%3 
            boundary.add(T.simplices[i][nk1])
            boundary.add(T.simplices[i][nk2])

# Plot result
plt.triplot(P[:,0], P[:,1], T.simplices)
plt.plot(P[:,0], P[:,1], 'o')
plt.plot(P[list(boundary),0], P[list(boundary),1], 'or')
plt.show()
{% endhighlight %}
... y lo que obtenemos es
![Output](https://i.stack.imgur.com/ZwaKv.png)
