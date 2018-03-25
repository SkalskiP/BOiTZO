def intro_view(router):
        
    with open("./data/intro.txt") as f:
        content = f.readlines()
        
    for index, line in enumerate(content):
        router.screen.addstr(index + 1, 4, line)
        
    router.screen.getch()
    router.current_view = "lunch_menu_view"
