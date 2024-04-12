import pandas as pd
import argparse
import subprocess
parser = argparse.ArgumentParser(description="Get args",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-f","--filename", help="file name", default=None)
parser.add_argument("-o", "--output", help = "output_file_name", default = None)
parser.add_argument("-n", "--nevents", help = "number_of_events", default = None)
args = parser.parse_args()

df = pd.read_pickle(args.filename)
if args.nevents:
    maxlength = int(args.nevents)
else:
    maxlength = len(df)    
lundstring = ""
xsecs, pids, pxs, pys, pzs, es, ms, vzs = df.loc[:, ["xsec", "pid", "px", "py", "pz", "e", "m", "vz"]].to_numpy().T
pids = pids.astype(int)
for i in range(maxlength):
    xsec, pid, px, py, pz, e, m, vz = xsecs[i], pids[i], pxs[i], pys[i], pzs[i], es[i], ms[i], vzs[i]
    vx, vy = 0, 0
    if i%10000==0:
        print(i)
    lundstring = lundstring + "1   1       1  0.0{:>4}   11   {:.3f}   1       1      {:6f}\n".format(0,10.604,xsec)
    lundstring = lundstring + "1   0  1   {:d}   0    4   {: .4f} {: .4f} {: .4f} {: .4f} {: .4f} 0.0000 0.0000  {: .4f}\n".format(pid, px, py, pz, e, m, vz)

with open(args.output, "w") as file:
    file.write(lundstring)
print ("./convert.sh {} {:d}".format(args.output, pid))
subprocess.run(["./convert.sh", "{}".format(args.output), "{:d}".format(pid)])
                
