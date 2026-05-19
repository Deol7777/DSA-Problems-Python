def isPalindrome(s: str) -> bool:

    i = 0
    j = len(s)-1
    while(i < j):
        if not s[i].isalnum():
            i+=1
        elif not s[j].isalnum():
            j-=1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i+=1
            j-=1
    return True

    
    
    return True


def main():
    # Your program's logic goes here
    tests = ["A man, a plan, a canal: Panama", "race a car", "", "0P"]

    for t in tests:
        print(f'"{t}" ->', isPalindrome(t))

    a = "ab3cd"
    for i in a:
        print(i + "->" + str(i.isalnum()))


if __name__ == "__main__":
    main()