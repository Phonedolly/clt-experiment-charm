""" 히스토그램과 그에 맞는 정규분포 그래프를 그린다 """

import math
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from tools import const


def draw(x_bars, ideal_mean, ideal_var, graph_title):
    idel_std_deviation = math.sqrt(ideal_var)
    sample_mean = x_bars.mean()  # 표본평균
    sample_variance = x_bars.var(ddof=1)  # 표본분산. ddof=1 옵션을 주면 N-1로 나누게된다
    # std_deviation = math.sqrt(variance)  # 표본표준편차
    axis_x = np.linspace(sample_mean - 3 * idel_std_deviation, sample_mean + 3 * idel_std_deviation)  # 그래프가 가질 x축

    fig, ax1 = plt.subplots()

    ''' 히스토그램 세팅 '''
    color = 'xkcd:lightgreen'
    # ax1.set_xlabel("class of $\\bar X_{i}$")
    ax1.set_xlabel(
        "ideal mean: " + str(round(ideal_mean, 5)) + "   ideal variance: " + str(
            round(ideal_var, 5)) + "\nsample mean: " + str(round(
            sample_mean, 5)) + "   sample variance: " + str(round(sample_variance, 5)))
    ax1.set_ylabel("num of $\\bar X_{i}$ for each class")
    bins = math.floor(math.log2(const.EXPERIMENTS)) + 1  # Sturges' formula로 적절한 계급의 수 구하기
    ax1.hist(x_bars, bins=bins, histtype='bar', label="num of $\\bar X_{i}$ for each class", color=color)
    ax1.set_xlim(xmin=0)
    ax1.set_ylim(ymin=0)

    ''' 정규분포 세팅 '''
    color = 'xkcd:fuchsia'
    ax2 = ax1.twinx()  # ax1과 x축을 공유하고 y축은 따로 쓴다

    gaussian_label = "N(" + str(round(sample_mean, 2)) + ", " + str(round(ideal_var, 5)) + ")"
    gaussian = stats.norm(ideal_mean, idel_std_deviation).pdf(axis_x)
    ax2.set_ylabel(gaussian_label)
    ax2.plot(axis_x, gaussian, label=gaussian_label, color=color)
    ax2.set_ylim(ymin=0)

    ''' legend 지정, 나머지 작업 처리 '''
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    lines = lines_1 + lines_2
    labels = labels_1 + labels_2
    plt.legend(lines, labels, loc=0)

    plt.title(graph_title)
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()
