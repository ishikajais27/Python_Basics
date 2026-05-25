#A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
#UP 5    DOWN 3     LEFT 3      RIGHT 2        o/p -  2 (for up add down subtract and for left subtract and right add )
#first value → left/right position (x)     second value → up/down position (y)  y = +5  -> y = 5-3 = 2 -> x = -3 -> x =-3+2 = -1,
# final position = (-1,2)
# -> o/p = distance formual (under root xsq+ ysq) 
class Robot:

    def move(self):

        x = 0
        y = 0

        for i in range(4):

            print("1.UP")
            print("2.DOWN")
            print("3.LEFT")
            print("4.RIGHT")

            choice = int(input("Enter option: "))
            step = int(input("Enter steps: "))

            match choice:

                case 1:
                    y = y + step

                case 2:
                    y = y - step

                case 3:
                    x = x - step

                case 4:
                    x = x + step

        distance = ((x*x) + (y*y)) ** 0.5

        print(round(distance))


obj = Robot()

obj.move()