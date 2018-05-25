import pickle

class Debugger():
    def record(self,**kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self,key).append(value)
            except AttributeError:
                setattr(self,key,[value])

    def save(self,key,filename):
        with open(filename,"wb") as f:
            pickle.dump(getattr(self,key),f)

debugger = Debugger()
record = debugger.record
