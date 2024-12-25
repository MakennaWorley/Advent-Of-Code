# day 21
import re
import heapq


def ints(s):
    return [int(x) for x in re.findall(r'-?\d+', s)]


def getPad1(count):
    r,c = count
    if not (0<=r<len(pad1) and 0<=c<len(pad1[r])):
        return None
    
    if pad1[r][c]==' ':
        return None
    
    return pad1[r][c]


def getPad2(p):
    r,c = p
    if not (0<=r<len(pad2) and 0<=c<len(pad2[r])):
        return None
    
    if pad2[r][c]==' ':
        return None
    
    return pad2[r][c]


def applyPad1(p, move):
    if move == 'A':
        return (p, getPad1(p))
    
    elif move=='<':
        return ((p[0], p[1]-1), None)
    
    elif move=='^':
        return ((p[0]-1, p[1]), None)
    
    elif move=='>':
        return ((p[0], p[1]+1), None)
    
    elif move=='v':
        return ((p[0]+1, p[1]), None)


def applyPad2(p, move):
    if move == 'A':
        return (p, getPad2(p))
    
    elif move=='<':
        return ((p[0], p[1]-1), None)
    
    elif move=='^':
        return ((p[0]-1, p[1]), None)
    
    elif move=='>':
        return ((p[0], p[1]+1), None)
    
    elif move=='v':
        return ((p[0]+1, p[1]), None)


def solve(code,pads):
    start = [0, (3,2), 'A', '', '']
    queue = []
    heapq.heappush(queue, start)
    visited = {}
    
    while queue:
        d,count,count2,out,path = heapq.heappop(queue)
        assert count2 in ['<', '>', 'v', '^', 'A']
        if out==code:
            return d
        
        if not code.startswith(out):
            continue
            
        if getPad1(count) is None:
            continue
            
        key = (count,count2,out)
        if key in visited:
            assert d>=visited[key], f'{key=} {d=} {visited[key]=}'
            continue
            
        visited[key] = d
        for move in ['^', '<', 'v', '>', 'A']:
            new_out = out
            new_count, output = applyPad1(count, move)
            if output is not None:
                new_out = out + output
                
            cost_move = cost2(move,count2,pads)
            new_path = path #+ cost_move
            assert cost_move >= 0
            heapq.heappush(queue, [d+cost_move, new_count, move, new_out, new_path])


def cost2(ch, prev_move, pads):
    key = (ch,prev_move, pads)
    if key in dict:
        return dict[key]
    
    if pads==0:
        return 1
    
    else:
        assert ch in ['^', '>', 'v', '<', 'A']
        assert prev_move in ['^', '>', 'v', '<', 'A']
        assert pads>=1
        queue = []
        start_pos = {'^': (0,1), '<': (1,0), 'v': (1,1), '>': (1,2), 'A': (0,2)}[prev_move]
        heapq.heappush(queue, [0, start_pos, 'A', '', ''])
        visited = {}
        
        while queue:
            d,p,prev,out,path = heapq.heappop(queue)
            if getPad2(p) is None:
                continue
                
            if out == ch:
                dict[key] = d
                return d
            
            elif len(out)>0:
                continue
                
            seen_key = (p,prev)
            if seen_key in visited:
                assert d>=visited[seen_key]
                continue
                
            visited[seen_key] = d
            for move in ['^', '<', 'v', '>', 'A']:
                new_p, output = applyPad2(p, move)
                cost_move = cost2(move, prev, pads-1)
                new_d = d + cost_move
                new_path = path
                new_out = out
                if output is not None:
                    new_out = new_out + output
                    
                heapq.heappush(queue, [new_d, new_p, move, new_out, new_path])
                
        assert False, f'{ch=} {pads=}'


count = 0
count2 = 0

ans = 0
text = open('inputs/day21_input.txt').read().strip()

pad1 = ['789', '456', '123', ' 0A']
pad2 = [' ^A', '<v>']
dict = {}

for line in text.split('\n'):
    s1 = solve(line, 2)
    s2 = solve(line, 25)
    line_int = ints(line)[0]
    count += line_int * s1
    count2 += line_int * s2
    
print(count)
print(count2)