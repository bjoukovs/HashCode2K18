class Ride:

    def __init__(self, a, b, x, y, s ,f, _id):
        self.start_inter_row = a
        self.start_inter_col = b
        self.end_inter_row = x
        self.end_inter_col = y
        self.earliest_start = s
        self.latest_finish = f
        self.id = _id

    def distance(self):
        return abs(self.start_inter_col - self.end_inter_col) + \ 
                abs(self.start_inter_row - self.end_inter_row)
