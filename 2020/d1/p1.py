def solution(file):
    n = []
    with open(file) as f:
        for line in f:
            line = line.strip()
            n.append(int(line))
    for i in range(len(n)):
        for j in range(i, len(n)):
            if n[i] + n[j] == 2020:
                return n[i] * n[j]
    return 0


if __name__ == '__main__':
    result = solution('input1.txt')
    print(result)