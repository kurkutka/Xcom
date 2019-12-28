import math


class Fire:
    def fire(self, x1, y1, x2, y2, spis):
        bools_way = math.sqrt((abs(x1 * 32 - x2 * 32) ** 2) + (abs(y1 * 32 - y2 * 32) ** 2))
        math.floor(bools_way)
        bools_way = int(bools_way)
        for k in range(bools_way):
            print(k, x1, x2, y1, y2)
            print(((bools_way - k) - (abs(x1 * 32 - x2 * 32) - k)) * ((bools_way - k) + (abs(x1 * 32 - x2 * 32) - k)))
            b = math.sqrt(((bools_way - k) - (abs(x1 * 32 - x2 * 32) - k)) * ((bools_way - k) +
                                                                              (abs(x1 * 32 - x2 * 32) - k)))
            coords = int(math.floor(b))
            coords += y2
            coords1 = x1 - k
            glob_coords = [coords1, coords]
            if glob_coords in spis:
                return False
            elif glob_coords[0] < x2 * 32 and glob_coords[0] > (x2 * 32 - 32) \
                    and glob_coords[1] < y2 * 32 and glob_coords[1] > (y2 * 32 - 32):
                return True
        return False
