import os
import hou

def import_bgeo(**kwargs):

    path = kwargs["path"]
    root, f = os.path.split(path)
    f = f.split('.')[0]

    container = hou.node("/obj").createNode("geo", f)
    file_node = container.node("file1")
    file_node.setName(f + "_import")
    file_node.parm("file").set(path)

def preview_bgeo(**kwargs):

    print "preview_bgeo"
    print str(kwargs)

def reload_geo(**kwargs):
    
    path = kwargs["path"]
    files = hou.sopNodeTypeCategory().nodeType("file")
    for f in files.instances():
        parm = f.parm("file")
        if parm.eval() == path:
            f.parm("reload").pressButton()