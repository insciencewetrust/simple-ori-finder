import matplotlib.pyplot as plt

def Skew(DNASeq):
    totalSkew=0
    totalSkewList=[0]
    positionList=[0]
    DNASeqCopy=DNASeq.lower()
    for i in range(0, len(DNASeqCopy)):
        if DNASeqCopy[i]=="g":
            totalSkew+=1
        elif DNASeqCopy[i]=="c":
            totalSkew-=1
        else:
            pass
        totalSkewList.append(totalSkew)
        positionList.append(i+1)
    skewMap={"positions": positionList, "skews": totalSkewList}
    return skewMap

def oriFinder(DNASeq):
    skewMap=Skew(DNASeq)
    """ #Optional plotting of skew
    plt.plot(skewMap["positions"], skewMap["skews"])
    plt.show()
    """
    idxList=[]
    oriList=[]
    minSkew=min(skewMap["skews"])
    for i in range(0, len(skewMap["skews"])):
        if (skewMap["skews"])[i]==minSkew:
            idxList.append(i)
        else:
            pass
    for a in range(0, len(idxList)):
        oriList.append((skewMap["positions"])[idxList[a]])
    return oriList

f=open("E_coli.txt")
genome=f.read().strip()
f.close()

oriList=oriFinder(genome)
print(*oriList)