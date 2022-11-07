def binarySearch(lower,upper,k):
    guess = 1
    count = 0
    while guess != k:
        guess = int((lower + upper) / 2)
        print("New guess is ", guess)
        count += 1
        if guess>k:
            upper = guess - 1
        elif guess<k:
            lower = guess + 1
        else:
            break
    return count

lower = input("enter lower bound")
upper = input("enter upper bound")
k = input("enter key to be searched")

print(binarySearch(lower,upper,k))

