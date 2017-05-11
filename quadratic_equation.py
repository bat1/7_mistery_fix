from math import sqrt

def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    try:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
    except ValueError:
        print("A sqrt from negative is impossible in the set of the real number, so you can't get any real roots")
    if discriminant == 0:
        return root1, None
    elif discriminant < 0: # There are no real roots in this case, But there are 2 complex,
        return None, None  # You can get it by using cmath module.
    else: 
        return root1, root2