import numpy as np
import quantumrandom as qt
import const


def get_sample():
    """ 퀀텀 난수를 가지는 2차원 배열을 반환한다 """

    # 서버에서 받아올 수 있는 배열의 최대길이가 1024이므로
    # 1024개씩 받아 chunk[]에 합친다
    chunk = np.array(qt.get_data(data_type='uint16', array_length=1024))
    chunk2 = np.array(qt.get_data(data_type='uint16', array_length=1024))
    chunk = np.concatenate((chunk, chunk2))

    randomNumber = np.zeros((const.EXPERIMENTS, const.SAMPLES))
    cnt = 0
    for i in range(const.EXPERIMENTS):
        for j in range(const.SAMPLES):
            randomNumber[i][j] = chunk[cnt]
            cnt += 1

    return randomNumber
