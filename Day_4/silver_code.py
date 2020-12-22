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
    new_arr = []
    marker = 0
    
    # everything in one line
    for i in range(len(content)):
        if content[i] == '\n':
            input_arr.append(content[marker:i])
            marker = i+1
    # every element in one line in one spot
    for i in range(len(input_arr)):
        for j in range(len(input_arr[i])):
            input_arr[i][j] = input_arr[i][j].split(" ")
    
    # reduce unnecessary list dimension (3D-->2D) 
    for i in range(len(input_arr)):
        tmp_arr = []
        for j in range(len(input_arr[i])):
            for k in range(len(input_arr[i][j])):
                tmp_arr.append(input_arr[i][j][k])
        new_arr.append(tmp_arr)
    
    # remove linebreaks from elements
    """
    for i in range(len(new_arr)):
        for j in range(len(new_arr[i])):
            if new_arr[i][j][-1] == '\n':
                new_arr[i][j] = new_arr[i][j][:-1]
    """
    
    return new_arr
#didnt work... maybe regex?
def solve_riddle(input_arr): 
    solution = len(input_arr)
    print(solution)
    for i in input_arr:
        if len(i) == 8:
            solution -= 1
        if len(i) == 7:
            is_valid = False
            for j in i:  
                if i[:3]=='cid':
                    is_valid = True
            if is_valid:
                solution-=1

    return solution

if __name__=='__main__':
    input_arr = get_txt_content()
    solution = solve_riddle(input_arr)
    print(solution)
