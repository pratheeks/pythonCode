import xml.etree.ElementTree as ET

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if level==maxdepth:
        maxdepth+=1
        print(maxdepth)
    for child in elem:
        print(child)
        depth(child,level+1)

if __name__ == '__main__':
    tree = ET.parse('D:\sample.xml')
    root = tree.getroot()
    print(ET.tostring(root,encoding='utf8').decode('utf8'))
    depth(root, -1)
    print(maxdepth)