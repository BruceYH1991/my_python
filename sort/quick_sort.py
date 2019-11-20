import random

my_list = [4, 7, 6, 5, 3, 2, 11, 8, 1, 9, 10]


# def quick_sort(l):
#     pivot_index = random.randint(0, len(l)-1)
#     pivot = l[pivot_index]
#     # pivot = random.choice(l)
#     left_index = 0
#     right_index = len(l) - 1
#
#     if pivot > l[right_index]:
#         l[pivot_index] = l[right_index]
#         pivot_index = right_index
#         left_index += 1
#     else:
#         right_index -= 1


class QuickSortOld:
    def __init__(self, arr):
        self.arr = arr
        self.left = 0
        self.right = len(arr) - 1
        self.pivot = random.choice(arr)
        self.index = arr.index(self.pivot)

    def exchange_r(self):
        while self.pivot < self.arr[self.right]:
            self.right -= 1
            if self.right == self.left:
                break

        self.arr[self.index] = self.arr[self.right]
        self.index = self.right

    def exchange_l(self):
        # print(self.pivot)
        while self.pivot > self.arr[self.left]:
            # print(self.left)
            self.left += 1
            if self.left == self.right:
                break

        self.arr[self.index] = self.arr[self.left]
        self.index = self.left

    def sort(self):
        while self.right != self.left:
            if self.index != self.right:
                self.exchange_r()
                self.exchange_l()
            else:
                self.exchange_l()
                self.exchange_r()

        self.arr[self.index] = self.pivot

        return self.arr


class QuickSort:
    def __init__(self, array):
        self.array = array

    def sort(self, left, right):
        if right <= left:
            return

        index = self.exchange(left, right)
        self.sort(left, index - 1)
        self.sort(index + 1, right)

    def exchange(self, left, right):
        index = random.randint(left, right)
        pivot = self.array[index]
        while left < right:
            while pivot < self.array[right]:
                right -= 1
                if right == left:
                    break
            self.array[index] = self.array[right]
            index = right

            while pivot > self.array[left]:
                left += 1
                if left == right:
                    break
            self.array[index] = self.array[left]
            index = left

        self.array[index] = pivot

        return index

    def sort_new(self, left, right):
        if left >= right:
            return

        index = self.exchange_new(left, right)
        # print(self.array)
        self.sort_new(left, index - 1)
        self.sort_new(index + 1, right)

    def exchange_new(self, left, right):
        index = random.randint(left, right)
        # index = left
        pivot = self.array[index]

        while left < right:
            while left < right:
                if pivot <= self.array[right]:
                    right -= 1
                else:
                    break

            while left < right:
                if pivot >= self.array[left]:
                    left += 1
                else:
                    break

            self.array[left], self.array[right] = self.array[right], self.array[left]

        # if left == right:
        # 例外: 4,2,3 --> 2,4,3   l==r==0,index==2,p==3
        if index > right and self.array[index] > self.array[right]:
            self.array[index], self.array[right+1] = self.array[right+1], self.array[index]
            return right + 1
        elif index < left and self.array[index] < self.array[left]:
            self.array[index], self.array[left-1] = self.array[left-1], self.array[index]
            return left - 1
        else:
            self.array[index], self.array[right] = self.array[right], self.array[index]

        return left


if __name__ == '__main__':
    # quick_sort_old = QuickSortOld(my_list)
    # print(quick_sort.pivot)
    # print(quick_sort.index)
    # sorted_list_old = quick_sort_old.sort()
    # print(sorted_list_old)
    # print(quick_sort.index)

    quick_sort = QuickSort(my_list)
    quick_sort.sort_new(0, len(my_list) - 1)
    # quick_sort.sort(0, len(my_list)-1)
    print(quick_sort.array)
