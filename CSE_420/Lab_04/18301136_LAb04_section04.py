import re
# opening input file
with open("input.txt","r")as f:
    methodList = []
    # pattern for matching with file
    methodPatternRegex = re.compile(r"(public|private|protected)( static)? (int|double|float|void) \w*\((.*)?\)")
    methodNotAcceptedRegex = re.compile(r"(public|private) (static) (void) (main)")
    # loop to iterate over file line by line
    for line in f.readlines():
        if re.match(methodPatternRegex, line) and not re.match(methodNotAcceptedRegex,line):
            # appending into our list by checking function name and after that
            methodList.append(re.findall("(int|double|float|void) (\w*)\((.*)?\)",line)[0])
    # printing methods
    print("Methods :")
    for i in methodList:
        # "i[1]" is function name,"i[2]" is argument,"i[0]" is function type
        print(i[1]+"("+i[2]+")"+" ,return type: "+i[0])