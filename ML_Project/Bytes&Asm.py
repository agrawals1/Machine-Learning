import os
import pandas as pd
import random
import shutil
# _ = [1,2,3,4,5,6,7,8,9]
# for foldr in _:
#     All_asm = os.listdir(f"./Data/{foldr}/asm")
#     All_byte = os.listdir(f"./Data/{foldr}/bytes")
#     asm_42 = random.sample(All_asm, 42)
#     for asmfile in asm_42:
#         asmpth = f"./Data/{foldr}/asm/{asmfile}"
#         bytepth = f"./Data/{foldr}/bytes/{asmfile[:-4]}" + ".bytes"
#         shutil.copy(asmpth, f"./Reduced_Data/asms/{asmfile}")
#         shutil.copy(bytepth, f"./Reduced_Data/bytes/{asmfile[:-4]}" + ".bytes")

# df = pd.DataFrame(columns=["Id", "Class"])
# _ = [1,2,3,4,5,6,7,8,9]
# for foldr in _:
#     for i in range(os.listdir(""))
df_big = pd.read_csv("./Data/trainLabels.csv")
df_small = pd.DataFrame(columns=["Id", "Class"])
for i in os.listdir("./train/asms"):
    df_small = pd.concat([df_small, df_big.loc[df_big["Id"] == f"{i[:-4]}"]], ignore_index=True)
df_small.to_csv("trainLabels.csv")  





        
