my_list = [2, 3, 4, 5, 6, 7, 8, 1]


def cock_tail_sort(l):
    outer_times = len(l) - 1

    for i in range(outer_times):
        is_sorted = True
        print(i)
        for j in range(outer_times - i):
            if i % 2 == 0:
                if l[j] > l[j + 1]:
                    l[j], l[j + 1] = l[j + 1], l[j]
                    is_sorted = False

            else:
                if l[outer_times - i - j] < l[outer_times - i - j - 1]:
                    l[outer_times - i - j], l[outer_times - i - j - 1] = l[outer_times - i - j - 1], l[
                        outer_times - i - j]
                    is_sorted = False

        if is_sorted:
            print(l)
            break


cock_tail_sort(my_list)
print(my_list)
