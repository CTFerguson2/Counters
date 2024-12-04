

class FlipFlop:
    def __init__(self):
        self.style = ""
        self.indices = 0

    def map(self, q, q_star):
        pass


class JK(FlipFlop):
    def __init__(self):
        super().__init__()
        self.style = "JK"
        self.indices = 2

    def map(self, q, q_star):
        match q, q_star:
            case 0, 0:
                return 0, -1
            case 0, 1:
                return 1, -1
            case 1, 0:
                return -1, 1
            case 1, 1:
                return -1, 0
            case _:  # Return dontcares if an input is a dontcare
                return -1, -1


class D(FlipFlop):
    def __init__(self):
        super().__init__()
        self.style = "D"
        self.indices = 1

    def map(self, q, q_star):
        return tuple([int(q_star)])


class SR(FlipFlop):
    def __init__(self):
        super().__init__()
        self.style = "SR"
        self.indices = 2

    def map(self, q, q_star):
        match q, q_star:
            case 0, 0:
                return 0, -1
            case 0, 1:
                return 1, 0
            case 1, 0:
                return 0, 1
            case 1, 1:
                return -1, 0
            case _:  # Return dontcares if an input is a dontcare
                return -1, -1


class T(FlipFlop):
    def __init__(self):
        super().__init__()
        self.style = "T"
        self.indices = 1

    def map(self, q, q_star):
        return tuple([int(q != q_star)])

