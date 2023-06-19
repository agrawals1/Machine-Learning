import pandas as pd
import os
import shutil

df = pd.read_csv("trainLabels.csv")
for i in range(len(df)):
    fasm = str(df.loc[i, "Id"]) + '.asm'
    fbyte = str(df.loc[i, "Id"]) + '.bytes'
    fclass = df.loc[i, "Class"]
    if os.path.exists(f'./{fclass}'):
        if fasm in os.listdir('./train'):
                shutil.move(f'./train/{fasm}', f'./{fclass}/asm/{fasm}')
        else:
            print(f'{fasm} does not exist in train data')   

        if fbyte in os.listdir('./train'):
                shutil.move(f'./train/{fbyte}', f'./{fclass}/bytes/{fbyte}')
        else:
            print(f'{fbyte} does not exist in train data')        

          
    else:
        os.mkdir(f'./{fclass}')
        os.mkdir(f'./{fclass}/asm')
        os.mkdir(f'./{fclass}/bytes')
        shutil.move(f'./train/{fasm}', f'./{fclass}/asm/{fasm}')
        shutil.move(f'./train/{fbyte}', f'./{fclass}/bytes/{fbyte}')

