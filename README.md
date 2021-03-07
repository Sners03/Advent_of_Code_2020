# Advent of Code 2020 Solutions 
<center>All solutions to Advent of Code 2020 by Sners03</center>

You can find the tasks on [adventofcode.com](https://adventofcode.com/2020).

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

## Folow this repository

[<img src="https://s18955.pcdn.co/wp-content/uploads/2018/02/github.png" width="25"/>](https://github.com/Sners03/Advent_of_Code_2020/subscription)

## Download

Here is the download for the [ZIP](https://github.com/Sners03/Advent_of_Code_2020/raw/master/all_files.zip)


Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[ZIP](https://github.com/Sners03/Advent_of_Code_2020/raw/master/all_files.zip) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

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

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
