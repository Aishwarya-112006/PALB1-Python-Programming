'''Write an API that generates fancy sequences using the append, addAll, and multAll operations.

Implement the Fancy class:

Fancy() Initializes the object with an empty sequence.
void append(val) Appends an integer val to the end of the sequence.
void addAll(inc) Increments all existing values in the sequence by an integer inc.
void multAll(m) Multiplies all existing values in the sequence by an integer m.
int getIndex(idx) Gets the current value at index idx (0-indexed) of the sequence modulo 109 + 7. If the index is greater or equal than the length of the sequence, return -1.
 '''
class Fancy:

    def __init__(self):
        self.seq=[]
        self.add=0
        self.mult=1
        self.M=10**9+7
        

    def append(self, val: int) -> None:
        
        val=((val - self.add) % self.M) * pow(self.mult, -1, self.M) % self.M
        self.seq.append(val)
        

    def addAll(self, inc: int) -> None:
        self.add=(self.add+inc)%self.M
        

    def multAll(self, m: int) -> None:
        self.add=(self.add*m)%self.M
        self.mult=(self.mult*m)%self.M

    def getIndex(self, idx: int) -> int:
        if(idx>=len(self.seq)):
            return -1
        return(self.seq[idx]*self.mult+self.add)%self.M
        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
