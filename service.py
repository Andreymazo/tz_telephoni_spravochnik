def sort_single_file(nums, low, high, nomer):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        
        i += 1
        try:
            while nums[i][nomer] < pivot[nomer]:
                i += 1
        except IndexError:
            # i += 1
            pass

        j -= 1
        print('jjjjjjjjjjjjjjjjjj',j)
        # print('---------------------', nums[j][nomer])
        try:
            while nums[j][nomer] > pivot[nomer]:
                j -= 1
        except IndexError:
            # j -= 1
            pass

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums, nomer):
        def _quick_sort(items, low, high):
            if low < high:
                split_index = sort_single_file(items, low, high, nomer)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)

        _quick_sort(nums, 0, len(nums) - 1)

def binary_search(low, high, values, search_name, item_to_find):
    while low <= high:
        mid = low + (high - low) // 2
        # print('search_name', search_name)
        # print('mid', mid)
        # print(values[mid])
        try:
            if item_to_find == values[mid][search_name]:
                return mid
        except IndexError:
            print('here IndexError1')
        try:
            if item_to_find < values[mid][search_name]:
                high = mid - 1
        except IndexError:
            print('here IndexError2')
        try:

            if item_to_find > values[mid][search_name]:
                low = mid + 1
        except IndexError:
            print('here IndexError3')

    return 'No such name'