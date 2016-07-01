



def find_consecutive_answers(listo):
    ab = 0
    temp = []

    while ab < len(listo)-1:


        #check if goes up
        if int(listo[ab]) == int(listo[ab+1])-1:

            ac = ab
            x = ab
            while ac < len(listo)-1:
                found = False
                if int(listo[ac]) == int(listo[ac+1])-1:
                    found = True
                    ac = ac + 1
                    ab = ac-1

                else:
                    temp.append(x)
                    ab = ac-1
                    ac = len(listo)-1

            if found:
                temp.append(x)

        #check if goes down
        if int(listo[ab]-1) == int(listo[ab+1]):

            ac = ab
            x = ab
            while ac < len(listo)-1:
                found = False
                if int(listo[ac]-1) == int(listo[ac+1]):
                    found = True
                    ac = ac + 1
                    ab = ac-1

                else:

                    temp.append(x)
                    ab = ac-1
                    ac = len(listo)-1

            if found:
                temp.append(x)


        ab = ab + 1
    #return is index
    return temp

