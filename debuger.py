from setting import *
import datetime

def CSV_line(values) -> str :
    line = ""
    for value in values:
        line += str(value)
        line += ","
    line += '\n'
    return line

class Debuger:
    def __init__(self):
        self.content = ""

    def activateDebugMode(self, v):
        self.isDebug = v

    def microbesSpawnDebug(self, microbe):
        if DEBUG_MODE:
            values_list = []
            values_list.append(microbe.id)
            values_list.append(microbe.gene.getGene())
            values_list.append(microbe.gene.getGeneLen())

            self.content += CSV_line(values_list)


    def write_content(self):
        self.debug_output = open('output.csv','w')

        # now = datetime.datetime.now()
        # footer = ('Debug du,'+ str(now) + "\n")
        # self.content += footer

        self.debug_output.write(self.content)

        self.debug_output.close()

mainDebugger = Debuger()