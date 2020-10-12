from .vyTreeNode import VyTreeNode

class VyTreeLevelNode(VyTreeNode):
    def __init__(self, level=0, **kwrags):
        super().__init__(**kwrags)
        self.__level = level

    @property
    def level(self):
        return self.__level

    @property
    def __level(self):
        return self.__level_

    @__level.setter
    def __level(self, level):
        self.__level_ = level
        for childNode in self.childNodes:
            childNode.__level = level + 1

    def insertChildNode(self, idx, childNode):
        super().insertChildNode(idx, childNode)
        childNode.__level = self.level + 1
