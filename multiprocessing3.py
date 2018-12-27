import multiprocessing


def calc_square(numbers, result):
    # v.value = 5.67
    for idx, n in enumerate(numbers):
        result[idx] = n*n

if __name__ == "__main__":
    numbers = [2, 3, 5]
    result = multiprocessing.Array('i', 3)
    v = multiprocessing.Value('d', 0.0)
    p = multiprocessing.Process(target=calc_square, args=(numbers))
    print("result", result)
    print("v", v)

    p.start()
    p.join()

    print(v.value)
