class base(object):
    def __init__(self) :
        self.delemitor="-"
        self.splitter=" "    
            
    def splitString(self, a):
        string_new=a.split(self.splitter)
        #print string_new
        self.joinString(string_new)
    def joinString(self, str):
        str=self.delemitor.join(str)
        print str
raw = base()
raw.splitString(raw_input())
