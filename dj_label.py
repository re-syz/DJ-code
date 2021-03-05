"""
131072
netheremp
050321
labeling.py



"""

import os
import eyed3
import pathlib
import os.path
from os import path
import shutil

sour = r"C:\Users\spark\Desktop\scnoj"  # change source path here
dest = r"C:\remp\Techno"  # change destination path here

path_list = []

for filepath in pathlib.Path(sour).glob('**/*'):  # change source folder here
    path_list.append(filepath.absolute())

pub = ""  # publisher
art = ""  # album artist
alb = ""  # album

amount = len(path_list)

new_pub = []
new_alb = []

for i in range(amount):
    audio = eyed3.load(path_list[i])

    pub = audio.tag.publisher
    art = audio.tag.album_artist
    alb = audio.tag.album

    # print(pub)
    # print(art)
    # print(alb)

    restrict = ["\\", "/", ":", "*", "?", "\"", "<", ">", "|"]
    for p in range(len(restrict)):
        if restrict[p] in pub:
            print("There's replacement in the publisher: " + str(pub))
            pub = pub.replace(restrict[p], "")

        if restrict[p] in alb:
            print("There's replacement in the album: " + str(alb))
            alb = alb.replace(restrict[p], "")

        if restrict[p] in art:
            print("There's replacement in the artist: " + str(art))
            art = art.replace(restrict[p], "")


    pub_fol = str(dest) + "\\" + str(pub)  # change destination folder here
    alb_fol = pub_fol + "\\" + str(art) + " - " + str(alb)



    if path.exists(pub_fol) == True:

        if path.exists(alb_fol) == True:
            newPath = shutil.copy(path_list[i], alb_fol)
            # print(newPath)

        else:
            os.mkdir(alb_fol)
            new_alb.append(alb)

            newPath = shutil.copy(path_list[i], alb_fol)
            # print(newPath)

    else:
        os.mkdir(pub_fol)
        new_pub.append(pub)
        os.mkdir(alb_fol)
        new_alb.append(alb)

        newPath = shutil.copy(path_list[i], alb_fol)
        # print(newPath)


    pub = ""
    art = ""
    alb = ""

    pub_fol = ""
    alb_fol = ""


print("=" * 52, end = "\n\n")
print(str(len(new_pub)) + " new publisher(s)", end = "\n\n")
for x in range(len(new_pub)):
    print(new_pub[x])

print("=" * 52, end = "\n\n")
print(str(len(new_alb)) + " new album(s)", end = "\n\n")
for y in range(len(new_alb)):
    print(new_alb[y])
