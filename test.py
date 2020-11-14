a = [0,1,2]
def check():
    if f(0,1,2):
        return

def f(e1,e2,e3):
    m = False
    if a[e1] == 0:
        a[e1] = 2
        m = True
    return m
check()
print(a)
        