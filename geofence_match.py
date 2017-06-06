from sympy.geometry import Point, Polygon

def geofence_match(poly1_lon, poly1_lat, poly2_lon, poly2_lat, poly3_lon, poly3_lat, poly4_lon, poly4_lat, pnt_lon, pnt_lat):
    poly = Polygon((poly1_lon,poly1_lat),(poly2_lon,poly2_lat),(poly3_lon,poly3_lat),(poly4_lon,poly4_lat))
    pnt = Point((pnt_lon, pnt_lat))
    return poly.encloses_point(pnt)

