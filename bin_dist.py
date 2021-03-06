""" Binomial Distribution을 따르는 샘플로 실험 """

import numpy as np
from tools import draw, sample, const

if __name__ == "__main__":
    randomNumber = sample.get_sample('binomial')  # 샘플 받아오기
    x_bars = np.zeros((const.EXPERIMENTS,))
    X = 0

    ''' 실험하기 '''
    for i in range(const.EXPERIMENTS):
        for j in range(const.SAMPLES):
            # 짝수일 때를 카운트
            if randomNumber[i][j] % 2 == 0:
                X += 1
            else:
                pass
        x_bars[i] = X / const.SAMPLES
        X = 0

    ideal_mean = 1/2
    ideal_var = (1 / 2) * (1 / 2) * (1 / const.SAMPLES)

    draw.draw(x_bars, ideal_mean, ideal_var,
              graph_title="Distribution of Samples of Binomial Distribution with $p$ = 0.5")
