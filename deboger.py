import microbes

class Debuger:
    def __init__(self):
        self.debug_output = open('output.csv','w')
        header = ('ID,ENERGY,COST,tout-droit,devant-droite,droite,derriere-droite,derriere,derriere-gauche,gauche,devant-gauche\n')
        self.debug_output.write(header)

    def activateDebugMode(self, v):
        self.isDebug = v

    def writeChild(self,geneSTR):
        if not self.isDebug:
            pass

        line = ('NewCHILD,,,' + str(geneSTR) + '\n')
        self.debug_output.write(line)

    def __del__(self):
        self.debug_output.close()
    
    def writeMicrobeInfos(self, microbe : microbes.Microbe, energy_used, geneSTR = ''):
        if not self.isDebug:
            pass

        if microbe.id !=1:
            pass
        microbe_id = microbe.id
        microbe_energy = microbe.energy
        line = (str(microbe_id) + ',' + str(microbe_energy) + ',-' + str(energy_used) + ',' + str(geneSTR) + '\n')
        self.debug_output.write(line)
