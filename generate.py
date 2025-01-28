#Jack Vickers
import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("box.sdf")

for xAxis in range(0,4):
    for yAxis in range(0,4):
        y=1
        for x in range(1, 11):
            pyrosim.Send_Cube(name="Box", pos=[xAxis, yAxis, x], size=[y, y, y])
            y *= .9
pyrosim.End()