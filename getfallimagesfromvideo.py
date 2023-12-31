# -*- coding: utf-8 -*-
'''
从视频中把图像分离出来
'''

import cv2
import os

input_video_path = '/home/root2/anaconda3/bin/my-object/images/test/videos'
output_path = '/home/root2/anaconda3/bin/my-object/images/test/images'
prefix = 'Home_01_'

for _, _, filelist in os.walk(input_video_path):
    pass


image_counter = 1
video_counter = 1
for i in filelist:
    filename = os.path.join(input_video_path, i)
    
    vs = cv2.VideoCapture(filename)

    
    while True:
        # grab the current frame
        (grabbed, frame) = vs.read()
        if filename and not grabbed:
            break
        
        cv2.imwrite(os.path.join(output_path, 
                                 prefix + '%d.jpg' %(image_counter)), 
                    frame)
        
        image_counter += 1
        
    vs.release()
    
    print('processed %d/%d videos' %(video_counter, len(filelist)))
    
    video_counter += 1


cv2.destroyAllWindows()

