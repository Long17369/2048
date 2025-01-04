class G2048:
    RIGHT = int
    DOWN = int
    """2048 game class"""
    def __init__(self,width:int=4,height:int=4,is_print:bool=False) -> None:
        """Initialize the game"""
        self.width = width
        self.height = height
        self.is_print = is_print
        self.set : list[list[int]] = [[0 for _ in range(width)] for _ in range(height)]
        self.random_num()
        """### Game board
        - `set[i][j]` is the number at `(i,j)`
        #### Example
        - `0` `0` `2` `0`
        - `0` `0` `0` `0`
        - `0` `0` `0` `0`
        - `0` `0` `0` `0`
        - the number 2 is at `(0,2)`
        """

    def random_num(self) -> bool:
        """Generate a random number"""
        import random
        empty = [(i,j) for i in range(self.height) for j in range(self.width) if self.set[i][j]==0]
        if empty:
            i,j = random.choice(empty)
            self.set[i][j] = random.choice([2,4])
            return True
        else:
            return False

    def print(self) -> None:
        """Print the game board"""
        for i in range(self.height):
            print(self.set[i])

    def move(self,type:tuple[RIGHT,DOWN]):
        if type[0]:
            if type[0]>0:
                if not self.right():
                    return
                if self.merge(0):
                    self.right()
            else:
                if not self.left():
                    return
                if self.merge(0):
                    self.left()
        else:
            if type[1]>0:
                if not self.down():
                    return
                if self.merge(1):
                    self.down()
            else:
                if not self.up():
                    return
                if self.merge(1):
                    self.up()
        self.random_num()
        if self.is_print:
            self.print()

    def left(self) -> bool:
        """Move left"""
        ret = False
        for i in range(self.height):
            k = [n for n in self.set[i] if n!=0]
            k += [0]*(self.width-len(k))
            if self.set[i] != k:
                self.set[i] = k
                ret = True
        return ret

    def right(self) -> bool:
        """Move right"""
        ret = False
        for i in range(self.height):
            k = [n for n in self.set[i] if n!=0]
            k = [0]*(self.width-len(k))+k
            if self.set[i] != k:
                self.set[i] = k
                ret = True
        if(self.merge(0)):
            self.right()
        return ret

    def up(self) -> bool:
        """Move up"""
        ret = False
        for j in range(self.width):
            k = [n[j] for n in self.set if n[j] != 0]
            k += [0]*(self.height-len(k))
            for i in range(self.height):
                if self.set[i][j] != k[i]:
                    self.set[i][j] = k[i]
                    ret = True
        if(self.merge(1)):
            self.up()
        return ret

    def down(self) -> bool:
        """Move down"""
        ret = False
        for j in range(self.width):
            k = [n[j] for n in self.set if n[j] != 0]
            k = [0]*(self.height-len(k)) + k
            for i in range(self.height):
                if self.set[i][j] != k[i]:
                    self.set[i][j] = k[i]
                    ret = True
        if(self.merge(1)):
            self.down()
        return ret

    def merge(self,type:int) -> bool:
        ret = False
        if type == 0:
            for i in range(self.height):
                for j in range(1,self.width):
                    if self.set[i][j]==0:
                        continue
                    if self.set[i][j]==self.set[i][j-1]:
                        self.set[i][j-1]*=2
                        self.set[i][j]=0
                        ret = True
        elif type == 1:
            for j in range(self.width):
                for i in range(1,self.height):
                    if self.set[i][j]==0:
                        continue
                    if self.set[i][j]==self.set[i-1][j]:
                        self.set[i-1][j]*=2
                        self.set[i][j]=0
                        ret = True
        return ret

if __name__ == '__main__':
    game = G2048()

else:
    print("snd.core imported")