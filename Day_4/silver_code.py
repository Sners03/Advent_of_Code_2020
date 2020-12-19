from tkinter import filedialog

def get_txt_content():
    filename =  filedialog.askopenfilename(initialdir = "",
                                            title = "Select file",
                                            filetypes = (("txt files","*.txt")
                                                        ,("all files","*.*")))
    file = open(filename,'r')
    content = file.readlines()
    file.close()

    #content.split(" ")
    input_arr = []
    marker = 0
    for i in range(len(content)):
        if content[i] == '\n':
            input_arr.append(content[marker:i])
            marker = i+1

    for i in range(len(input_arr)):
        for j in range(len(input_arr[i])):
            input_arr[i][j] = input_arr[i][j].split(" ")

    return input_arr

if __name__=='__main__':
    input_arr = get_txt_content()
    for i in input_arr:
        print(i)