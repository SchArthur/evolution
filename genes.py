import random

SUM_GEN_MAX = 8000
NBR_GEN = 8
GEN_MAX = SUM_GEN_MAX // NBR_GEN
GEN_MUTATION_MAX = 500
move_cost_array = [0,1,2,4,8,4,2,1]

# Fonctions utilitaires
def normalise(gene):
    """Normalise un gène sur GEN_MAX"""
    s = sum(gene)
    return [ int(x * SUM_GEN_MAX/s) for x in gene]

def gen_v():
    """renvoie une valeur de gène"""
    return random.randint(0,GEN_MAX)

# classe principale
class GeneMovement:
    def __init__(self, parentGene = None) -> None:
        self.gene = []
        if parentGene == None:
            self.createRandomGene()
        else:
            children_genes = parentGene.getGene()
            mutation = random.randint(0,GEN_MAX)-GEN_MAX//2
            indice = random.randrange(NBR_GEN)
            children_genes[indice] += mutation
            if children_genes[indice] < 0:
                children_genes[indice] = 0
            self.gene = normalise(children_genes)

    def mutateGene(self, gene):
        new_genes = gene
        i = random.randrange(len(new_genes))
        mutation = random.randint(- GEN_MUTATION_MAX, GEN_MUTATION_MAX)
        new_genes[i] += mutation
        if new_genes[i] < 0:
            new_genes[i] = 0

        new_genes = normalise(new_genes)
        self.gene = new_genes

    def createRandomGene(self):
        """Crée un gène aléatoire normalisé"""
        empty_gene = [gen_v() for _ in range(NBR_GEN)]
        self.gene = normalise(empty_gene)

    def __str__(self):
        """retourne sous forme de str le contenu du gène"""
        return str(self.gene)
    
    def getGeneLen(self) -> int:
        """renvoie la longueur totale du gene"""
        somme = 0
        for i in range(NBR_GEN):
            somme += self.gene[i]
        return somme
    
    def getGene(self):
        return self.gene
    
    def getGeneDirection(self):
        """renvoie la direction du gène"""
        rnd = random.randrange(self.getGeneLen())
        somme = 0
        for i in range(NBR_GEN):
            somme += self.gene[i]
            if somme > rnd:
                return i

"""
print(newGene(None))
gen1 = newGene([1000]*8) 
print(gen1)
print(gen1.getGeneDirection())
"""
