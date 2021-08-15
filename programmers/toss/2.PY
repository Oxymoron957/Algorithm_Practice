"""
나만의 L4 만들기
"""

def solution(servers, sticky, requests):
    server = {}
    for s in range(1, servers+1):
        server[s] = []

    if sticky:
        turn = 1
        for r in requests:
            isSticky = False
            for key, li in enumerate(server.values()):
                key+=1
                if r in li:
                    server.get(key).append(r)
                    isSticky = True
                    break
            if not isSticky:
                server.get(turn).append(r)
                turn += 1
                if turn > servers:
                    turn = 1
                
            
    else:
        turn = 1
        for r in requests:
            server.get(turn).append(r)
            turn += 1
            if turn > servers:
                turn = 1
    
    return list(server.values())



servers = 2
sticky = True
requests = [1,2,2,3,4,1]

result = solution(servers, sticky, requests)

print(result)