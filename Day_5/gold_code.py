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
    lower_row_marker = 0
    higher_row_marker = 127
    lower_column_marker = 0
    higher_column_marker = 7

    for i, char in enumerate(pass_code[:-3]):
        if(char=='F'):
            higher_row_marker -= int(64/2**(i))
        if(char=='B'):
            lower_row_marker += int(64/2**(i))

    for j, char in enumerate(pass_code[-3:]):
        if(char=='L'):
            higher_column_marker -= int(4/2**(j))
        if(char=='R'):
            lower_column_marker += int(4/2**(j))

    # the higher marker should be equal to the lower one in each case
    return higher_row_marker*8 + lower_column_marker

def get_all_IDs(input_arr):
    ID_arr = []

    for code in input_arr:
        ID_arr.append(get_seat_ID(code))
    ID_arr.sort()

    return ID_arr

def get_my_ID(ID_arr):
    for ID in range(ID_arr[0],ID_arr[-1]):
        if ID not in ID_arr:
            return ID

if __name__ == "__main__":
    input_arr = get_txt_content()
    ID_arr = get_all_IDs(input_arr)
    my_ID = get_my_ID(ID_arr)
    print(f"My ID is: {my_ID}")
    