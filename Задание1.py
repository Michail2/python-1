number_day = int( input() )
if number_day > 1 and number_day < 8:
    if number_day == 6 or number_day == 7:
        print( '{} -> {}'.format( number_day, 'Выходной' ) )
    else:
        print( '{} -> {}'.format( number_day, 'Будний' ) )
else:
    print( 'Введено недопустимое значение' )

