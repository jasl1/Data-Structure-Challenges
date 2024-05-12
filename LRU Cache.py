
class ListNode(object):
    def __init__(self, key = 0, val= 0):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.tail.prev = self.head
        self.head.next = self.tail
        

    def addNode(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveNode(self, node):
        self.removeNode(node)
        self.addNode(node)

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.moveNode(node)
            return node.val
        else:
            return -1
 

    def put(self, key, value):
        
        if key in self.cache:
            node =  self.cache[key]
            node.val = value
            self.moveNode(node)            
        else:
            node =  ListNode(key, value)
            self.cache[key] = node
            self.addNode(node)
            if len(self.cache) > self.cap:
                delNode = self.head.next
                self.removeNode(delNode)
                del self.cache[delNode.key]


             

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
