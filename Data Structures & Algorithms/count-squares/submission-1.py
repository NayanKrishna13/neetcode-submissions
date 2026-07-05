class CountSquares:
    def __init__(self):
        self.points=defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)]+=1

    def count(self, point: List[int]) -> int:
        s=0
        point=tuple(point)
        for key in self.points:
            x_diff=-point[0]+key[0]
            y_diff=-point[1]+key[1]
            if abs(x_diff)==abs(y_diff) and x_diff!=0:
                s+=(self.points.get((key[0],point[1]),0)*self.points[key]*self.points.get((point[0],key[1]),0))
        return s


        
