def introView(ruter):
        
    with open("./data/intro.txt") as f:
        content = f.readlines()
        
    for index, line in enumerate(content):
        ruter.screen.addstr(index + 1, 4, line)
        
    ruter.screen.getch()