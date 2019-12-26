class Move:
    def way(self, spis, x1, y1, x2, y2):
        lab = []
        ss = []
        if abs(x2 - x1) > 4 or abs(y2 - y1) > 4:
            return False
        else:
            for h in range(9):
                for b in range(9):
                    if [(y1 - 4) + h, (x1 - 4) + b] not in spis:
                        ss.append(0)
                    elif [(y1 - 4) + h, (x1 - 4) + b] in spis:
                        ss.append(-1)
                lab.append(ss)
                ss = []
            x2 = x2 - x1 + 4
            y2 = y2 - y1 + 4
            x1 = 4
            y1 = 4
            lab = self.voln(x1, y1, 1, 9, 9, lab)
            if lab[y2][x2] > 0 and lab[y2][x2] <= 5:
                print(lab)
                return True
            else:
                return False

    def voln(self, x, y, cur, n, m, lab):
        lab[x][y] = cur
        if y + 1 < m:
            if lab[x][y + 1] == 0 or (lab[x][y + 1] != -1 and lab[x][y + 1] > cur):
                self.voln(x, y + 1, cur + 1, n, m, lab)
        if x + 1 < n:
            if lab[x + 1][y] == 0 or (lab[x + 1][y] != -1 and lab[x + 1][y] > cur):
                self.voln(x + 1, y, cur + 1, n, m, lab)
        if x - 1 >= 0:
            if lab[x - 1][y] == 0 or (lab[x - 1][y] != -1 and lab[x - 1][y] > cur):
                self.voln(x - 1, y, cur + 1, n, m, lab)
        if y - 1 >= 0:
            if lab[x][y - 1] == 0 or (lab[x][y - 1] != -1 and lab[x][y - 1] > cur):
                self.voln(x, y - 1, cur + 1, n, m, lab)
        return lab