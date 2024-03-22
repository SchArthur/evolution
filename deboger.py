import microbes

debug_output = open('output.csv','w')

header = ('ID,ENERGY,COST,tout-droit,devant-droite,droite,derriere-droite,derriere,derriere-gauche,gauche,devant-gauche\n')
debug_output.write(header)

def writeMicrobeInfos(microbe : microbes.Microbe, energy_used, geneSTR = ''):
    microbe_id = microbe.id
    microbe_energy = microbe.energy
    line = (str(microbe_id) + ',' + str(microbe_energy) + ',-' + str(energy_used) + ',' + str(geneSTR) + '\n')
    debug_output.write(line)

def writeChild(geneSTR):
    line = ('NewCHILD,,,' + str(geneSTR) + '\n')
    debug_output.write(line)

def closeFile():
    debug_output.close()