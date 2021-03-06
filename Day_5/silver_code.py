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

if __name__ == "__main__":
    assert get_seat_ID("BFFFBBFRRR") == 567
    assert get_seat_ID("FFFBBBFRRR") == 119
    assert get_seat_ID("BBFFBBFRLL") == 820
    print("all tests passed")


