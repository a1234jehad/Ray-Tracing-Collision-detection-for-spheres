import numpy as np


def sphere_collison(dict_of_list_obj, width_frame, height_frame, cam_pos):
    def normalize(vector):
        return vector / np.linalg.norm(vector)

    def sphere_intersect(center, radius, ray_origin, ray_direction):
        b = 2 * np.dot(ray_direction, ray_origin - center)
        c = np.linalg.norm(ray_origin - center) ** 2 - radius ** 2
        delta = b ** 2 - 4 * c
        if delta > 0:
            t1 = (-b + np.sqrt(delta)) / 2
            t2 = (-b - np.sqrt(delta)) / 2
            if t1 > 0 and t2 > 0:
                return min(t1, t2)
        return None

    objects = dict_of_list_obj
    width = width_frame
    height = height_frame
    # the frame of the camera

    camera = cam_pos  # position of the camera
    ratio = float(width) / height
    frame = (-1, 1 / ratio, 1, -1 / ratio)  # left, top, right, bottom ( aspect ratio for top and bottom...)
    results = {}
    image = np.zeros((height, width, 3))  # fill array with zero
    for i, y in enumerate(np.linspace(frame[1], frame[3], height)):  # top to bottom
        for j, x in enumerate(np.linspace(frame[0], frame[2], width)):  # left to right
            # note that camera = origin, pixel = destination
            pixel = np.array([x, y, 0])  # z=0 since it lies on the screen
            origin = camera
            direction = normalize(pixel - origin)  # to get unit vector which is basically the direction
            count = 0
            for obj in objects:
                k = sphere_intersect(obj['center'], obj['radius'], origin, direction)
                count += 1
                if k != None:
                    results[f'object{count}'] = True
    print(results)


objects = [{'center': np.array([-0.2, 0, -1]), 'radius': 0.7}
    , {'center': np.array([-0.2, 2, -1]), 'radius': 2.7}
    , {'center': np.array([-0.2, 22, -1]), 'radius': 5.7}
           ]
width = 300
height = 200
camera = np.array([0, 0, 1])  # position of the camera
sphere_collison(objects, width, height, camera)  # returns objects that will collide
