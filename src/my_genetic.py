import random
import math

def evaluate(gene):
    return sum(gene)

def epoch(present, epoch_count, gene_num):
    print(f"epoch {epoch_count}")
    
    mutation_rate = 0.05

    eval = [evaluate(gene) for gene in present]
    weights = list(map(math.exp, eval))
    print(f"weight {weights}")

    children = []
    for j in range(gene_num):
        child = []
        parents = random.choices(present, k=2, weights=weights)
        pivot = random.randrange(1, 10)

        child = parents[0][:pivot] + parents[1][pivot:]
        
        if random.random() < mutation_rate:
            child[random.randrange(10)] ^= 1
        
        children.append(child)
    
    print(f"present_top {['{:.0f}'.format(x) for x in present[eval.index(max(eval))]]}")
    return children
    
def main():
    max_epochs = 100
    gene_num = 10
    present = []
    for i in range(gene_num):
        gene = []
        for j in range(10):
            gene.append(0 if random.random() > 0.3 else 1)
        present.append(gene)
    
    print(present)

    for i in range(max_epochs):
        children = epoch(present, i+1, gene_num)
        present = children
    
    print(present)

    eval = [evaluate(gene) for gene in present]
    print(f"solution: {['{:.0f}'.format(x) for x in present[eval.index(max(eval))]]}")



if __name__ == "__main__":
    main()