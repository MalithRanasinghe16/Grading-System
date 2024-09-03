#variables
marks = [0,20,40,60,80,100,120]
progress = 0
moduel_trailer = 0
exclude = 0
do_not_progress=0
total = 120
new_list = []
newlist = ()
st_id_list = []
dict = {}
loop = True

while loop == True:
    #student id
    while True:
        try:
            st_id = int(input("Enter the student ID number:"))
            break
        except:
            print("Sorry.. Enter only integers ")

    try:
        #enter pass credit
        pass_credit = int(input("Enter the pass credit: "))
        if pass_credit in marks:
            try:
                #enter defer credit
                defer_credit = int(input("Enter the Defer credit: "))
                if defer_credit in marks:
                    try:
                        #enter fail credit
                        fail_credit = int(input("Enter the Fail credit: "))
                        if fail_credit in marks:
                            total = pass_credit + defer_credit + fail_credit
                            # total
                            if total == 120:
                                    #check progress
                                if pass_credit == 120 and defer_credit == 0 and fail_credit == 0:
                                    outcome = "Progress"
                                    progress += 1
                                    #check moduel trailer
                                elif pass_credit == 100 and defer_credit == 20 or pass_credit == 100 and fail_credit == 20:
                                    outcome = "Moduel trailer"
                                    moduel_trailer += 1
                                    #check exclude
                                elif fail_credit in (80,100,120):
                                    outcome = "Exclude"
                                    exclude += 1
                                    #otherwise do not progress
                                else:
                                    outcome = "Do not progress"
                                    do_not_progress += 1

                                st_id_list.append(st_id)
                                new_list = (outcome, ' => ','PASS =', pass_credit, ' , ', 'DEFER = ',defer_credit, ' , ','FAIL =', fail_credit)
                                newlist = list(new_list)
                                dict[st_id]= newlist


                            else:
                                print("Total incorrect")
                        else:
                            print("out of range")#o_o_r 3
                    except:
                        print("integer required ")#i_r 3
                else:
                    print("out of range")#o_o_r2
            except:
                print("integer required ")#i_r 2
        else:
            print("out of range ")#o_o_r 1
    except:
        print("integer required ")#i_r 1
    print("would you like to enter another data ")
    loop = input("Enter 'y' for yes or enter 'q' for quit to see results: ").lower()
    if loop == "y":      #y for yes
        loop = True
    elif loop == "q":        #q for quit
        loop = False
        # printing the histogram
        print()
        print("-------------------------------------------------------------------------------------------------------------------------")
        print('Histogram')
        print()
        print('Progress', progress, ' : ', end=' ')
        for i in range(progress):
            print("*", end=' ')
        print()
        print('Progress(module trailer)', moduel_trailer, ' : ', end=' ')
        for i in range(moduel_trailer):
            print("*", end=' ')
        print()
        print('Do not progress (module retriever)', do_not_progress, ' : ', end=' ')
        for i in range(do_not_progress):
            print("*", end=' ')
        print()
        print('Exclude', exclude, ' : ', end=' ')
        for i in range(exclude):
            print("*", end=' ')
        print()
        print(f'Total outcome is {len(st_id_list)}')
        print()
        print("----------------------------------------------------------------------------------------------------------------------------")
        print('printing the Dictionaries')
        i = 0
        for i in range(len(st_id_list)):
            x = int(str(st_id_list[i]))
            OP = dict.get(x)
            print(x, " : ", *OP)










