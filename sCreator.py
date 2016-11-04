import sys
import subprocess
import os


def makeQsub(outDir, iterations=10,restarts=2):
    for fold in range(10):
        for it in range(restarts):
            queue = "small.q"
            jobName = "h_%s_F%d_%d" % (outDir, fold, it)

            echoArgs = ["/campusdata/csbao/usr/local/bin/python3.3", "/campusdata/csbao/sluicing/scripts/xml_parser.py", "-iterations", str(iterations)]#, "/campusdata/csbao/test3/" + features, str(fold), foldFile, "-ignoreFeats", ignoreSet]

            outputFile = "/campusdata/csbao/sluicing/scripts/%s/i_F%d_%d" % (outDir, fold,it)
            errorFile = "/campusdata/csbao/sluicing/scripts/%s/e_F%d_%d" % (outDir, fold,it)

            qsubArgs = ["qsub", "-cwd", "-b", "y", "-V", "-q", queue, "-N", jobName, "-o", outputFile, "-e", errorFile]
            wholeCmd = " ".join(qsubArgs) + " " + " ".join(echoArgs)
            print (wholeCmd)
            out = subprocess.Popen(wholeCmd, shell=True, stdout=subprocess.PIPE)
            out = out.communicate()[0]
            jobId = out.split()[2]

def makeQsub2():
   
    job_param1 = 12.5
    job_param2 = 5.0
    jobName = "python my_script.py %f %f" % (job_param1,job_param2)
    cmd = "module load Python/2.7; sleep 0.2; %s" % jobName
    echoArgs = ["echo", "-e", "'%s'" % cmd]
    print(" ".join(echoArgs))
    qsubArgs = ["qsub","-cwd"]
    print(" ".join(qsubArgs))

    wholeCmd = " ".join(echoArgs) + " | " + " ".join(qsubArgs)
    out = subprocess.Popen(wholeCmd, shell=True, stdout=subprocess.PIPE)
    out = out.communicate()[0]

    jobId = out.split()[2]
    print jobId

def main():
    makeQsub("work", iterations=50, restarts=50)

if __name__=="__main__":
    main()
