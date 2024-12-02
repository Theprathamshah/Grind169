arr = list(map(int,input().split()))
print(arr)

minSoFar = arr[0]
ans = -1
for i in arr:
    ans = max(ans,i-minSoFar)
    minSoFar = min(minSoFar,i)

print(f"most profit from stock is {ans}")    