import math
coord_x_A = float( input() )
coord_y_A = float( input() )
coord_x_B = float( input() )
coord_y_B = float( input() )

distance = round( math.sqrt( ( ( coord_x_A - coord_x_B )**2 ) + ( ( coord_y_A - coord_y_B )**2 ) ), 2 )
print( f'A:({coord_x_A},{coord_y_A}); B:({coord_x_B},{coord_y_B}) -> {distance}' )