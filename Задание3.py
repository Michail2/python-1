coord_x = float( input() )
coord_y = float( input() )
if coord_x != 0 and coord_y != 0:
    if coord_x > 0 and coord_y > 0:
        print( '{}; {} -> 1'.format( coord_x, coord_y ) )
    elif coord_x < 0 and coord_y > 0:
        print( '{}; {} -> 2'.format( coord_x, coord_y ) )
    elif coord_x < 0 and coord_y < 0:
        print( '{}; {} -> 3'.format( coord_x, coord_y ) )
    elif coord_x > 0 and coord_y < 0:
        print( '{}; {} -> 4'.format( coord_x, coord_y ) )
else:
    print( 'Введены некорекные значения' )