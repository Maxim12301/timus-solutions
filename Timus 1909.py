import math

class Vec:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, scalar):
        return Vec(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar):
        return Vec(self.x / scalar, self.y / scalar, self.z / scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vec(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def length_squared(self):
        return self.x**2 + self.y**2 + self.z**2

    def normalize(self):
        mag = self.length()
        return Vec(self.x / mag, self.y / mag, self.z / mag)


def dv(x, r):

    return x / math.sqrt(r**2 - x**2)


def find(r, k):
    
    L, R = -r, r
    while R - L > 1e-9:
        m = L + (R - L) / 2
        if dv(m, r) < k:
            L = m
        else:
            R = m
    return R




def main():
    
    x0, y0, z0, R = map(float, input().split())
    c = Vec(x0, y0, z0)
    p1 = Vec(*map(float, input().split()))
    p2 = Vec(*map(float, input().split()))
    v = Vec(*map(float, input().split()))

    w = p2 - p1
    v = v.normalize()
    along = False

    
    if (v.cross(w.normalize())).length() < 1e-5:
        w = Vec(1000001, 1000002, 1000003)
        along = True

    
    a = (w.cross(v)).normalize()
    b = (v.cross(a)).normalize()

    
    x = w.dot(b)
    y = v.dot(w)

    
    cy = (c - p1).dot(a)
    cx = (c - p1).dot(b)


    d = ((w.cross(v)).cross(w)).dot(c - p1)
    D = R**2 - cy**2  

    if D < -1e-9:  
        print("False alarm")
        return

    if along:
        eps = 1e-5
        if (d > 0 and cx**2 + cy**2 <= R**2 + eps) or ((cx - x)**2 + cy**2 <= R**2 + eps):
            print("Crash")
            return

    if not along:
        D = max(D, 0.0)
        
        x1 = cx - math.sqrt(D)
        x2 = cx + math.sqrt(D)

        
        p = find(math.sqrt(D), y / x)
        if p + cx > 1e-9 and p + cx < x - 1e-9 and (c - (p1 + w.normalize() * (p + cx) / (w.dot(b) / w.length()))).dot(v) > -1e-9:
            print("Warning")
            return

        
        if (v.dot(c - p1) > -1e-9 and x1 < 1e-9 and x2 > -1e-9) or (v.dot(c - p2) > -1e-9 and x1 < x + 1e-9 and x2 > x - 1e-9):
            print("Crash")
            return

    print("False alarm")


if __name__ == "__main__":
    main()