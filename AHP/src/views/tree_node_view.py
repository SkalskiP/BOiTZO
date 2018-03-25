from ..util.file_utils import FileUtils
import curses


def tree_node_view(router):

    selection = -1
    option = 0
        
    while selection < 0:
        router.screen.clear()
        
        marker = router.current_node
        
        if router.current_node.parent is None:
            router.screen.addstr(1, 4, "This is root of hierarchy tree", curses.A_BOLD)
        else:
            history = []
            
            while marker is not None:
                history.insert(0, (marker.name if marker.name is not None else "Anonim feature"))
                marker = marker.parent
                
            router.screen.addstr(1, 4, "Current brunch: " + " > ".join(history), curses.A_BOLD)
        
        router.screen.addstr(3, 4, "Feature name: {}".format(router.current_node.name if router.current_node.name != None else ""))
        
        router.screen.addstr(4, 4, "Feature preferences: {}".format(router.current_node.preferences_to_string()))
        
        if router.current_node.is_lief():
            router.screen.addstr(5, 4, "Sub-features: {}".format(router.current_node.children))
        else:
            sub_names = []
            for sub_feature in router.current_node.children:
                sub_names.append(sub_feature.name if sub_feature.name is not None else "Anonymous feature")
            router.screen.addstr(5, 4, "Sub-features: [{}]".format(", ".join(sub_names) if router.current_node.children != [] else ""))
        
        if router.current_view == "tree_node_view":
            
            h = [0] * 7
            h[option] = curses.color_pair(1)
            
            router.screen.addstr(7, 4, "1 - Edit feature name", h[0])
            router.screen.addstr(8, 4, "2 - Edit feature preferences", h[1])
            router.screen.addstr(9, 4, "3 - Add sub-features", h[2])
            
            if router.current_node.is_lief():
                router.screen.addstr(10, 4, "4 - Set as tree brunch", h[3])
            else:
                router.screen.addstr(10, 4, "4 - Set as tree lief", h[3])
            
            router.screen.addstr(12, 4, "5 - Go to parent", h[4])
            router.screen.addstr(13, 4, "6 - Go to sub-feature", h[5])
            router.screen.addstr(15, 4, "7 - Back ('q')", h[6])
            
            q = router.screen.getch()
            
            if q == curses.KEY_UP:
                option = (option - 1) % len(h)
            elif q == curses.KEY_DOWN:
                option = (option + 1) % len(h)
            elif q == ord('\n'):
                selection = option
                
            if selection == 0 :
                router.current_view = "edit_name"
            elif selection == 1 :
                router.current_view = "edit_preferences"
            elif selection == 2 :
                router.current_view = "add_sub_feature"
            elif selection == 3:
                if router.current_node.is_lief():
                    router.current_node.set_as_brunch()
                else:
                    router.current_node.set_as_lief(alternatives_size = len(router.alternatives))
                router.current_view = "tree_node_view"
            elif selection == 4:
                if router.current_node.parent is not None:
                    router.current_node = router.current_node.parent
                router.current_view = "tree_node_view"
            elif selection == 5 :
                router.current_view = "sub_feature_view"
            elif q == ord('q') or selection == len(h) -1 :
                router.current_view = "lunch_menu_view"
                
        elif router.current_view == "edit_name":
            
            router.screen.addstr(7, 4, "Set current feature name to:")
            
            s = router.read_text_from_user(9, 4)
            
            router.current_node.name = s
            router.current_view = "tree_node_view"
            
        elif router.current_view == "add_sub_feature":
            
            router.screen.addstr(7, 4, "Insert name of new feature:")
                            
            name = router.read_text_from_user(9, 4)
            router.current_node.add_child_with_name(name)
            router.current_view = "tree_node_view"
            
        elif router.current_view == "insert_file_name":
            
            router.screen.addstr(7, 4, "Insert file name:")
                            
            name = router.read_text_from_user(9, 4)
            
            model = {"alternatives": router.alternatives, "gole": router.root}
            FileUtils.save_model_to_file(model, name + ".json")
            router.current_view = "tree_node_view"
            
        elif router.current_view == "edit_preferences":
            
            router.screen.addstr(7, 4, "Insert preferences values in MATLAB notation:")
            router.screen.addstr(8, 4, "[If you don't want to change preferences values just press Enter]")
                            
            preferences = router.read_text_from_user(10, 4)
            if router.current_node.is_lief():
                router.current_node.update_preferences(preferences, len(router.alternatives))
            else:
                router.current_node.update_preferences(preferences)
            router.current_view = "tree_node_view"
             
        elif router.current_view == "sub_feature_view":
            
            h = [0] * (len(router.current_node.children) + 1)
            h[option] = curses.color_pair(1)
            
            for index, value in enumerate(router.current_node.children):
                router.screen.addstr(7 + index, 4, "{} - {}".format(index + 1, value.name), h[index])
                
            router.screen.addstr(7 + len(router.current_node.children) + 1, 4, "{} - Back ('q')".format(len(router.current_node.children) + 1), h[len(router.current_node.children)])
            
            q = router.screen.getch()
            
            if q == curses.KEY_UP:
                option = (option - 1) % len(h)
            elif q == curses.KEY_DOWN:
                option = (option + 1) % len(h)
            elif q == ord('\n'):
                selection = option
                
            if q == ord('q') or selection == len(h) -1 :
                router.current_view = "lunch_menu_view"
            elif selection != -1:
                router.current_node = router.current_node.children[option]
                router.current_view = "tree_node_view"
