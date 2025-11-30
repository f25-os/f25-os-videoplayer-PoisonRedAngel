#!/usr/bin/env python3
import cv2

def extract_frames(fileName, outputBuffer):
    count = 0
    vidcap = cv2.VideoCapture(fileName)
    success, image = vidcap.read()
    
    print(f'Extracting frame {count}')
    while success and count < 72:
        outputBuffer.put(image)
        success, image = vidcap.read()
        count += 1
        print(f'Extracting frame {count}')
    
    outputBuffer.put(None)
    print('Frame extraction complete')

def convert_to_grayscale(inputBuffer, outputBuffer):
    count = 0
    while True:
        frame = inputBuffer.get()
        
        if frame is None:
            outputBuffer.put(None)
            break
            
        print(f'Converting frame {count}')
        grayscaleFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        outputBuffer.put(grayscaleFrame)
        count += 1
        
    print('Grayscale conversion complete')

def display_frames(inputBuffer):
    count = 0
    while True:
        frame = inputBuffer.get()
        
        if frame is None:
            break

        print(f'Displaying frame {count}')
        cv2.imshow('Video', frame)
        
        if cv2.waitKey(42) and 0xFF == ord("q"):
            break
        
        count += 1

    print('Finished displaying all frames')
    cv2.destroyAllWindows()