import random

def evaluate(gene):
    return sum(gene)

def epoch(present):
    n = 10
    mutation_rate = 0.005

    for i in range(n):
        present.append([random.random()] * 10)

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
            child[random.randrange(10)] = random.random()
        
        children.append(child)
    
    return children
    
def main():
    max_epochs = 10
    present = []
    for i in range(max_epochs):
        children = epoch(present)
        present = children
    
    eval = [evaluate(gene) for gene in present]
    print(present[eval.index(max(eval))])



if __name__ == "__main__":
    main()