def to_jaden_case(string):
    listed = list(string)
    string = listed[0].upper()
    for i in range(len(listed)-1):
        if listed[i] == " ":
            string = string+listed[i+1].upper()
        else:
            string = string + listed[i+1]
    return string
#made by: Pdxr
