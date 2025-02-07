from beacon import Beacon
import math

def calculate_distance(y, h, height):
    cameraHeight = 1.80
    y_coordinate = y + h

    #extract angle a from the currentBeacon
    angle_a = 90*((y_coordinate - (height/2))/(height/2))

    #calculate distance d 
    distance_d = cameraHeight * math.cos(math.radians(angle_a))/ math.sin(math.radians(angle_a))

    return distance_d