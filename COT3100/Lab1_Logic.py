def conjunction(p,q):
    if p and q:
        return True
    return False
def disjunction(p,q):
    if p or q:
        return True
    return False
def negation(p):
    if not p:
        return True
    return False
def implication(p,q):
    if p:
        if p != q:
            return False
    return True
def exclusive_or(p,q):
    if p:
        if not q:
            return True
    elif q:
        if not p:
            return True
    return False
def biconditional(p,q):
    if p == q:
        return True
    return False

