import os
def soldier(path,file,format):
    os.chdir(path)
    i=1
    files = os.listdir(path)
    print(files)
    with open(file) as f:
        filelist=f.read().split("\n")
    for file in files:
        if os.path.splitext(file)[0] not in filelist:
            os.rename(file,file.capitalize())
        if os.path.splitext(file)[1]==(format) :
            os.rename(file,f"{i}{format}")
            i +=1
if __name__=='__main__':
    path=input("Path= ")
    file=input("File= ")
    format=input("format= ")
    soldier(path,file,format)
