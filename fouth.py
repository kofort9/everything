def create_box(w,h):
    for i in range(h):
        print (w)*'#'
    
width = raw_input('Enter box width: ')
height = raw_input('Enter box height: ')

create_box(int(width),int(height))



