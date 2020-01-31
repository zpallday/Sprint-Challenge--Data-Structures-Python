class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # if you are inserting, there must be a root
    def insert(self, value):
        if self.value < value:    # if the value is less then self.value/ doesn't have a node
          if self.right is None:     # if it doesn't have a node then it creates a new one 
              self.right = BinarySearchTree(value)     
          else: 
              self.right.insert(value) # if it does have a node
        elif self.value >= value: 
           if self.left is None: 
              self.left = BinarySearchTree(value) 
           else: 
              self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    # Checks for the inputs target
    # if the target = self.value. then it returns
    #  or if not go left or right depending on the value number
    def contains(self, target):
        if target == self.value: 
          return True 
        elif self.right and self.value < target: 
          return self.right.contains(target) 
        elif self.left and self.value > target: 
          return self.left.contains(target) 
        else: 
          return False

    # Return the maximum value found in the tree
    # def get_max(self):
    #     if self.right != None: 
    #       return self.right.get_max() 
    #     else:
    #       return self.value