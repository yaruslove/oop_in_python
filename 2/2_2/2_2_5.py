
class TreeObj:
    def __init__(self, indx, value=None):
        self.indx=indx
        self.value=value
        self.__left=None
        self.__right=None
        
    @property
    def left(self):
        return self.__left
    
    @left.setter
    def left(self,branch):
        self.__left=branch
        
    @property
    def right(self):
        return self.__right
    
    @right.setter
    def right(self,branch):
        self.__right=branch


class DecisionTree:
    dict_indx=dict()
    
    @classmethod
    def predict(cls, root, x):
        
        if x[root.indx]==1: # left
            next_node=DecisionTree.dict_indx[root.indx].left ## 0==root-node
        else:
            next_node=DecisionTree.dict_indx[root.indx].right ## 0==root-node, next-node - point to next TreeObj
        
        while True:
            if x[next_node.indx]==1: ## answer True/False or same Right/Left
                next_node=DecisionTree.dict_indx[next_node.indx].left
            else:
                next_node=DecisionTree.dict_indx[next_node.indx].right
            if next_node.indx==-1:
                return next_node.value
        
        
    @classmethod    
    def add_obj(cls, obj, node=None, left=True):
        DecisionTree.dict_indx[obj.indx]=obj
        if node!=None:
            if left==True:
                node.left=obj
            else:
                node.right=obj
        return obj

    
    
root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x) # будет программистом