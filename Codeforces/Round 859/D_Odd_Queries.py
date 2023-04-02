from operator import add


def is_odd(n):
    if n%2!=0:
        return True
    return False

for tc in range(int(input())):
    n, q =  map(int, input().split())
    arr = list(map(int, input().split()))
    
    for i in range(q):
        l, r, k = map(int, input().split())
        if ((l==1)) and (r==n):
            if is_odd((r-l+1)*k):
                print("YES")
            else:
                print("NO")
        else:
            is_k_sum_odd = is_odd((r-l+1)*k)
            t = arr[:l-1]
            if r < n:
                for element in arr[r:]:
                    t.append(element)
            is_remaining_sum_odd = is_odd(sum(t))

            if is_k_sum_odd and is_remaining_sum_odd:
                print("NO")
            elif (not is_k_sum_odd) and (not is_remaining_sum_odd):
                print("NO")
            else:
                print("YES")
