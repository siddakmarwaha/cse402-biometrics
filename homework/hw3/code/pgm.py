from pgm_reader  import Reader 
from matplotlib import pyplot as plt
import numpy as np

f = './data/subject01.centerlight.pgm' 

reader = Reader() 
image = reader.read_pgm(f) 


plt.imshow(image, cmap='gray')
plt.show()

print(reader.height)  

