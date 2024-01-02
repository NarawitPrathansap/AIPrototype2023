from re import sub
import subprocess #สำหรับรัน terminal command

if __name__ == "__main__":
    sum_output = 0
    # basic terminal command
    #subprocess.run(["ls","-ltr"])
    #subprocess.run(["rm","-r","/home/tohn/testfolder1"])

    #python commands
    print(f"first run num=100 XX=90")
    result = subprocess.run(["python","firstpy.py", "--num", "100", "--XX", "90"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sum_output += int(result.stdout.decode('utf-8').split()[0])
    print(f"------------------------------------------------")
    print(f"second run num=-10 XX=-90")
    result = subprocess.run(["python","firstpy.py", "--num", "-10", "--XX", "-90"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sum_output += int(result.stdout.decode('utf-8').split()[0])
    print(f"------------------------------------------------")
    print(f"third run num=0")
    result = subprocess.run(["python","firstpy.py", "--num", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sum_output += int(result.stdout.decode('utf-8').split()[0])
    print(f"------------------------------------------------")

    print(f'Sum of the numbers before Hello world!: {sum_output}')


    #use output from other program
    #process_output = subprocess.Popen(["python","firstpy.py", "--num", "0"],
                                      #stdout=subprocess.PIPE,
                                      #stderr=subprocess.PIPE)
    #out, err = process_output.communicate()
    #print(out.decode('utf-8'))
    #print(len(out.decode('utf-8')))
