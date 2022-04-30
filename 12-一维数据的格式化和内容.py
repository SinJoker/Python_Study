"""
Operating Circle of the Data
    1 write_focus on format
    2 expression_focus on format
    3 Execution_focus on method(different from Operation)

    Expression of 1 dimension Data
        (1) Use list method, list = [3.1415, 3.1516, 3.1918] exist order.
        (2) Use Set method, set = {3.1415, 3.1516, 3.1918} do not exist order.
    Write of 1 dimension Data
        (1) Use Space to separate elements, no need to build a new line, but not allow space between elements.
        (2) Use comma(逗号) to separate elements, no need to build a new line, but not allow comma between elements.
        (3) else Use other symbol to separate elements
    Execution of 1 dimension Data(different from Operation)
        Execution the problem of transformation between the write format and expression format
        more details in case 1

# case 1
txt = open(fname).read()
ls = txt.split(" ")  # Use space to separate lines
txt.close()

list1 = ['China', 'American', 'Japan']
f.open(fname,'w')
f.write(' ', join(list1))
f.close
"""
