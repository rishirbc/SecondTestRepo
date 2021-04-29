listing = [10, 20, 5, 22, 30, 453, 99, 23]
n = int(input('Enter the element you need to search:'))
listing.sort()

def Bubble(listing, number):
    l = 0
    u = len(listing)
    while l < u:
        m = int((l + u) / 2)
        if listing[m] == number:
            return True, m
        else:
            if listing[m] < number:
                l = m + 1
            else:
                u = m - 1
    return False, False

ans, pos = Bubble(listing, n)
if ans == True:
    print('We found the element', n, 'by for while at position', pos + 1, '\n')
else:
    print('We cannot find the element', n, 'by while loop. \n')






