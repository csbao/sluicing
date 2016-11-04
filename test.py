import sys, subprocess

outDir = "work"
for i in range(500):
    for j in range(4):
       #jobName = "python my_script.py %f %f" % (i,j)
       #cmd = "module load Python/2.7; %s" % jobName
       #echoArgs = ["echo", "-e", "'%s'" % cmd]
       echoArgs = ["python", "/campusdata/csbao/sluicing/scripts/my_script.py", "%f %f" %(i,j)]
       jobName = "h_%s_F%d_%d" % (outDir, i, j)
       outputFile = "/campusdata/csbao/sluicing/scripts/%s/i_F%d_%d" % (outDir, i,j)
       errorFile = "/campusdata/csbao/sluicing/scripts/%s/e_F%d_%d" % (outDir, i,j)
       print(" ".join(echoArgs))
       qsubArgs = ["qsub","-cwd", "-V", "-N", jobName, "-o", outputFile, "-e", errorFile]
       print(" ".join(qsubArgs))

       #wholeCmd = " ".join(echoArgs) + " ".join(qsubArgs)
       wholeCmd = " ".join(qsubArgs) + " ".join(echoArgs)
       out = subprocess.Popen(wholeCmd, shell=True, stdout=subprocess.PIPE)
       out = out.communicate()[0]

       jobId = out.split()[2]
       print jobId
