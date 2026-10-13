def left_rotate(n):
    arr = [1, 2, 3, 4, 5]
    n = n % len(arr)
    return arr[n:] + arr[:n]

input("left_rotate(n) shifts [1, 2, 3, 4, 5] left by n position, press enter ")
print(" left_rotate(1) =", left_rotate(1))
print(" left_rotate(2) =", left_rotate(2))
n = int(input("Rotate by how many? "))
guess = input("What is left_rotate(" + str(n) + ")? ")
input("slice from index n to end, then attach the first n elements, press enter ")
print(" (" + str(n) + ") =", left_rotate(n), " your guess:", guess)