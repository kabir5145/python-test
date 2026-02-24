# Q - 2 Exceptions
t = int(input())

for _ in range(t):
    a, b = input().split()

    try:
        print(int(a) // int(b))  # IMPORTANT: use //
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)