def run(strs):
    part = 0
    single = set()
    while True:
        print(len(single))
        for i in strs:
            print(i)
            single.add(i[part])
            print(i[part])
        print(len(single))
        print(part)
        if len(single) != part + 1:
            if part <= 0:
                return ""
            else:
                return f"result {strs[0][:part]}"
        part += 1

print(run(["flower", "gflurm", "flare"]))