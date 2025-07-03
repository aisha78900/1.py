# finally chahy koi bhi condition ho chlta hi chlta hy 
#finally mainly function jb hm bnaty hen hmen tb 
# uski zrorat prti hy q ky
# agr hm esi print krwayengy tw print nahi hoga
# or han retrun jo hy wo agr wo return hogya tw 
# agy ka code nahi chlta lekin 
# finally isko over write kr ke chlta rehta hy 


def main():
    try:
        a = int(input("Enter numb: "))
        print(a) 
        
    except Exception as e:
        print(e)
        
    finally:
        print("fianlly")
        
main()