def solution(lottos, win_nums):
    jackpot = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    jackpot_num = 0
    zero_num = 0
    for l_num in lottos:
        if l_num == 0:
            zero_num += 1
        for w_num in win_nums:
            if l_num == w_num:
                jackpot_num += 1
    min = jackpot[jackpot_num]
    max = jackpot[jackpot_num + zero_num]
    return [max, min]
