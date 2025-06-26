# ek character ko ek word me se remove krna hy jo sary items hen list men sb me se remove hojaye

def remove_character(l, word):
    n = []                          #  Step 1: n list banayi
    for item in l:                  #  Step 2: list loop start
        if not(item == word):       #  Step 3: agar item "an" nahi hai
            n.append(item.strip(word))  #  Step 4: word ko strip karo aur n me daalo
    return n                        #  Step 5: loop ke baad final n return karo


# agr hmen ek condition pr kuch check krna hy tw if menor agr hmen sbko dekhna hy tw for me 