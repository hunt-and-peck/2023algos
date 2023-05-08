n, m = map(int, input().split())
daily = list(int(input()) for _ in range(n))
lt = min(daily)
rt = sum(daily)

while lt <= rt:
    mid = (lt + rt) // 2		
    charge = mid	
    num = 1	
    for i in range(n):	
        if charge < daily[i]:
            charge = mid
            num += 1
        charge -= daily[i]	

    if num > m or mid < max(daily):	
        lt = mid + 1
    else:		
        rt = mid - 1
        k = mid		

print(k)

#출처: https://velog.io/@deannn/BOJ-%EB%B0%B1%EC%A4%80-6236-%EC%9A%A9%EB%8F%88%EA%B4%80%EB%A6%AC-Python
