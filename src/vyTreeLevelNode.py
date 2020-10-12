from .vyTreeNode import VyTreeNode

class VyTreeLevelNode(VyTreeNode):
    def __init__(self):
        super().__init__()
        self.__level = 0

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
