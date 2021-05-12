class A:
    pass

class B:
    pass

class C:
    pass

class D(A,B):
    pass

class E(B,C):
    pass

class F:
    pass

class U(D,E,F):
    pass

class V(E,D,F):
    pass

class X(E,D,C):
    pass

print(U.mro())
print(V.mro())
print(X.mro())