import graphics.engine
import rubics

distance = 20
scale = 60

cube = rubics.rubicsCube()
points, triangles = cube.readPoints, cube.readTriangles

world = graphics.engine.Engine3D(points, triangles, scale=scale, distance=distance, width=400, height=600, title="Rubik's cube")
world.rotate('y', -20)
world.rotate('x', -20)
world.render()

def interact(event):
    if event.keysym in ['r', 'l', 'u', 'd', 'f', 'b', 'R', 'L', 'U', 'D', 'F', 'B']:
        k = event.keysym
        exec('cube.' + k)
        triangles = cube.readTriangles

        world.clear()
        world.writeTriangles(triangles)
        world.render()
    elif event.keysym == 'n':
        cube.randomize(20)
        triangles = cube.readTriangles

        world.clear()
        world.writeTriangles(triangles)
        world.render()
        
world.screen.window.bind('<Key>', interact)
world.screen.window.mainloop()

'''
Play around with the rubics cube:
r => right
l => left
u => up
d => down
b => back
f => front

lower = clockwise
caps = anticlockwise

n => shuffle

Drag to rotate
'''
