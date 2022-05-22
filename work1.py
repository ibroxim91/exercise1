

def parking_attendant(white,red):
    if not isinstance(white,int) and isinstance(red,int):
        raise ValueError("Значения должны быть только числами")
    max_ = max(white,red) 
    min_ = min(white,red) 
    c = max_ - min_
    if c > white or c > red:
        return "Нет решения"
    if max_ == white: 
        more, length_more = "W" ,white 
        less,length_less = "R" ,red
    else:
        more, length_more = "R" ,red 
        less,length_less = "W" ,white   
    if max_ == 2 and min_ == 1:
        return f"{more}{less}{more}"
    res = []
    for i in range(1,length_less + 1):
        res.extend([less,more,more])
        length_more -= 2
        length_less -= 1
        if length_more == 2:
            res.insert(0,more)
            res.append(less) ;length_less -= 1
            res.append(more); length_more -= 2
            if length_less:
                res.append(less)
            break
        elif length_more == 1:
            res.insert(0,more);length_more -= 1
            res.append(less);length_less -= 1
            if length_less:
                res.insert(0,less)
            break
    return "-".join(res)        
        
res = parking_attendant(white=9,red=5)
print(res)    
  
