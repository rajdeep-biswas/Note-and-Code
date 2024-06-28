# stole the idea from twosum. did a 'sorted' hack to make smaller appears element first so that i can just set() them at the end

def solution(k, a):
    
    numbers = []
    
    two_sum = {}
    
    for i in range(len(a)):
        if a[i] in two_sum:
            numbers.append(tuple(sorted([a[i], a[two_sum[a[i]]]])))
        two_sum[k - a[i]] = i
        
    return len(set(numbers))