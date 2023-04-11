import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 140576679 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы

    x  = x_success/x_cnt
    y = y_success/y_cnt

    p = ttest_ind(x, y, equal_var=False, alternative="less").pvalue
    
    if p < 0.02:
      return True
    else: 
      return False

