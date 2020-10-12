from .vyTreeNode import VyTreeNode

class VyTreeDataNode(VyTreeNode):
    def __init__(self, data):
        super().__init__()
        self.data = data
