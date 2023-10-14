# def isPalindrome(x):
#     # x- ədəd
#     # Tələblər:
#     # Daxil edilən `x` ədədinin palindrom olub olmadığını yoxlayın.Yəni sağdan sola və soldan sağa oxuyanda eyni olmalıdır. Məsələn 121, 12321, 1001, 111 və s.
#     pass


# def isPalindrome(x):
#     x = x.lower()
#     x_reversed = x.reverse()
#     if x == x_reversed:
#         print("Palindromdu")
#     else:
#         print("Palindrom deyil")

# x = input("Input: ")
# isPalindrome(x)

def isPalindrome(x):
    x = x.lower()
    # x_low = x.lower()
    x_reverse = x[::-1]

    if x == x_reverse:
        print("Polindromdur")
    else:
        print("Polindrom deyildir")


x = input("Daxil edin: ")
isPalindrome(x)
