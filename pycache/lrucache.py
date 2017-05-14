from collections import UserDict

class LRUCache(UserDict):
    '''
    LRU 缓存
    非多线程安全，协程环境下使用
    '''
    def __init__(self, maxsize=1024):
        super(LRUCache, self).__init__() 
        # Link node layout:     [PREV, NEXT, KEY, RESULT]
        self.head = None
        self.maxsize = maxsize

    def _overflow(self):
        head = self.head
        count = len(self.data)
        if count > self.maxsize:
            target = head[0]
            prev, next_, key, _ = target
            prev[1] = next_
            next_[0] = prev
            #print("remove key=", key)
            del self.data[key]

    def __setitem__(self, key, value):
        head = self.head
        link = self.data.get(key)
        if link is not None:
            link_prev, link_next, _, _ = link
            link_prev[1] = link_next
            link_next[0] = link_prev
        link = [None, None, key, value]

        if head is not None:
            link_prev, _, _, _ = head
            link_prev[1] = link
            head[0] = link
            link[1] = head
            link[0] = link_prev
        else:
            link[0] = link
            link[1] = link
                
        self.head = link
        self.data[key]= link
        self._overflow()

    def __getitem__(self, key):
        return self.data[key][3]
        
    def __delitem__(self, key):
        head = self.head
        count = len(self.data)
        link = self.get(key)
        if link is None:
            return
        elif count == 1:
            self.head = None
        elif link is head:
            self.head = head[1]
        else:
            link_prev, link_next, _, result = link
            link_prev[1] = link_next
            link_next[0] = link_prev


        del self.data[key]

