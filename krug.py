from matrix_reload import *

m = Matrix(5,6,coordinates=[3, 4])
a = Matrix(10, 10, homogeneous=True, value=0)
b = turner(m, a=-2)
a.glue(b)
print(a)