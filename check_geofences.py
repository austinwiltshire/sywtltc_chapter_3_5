from geofence_match import geofence_match

#load geo fences
f = open("geofences.txt")
polygons = []
for l in f.readlines()[1:]:
    ps = l.split(";")
    p1 = tuple(float(x) for x in ps[0][1:-1].split(","))
    p2 = tuple(float(x) for x in ps[1][1:-1].split(","))
    p3 = tuple(float(x) for x in ps[2][1:-1].split(","))
    p4 = tuple(float(x) for x in ps[3][1:-2].split(","))
    polygons.append([p1,p2,p3,p4])

#load points
f = open("gpsdata.txt")
points = []
for l in f.readlines()[1:]:
    ps = l.split(",")
    points.append([float(ps[0]), float(ps[1])])

for p1 in polygons:
    for p2 in points:
        print "Does polygon", p1, " contain point", p2, ":", geofence_match(p1[0][0], p1[0][1], p1[1][0], p1[1][1], p1[2][0], p1[2][1], p1[3][0], p1[3][1], p2[0], p2[1])

