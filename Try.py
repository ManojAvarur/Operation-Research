def minimize_to_maximize():
    global obj_func_list
    for i in range(0, len(obj_func_list)):
        obj_func_list[i] = (obj_func_list[i]) * -1
        # temp = obj_func_list[i]
        # temp = temp.replace('-', '+')

# # ------------------------------ Objective Function Input ------------------------------


print("\n(+) Select the kind of problem \n   1. Maxz \t 2. Minz")
obj_func_selec = int(input("\nEnter Your Option : "))
print()

obj_func_ = str(input("""\n       -> Enter The Objective Function
          \033[4mExample :\033[0m
      \t     ▶ If your objective function is \" Maxz = -3x1 + x2 \" 
      \t     ▶ Then you have to enter \" -3 + 1 \" 
      \n\t         =>   """))

if obj_func_[0] != '+' and obj_func_[0] != '-':
    obj_func_ = '+' + obj_func_

obj_func_ = obj_func_.replace(' ', '')
obj_func_list_temp = []
obj_func_list = []

for i in obj_func_:
    obj_func_list_temp.append(i)

# for i in range(0,len(obj_func_list_temp)):
temp = ""
i = 0
while i < len(obj_func_list_temp):
    # temp = obj_func_list_temp[i] + obj_func_list_temp[i + 1]
    # obj_func_list.append("{}".format(temp))  [ +,2,+, 8, -,3,8, +, 2,]

    if i == 0:
        temp += obj_func_list_temp[i]

    elif not obj_func_list_temp[i] in ['+', '-']:
        temp += obj_func_list_temp[i]

    else:
        obj_func_list.append(int(temp))
        temp = ""
        temp += obj_func_list_temp[i]

    i += 1
    if i == len(obj_func_list_temp):
        obj_func_list.append(int(temp))


if obj_func_selec == 2:
    minimize_to_maximize()

# print(obj_func_list)

# ------------------------------ Constraint Input ------------------------------

no = int(input("\n(+) Enter number of constraints to be entered : "))

print("""\n     -> Enter The Constraints
            \033[4mExample :\033[0m
        \t     ▶ If your constraint is \" x1 + 2x2 <= 10 \" 
        \t     ▶ Then you have to enter \" 1 + 2 <= 10 \" """)

constant = {}

for i in range(no):
    const_ = str(input("        \n\t         =>   "))

    if const_[0] != '+' and const_[0] != '-':
        const_ = '+' + const_

    const_ = const_.replace(' ', '')

    constant["const_{}".format(i)] = const_


# print(constant)
strng = ""
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

if obj_func_selec == 1:
    strng = "Max z = "
else:
    strng = "Max z` = "

temp = ""
for i in range(len(obj_func_list)):
    # temp += "{}x{}".format(obj_func_list[i],str((i+1)).translate(SUB))
    temp += "%+dx%s" % (obj_func_list[i], str((i+1)).translate(SUB))

strng += temp


print("\n\033[4mProblem Statement\033[0m")

print("\t"+strng)
print("\tSubject To,")


for i in range(no):
    temp = constant["const_{}".format(i)]
    templist = []
    const_temp = []

    for j in temp:
        templist.append(j)

    tempo = ""
    k = 0
    while k < len(templist):

        if k == 0:
            tempo += templist[k]

        elif not templist[k] in ['+', '-', '<', '>', '=']:
            tempo += templist[k]

        else:
            if not templist[k] in ['<', '>', '=']:
                const_temp.append(int(tempo))

            tempo = ""
            if templist[k] == '<':
                const_temp.append('<=')

            elif templist[k] == '>':
                const_temp.append('>=')

            elif not templist[k] in ['<', '>', '=']:
                tempo += templist[k]

        k += 1
        if k == len(templist):
            const_temp.append(int(tempo))

    temp = ""
    for k in range(len(const_temp)):
        if (not const_temp[k] in ['<=', '>='] and (k != (len(const_temp) - 1))):
            temp += "%+dx%s" % (const_temp[k], str((k+1)).translate(SUB))
        elif const_temp[k] == '<=':
            temp += ' <= '
        elif const_temp[k] == '>=':
            temp += ' >= '
        elif k == (len(const_temp) - 1):
            temp += str(const_temp[k])

    print("\t   ", temp)



print("\n\033[4mSolution :\033[0m")


# ---------------------------------------------------- Solution --------------------------------------------------------------------------
