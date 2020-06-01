import math
import numpy as np
import quantumrandom as qt
from tools import const


def get_sample(dist_type):
    """ 퀀텀 난수를 가지는 2차원 배열을 반환한다 """

    if dist_type == 'poisson' or dist_type == 'expon':
        random_number = np.zeros((const.EXPERIMENTS, const.SAMPLES))
        cached_generator = qt.cached_generator()  # chached_generator를 생성하면 서버 딜레이를 회피할 수 있다
        for i in range(const.EXPERIMENTS):
            for j in range(const.SAMPLES):
                random_number[i][j] = qt.randfloat(0, 1, cached_generator)  # cached_generator로 0에서 1사이의 값을 생성한다

    elif dist_type == 'binomial':
        random_number = np.zeros((const.EXPERIMENTS, const.SAMPLES))
        cached_generator = qt.cached_generator()  # chached_generator를 생성하면 서버 딜레이를 회피할 수 있다

        for i in range(const.EXPERIMENTS):
            for j in range(const.SAMPLES):
                random_number[i][j] = math.ceil(
                    qt.randfloat(0, 10, cached_generator))  # 홀수인 경우는 1, 3, 5, 7, 9, 짝수인 경우는 2, 4, 6, 8, 10이 된다

    else:
        raise Exception("Invalid distribution type. Allowed types are 'poisson', 'expon', 'binomial'.")

    return random_number
