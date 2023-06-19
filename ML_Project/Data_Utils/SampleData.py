import shutil, random, os

for i in range(9):
    dirname = str(i+1)
    asmsrcdir = f'./{dirname}/asm'
    bytesrcdir = f'./{dirname}/bytes'
    asmdestdir = f'./{dirname}/asm_less'
    bytedestdir = f'./{dirname}/bytes_less'


    filenames = random.sample(os.listdir(dirpath), 100)
for fname in filenames:
    srcpath = os.path.join(dirpath, fname)
    shutil.copyfile(srcpath, destDirectory)