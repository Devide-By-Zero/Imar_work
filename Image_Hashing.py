from time import sleep
from PIL import Image
import os
import imagehash

#How Different the images have to be
Threshold_value = 10

def list_needles():
    return os.listdir("Images/Needles")

def list_haystack():
    return os.listdir("Images/Hay_Stack")

def main():
    needles = list_needles()
    i=0
    while(len(needles) != 0):
        print('Checking New Image')
        haystack = list_haystack()
        needle_hash = imagehash.dhash(Image.open('Images/Needles/'+ needles[i]))
        j=0
        similar_found=False
        similar_files = ""
        while(len(haystack) != 0 and j<len(haystack)):
            heystack_hash = imagehash.dhash(Image.open('Images/Hay_Stack/' + haystack[j]))
            difference = needle_hash - heystack_hash
            if(difference<Threshold_value):
                similar_found = True
                similar_files = similar_files + '\n' + haystack[j]
            j = j+1
        if(similar_found):
            os.rename("Images/Needles/"+needles[i], "Images/Check/"+needles[i])
            with open('Images/Check/'+needles[i]+'.txt', 'w') as f:
                f.write(similar_files)
        else:
            os.rename("Images/Needles/"+needles[i], "Images/Hay_Stack/"+needles[i])
        i = i+1
    print('sleeping')
    sleep(60)
    

if __name__ == "__main__":
    print("Process will keep checking and moving files untill script is stoped using Ctrl+x")
    try:
        if(not os.path.isdir('Images/Needles')):
            os.makedirs('Images/Needles')
        if(not os.path.isdir('Images/Hay_Stack')):
            os.makedirs('Images/Hay_Stack')
        if(not os.path.isdir('Images/Check')):
            os.makedirs('Images/Check')
        while(True):
            main()

    except KeyboardInterrupt:
        print("\nProcess stoped")
        exit()