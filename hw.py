scores = [10, 20, 30, 40, 50, 60, 70]

reverse_scores = scores.copy()
start = 0
end = len(reverse_scores) - 1
while start < end:
    reverse_scores[start], reverse_scores[end] = reverse_scores[end], reverse_scores[start]
    start += 1
    end -= 1
print("Original Scores:", scores)
print("Reversed Scores:", reverse_scores)

group_scores = scores.copy()
k = 3
i = 0
while i < len(group_scores):
    start = i
    end = min(i + k - 1, len(group_scores) - 1)
    while start < end:
        group_scores[start], group_scores[end] = group_scores[end], group_scores[start]
        start += 1
        end -= 1
    i += k
print("Group Size:", k)
print("Result:", group_scores)

rotate_one = scores.copy()
first = rotate_one[0]
for i in range(len(rotate_one) - 1):
    rotate_one[i] = rotate_one[i + 1]
rotate_one[-1] = first
print("Result:", rotate_one)

rotate_n = scores.copy()
n = 2
n = n % len(rotate_n)
for _ in range(n):
    first = rotate_n[0]
    for i in range(len(rotate_n) - 1):
        rotate_n[i] = rotate_n[i + 1]
    rotate_n[-1] = first
print("n =", n)
print("Result:", rotate_n)


leader_scores = [16, 17, 4, 3, 5, 2]
leaders = []
max_right = leader_scores[-1]
leaders.append(max_right)
for i in range(len(leader_scores) - 2, -1, -1):
    if leader_scores[i] > max_right:
        leaders.append(leader_scores[i])
        max_right = leader_scores[i]
leaders.reverse()
print("Scores:", leader_scores)
print("Leaders:", leaders)