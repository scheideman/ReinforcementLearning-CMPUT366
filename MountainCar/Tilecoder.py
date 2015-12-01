"""
Tile Coder for mountain car problem 
X = position
Y = velocity
"""
import numpy as np
numTilings = 4
numTiles = 9*9*numTilings
offsetX = np.zeros(4)
offsetY = np.zeros(4)

tileSizeX = float(1.7)/float(8) #0.2125
tileSizeY = float(0.14)/float(8) #0.0175

def tilecode(x,y,tileIndices):
     for i in range(0,numTilings):
        offsetx = i * tileSizeX/float(numTilings); 
        offsety = i * tileSizeY/float(numTilings);
        xy = [offsetx + x +1.2, offsety+y+0.07];
    	#xy = [offsetX[i] + x +1.2, offsetY[i]+y+0.07];
        tileIndex = np.floor(xy[0]/tileSizeX)  + np.floor(xy[1]/tileSizeY)*9; 
    	tileIndices[i] = int(tileIndex) + i*81; 
    #return tileIndices
    
def printTileCoderIndices(x,y):
    tileIndices = [-1]*numTilings
    tilecode(x,y,tileIndices)
    print 'Tile indices for input (',x,',',y,') are : ', tileIndices


def setOffset():
    global offsetX, offsetY
    offsetX = (tileSizeX*0.99)*np.random.random(4) 
    offsetY = (tileSizeY*0.99)*np.random.random(4)


setOffset()
#print offsetX
#print offsetY
#printTileCoderIndices(0.01,0.01)
#printTileCoderIndices(-1.1,-0.01)
#printTileCoderIndices(.49,0.069)
#printTileCoderIndices(-1.2,-0.07)


    
