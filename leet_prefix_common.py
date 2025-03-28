def run(strs):
    part = 0
    while True:
        single = set()
        for i in strs:
            single.add(i[part])
        if len(single) != part + 1:
            if part < 0:
                return strs[0][:part]
            else:
                return ""
        part += 1

print(run(["flower", "flurm", "flare"]))