import numpy as np

class Matrix:

    def __init__(self):
        self.matrix = np.full((3,3), " ")

    def reset(self):
        self.matrix = np.full((3,3), " ")

    def add_token(self, token, num):
        axis0 = (num - 1) // 3
        axis1 = (num - 1) % 3
        self.matrix[axis0, axis1] = token

    def check_diag(self):
        main_diag = np.diag(self.matrix)
        anti_diag = np.fliplr(self.matrix).diagonal()

        for row in [main_diag, anti_diag]:
            if (len(np.unique(row)) == 1 and row[0] != ' '):
               return True

    def check_axis(self):
        for axis in range(2):
            for i in range(3):
                row = np.take(self.matrix, i, axis=axis)
                if (len(np.unique(row)) == 1 and row[0] != ' '):
                    return True

    def get_token(self, num):
        axis0 = int((num - 1) / 3)
        axis1 = int((num - 1) % 3)
        return self.matrix[axis0, axis1]