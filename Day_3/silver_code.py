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

def solve_riddle(input_arr):
    line_length = len(input_arr[0])
    tree_count= 0
    pos = 0
    for line in input_arr:
        if line[pos%(line_length)] == '#':
            tree_count += 1
        pos += 3
        
    return tree_count

if __name__=="__main__":
    input_arr = get_txt_content()
    solution = solve_riddle(input_arr)
    print(solution) # solution = 195