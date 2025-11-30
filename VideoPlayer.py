#!/usr/bin/env python3

import threading
# Import our new separate files
from BoundedBuffer import BoundedBuffer
from WorkerFunctions import extract_frames, convert_to_grayscale, display_frames

def main():
    filename = 'clip.mp4'
    
    # Create the shared buffers
    extract_queue = BoundedBuffer(10)
    display_queue = BoundedBuffer(10)

    # Create the threads using the imported functions
    extract_thread = threading.Thread(target=extract_frames, args=(filename, extract_queue))
    convert_thread = threading.Thread(target=convert_to_grayscale, args=(extract_queue, display_queue))
    display_thread = threading.Thread(target=display_frames, args=(display_queue,))

    # Start and Join
    extract_thread.start()
    convert_thread.start()
    display_thread.start()

    extract_thread.join()
    convert_thread.join()
    display_thread.join()

if __name__ == "__main__":
    main()