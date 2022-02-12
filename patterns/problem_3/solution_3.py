n = int(input())
print("  " * (n) + " 1")
print("  " * (n-1) +" 1" + " " * (n-2) + "1")
for i in range(1, n+1):
    if i >= 2:
        for j in range(i+1):
            c = ""
            c += str(j)
        if i <= 2:
            b = "  " * (n - i) + " 1" + " " * 3 + c + " " * (i) + "1"
            print(b)
        if i > 2:
            b = "  " * (n - i) + " 1" + " " * 3 + c + " " * i + c + " 1"
            print(b)