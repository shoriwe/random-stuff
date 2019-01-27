map1 = [['x', -1, -1, -1, -1],
        [0, 1, 0, 0, 0],
        [-1, -1, -1, 0, -1],
        [0, 0, 0, 0, -1],
        [0, -1, -1, -1, -1]]

map2 = [[0, -1, -1, -1, -1],
        [0, 1, 0, 0, 0],
        [-1, -1, -1, 0, -1],
        [0, 0, 0, 0, -1],
        ['x', -1, -1, -1, -1]]

map3 = [[0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 'x', 0, 0, -1],
        [0, 0, 0, 0, -1],
        [0, -1, -1, -1, -1]]

map4 = [[ 1,'x',  0,  0],
        [ 0,  0,  0,'x'],
        [ 0,  0,  0,'x'],
        [ 0,  0,  0,'x']]


def better_set(iterable: iter):
    new = []
    for n in iterable:
        if n not in new:
            new.append(n)
    return new


class PathFinder:
    def __init__(self, map_):
        self.map = map_
        self.actual_number = 1
        self.actual_location = list(self.determine_start_cordenates())
        self.routes = [self.actual_location]
        self.number_of_x = []

    def determine_start_cordenates(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == self.actual_number:
                    yield [y, x]

    def determine_near(self):
        func = lambda y,x: ([y, x - 1], [y, x + 1], [y - 1, x], [y + 1, x])
        for location in self.actual_location:
            for n in func(*location):
                try:
                    if self.map[n[0]][n[1]] in ['x', 0] and -1 not in n:
                        yield n
                except Exception as e:
                    pass

    def change(self, locations):
        stop = True
        next_number = self.actual_number + 1
        for location in locations:
            try:
                if self.map[location[0]][location[1]] != 'x':
                    self.map[location[0]][location[1]] = next_number
                    stop = False
                else:
                    if location not in self.number_of_x:
                        self.number_of_x.append(location)
                        stop = False
            except:
                pass
        self.actual_number = next_number
        return stop

    def solve(self):
        while True:
            self.actual_location = self.determine_start_cordenates()

            near = better_set(self.determine_near())
            if self.change(near):
                break

        print('Final map')
        for line in self.map:
            print(line)
        print()
        print('Last step',self.actual_number-1)
        print()
        print('n of x found', len(self.number_of_x))
        print()

print('Analysing')
pf = PathFinder(map1)
x = pf.solve()