import sys


def heap_sort(nums):
 
    def build_heap(n):
        half = (n - 1) // 2
        for i in range(half, n):
            sift_down(n - i - 1, n - 1)
    
    def sort_heap(n):
        size = n - 1
        while size >= 1:
            nums[0], nums[size] = nums[size], nums[0]
            size = size - 1
            sift_down(0, size)

    def sift_down(index, size):
        
        while index < size:
            max_index = index
            left_child = 2 * index + 1
            right_child = 2 * index + 2

            if left_child <= size and nums[max_index] <= nums[left_child]:
                max_index = left_child

            if right_child <= size and nums[max_index] <= nums[right_child]:
                max_index = right_child
            
            if max_index == index:
                break

            nums[max_index], nums[index] = nums[index], nums[max_index]
            index = max_index

    n = len(nums)
    build_heap(n)
    sort_heap(n)
    
    return nums


def main():
    data = sys.stdin.readline()
    nums = list(map(int, data.split()))
    print(heap_sort(nums))


if __name__ == '__main__':
    main()