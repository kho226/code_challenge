import math
class Animation:
    @staticmethod
    def animate(speed,init):
        char_list = list(init)
        max_moves = 0
        for x in range (len(char_list)):
            tmp = 0
            if (char_list[x] == 'L'):
                tmp = float(x+1)/float(speed)
                ##print tmp
                max_moves = max(int(math.ceil(tmp)), max_moves)
                ##print max_moves
            elif (char_list[x] == 'R'):
                tmp = float((len(char_list)-x))/float(speed)
                ##print tmp
                max_moves = max(int(math.ceil(tmp)), max_moves)
        ##print max_moves
        Matrix = [['.' for x in range (len(char_list))] for x in range ((int(max_moves+1)))]

        
        for k in range(len(char_list)):
            position = char_list[k]
            j = k
            if (position == 'L'):
                for x in range(len(Matrix)):
                    if (j >= 0):
                        Matrix[x][j] = 'X';
                    else:
                        break
                    j = j - speed
            elif (position == 'R'):
                for x in range(len(Matrix)):
                    if (j < len(Matrix[x])):
                        Matrix[x][j] = 'X'
                    else:
                        break
                    j = j + speed
        for x in range(len(Matrix)):
            print ''.join(Matrix[x])
        
    ##print ''.join(map(str,Matrix))
                
            
            
                
        
    
