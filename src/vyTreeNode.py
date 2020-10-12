
class VyTreeNode1():
    def __init__(self):
        self.__childNodes = []
        self.__parent = None
        self.__level = 0
        self.__hasChildren = False
    
    @property
    def level(self):
        return self.__level

    @property
    def __level(self):
        return self.__level_

    @__level.setter
    def __level(self, level):
        self.__level_ = level
        for childNode in self.__childNodes:
            childNode.__level = level + 1

    @property
    def childNodes(self):
        return self.__childNodes

    @property
    def parent(self):
        return self.__parent

    @property
    def hasChildren(self):
        return self.__hasChildren

    def appendChildNode(self, childNode):
        self.insertChildNode(len(self.__childNodes), childNode)

    def insertChildNode(self, idx, childNode):
        self.__childNodes.insert(idx, childNode)
        self.__hasChildren = True
        childNode.__parent = self
        childNode.__level = self.level + 1

    @property
    def isFirstChild(self):
            if self.parent == None:
                return True
            elif self.parent.childNodes[0] == self:
                return True
            else:
                return False

    @property
    def isLastChild(self):
            if self.parent == None:
                return True
            elif self.parent.childNodes[-1] == self:
                return True
            else:
                return False

    def traverse(self):
        self.traversalState = 'pre'
        yield self
        for childNode in self.childNodes:
            for _ in childNode.traverse():
                yield _
        self.traversalState = 'post'
        yield self

class VyTreeNode():
    def __init__(self):
        self.__childNodes = []
        self.__parent = None
        self.__hasChildren = False
        super().__init__()
    
    @property
    def childNodes(self):
        return self.__childNodes

    @property
    def parent(self):
        return self.__parent

    @property
    def hasChildren(self):
        return self.__hasChildren

    def appendChildNode(self, childNode):
        self.insertChildNode(len(self.__childNodes), childNode)

    def insertChildNode(self, idx, childNode):
        self.__childNodes.insert(idx, childNode)
        self.__hasChildren = True
        childNode.__parent = self

    @property
    def isFirstChild(self):
            if self.parent == None:
                return True
            elif self.parent.childNodes[0] == self:
                return True
            else:
                return False

    @property
    def isLastChild(self):
            if self.parent == None:
                return True
            elif self.parent.childNodes[-1] == self:
                return True
            else:
                return False

    def traverse(self):
        self.traversalState = 'pre'
        yield self
        for childNode in self.childNodes:
            for _ in childNode.traverse():
                yield _
        self.traversalState = 'post'
        yield self
