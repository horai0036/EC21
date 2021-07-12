# 進化型計算特論  第 13 回課題
## 2210104071 寳来輝弥

### New Operator
2つの親に対しマスクを1つずつ用意し，それぞれで一様交叉のような操作を行った．

```
def my_new(ind1, ind2):
    offspring1 = []
    offspring2 = []
    for i in range(len(ind1)):
        p = random.random()
        if p < 0.5:
            offspring1.append(ind1[i])
        else:
            offspring1.append(ind2[i])
    for i in range(len(ind1)):
        p = random.random()
        if p < 0.5:
            offspring2.append(ind1[i])
        else:
            offspring2.append(ind2[i])
    return offspring1, offspring2
```