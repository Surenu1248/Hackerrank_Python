import xml.etree.ElementTree as etree


maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    fn1=[]
    cnt=0
    fn2=[]
    for i in elem.iter():
        if i.tag not in fn2:
            fn2.append(i.tag)
            fn1.append(len(list(i)))
    for i in fn1:
        if i>0:
            cnt+=1
    maxdepth=cnt
    

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
