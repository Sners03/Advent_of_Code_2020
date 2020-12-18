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

    for num in content:
        input_arr.append(int(num))
    return input_arr

def solve_riddle(input_arr):
    for num1 in input_arr:
        for num2 in input_arr:
            for num3 in input_arr:
                if num1 + num2 + num3 == 2020:
                    return num1*num2*num3

if __name__ == '__main__':
    input_arr = get_txt_content()
    solution = solve_riddle(input_arr)
    print(solution) # solution = 116168640