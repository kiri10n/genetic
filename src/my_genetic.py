import random

def evaluate(gene):
    return sum(gene)

def epoch(present, epoch_count):
    print(f"epoch {epoch_count}")
    
    n = 10
    mutation_rate = 0.005

    for i in range(n):
        gene = []
        for j in range(10):
            gene.append(0 if random.random() > 0.5 else 1)
        present.append(gene)

    eval = [evaluate(gene) for gene in present]

    sorted_eval = sorted(eval, reverse=True)
    top = eval.index(sorted_eval[0])
    second = eval.index(sorted_eval[1])

    children = []
    for j in range(n):
        child = []
        for i in range(10):
            if random.random() > 0.5:
                child.append(present[top][i])
            else:
                child.append(present[second][i])
        
        if random.random() < mutation_rate:
            child[random.randrange(10)] ^= 1
        
        children.append(child)
    
    print(f"present_top {['{:.0f}'.format(x) for x in present[top]]}")
    return children
    
def main():
    max_epochs = 30
    present = []
    for i in range(max_epochs):
        children = epoch(present, i+1)
        present = children
    
    eval = [evaluate(gene) for gene in present]
    print(f"solution: {['{:.0f}'.format(x) for x in present[eval.index(max(eval))]]}")



if __name__ == "__main__":
    main()