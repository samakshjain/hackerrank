def next_move(posx, posy, dimx, dimy, board):
    min_cord=[]
    dist=[]
    dirt =[]
#find dirt particles on the board
    for x in range(dimx) :
        for y in range(dimy):
            if board[x][y]=='d':
                dirt.append([x,y])
    
#find distance to dirt particles relative to bot
    for x in range(len(dirt)):
        dist.append(abs(dirt[x][0]-posx)   + abs(dirt[x][1]-posy))
      
#find closest dirt particle(s) from the list dist
    for op in range(len(dist)):
        if min(dist)==dist[op]:
            min_cord.append(dirt[op])
            #break
   
    if ((min_cord[0][0]-posx)>0):
        #move_down(posx,posy)
        print "DOWN"
    elif ((min_cord[0][0]-posx)<0):
        #move_up(posx,posy)
        print "UP"
    elif ((min_cord[0][0]-posx)==0):
        if((min_cord[0][1]-posy)>0):
            print "RIGHT"
            #move_right(posx,posy)
        elif((min_cord[0][1]-posy<0)):
            print "LEFT"
            #move_left(posx,posy)
        else:
            print "CLEAN" 
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    dim = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)