from loguru import logger
logger.add("log.log",rotation="10 MB",level="TRACE")

class G2048:
    RIGHT = int
    DOWN = int
    """2048 game class"""
    def __init__(self,width:int=4,height:int=4) -> None:
        """Initialize the game"""
        self.width = width
        self.height = height
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
        logger.info("G2048 : GENERATING RANDOM NUMBER")
        import random
        empty = [(i,j) for i in range(self.height) for j in range(self.width) if self.set[i][j]==0]
        if empty:
            i,j = random.choice(empty)
            self.set[i][j] = random.choice([1,1,1,1,1,1,1,1,1,2])
            logger.info(f"G2048 : RANDOM NUMBER GENERATED AT ({i},{j}) ,RANDOM NUMBER IS {self.set[i][j]}")
            return True
        else:
            logger.error("G2048 : NO EMPTY SPACE FOR RANDOM NUMBER")
            return False

    def check(self) -> bool:
        """Check game is stop"""
        for i in range(self.height):
            for j in range(self.width):
                if self.set[i][j] == 0:
                    return True
                if i>0 and self.set[i][j] == self.set[i-1][j]:
                    return True
                if j>0 and self.set[i][j] == self.set[i][j-1]:
                    return True
        logger.info("G2048 : GAME OVER")
        return False

    def print(self) -> None:
        """Print the game board"""
        logger.info("{:=^50}".format(""))
        [logger.info(" ".join(["%6d"%(1<<j if j>0 else 0) for j in self.set[i]])) for i in range(self.height)]
        logger.info("{:=^50}".format(""))

    def move(self,type:tuple[RIGHT,DOWN]) -> bool:
        if type[0] > 0 and not self.right():
            logger.info("G2048 : MOVE NOT RIGHT")
            return False
        elif type[0] < 0 and not self.left():
            logger.info("G2048 : MOVE NOT LEFT")
            return False
        elif type[1] > 0 and not self.down():
            logger.info("G2048 : MOVE NOT DOWN")
            return False
        elif type[1] < 0 and not self.up():
            logger.info("G2048 : MOVE NOT UP")
            return False
        self.random_num()
        self.print()
        if all(all(self.set[i]) for i in range(self.height)):
            self.run = False
        return True

    def left(self) -> bool:
        """Move left"""
        logger.info("G2048 : MOVE LEFT")
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
        logger.info("G2048 : MOVE RIGHT")
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
        logger.info("G2048 : MOVE UP")
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
        logger.info("G2048 : MOVE DOWN")
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
    logger.info("G2048 : IMPORTED")
