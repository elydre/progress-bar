from bar import Bar

def progress_loop():
    for i in range(8000):
        test.progress(i+1)


# percentage mode
test = Bar(8000, "*", "p")
progress_loop()

# steps mode
test = Bar(8000, "-", "s")
progress_loop()

# clean mode
test = Bar(8000, "#", "c")
progress_loop()

print()