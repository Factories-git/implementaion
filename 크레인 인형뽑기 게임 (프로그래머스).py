def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        i -= 1
        for j in range(len(board)):
            if board[j][i] == 0:
                continue
            basket.append(board[j][i])
            board[j][i] = 0
            break
        if len(basket) > 1:
            if basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                answer += 2
    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], 	[1,5,3,5,1,2,1,4]))