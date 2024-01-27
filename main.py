def max(x1,x2,x3):
    mav = x1
    if x2 > mav:
        mav = x2
    if x3 > mav:
        mav = x3
    return mav

print(max(666, 1 , 0))
