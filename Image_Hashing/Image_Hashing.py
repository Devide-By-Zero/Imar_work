from time import sleep
from PIL import Image
import threading
import os
import imagehash
import signal

#How Different the images have to be
Threshold_value = 10

#How many threads the script can use
#Keep at 1 While This line is here.
#As images are not cross referenced between threads
Thread_number = 1

def list_needles():
    return os.listdir("Images/Needles")

def list_haystack():
    return os.listdir("Images/Hay_Stack")

def move_unique(file_name):
    os.rename("Images/Needles/"+file_name, "Images/Hay_Stack/"+file_name)

def move_similar(file_name,similar_files):
    os.rename("Images/Needles/"+file_name, "Images/Check/"+file_name)
    with open('Images/Check/' + file_name.split('.')[0] + '.txt', 'w') as f:
        f.write(similar_files)


#Find a way to check images that are being used by other threads
def check_for_new_Image(old_hay_stack):
    new_hay_stack = list_haystack()
    if(new_hay_stack == old_hay_stack):
        return False

def main(starting_number):
    while(True):
        i=starting_number
        needles = list_needles()
        while(len(needles) != 0):
            print('Thread ' + str(starting_number) + ' checking New Image')
            needle_hash = imagehash.dhash(Image.open('Images/Needles/'+ needles[i]))
            haystack = list_haystack()
            similar_found=False
            similar_files = ""
            j=0
            while(len(haystack) != 0 and j<len(haystack)):
                heystack_hash = imagehash.dhash(Image.open('Images/Hay_Stack/' + haystack[j]))
                difference = needle_hash - heystack_hash
                if(difference<Threshold_value):
                    similar_found = True
                    similar_files = similar_files + '\n' + haystack[j]
                j = j+1
            if(similar_found):
                move_similar(needles[i],similar_files)
            else:
                move_unique(needles[i])
            i = i+Thread_number
        print('Thread ' + str(starting_number) + ' sleeping')
        sleep(60)
    
def signal_handler(signal, frame):
    print("\nProcess stoped")
    exit()

if __name__ == "__main__":
    print("Process will keep checking and moving files untill script is stoped using Ctrl+x")
    if(not os.path.isdir('Images/Needles')):
        os.makedirs('Images/Needles')
    if(not os.path.isdir('Images/Hay_Stack')):
        os.makedirs('Images/Hay_Stack')
    if(not os.path.isdir('Images/Check')):
        os.makedirs('Images/Check')
    signal.signal(signal.SIGINT, signal_handler)
    threads = []
    for i in range(0,Thread_number):
        t = threading.Thread(target=main, args=(i,))
        t.daemon = True
        t.start()
        threads.append(t)
    for thr in threads:
        thr.join()
