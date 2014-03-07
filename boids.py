"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes

x_min = -450
x_max = 50.0

y_min = 300.0
y_max = 600.0

x_min_velocities = 0
x_max_velocities = 10.0

y_min_velocities = -20
y_max_velocities = 20
increments = 50

boids_x=[random.uniform(x_min,x_max) for x in range(increments)]
boids_y=[random.uniform(y_min,y_max) for x in range(increments)]
boid_x_velocities=[random.uniform(x_min_velocities,x_max_velocities) for x in range(increments)]
boid_y_velocities=[random.uniform(y_min_velocities,y_max_velocities) for x in range(increments)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids,increment=0.01, rescale_birds =100, rescale_speed = 10000, speed_decrement=0.125):
	xs,ys,xvs,yvs=boids
	# Fly towards the middle
	for i in range(len(xs)):
		for j in range(len(xs)):
			xvs[i]=xvs[i]+(xs[j]-xs[i])*increment/len(xs)
	for i in range(len(xs)):
		for j in range(len(xs)):
			yvs[i]=yvs[i]+(ys[j]-ys[i])*increment/len(xs)
	# Fly away from nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < rescale_birds:
				xvs[i]=xvs[i]+(xs[i]-xs[j])
				yvs[i]=yvs[i]+(ys[i]-ys[j])
	# Try to match speed with nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < rescale_speed:
				xvs[i]=xvs[i]+(xvs[j]-xvs[i])*speed_decrement/len(xs)
				yvs[i]=yvs[i]+(yvs[j]-yvs[i])*speed_decrement/len(xs)
	# Move according to velocities
	for i in range(len(xs)):
		xs[i]=xs[i]+xvs[i]
		ys[i]=ys[i]+yvs[i]


figure=plt.figure()
x_axis_min=-500
x_axis_max=1500

y_axis_min = -500
y_axis_max = 1500

axes=plt.axes(xlim=(x_axis_min,x_axis_max), ylim=(y_axis_min,y_axis_max))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
