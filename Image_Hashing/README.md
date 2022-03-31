# Image_Hashing
Like finding a Needle in a Haystack, Trying to find similar images in a big dataset can be hard.
This python program will take one image from the Needles folder and create a hash for it.
Then it will check every file in the Hay_Stack folder for similar images using the same method.
If the difference between the hashes do not meet the threshold value, then a complementary file is made with the name
of the image that is too similar for human inspection.
If the differences are great enough then the Needle is moved to the Hay_Stack
