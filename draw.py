import math
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import const

def draw(pHats, hist_label):
    """ 히스토그램과 그에 맞는 정규분포 그래프를 그린다 """
    # # Sturges' formula로 적절한 계급 구하기
    # numOfBins = math.floor(math.log2(EXPERIMENTS)) + 1
    # # Square-root choice
    # numOfBins = math.floor(math.sqrt(EXPERIMENTS))
    numOfBins = 9  # 계급의 수는 9로

    p = np.mean(pHats)  # 정규분포의 평균
    variance = p * (1 - p) / const.EXPERIMENTS  # 정규분포의 분산
    std_deviation = math.sqrt(variance)  # 정규분포의 표준편차
    axis_x = np.linspace(p - 3 * std_deviation, p + 3 * std_deviation)  # 그래프가 가질 x축

    fig, ax1 = plt.subplots()
    # 히스토그램 세팅
    color = 'xkcd:salmon'
    ax1.set_ylabel(hist_label)

    ax1.hist(pHats, bins=numOfBins, label=hist_label,range=[0,1],  color=color)
    ax1.set_xlim(xmin=0,xmax=1)
    ax1.set_ylim(ymin=0)
    # y_axis2.tick_params(axis='y', labelcolor=color)

    # 정규분포 세팅
    color = 'xkcd:yellowgreen'
    gaussian_label = "N(" + str(round(p, 2)) + ", " + str(round(variance, 5)) + ")"
    gaussian = stats.norm(p, std_deviation).pdf(axis_x)

    ax2 = ax1.twinx()  # 히스토그램이 가지는 y축
    ax2.set_ylabel(gaussian_label)
    ax2.plot(axis_x, gaussian, label=gaussian_label, color=color)
    ax2.set_ylim(ymin=0)

    # legend
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    lines = lines_1+lines_2
    labels = labels_1+labels_2
    plt.legend(lines, labels, loc=0)
    plt.show()