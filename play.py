import graphics.engine
import rubics

distance = 20
scale = 60

cube = rubics.rubicsCube()
points, triangles = cube.readPoints, cube.readTriangles

world = graphics.engine.Engine3D(points, triangles, scale=scale, distance=distance, width=400, height=600)
world.rotate('y', -20)
world.rotate('x', -20)
world.render()

def interact(event):
    if event.keysym in ['r', 'l', 'u', 'd', 'f', 'b']:
        k = event.keysym.upper()
        exec('cube.' + k)
        triangles = cube.readTriangles

        world.clear()
        world.writeTriangles(triangles)
        world.render()
    elif event.keysym == 'n':
        cube.randomize(30)
        triangles = cube.readTriangles

        world.clear()
        world.writeTriangles(triangles)
        world.render()
        
world.screen.window.bind('<Key>', interact)

'''
Play around with the rubics cube:
r => right
l => left
u => up
d => down
b => back
f => front

n => shuffle
'''
