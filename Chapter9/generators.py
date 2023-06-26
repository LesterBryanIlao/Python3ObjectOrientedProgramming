import sys
# generator expression
inname, outname = sys.argv[1:3]
with open(inname) as infile:
    with open(outname, "w") as outfile:
        warnings = (l.replace("\tWARNING", "")
                    for l in infile if "WARNING" in l)
        print(type(warnings))
        for l in warnings:
            outfile.write(l)
