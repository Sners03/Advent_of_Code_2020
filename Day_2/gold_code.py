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
        line = line.split("-")
        input_arr.append([line[0], line[1].split(" ")])
    return input_arr

def solve_riddle(input_arr):
    valid_password_num = 0
    for line in input_arr:
        bool1 = (line[1][2][int(line[0])-1] == line[1][1][0] != line[1][2][int(line[1][0])-1])
        bool2 = (line[1][2][int(line[0])-1] != line[1][1][0] == line[1][2][int(line[1][0])-1])
        if bool1 or bool2:
             valid_password_num += 1
    return valid_password_num


if __name__ == "__main__":
    input_arr = get_txt_content()
    solution = solve_riddle(input_arr)
    print(solution) # solution = 249