import subprocess

def run(arg):
    p = subprocess.Popen(arg, bufsize=100000,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, shell=True, universal_newlines=True)
    out, err = p.communicate()
    if len(err) > 0:
        return err
    return out

if __name__ == "__main__":
    nmap = run("nmap -O 127.0.0.1")
    print(nmap)


