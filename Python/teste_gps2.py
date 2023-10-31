import math
import numpy as np

def decompond_degrees(degrees):
    deg = int(degrees)
    minutes = (degrees - deg)*60
    sec = np.float32((minutes - int(minutes))* 60)
    minutes = int(minutes)
    print(f"pos {degrees} decomposta = {deg}° ,{minutes}',{sec}''")
    degrees = np.float32(degrees)
    return deg,minutes,sec,degrees

lat_1 = decompond_degrees(20.218588)
long_1 = decompond_degrees(43.871331)
lat_2 = decompond_degrees(20.218585)
long_2 = decompond_degrees(43.870877)



Graus_Lat_01 = lat_1[0]
Min_Lat_01 = lat_1[1]
Seg_Lat_01 = lat_1[2]

Graus_Lat_02 = lat_2[0]
Min_Lat_02 = lat_2[1]
Seg_Lat_02 = lat_2[2]

Graus_Long_01 = long_1[0]
Min_Long_01 = long_1[1]
Seg_Long_01 = long_1[2]

Graus_Long_02 = long_2[0]
Min_Long_02 = long_2[1]
Seg_Long_02 = long_2[2]
NORTE_OFFSET = 0

LAT_01= -lat_1[3]
LAT_02= -lat_2[3]
LONG_01= -long_1[3]
LONG_02= -long_2[3]

DLAT= np.float32(math.radians(LAT_01) - math.radians(LAT_02) )
DLONG =np.float32( math.radians(LONG_01) - math.radians(LONG_02) )
HALF_DLAT = DLAT/2  
HALF_DLONG = DLONG/2 
SIN_HALF_DLAT = math.sin(HALF_DLAT) 
SIN_HALF_DLONG= math.sin(HALF_DLONG) 
PWD_SIN_HALF_LAT=SIN_HALF_DLAT *SIN_HALF_DLAT 
PWD_SIN_HALF_LONG=SIN_HALF_DLONG*SIN_HALF_DLONG 
COS_LAT_01 = math.cos(math.radians(LAT_01)) 
COS_LAT_02 = math.cos(math.radians(LAT_02)) 
VAL_A= PWD_SIN_HALF_LAT+ COS_LAT_01 * COS_LAT_02 * PWD_SIN_HALF_LONG 
SQRT_VAL_A =math.sqrt(VAL_A) 
SQRT_VAL_1_MINUS_A= math.sqrt((1-VAL_A)) 
VAL_B= 2 * math.atan2(SQRT_VAL_A,SQRT_VAL_1_MINUS_A)
DIST = np.float32(VAL_B * 6373000.0)
    #ATAN(X/Y) X = #cos Long-b * sin Delta-Lat E Y = #cos Long-a * sin Long-b – sin Long-a * cos Long-b * cos Delta-Lat 
X=math.cos(math.radians(LAT_02)) * math.sin(DLONG) 
Y=math.cos(math.radians(LAT_01)) * math.sin(math.radians(LAT_02)) - math.cos(math.radians(LAT_02)) * math.sin(math.radians(LAT_01)) * math.cos(DLONG) 
XY = X/Y 
"""IF y > 0 THEN
    BEARING = ATAN(XY) 
ELSIF Y<0 AND X >= 0 THEN
    BEARING = ATAN(XY) + 3.141592653589793  
ELSIF Y<0 AND X < 0 THEN
    BEARING = ATAN(XY) - 3.141592653589793  
ELSIF Y = 0 AND X > 0 THEN
    BEARING = ATAN(XY) + 3.141592653589793/2  
ELSIF Y = 0 AND X < 0 THEN
    BEARING = ATAN(XY) - 3.141592653589793/2  
ELSE
    BEARING = 0 
END_IF """
if Y >= 0:
    BEARING = math.atan(XY)
elif Y < 0 and X >= 0:
    BEARING = math.atan(XY) + math.pi
elif Y < 0 and X < 0:
    BEARING = math.atan(XY) - math.pi

BEARING =  (BEARING * 180) / 3.141592653589793 
BEARING_RELATIVO = BEARING + NORTE_OFFSET 

print(f"distancia = {DIST}")
print(f"Rotação = {BEARING}")