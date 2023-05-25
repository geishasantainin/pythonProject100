import os


class Tile:
    def __init__(self, text) -> None:
        self.text = text
        self.flag = False
        self.create_tile()

    def create_tile(self):
        length = len(self.text)
        if self.flag:
            self.tile = [f"   ┏{'━' * (length + 2)}┓", f"   ┃ {self.text} ┃", f"   ┗{'━' * (length + 2)}┛"]
        else:
            self.tile = [f"    {' ' * length} ", f"    {self.text} ", f"    {' ' * length} "]

    def is_flag(self, flag):
        self.flag = flag
        self.create_tile()


def draw_tile(list_tiles, num=None, end=18):
    result = ''
    cnt = 0
    for i in range(3):
        mask = ''
        for tile in list_tiles:
            tile.is_flag(False)
            try:
                if num is not None:
                    list_tiles[num].is_flag(True)
            except:
                print(num)
            mask += tile.tile[i]
        result += mask + '\n'

    return result


def columns_tile(list_tiles, end):
    count = 0
    while True:
        for i in range(len(list_tiles)):
            if (count % len(list_tiles)) == i:
                os.system('CLS')
                num = count % len(list_tiles)
                start = 0
                int_num = num // end
                new_list = list_tiles.copy()
                while len(new_list) > 0:
                    if len(new_list) < end:
                        new_list = list_tiles[start * end: len(new_list)]
                    else:
                        new_list = list_tiles[start * end: end * (start + 1)]
                    if int_num == start:
                        print(draw_tile(new_list, num % end))
                    else:
                        print(draw_tile(new_list))
                    if len(new_list) < end:
                        break
                    start += 1
                key = ''

        key = input()

        if key == ' ':
            if list_tiles[count % len(list_tiles)].text == '//':
                input('[ERROR]: This seat is already booked ')
                continue
            elif list_tiles[count % len(list_tiles)].text == '[]':
                input('Successfully!')
                os.system('CLS')
                break
            else:
                print('count % len(list_tiles) = ', count % len(list_tiles))
                print('list_tiles[count % len(list_tiles)] = ', list_tiles[count % len(list_tiles)])
                print('list_tiles[count % len(list_tiles)].text = ', list_tiles[count % len(list_tiles)].text)

        count += 1

    return count, num


def print_tile(list_tiles, count):
    for i in range(len(list_tiles)):
        if (count % len(list_tiles)) == i:
            os.system('CLS')
            num = count % len(list_tiles)
            print(draw_tile(list_tiles, num))
            key = ''
    count += 1
