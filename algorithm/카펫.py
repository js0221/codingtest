# solution 1
def solution(brown, yellow):
    if yellow == 1:
        return [3,3]
    
    for i in range(1, yellow//2+1):
        if yellow % i == 0:
            yx, yy = yellow // i, i
            if 2*(yx+yy)+4 == brown: 
                return [yx+2, yy+2]
                

# solution 2
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]


# solution 3
def solution(brown, red):
    pair = []
    for i in range(1, (red // 2) + 2):
        a, b = divmod(red, i)
        if b == 0 and a >= i:
            pair.append((a, i))
            
    for x, y in pair:
        if 2 * (x + y + 2) == brown:
            return [x + 2, y + 2]


# solution 4
def solution(brown, red):
    width = (brown + red) // 3
    height = 3
    
    while (width - 2) * (height - 2) != red:
        width -= 1
        height = (brown + red) // width
    
    return [width, height]
