import pytest
from vyTree import VyTreeDataNode

def test_001():
    root = VyTreeDataNode(0)
    assert(root.childNodes == [])
    assert(root.level == 0)
    assert(root.hasChildren == False)
    assert(root.parent == None)
    assert(root.level == 0)
    with pytest.raises(AttributeError):
        root.level = 1
    assert(root.level == 0)
    with pytest.raises(AttributeError):
        root.childNodes = 1
    assert(root.childNodes == [])
    assert(root.data == 0)
    
    # add a child
    child0 = VyTreeDataNode(1)
    assert(child0.childNodes == [])
    assert(child0.level == 0)
    assert(child0.hasChildren == False)
    assert(child0.parent == None)
    assert(child0.data == 1)
    root.appendChildNode(child0)
    assert(root.childNodes[0] == child0)
    assert(root.hasChildren == True)
    assert(root.level == 0)
    assert(root.parent == None)
    assert(root.data == 0)
    assert(child0.childNodes == [])
    assert(child0.level == 1)
    assert(child0.hasChildren == False)
    assert(child0.parent is root)
    assert(child0.data == 1)

    # add another child
    child1 = VyTreeDataNode(2)
    root.appendChildNode(child1)
    assert(root.childNodes[0] is child0)
    assert(root.childNodes[1] is child1)
    assert(root.hasChildren == True)
    assert(child0.data == 1)
    assert(child1.data == 2)

    # insert a child in the beginning
    child2 = VyTreeDataNode(3)
    root.insertChildNode(0, child2)
    assert(root.childNodes[0] is child2)
    assert(root.childNodes[1] is child0)
    assert(root.childNodes[2] is child1)
    assert(root.hasChildren == True)
    assert(root.childNodes[0].data == 3)
    assert(root.childNodes[1].data == 1)
    assert(root.childNodes[2].data == 2)

    # insert a child with a children
    child3 = VyTreeDataNode(4)
    gchild0 = VyTreeDataNode(5)
    gchild1 = VyTreeDataNode(6)
    assert(child3.level == 0)
    assert(gchild0.level == 0)
    assert(gchild1.level == 0)
    child3.appendChildNode(gchild0)
    child3.appendChildNode(gchild1)
    assert(child3.level == 0)
    assert(gchild0.level == 1)
    assert(gchild1.level == 1)
    root.appendChildNode(child3)
    assert(child3.level == 1)
    assert(gchild0.level == 2)
    assert(gchild1.level == 2)

    assert(root.childNodes[0] is child2)
    assert(root.childNodes[1] is child0)
    assert(root.childNodes[2] is child1)
    assert(root.childNodes[3] is child3)
    assert(root.hasChildren == True)
    assert(root.childNodes[0].data == 3)
    assert(root.childNodes[1].data == 1)
    assert(root.childNodes[2].data == 2)
    assert(root.childNodes[3].data == 4)
    assert(root.childNodes[3].childNodes[0].data == 5)
    assert(root.childNodes[3].childNodes[1].data == 6)

if __name__ == '__main__':
    pytest.main()
