n = int(input())

arr = [[int(item) for item in input().split()] for _ in range(n)]

max_num = arr[0][0]
for i in range(n):
	for j in range(n):
		if i >= j:
			max_num = max(max_num, arr[i][j])

print(max_num)
