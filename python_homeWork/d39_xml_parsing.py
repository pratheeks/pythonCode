import sys
import xml.etree.ElementTree as ET

def get_attr_number(node):
    c=len(node.attrib)
    # your code goes here
    print(ET.tostring(node,encoding='utf8').decode('utf8'))
    for child in node:
        print(child.attrib)
        # c+=(len(child.attrib))
        c+=get_attr_number(child)
    return c

if __name__ == '__main__':
    tree = ET.parse('D:\sample.xml')
    root = tree.getroot()
    print(get_attr_number(root))