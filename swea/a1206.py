T = 10

for j in range(1, T+1):
    N = int(input())
    h = list(map(int, input().split()))
    h_zip = []
    result = 0

    for i in range(2, len(h)-2):
        h_zip = (h[i-2:i+3])
    
        if h_zip[2] == max(h_zip):
            h_zip.sort(reverse=True)
            result += (h_zip[0]-h_zip[1])
         

    print(f"#{j} {result}")