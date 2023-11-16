import random
import sys
import os, threading, multiprocessing
from tqdm import tqdm
from pathlib import Path

indir = Path(sys.argv[1])
outdir = Path(sys.argv[2])
repeat_count = int(sys.argv[3])

THREAD_LIMIT = multiprocessing.cpu_count() * 2
threads = []

for in_fp in tqdm(sorted(indir.glob("**/*"))):
    if not os.path.isfile(in_fp):
        continue

    infile_relative = str(in_fp.resolve()).split(str(indir.resolve()))[-1].strip("/")
    for count in range(repeat_count):
        out_fp = outdir / str(count + 1) / infile_relative

        # print(in_fp, out_fp)
        # break
        os.makedirs(out_fp.parent, exist_ok=True)

        t = threading.Thread(
            target=os.system,
            args=(
                f""" python scripts/add_noise.py "{in_fp.resolve()}" "{out_fp.resolve()}" "{random.randint(100, 1000)}" """,
            ),
        )
        t.start()
        threads.append(t)

        while sum([t.is_alive() for t in threads]) >= THREAD_LIMIT:
            continue

    while sum([t.is_alive() for t in threads]) >= THREAD_LIMIT:
        continue

while sum([t.is_alive() for t in threads]) > 0:
    continue

    #     break
    # break
