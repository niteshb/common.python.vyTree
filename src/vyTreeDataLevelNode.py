from .vyTreeDataNode import VyTreeDataNode
from .vyTreeLevelNode import VyTreeLevelNode

class VyTreeDataLevelNode(VyTreeDataNode, VyTreeLevelNode):
    def __init__(self, **kwrags):
        super().__init__(**kwrags)

