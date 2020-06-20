SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

#-----------------------------------    Manual Input -------------------------------------------------------------------------- 135 - 143

obj_func_selec = 1      #     Input for Kind of problem
obj_func_ = "-3 + 1"    #     Input for Objective Function

#-----------------------------------    Manual Input -------------------------------------------------------------------------- 193 - 202, 203 - 211
constraint = {}
no = 2
constraint['const_0'] = "+1+2-3<=10"
constraint['const_1'] = "+1+2+4<=10"


def signChange(lst):

    # if op == 0:
        for i in range(0,len(lst)):
            lst[i] = (lst[i]) * -1

        return lst 

    # elif op == 1:
        #     for i in range(0,len(lst)):
        #         lst[i] = str(int(lst[i]) * -1)

        #     return lst 

def signedIntegerAppend(temp_list):
    permanent_list = []
    temp = ""
    i = 0

    while i < len(temp_list):
        # temp = temp_list[i] + temp_list[i + 1]
        # obj_func_list.append("{}".format(temp))
        
        if i == 0:
            temp += temp_list[i]

        elif not temp_list[i] in ['+','-']:                 
            temp += temp_list[i]

        else:          
            permanent_list.append(int(temp))
            temp = ""
            temp += temp_list[i]

        i += 1
        if i == len(temp_list):
            permanent_list.append(int(temp))

    return permanent_list

def ProblemStmt():
    strng = ""
    # SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    # SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

    if obj_func_selec == 1:
        strng = "Max z = "
    else:
        strng = "Max z'= "

    temp = ""
    for i in range(len(obj_func_list)):
        temp += "%+dx%s"%( obj_func_list[i], str((i+1)).translate(SUB) )

    strng += temp

    for i in range(no):
        temp = alt_constraint["const_{}".format(i)]
        temp = (temp[ (len(temp)) - 2 ])
        if temp > 0:
            temp = 'S%s'%( str((i+1)).translate(SUB) ) 
            strng += '+0' + temp
        else:
            temp = 'S%s'%( str((i+1)).translate(SUB) ) 
            strng += '-0' + temp


    print("\n\033[4mProblem Statement\033[0m")

    print("\t"+strng)
    print("\t\tSubject To,")

    
    for i in range(no):
        temp2 = []
        extrastrng = ""
        count = 0
        temp = constraint["const_{}".format(i)]

        for j in temp:
            
            if not j in ['<','>']:
                temp2.append(j)
                count += 1
            else:
                break

        # while count < len(temp):
            #     extrastrng += temp[count]
            #     if extrastrng[count] == '<':
            #         extrastrng[count] = 'S%s'%( str((i+1)).translate(SUB) )
            #     else:
            #         extrastrng[count] = '-S%s'%( str((i+1)).translate(SUB) )
            #     count += 1

        while count < len(temp):

            if temp[count] == '<':
                extrastrng += '+S%s'%( str((i+1)).translate(SUB) )
                count += 1
                continue
            elif temp[count] == '>':
                extrastrng += '-S%s'%( str((i+1)).translate(SUB) )
                count += 1
                continue

            extrastrng += temp[count]
            count += 1

        temp2 = signedIntegerAppend(temp2)

        temp = ""
        for k in range(len(temp2)):
            temp += "%+dx%s"%( temp2[k], str((k+1)).translate(SUB) )

        temp += extrastrng
        print("\t\t\t",temp)


# ------------------------------ Objective Function Input ------------------------------

# print("\n(+) Select the kind of problem \n   1. Maxz \t 2. Minz")
# obj_func_selec = int(input("\nEnter Your Option : "))
# print()

# obj_func_ = str(input("""\n       -> Enter The Objective Function
#           \033[4mExample :\033[0m
#       \t     ▶ If your objective function is \" Maxz = -3x1 + x2 \" 
#       \t     ▶ Then you have to enter \" -3 + 1 \" 
#       \n\t         =>   """))






obj_func_ = obj_func_.replace(' ','')

if obj_func_[0] != '+' and obj_func_[0] != '-':
    obj_func_ = '+' + obj_func_

obj_func_ = obj_func_.replace(' ','')
obj_func_list_temp = []
obj_func_list = []

for i in obj_func_:
    obj_func_list_temp.append(i)

# for i in range(0,len(obj_func_list_temp)):
    # temp = ""
    # i = 0
    # while i < len(obj_func_list_temp):
    #     # temp = obj_func_list_temp[i] + obj_func_list_temp[i + 1]
    #     # obj_func_list.append("{}".format(temp))  [ +,2,+, 8, -,3,8, +, 2,]
        
    #     if i == 0:
    #         temp += obj_func_list_temp[i]

    #     elif not obj_func_list_temp[i] in ['+','-']:                 
    #          temp += obj_func_list_temp[i]

    #     else:          
    #         obj_func_list.append(int(temp))
    #         temp = ""
    #         temp += obj_func_list_temp[i]

    #     i += 1
    #     if i == len(obj_func_list_temp):
    #         obj_func_list.append(int(temp))


obj_func_list = signedIntegerAppend(obj_func_list_temp)

if obj_func_selec == 2:
    obj_func_list = signChange(obj_func_list)

del obj_func_list_temp
del obj_func_

# ------------------------------ Constraint Input ------------------------------

# no = int(input("\n(+) Enter number of constraints to be entered : "))

