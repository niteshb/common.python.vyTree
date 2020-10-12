from .vyTreeNode import VyTreeNode

class VyTreeDataNode(VyTreeNode):
    def __init__(self, data, **kwrags):
        super().__init__(**kwrags)
        self.data = data
