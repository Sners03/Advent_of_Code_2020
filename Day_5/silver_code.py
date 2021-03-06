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

def get_seat_ID(pass_code):
    rownum = 0
    columnnum = 0
    lower_row_marker = 0
    higher_row_marker = 127
    lower_column_marker = 0
    higher_column_marker = 127

    for i, char in enumerate(pass_code[:-3]):
        if(char=='F'):
            higher_row_marker -= (64/(i+1))
        if(char=='B'):
            lower_row_marker += (64/(i+1))
    
    return higher_row_marker*8

