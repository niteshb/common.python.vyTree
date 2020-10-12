from .vyTreeDataNode import VyTreeDataNode
from .vyTreeLevelNode import VyTreeLevelNode

class VyTreeDataLevelNode(VyTreeDataNode, VyTreeLevelNode):
    def __init__(self, data):
        super().__init__(data)

