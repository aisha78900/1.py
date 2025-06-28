import random 

def game():
    print("you are playing tha game ")
    score = random.randint(1 , 62)
    print(f"your score: {score}")
    #fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read() 
        if(hiscore !=""): # agr ye ek empty string nahi hy tw isko int me kr do taky baad me hm compare kr sken
            hiscore = int(hiscore)
        else:
            hiscore = 0
    if(score>hiscore ): #write hiscore ko file
     with open("hiscore.txt" , "w") as f:
        f.write(str(score)) #File ke andar hiscore wali value likh do.


    return score

game()


# smjh gai sb se pehly hm ek score variable bnaya
# phr hmne ek file bnai hicore ki ab hmne ek variable 
# bnaya hiscore name ka jo file read kr rha hy agr tw
# value hicore varaibale ki khali 
# nahi hy tw usko int bna do or agr khali hy tw zero. 
# phr hmne ek or condition di ke agr 
# hmara score high agr score se bra hy tw tm hiscre ki file kholo or usmen
# tm score ko as string print krwa do 