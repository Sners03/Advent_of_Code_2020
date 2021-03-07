<h1 style="text-align: center;"> Advent of Code 2020 Solutions </h1>
All solutions to Advent of Code 2020 by Sners03

You can find the tasks on [adventofcode.com](https://adventofcode.com/2020).

## Folow this repository

[<img src="https://s18955.pcdn.co/wp-content/uploads/2018/02/github.png" width="25"/>](https://github.com/Sners03/Advent_of_Code_2020/subscription)

## Download

Here is the download for the [ZIP](https://github.com/Sners03/Advent_of_Code_2020/raw/master/all_files.zip). <br />
Note that at this point all files are written in Python3, therefore Python 3 is required.

### Example Input Code in Python


```python
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
```

