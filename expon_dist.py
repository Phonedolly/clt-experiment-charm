import numpy as np
import scipy.stats as stats
import quantumrandom as qt
from tools import draw, sample, const

LAMBDA = 0.1

if __name__ == "__main__":
    randomNumber = sample.get_sample('expon')  # 샘플 받아오기
    sum_of_samples = 0
    pHats = np.zeros((const.EXPERIMENTS,))

    ''' 실험하기 '''
    # scpipy의 expon()에서 scale은 확률분포의 기댓값(1 / lambda)와 같다.
    for i in range(const.EXPERIMENTS):
        inverse_exp_sample = stats.expon(scale=(1 / LAMBDA)).ppf(randomNumber[i])
        for j in range(const.SAMPLES):
            sum_of_samples += inverse_exp_sample[j]

        pHats[i] = sum_of_samples / const.SAMPLES
        sum_of_samples = 0

    draw.draw(pHats, graph_title="Distribution of Samples of Exponential Distribution with $\\lambda$ = " + str(LAMBDA))
