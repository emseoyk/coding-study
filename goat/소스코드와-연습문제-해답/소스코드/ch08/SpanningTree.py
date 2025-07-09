# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 8장. 그래프


#=========================================================
# 코드 8.5: DFS를 이용한 신장트리(인접행렬 방식)

def ST_DFS(vtx, adj, s, visited) :
    visited[s] = True               # 현재 정점 s를 visited에 추가함
    for v in range(len(vtx)) :      # 인접행렬
        if adj[s][v] != 0 :         # 모든 간선 (s,v)에 대해
            if visited[v]==False:   # v를 아직 방문하지 않았으면 
                print("(", vtx[s], vtx[v], ")", end=' ')  # 간선 출력
                ST_DFS(vtx, adj, v, visited)


# DFS를 이용한 신장트리 테스트 프로그램
vtx = ['U','V','W','X','Y']
edge= [[0,  1,  1,  0,  0],
       [1,  0,  1,  1,  0],
       [1,  1,  0,  0,  1],
       [0,  1,  0,  0,  0],
       [0,  0,  1,  0,  0]]

print('ST_DFS_AM: ', end="")
ST_DFS(vtx, edge, 0, [False]*len(vtx))
print()