import glob
print("Solitaire files found:")
for f in glob.glob("*solitaire*.html"):
    print(f)
