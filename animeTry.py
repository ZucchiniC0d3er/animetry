#is centered method takes in an object form the
def is_centered(image_metadata):
    #print(image_metadata)
    left_eye_x = int(image_metadata[1])
    left_eye_y = int(image_metadata[2])
    right_eye_x = int(image_metadata[3])
    right_eye_y = int(image_metadata[4])
    nose_x = int(image_metadata[5])

    if abs(left_eye_y - right_eye_y)>2:
        return False
    if abs((left_eye_x + right_eye_x)/2- nose_x)>3:
        return False
    return True
def filterPeople(peopleAtributes):

    if peopleAtributes[11] == True or peopleAtributes[21] == True:
        return False
    if peopleAtributes[3] == False:
        return False
    return True



lines = []
# reading from the file and puting values into an multidemensional array

with open('list_attr_celeba.txt') as inputfile:
    inputfile.next()
    headers = inputfile.next().strip().split()
    for line in inputfile:
        lines.append(line.strip().split())
#converting the values to booleans
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "-1":
         lines[i][j] = False
        elif lines[i][j] == "1":
            lines[i][j] = True
        #print(lines[i][j])


for i,header in enumerate(headers):
    print(str(i) + str(header))

separator = (len(lines[0]))


with open('list_landmarks_align_celeba.txt') as inputfile:
    print(inputfile.next())
    print(inputfile.next())
    for i,line in enumerate(inputfile):
        separated_line=line.strip().split()

        if len(separated_line)>1:
            lines[i] += separated_line


images_removed=0
for entry in lines:
    centered = is_centered(entry[separator:])
    isIdeal = filterPeople(entry)
    idealandCenterd = centered and isIdeal
    if not idealandCenterd:
        images_removed = images_removed + 1
    entry.append(idealandCenterd)


print images_removed
print(lines[-1])







