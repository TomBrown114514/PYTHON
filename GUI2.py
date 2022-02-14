txt="床前明月光，疑是地上霜。举头望明月，低头思故乡。"
def linesplit(line):
    plist=["，","。"]
    for p in list:
        line=line.replace(p,"\n")
    return line.split("\n")
def lineprint(line):
    global linewidth
    while len(line)>linewidth:
        print(line[0:linewidth])
        line=line[linewidth:]
    print(line.center(linewidth,chr(12288)))
newlines=linesplit(txt)
for newline in newlines:
    lineprint(newline)