# print("""\n     -> Enter The Constraints
#             \033[4mExample :\033[0m
#         \t     ▶ If your constraint is \" x1 + 2x2 <= 10 \" 
#         \t     ▶ Then you have to enter \" 1 + 2 <= 10 \" """)

# constraint = {}
alt_constraint = {}

# for i in range(no):
#     const_ = str(input("        \n\t         =>   "))

#     const_ = const_.replace(' ','')

#     if const_[0] != '+' and const_[0] != '-':
#         const_ = '+' + const_

#     constraint["const_{}".format(i)] = const_
    
# print(obj_func_list)

# print(constraint)

#---------------------------------------------------- Solution --------------------------------------------------------------------------


for i in range(no):  # Converting string to int and removing unessary data from the constraints

    temp = constraint["const_{}".format(i)]
    index = temp.index('=')
    index += 1

    if temp[index] not in ['+','-']:
        temp = temp[ : index] + '+' + temp[ index : ]

    temp_constraint = []
    temp2_constraint = []

    for k in temp:
        temp_constraint.append(k)
    
    if '<' in temp_constraint:
        index = temp_constraint.index('<')
        temp_constraint.insert(index,"+")
        index += 1
        temp_constraint.insert(index,"9999")
        index += 1
        del temp_constraint[index]
        del temp_constraint[index]
        
        temp_constraint = signedIntegerAppend(temp_constraint)

        temp2 = str(temp_constraint[(len(temp_constraint)-1)])

        if temp2[0] == '-':
            temp_constraint = signChange(temp_constraint)

        for k in temp_constraint:
            temp2_constraint.append( int(k) )

        alt_constraint["const_{}".format(i)] = temp2_constraint

    elif '>' in temp_constraint:
        index = temp_constraint.index('>')
        temp_constraint.insert(index,"-")
        index += 1
        temp_constraint.insert(index,"9999")
        index += 1
        del temp_constraint[index]
        del temp_constraint[index]
        
        temp_constraint = signedIntegerAppend(temp_constraint)

        temp2 = str(temp_constraint[(len(temp_constraint)-1)])

        if temp2[0] == '-':
            temp_constraint = signChange(temp_constraint)
        
        for k in temp_constraint:
            temp2_constraint.append( int(k) )

        alt_constraint["const_{}".format(i)] = temp2_constraint


    # print(alt_constraint["const_{}".format(i)])

# for i in range(n1o):
    
# print(obj_func_list)

ProblemStmt()
print("\n\033[4mSolution :\033[0m")

# -------------------------------------------------     Intializing Problem Variables ----------------------------------------------------------------
alt_constraint_2 = {}

for i in range(len(alt_constraint)):
    temp = []

    for j in range(len(obj_func_list)):
        temp.append(alt_constraint["const_{}".format(i)][j])

    alt_constraint_2["const_{}".format(i)] = temp
    
    

cj = []

for i in obj_func_list:
    cj.append(i)

basic_variables = []

cb = []

xb = []

dj = []

z = 0


    
# print(obj_func_list)
for i in range(no):
    # appending cj values
    temp = alt_constraint["const_{}".format(i)] [ len(alt_constraint["const_{}".format(i)]) - 2 ]
    cj.append(temp)

    # appending basic_variables values
    if temp > 0:
        strng = '+S%s'%( str((i+1)).translate(SUB) )
        basic_variables.append(strng)
    else :
        strng = '-S%s'%( str((i+1)).translate(SUB) )
        basic_variables.append(strng)

    # appending cb values
    cb.append(0)

    # appending xb values
    temp = alt_constraint["const_{}".format(i)] [ len(alt_constraint["const_{}".format(i)]) - 1 ]
    xb.append(temp)

    
# print(obj_func_list)

# print("Cj = {}, basic_variables = {}, cb = {}, xb = {}, dj = {} ".format(cj, basic_variables, cb, xb, dj))

# innercounter = 0
# anothercounter = 0
# i = 0
# count = 0
# while i < no:
    
#     if count == innercounter:
#         if (alt_constraint["const_{}".format(i)] [ len(alt_constraint["const_{}".format(i)]) - 2 ]) > 0:
#             alt_constraint_2["const_{}".format(i)].append(1)
#             innercounter += 1
#             anothercounter += 1
#         else:
#             alt_constraint_2["const_{}".format(i)].append(-1)
#             innercounter += 1
#             anothercounter += 1
#     else:
#         alt_constraint_2["const_{}".format(i)].append(0)
#         count += 1
#         anothercounter += 1

#     if (anothercounter == (len(cj) - len(obj_func_list))):
#         i += 1
#         anothercounter = 0
#         count = 0
    
counter = 0
for i in range(no):
    length = len(alt_constraint["const_{}".format(i)])
    length += no
    j = 0
    while True:
        
        if counter == j:
            alt_constraint["const_{}".format(i)].append(1)
            counter += 1
        else:
            alt_constraint["const_{}".format(i)].append(0)
            j += 1

        if len(alt_constraint["const_{}".format(i)]) == length :
            break

print(alt_constraint)

# calculating z


for i in range(no):
    temp = cb[i] * xb[i]
    z = z + temp

# calculating delta(j)
# tmp_lst = []
# temp = 0
# for i in range(len(obj_func_list)):
#     if i != len(alt_constraint["const_{}".format(i)]):
#         tmp_lst.append(alt_constraint["const_{}".format(i)][i])
#         for j in range(i,no):
#             tmp_lst.append(alt_constraint["const_{}".format(temp)][i])





