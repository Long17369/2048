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
            self.set[i][j] = random.choice([1,1,1,1,1,1,1,1,1,2])
            return True
        else:
            return False

    def print(self) -> None:
        """Print the game board"""
        for i in range(self.height):
            print(self.set[i])

    def move(self,type:tuple[RIGHT,DOWN]):
        if type[0] > 0 and not self.right():
            return
        elif type[0] < 0 and not self.left():
            return
        elif type[1] > 0 and not self.down():
            return
        elif type[1] < 0 and not self.up():
            return
        self.random_num()
        if self.is_print:
            self.print()

    def left(self) -> bool:
        """Move left"""
        ret = False
        for i in range(self.height):
            k = [n for n in self.set[i] if n!=0]
            for j in range(len(k)-1):
                if k[j] == k[j+1]:
                    k[j] += 1
                    k[j+1] = 0
            k = [n for n in k if n!=0]
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
            for j in range(len(k)-1,0,-1):
                if k[j] == k[j-1]:
                    k[j] += 1
                    k[j-1] = 0
            k = [n for n in k if n!=0]
            k = [0]*(self.width-len(k))+k
            if self.set[i] != k:
                self.set[i] = k
                ret = True
        return ret

    def up(self) -> bool:
        """Move up"""
        ret = False
        for j in range(self.width):
            k = [n[j] for n in self.set if n[j] != 0]
            for i in range(len(k)-1):
                if k[i] == k[i+1]:
                    k[i] += 1
                    k[i+1] = 0
            k = [n for n in k if n!=0]
            k += [0]*(self.height-len(k))
            if k == [n[j] for n in self.set]:
                continue
            for i in range(self.height):
                self.set[i][j] = k[i]
            ret = True
        return ret

    def down(self) -> bool:
        """Move down"""
        ret = False
        for j in range(self.width):
            k = [n[j] for n in self.set if n[j] != 0]
            k = [0]*(self.height-len(k)) + k
            for i in range(len(k)-1,0,-1):
                if k[i] == k[i-1]:
                    k[i] += 1
                    k[i-1] = 0
            k = [n for n in k if n!=0]
            k = [0]*(self.height-len(k)) + k
            if k == [n[j] for n in self.set]:
                continue
            for i in range(self.height):
                self.set[i][j] = k[i]
            ret = True
        return ret

if __name__ == '__main__':
    game = G2048()

else:
    print("snd.core imported")