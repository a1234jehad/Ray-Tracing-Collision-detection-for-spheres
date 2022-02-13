import numpy as np


def normalize(vector):
    return vector / np.linalg.norm(vector)


def Cylinder_infinite_intersect(center, radius, ray_origin, ray_direction):
    a = (ray_direction[0] ** 2) + (ray_direction[1] ** 2)
    b = 2 * ((ray_direction[0] * (ray_origin[0] - center[0])) + (ray_direction[1] * (ray_origin[1] - center[1])))
    c = ((ray_origin[0] - center[0]) ** 2) + ((ray_origin[1] - center[1]) ** 2) - radius ** 2
    delta = (b ** 2) - 4 * (a * c)
    if abs(delta) < 0.001 or delta < 0.0:
        return None

    t1 = (-b + np.sqrt(delta)) / (2 * a)
    t2 = (-b - np.sqrt(delta)) / (2 * a)
    if t1 > 0 and t2 > 0:
        return t1, t2
    return None


def Cylindr_cap_intersect(center, radius, ray_origin, ray_direction, zmin, zmax):
    if Cylinder_infinite_intersect(center, radius, ray_origin, ray_direction) == None:
        return None
    t1, t2 = Cylinder_infinite_intersect(center, radius, ray_origin, ray_direction)
    z1 = (ray_origin[2] - center[2]) + t1 * ray_direction[2]
    z2 = (ray_origin[2] - center[2]) + t2 * ray_direction[2]

    if zmin < z1 < zmax and zmin < z2 < zmax:
        return min(t1, t2)
    return None


origin = np.array([0, 0, 0])
destination = np.array([-1, -1, -1])  # z=0 since it lies on the screen
direction = normalize(destination - origin)

objects = [{'center': np.array([-0.2, -1, 0]), 'radius': 0.7, 'zmin': 0.1, 'zmax': 0.6}
    , {'center': np.array([-0.4, -0.6, -0.7]), 'radius': 0.7, 'zmin': -0.3, 'zmax': 0.7}
    , {'center': np.array([-0.2, 22, -1]), 'radius': 5.7, 'zmin': 0.1, 'zmax': 0.6}]

count = 0
for obj in objects:
    ci = Cylinder_infinite_intersect(obj['center'], obj['radius'], origin, direction)
    cc = Cylindr_cap_intersect(obj['center'], obj['radius'], origin, direction, obj['zmin'], obj['zmax'])
    if ci != None:
        print(f'Object{count} has infinite cylinder intersection')
    if cc != None:
        print(f'Object{count} has cap cylinder intersection')
    count += 1
