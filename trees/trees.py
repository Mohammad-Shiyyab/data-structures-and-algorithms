from trees.data_struct import Node,Queue,Stack


class Tnode:
  def __init__(self,value):
    self.value=value
    self.right= None
    self.left = None
    # children = []





class Tree:
  def __init__(self):
    self.root=None

  def breadth_first(self):
    if not self.root:
      return self.root
      
    output = []
    queue = Queue()
    queue.enqueue(self.root)

    while not queue.is_empty():
      
      front = queue.dequeue()
      output.append(front.value)
      
      if front.left :
          queue.enqueue(front.left)
      if front.right :
          queue.enqueue(front.right)  
        
    return output

  def pre_order(self):

    output=[]
    
    def _walk(root):
      output.append(root.value)

      #left
      if root.left:
        _walk(root.left)

      #right  
      if root.right:
        _walk(root.right)


    _walk(self.root)
    return output     

      

  def in_order(self):

    output=[]

    def _walk(root):
      
      #left
      if root.left :
        _walk(root.left)

      output.append(root.value)


      #right
      if root.right :
        _walk(root.right)

    _walk(self.root)
    return output
      
    
  def post_order(self):

    output=[]

    def _walk(root):
        #left
        if root.left:
          _walk(root.left)

        #right
        if root.right:
          _walk(root.right)

        output.append(root.value)


    _walk(self.root)
    return output
  

  def max_value(self):
      if self.node is None:
          return ValueError("tree is empty")
      max_value = self.root.value
      return self._max_value(self.root,max_value)

  def _max_value(self,node,max_value):
      if node.value >max_value:
        max_value=node.value
      if node.left is not None:
        max_value=self._max_value(node.left,max_value)
      if node.right is not None:
        max_value=self._max_value(node.right,max_value)
        
      return max_value
  

  def sum_odd_numbers(self):
        return self._sum_odd_numbers_helper(self.root)
  
  def _sum_odd_numbers_helper(self, node):
        if not node:
            return 0

        sum_odd = 0

        if node.value % 2 != 0:
            sum_odd += node.value

        sum_odd += self._sum_odd_numbers_helper(node.left)
        sum_odd += self._sum_odd_numbers_helper(node.right)

        return sum_odd
  


  
class BinarySearchTree(Tree):
  def __init__(self):
    super().__init__()

  def add(self,value):  
    if not self.root :
      self.root = Tnode(value)
      return 
  
    def _add_node(node,value):
      if value < node.value:
          if node.left:
            _add_node(node.left,value)

          else:
            node.left=Tnode(value)

      elif value >node.value:
        if node.right:
          _add_node(node.right,value)

        else :
          node.right=Tnode(value)

    _add_node(self.root,value)


  def contains(self,value):

    def _search(node,value):
      if not node:
        return False

      if node.value==value:
        return True

      if value<node.value:
        return _search(node.left,value)

      else:
        return _search(node.right,value)

    return _search(self.root,value)

if __name__ == "__main__":

  searc = BinarySearchTree()

  searc.add(10)
  searc.add(20)
  searc.add(5)
  searc.add(15)
  searc.add(25)
  searc.add(0)
  print("breadth")
  print(searc.breadth_first())
  print("pre_order")
  print(searc.pre_order())
  print("in_order")
  print(searc.in_order())
  print("post_order")
  print(searc.post_order())

  print("Contains 20:", searc.contains(20))
  print("Contains 30:", searc.contains(30))