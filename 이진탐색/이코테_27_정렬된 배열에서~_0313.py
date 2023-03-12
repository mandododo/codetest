import sys

def countValue(arr, target):
    first = 0
    last = len(arr)-1

    start = findFirstIndex(arr, target, first, last)
    if start == None:
        return 0
    end = findLastIndex(arr, target, first, last)
    return end - start + 1


def findFirstIndex(arr, target, first, last):
    if first > last:
        return None
    mid = (first + last) // 2
    if (mid == 0 or arr[mid - 1] < target) and target == arr[mid]:
        return mid
    elif arr[mid] < target:
        return findFirstIndex(arr, target, mid + 1, last)
    elif arr[mid] >= target:
        return findFirstIndex(arr, target, first, mid - 1)


def findLastIndex(arr, target, first, last):
    if first > last:
        return None
    mid = (first + last) // 2
    if (mid == n - 1 or arr[mid + 1] > target) and target == arr[mid]:
        return mid
    elif arr[mid] <= target:
        return findLastIndex(arr, target, mid + 1, last)
    else:
        return findLastIndex(arr, target, first, mid - 1)


n, x = map(int, input().split())
array = list(map(int, input().split()))
count = countValue(array, x)
if count == 0:
    print(-1)
else:
    print(count)