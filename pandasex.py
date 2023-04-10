import pandas as pd
import numpy as np
sal=pd.read_csv("Salaries.csv")
print(sal.head(),5)
meansaltpb=sal["TotalPayBenefits"].mean()
print(meansaltpb)
meansalbp=sal["BasePay"].mean(axis=0,skipna=True,numeric_only=True)



