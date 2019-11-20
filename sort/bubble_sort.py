l = [5, 8, 6, 3, 9, 2, 1, 7]


class BubbleSort:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1
        self.is_sorted = True
        self.last_exchange_index = 0

    def change_beside(self, _id):
        if self.data[_id] > self.data[_id + 1]:
            self.data[_id], self.data[_id + 1] = self.data[_id + 1], self.data[_id]
            self.is_sorted = False
            self.last_exchange_index = _id

    def once_sort(self, last_index):
        for i in range(last_index):
            self.change_beside(i)
        self.index = self.last_exchange_index - 1

    def main(self):
        if_go = True
        last_index = self.index
        while if_go:
            self.once_sort(last_index)
            if self.index < 0:
                if_go = False
            if self.is_sorted:
                break
            last_index = self.last_exchange_index
        return self.data


bs = BubbleSort(l)
has_sorted = bs.main()
print(has_sorted)
