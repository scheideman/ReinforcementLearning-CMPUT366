import numpy as np
numTilings = 8
    
def tilecode(x,y,tileIndices):
     # write your tilecoder here (5 lines or so)
     tileSize = float(6)/float(10);
     #print tileSize
     for i in range(0,numTilings):
	offset = i * tileSize/float(numTilings);   
	xy = [offset + x, offset+y];
	tileIndex = np.floor(xy[0]/tileSize) + np.floor(xy[1]/tileSize)*11;
	tileIndices[i] = int(tileIndex) + i*121; 

    
def printTileCoderIndices(x,y):
    tileIndices = [-1]*numTilings
    tilecode(x,y,tileIndices)
    print 'Tile indices for input (',x,',',y,') are : ', tileIndices

printTileCoderIndices(0.1,0.1)
printTileCoderIndices(4.0,2.0)
printTileCoderIndices(5.99,5.99)
printTileCoderIndices(4.0,2.1)

'''
#extra test cases not to be handed in 
printTileCoderIndices(0,5.99)
printTileCoderIndices(0.7,0.7)
printTileCoderIndices(1.3,1.3)
'''
#Also need to answer why questions in why1.pdf
    
