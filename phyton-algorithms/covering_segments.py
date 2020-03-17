# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = {};
    
    for n in range( len( segments ) ):
        for j in range( segments[n].start , segments[n].end + 1 ):
            if( j in points):
                array = points[j];
                array.append(n);
            else:               
                points[j] = [ n ];
                
    selectedPoints = [ segments[0].start ];
    
    for p, currentIntersec in points.items():
      for n in range( len( selectedPoints ) ):
        index = selectedPoints[n] ;
        selectedIntersec = points[ index ];
        touchNewPoints = False;
        includeSame = False;
        for j in range( len( selectedIntersec ) ):
            if currentIntersec[j] < selectedIntersec[j]:
                touchNewPoints = True;
    return points


a = Segment(1 , 5);
b = Segment(2 , 10);
segments = [a , b];
points = optimal_points(segments)

for x, y in points.items():
  for n in range( len( y ) ):
      print( x , " : " , y[n]);
