def solution(array_a, array_b):
    sol = 0
    for i in range(len(array_a)):
        sol += abs(array_a[i] - array_b[i]) ** 2
    return sol / len(array_a)