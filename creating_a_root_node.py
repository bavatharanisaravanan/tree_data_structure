class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def printtree(self):
        print(self.data)
root=node(10)
root.printtree()
