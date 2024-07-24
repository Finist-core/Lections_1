def room_square(side1, side2):
    room = side1 * side2
    return room
def tile(side1, side2):
    one_tile = (side1 * side2)
    one_tile = one_tile / 1000000
    return one_tile
print('Введите длину комнаты в метрах')
len_room = int(input())
print('Введите ширину комнаты в метрах')
width_room = int(input())
if width_room <= 0:
    print('Не бывает )))')
    exit()
room_size = room_square(len_room, width_room)
print('Площадь комнаты', room_size, 'квадратных метров')
print('Введите длину плитки в миллиметрах')
len_tile = int(input())
print('Введите ширину плитки в миллиметрах')
width_tile = int(input())
tile_size = tile(len_tile, width_tile)
print('Площадь плитки', int(tile_size), 'квадратных метров')

#В формуле ошибка, почитать как посчитать
need = room_size * tile_size
print('Нужно', int(need), 'плиток')