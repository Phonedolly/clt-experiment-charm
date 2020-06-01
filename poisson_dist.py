import numpy as np
import scipy.stats as stats
import quantumrandom as qt
from tools import draw, sample, const

LAMBDA = 3

if __name__ == "__main__":
    randomNumber = sample.get_sample('poisson')  # 샘플 받아오기
    sum_of_samples = 0
    x_bars = np.zeros((const.EXPERIMENTS,))

    ''' 실험하기 '''
    # scpipy의 expon()에서 scale은 확률분포의 기댓값(1 / lambda)와 같다.
    for i in range(const.EXPERIMENTS):
        inverse_exp_sample = stats.poisson(mu=LAMBDA).ppf(randomNumber[i])
        for j in range(const.SAMPLES):
            sum_of_samples += inverse_exp_sample[j]

        x_bars[i] = sum_of_samples / const.SAMPLES
        sum_of_samples = 0

    draw.draw(x_bars, graph_title="Distribution of Samples of Posisson Distribution with $\\lambda$ = " + str(LAMBDA))
