import numpy as np
import quantum_sample as qs
import draw
import const

if __name__ == "__main__":
    randomNumber = qs.get_sample()  # 샘플 받아오기
    pHats = np.zeros((const.EXPERIMENTS,))
    X = 0

    ''' 실험하기 '''
    for i in range(const.EXPERIMENTS):
        for j in range(const.SAMPLES):
            if randomNumber[i][j] % 2 == 0:
                X += 1
            else:
                pass
        pHats[i] = X / const.SAMPLES
        X = 0

    draw.draw(pHats, "num of success")
