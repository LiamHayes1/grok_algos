
def sum(arr):
    if (arr == []):
        return 0
    return arr[0] + sum(arr[1:])

def count(arr):
    if (arr == []):
        return 0
    return 1 + count(arr[1:])

def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print('sum: ' + str(sum([1,2,3,4])))
print('count: ' + str(count([1,2,3,4])))
print('max: ' + str(max([1,2,6,3,4])))