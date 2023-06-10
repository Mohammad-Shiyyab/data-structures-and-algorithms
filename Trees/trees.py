from data_struct import Node,Queue,Stack
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
      if root.left:
        _walk(root.left)

      if root.right:
        _walk=root.right

      output.append(root.value)


    _walk(self.root)
    return output
  


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
        _search(node.right,value)



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