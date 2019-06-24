
class SelectionSort:
    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def sort(self):
        for i in range(self.length-1):
            min_data = self.array[i]
            min_index = i
            for j in range(self.length-i-1):
                if self.array[i+j+1] < min_data:
                    min_data = self.array[i+j+1]
                    min_index = i + j + 1
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]

    def sort_new(self):
        for i in range(self.length//2):
            min_data = self.array[i]
            max_data = self.array[i]
            min_index = i
            max_index = i
            for j in range(self.length-2*i-1):
                if self.array[i+j+1] < min_data:
                    min_data = self.array[i+j+1]
                    min_index = i + j + 1
                elif self.array[i+j+1] > max_data:
                    max_data = self.array[i+j+1]
                    max_index = i + j + 1

            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            self.array[self.length-i-1], self.array[max_index] = self.array[max_index], self.array[self.length-i-1]


if __name__ == '__main__':
    my_list = [4, 7, 6, 5, 3, 2, 11, 8, 1, 9, 10]
    selection_sort = SelectionSort(my_list)
    # selection_sort.sort()
    selection_sort.sort_new()
    print(selection_sort.array)

