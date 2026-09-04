class A:
    def show_a(self):
        print("Hii")
class B(A):
    def show_b(self):
        print("Heloooo")
class C(A):
    def show_c(self):
        print("Byee")
class D(B,C):
    def show_d(self):
        print("Abhaaaa")

D = D()

D.show_a()
D.show_b()
D.show_c()
D.show_d()

