import sys
import subprocess




def makeQsub(dividend=7, count=4634):

    prev = 0
    for i in range(1,dividend+1):
        curr = count/dividend * i

        queue = "small.q"
        echoArgs = ["/campusdata/csbao/usr/local/bin/python3.3", "/campusdata/csbao/sluicing/scripts/xml_parser.py", str(prev), str(curr)]
        outputFile = "/campusdata/csbao/sluicing/scripts/%s/output_%d" % (i)
        errorFile = "/campusdata/csbao/sluicing/scripts/%s/error_%d" % (i)

        qsubArgs = ["qsub", "-cwd", "-b", "y", "-V", "-q", queue, "-o", outputFile, "-e", errorFile]
        wholeCmd = " ".join(qsubArgs) + " ".join(echoArgs)
        out = subprocess.Popen(wholeCmd, shell=True, stdout=subprocess.PIPE)
        out = out.communicate()[0]
        jobId = out.split()[2]
        print (jobId)
        prev = curr




def main():
    makeQsub()
    # initialize dividend to 7 and count to 4634 since it splits evenly.
    # enter length of rows into the function for now.

if __name__=="__main__":
    main()
