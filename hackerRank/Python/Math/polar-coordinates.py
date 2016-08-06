import cmath

a=complex(input())
print (abs(complex(a.real, a.imag)))
print (cmath.phase(complex(a.real, a.imag)))
