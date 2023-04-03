import pandas as pd
import numpy as np


chat_id = 544835691 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return 459+np.log(np.mean(x)) - (np.log((np.std(x))**2/(np.mean(x))**2 + 1))**2/2 # Ваш ответ
