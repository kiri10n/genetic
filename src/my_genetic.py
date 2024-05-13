import random
import math

def evaluate(gene):
    return sum(gene)

def epoch(present, epoch_count, gene_num, gene_len):
    print(f"epoch {epoch_count}")
    
    mutation_rate = 0.05

    eval = [evaluate(gene) for gene in present]
    weights = list(map(math.exp, eval))
    #print(f"weight {weights}")

    children = []
    for j in range(gene_num):
        child = []
        parents = random.choices(present, k=2, weights=weights)
        pivot = random.randrange(1, gene_len)

        child = parents[0][:pivot] + parents[1][pivot:]
        
        if random.random() < mutation_rate:
            child[random.randrange(gene_len)] ^= 1
        
        children.append(child)
    
    print(f"present_top {['{:.0f}'.format(x) for x in present[eval.index(max(eval))]]}")
    return children
    
def main():
    max_epochs = 200
    gene_num = 10
    gene_len = 20
    present = []
    for i in range(gene_num):
        gene = []
        for j in range(gene_len):
            gene.append(0 if random.random() > 0.5 else 1)
        present.append(gene)
    
    #print(present)

    for i in range(max_epochs):
        children = epoch(present, i+1, gene_num, gene_len)
        present = children
    
    #print(present)

    eval = [evaluate(gene) for gene in present]
    print(f"solution: {['{:.0f}'.format(x) for x in present[eval.index(max(eval))]]}")



if __name__ == "__main__":
    main()