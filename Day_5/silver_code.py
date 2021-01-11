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

