
def sift_down(data, i, swaps):
    min_index = i
    left = 2 * i + 1
    if left < len(data) and data[left] < data[min_index]:
        min_index = left
    right = 2 * i + 2
    if right < len(data) and data[right] < data[min_index]:
        min_index = right
    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        sift_down(data, min_index, swaps)

def build_heap(data):
    swaps = []
    for i in range(len(data) // 2, -1, -1):
        sift_down(data, i, swaps)
    return swaps


def main(): 
    n = int(input())
    data = list(map(int, input().split()))
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
