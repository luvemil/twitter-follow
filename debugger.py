import pickle

class Debugger():
    def __init__(self):
        self.debugging=False
    def _record(self,**kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self,key).append(value)
            except AttributeError:
                setattr(self,key,[value])

    def record(self,**kwargs):
        if self.debugging:
            self._record(**kwargs)
        else:
            return None

    def save(self,key,filename):
        with open(filename,"wb") as f:
            try:
                pickle.dump(getattr(self,key),f)
            except AttributeError:
                return None

    def set_debugging(self,flag=True):
        self.debugging=flag

debugger = Debugger()
record = debugger.record
