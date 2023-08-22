def sort_single_file(nums, low, high, nomer):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i][nomer] < pivot[nomer]:
            i += 1

        j -= 1
        while nums[j][nomer] > pivot[nomer]:
            j -= 1

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

def binary_search(low, high, values, item_to_find):
    while low <= high:
        mid = low + (high - low) // 2

        if item_to_find == values[mid][0]:
            return mid
        elif item_to_find < values[mid][0]:
            high = mid - 1
        elif item_to_find > values[mid][0]:
            low = mid + 1

    return 'No such name'