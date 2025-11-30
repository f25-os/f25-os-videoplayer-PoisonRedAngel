#!/usr/bin/env python3
import threading

class BoundedBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.lock = threading.Lock()
        self.empty_slots = threading.Semaphore(capacity)
        self.full_slots = threading.Semaphore(0)

    def put(self, item):
        self.empty_slots.acquire()
        with self.lock:
            self.buffer.append(item)
        self.full_slots.release()

    def get(self):
        self.full_slots.acquire()
        with self.lock:
            item = self.buffer.pop(0)
        self.empty_slots.release()
        return item