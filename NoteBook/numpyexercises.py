import numpy as np

# #3x3 matrix with values from 2 to 10
# alpha = np.arange(2,11).reshape(3,3)
# print(alpha)
#
# # Null vector of size 10
# # Update 6th value to 11
# beta = np.zeros(10)
# beta[5] = 11
# print(beta)
#
#Array with values from 12 to 38
# charlie = np.arange(12,39)
# print(charlie)
#
# #Reverse it
# delta = charlie[::-1]
# print(delta)
#
# #8x8 matrix with checkerboard pattern
# echo = np.zeros((8,8))
# echo[1::2, ::2] = 1
# #^every second row, starting from the first, with a skip of 1 column
# echo[::2, 1::2] = 1
# print(echo)

foxtrot = np.zeros((10,10))
foxtrot[0] = 9
foxtrot[::1,0::9]=9
foxtrot[9] = 9
foxtrot[2:5,3] = 44
#Remember start:stop:step
foxtrot[2:5,6] = 44
foxtrot[7,2::5] =44
foxtrot[8,3:7] = 44
print(foxtrot)


