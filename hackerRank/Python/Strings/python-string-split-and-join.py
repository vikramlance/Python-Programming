#print raw_input()


class base(object):
    def __init__(self) :
        self.delemitor="-"
        self.splitter=" "
    @staticmethod        
    def splitString(string):
        string_new=string.split(self.splitter)
        joinString(string_new)
    def joinString(string):
        string=self.delemitor.join(string)
man = base()
a=raw_input()
man.splitString(a)

