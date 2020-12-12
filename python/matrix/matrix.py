class Matrix:
    def __init__(self, matrix_string):
        self.m = y = [list(map(int, e.split())) 
                        for e in matrix_string.splitlines()]

    def row(self, index):
        return self.m[index-1] 

    def column(self, index):
        return list(list(zip(*self.m))[index-1])
