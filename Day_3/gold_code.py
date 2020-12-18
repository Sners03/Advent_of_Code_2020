from tkinter import filedialog

def get_txt_content():
    filename =  filedialog.askopenfilename(initialdir = "",
                                            title = "Select file",
                                            filetypes = (("txt files","*.txt")
                                                        ,("all files","*.*")))
    file = open(filename,'r')
    content = file.readlines()
    file.close()

    input_arr = []

    for line in content:
        input_arr.append(line[:-1]) # filter \n

    return input_arr

def right1_down1(input_arr, line_length):
    tree_count= 0
    pos = 0
    for line in input_arr:
        if line[pos%(line_length)] == '#':
            tree_count += 1
        pos += 1
        
    return tree_count

def right3_down1(input_arr, line_length):
    tree_count= 0
    pos = 0
    for line in input_arr:
        if line[pos%(line_length)] == '#':
            tree_count += 1
        pos += 3
    
    return tree_count

def right5_down1(input_arr, line_length):
    tree_count= 0
    pos = 0
    for line in input_arr:
        if line[pos%(line_length)] == '#':
            tree_count += 1
        pos += 5
    
    return tree_count

def right7_down1(input_arr, line_length):
    tree_count= 0
    pos = 0
    for line in input_arr:
        if line[pos%(line_length)] == '#':
            tree_count += 1
        pos += 7
    
    return tree_count

def right1_down2(input_arr, line_length):
    tree_count= 0
    pos = 0
    for line in input_arr[::2]:
        if line[pos%(line_length)] == '#':
            tree_count += 1
        pos += 1
    
    return tree_count

def solve_riddle(input_arr):
    line_length = len(input_arr[0])
    # takes longer than using one for-loop but looks nicer/cleaner
    sol1 = right1_down1(input_arr, line_length)
    sol2 = right3_down1(input_arr, line_length)
    sol3 = right5_down1(input_arr, line_length)
    sol4 = right7_down1(input_arr, line_length)
    sol5 = right1_down2(input_arr, line_length)
        
    return sol1 * sol2 * sol3 * sol4 * sol5 

if __name__=="__main__":
    input_arr = get_txt_content()
    solution = solve_riddle(input_arr)
    print(solution) # solution = 3772314000