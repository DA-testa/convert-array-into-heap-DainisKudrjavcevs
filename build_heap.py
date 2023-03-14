
def keyboard():
    n = input().strip()

    if n:
        parents = input().strip().split(" ")
        if parents:
            return n, parents

    return None, None


def file(filename):
    try:
        with open(f"./test/{filename}") as f:
            contents = f.readlines()
    except FileNotFoundError:
        print("File not found")
        return None, None
    except:
        print("Error reading file")
        return None, None
    
    n = contents[0].strip()
    if not n:
        print("Invalid input: n not provided")
        return None, None
    
    parents = contents[1].strip().split(" ")
    if not parents:
        print("Invalid input: parents not provided")
        return None, None
    
    return n, parents


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


def compute_height(n, parents):
    root = parents.index("-1")
    tree = {}
    for i, parent in enumerate(parents):
        if i != root:
            if parent in tree:
                tree[parent].append(i)
            else:
                tree[parent] = [i]
    height = 0
    queue = [(root, 0)]
    while queue:
        node, level = queue.pop(0)
        height = max(height, level)
        if node in tree:
            for child in tree[node]:
                queue.append((child, level + 1))
    return height + 1


def main():
    input_method = input().strip()

    if input_method == "I":
        n, parents = keyboard()
        if n and parents:
            height = compute_height(n, parents)
            print(int(height))

    elif input_method == "F":
        filename = input().strip()
        if str(filename[-1]) != "a":
            n, parents = file(filename)
            if n and parents:
                height = compute_height(n, parents)
                print(int(height))
        else:
            n, data = None, []
            with open(f"./test/{filename}") as f:
                n = int(f.readline().strip())
                data = list(map(int, f.readline().strip().split()))
            swaps = build_heap(data)
            print(len(swaps))
            for i, j in swaps:
                print(i, j)

if __name__ == "__main__":
    main()