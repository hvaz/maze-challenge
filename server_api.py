import requests

server = 'http://52.27.140.147:9099/'

## Tries 100 times to get a maze from the server.
## Returns maze payload upon first success
## Returns None upon failure
def get_maze():

    get_maze_addr = server + 'maze'
    num_tries = 0
    while (True):
        
        r = requests.post(get_maze_addr)

        if (r.status_code == 201):
            print r.content
            return r.content

        elif (num_tries >= 100):
            print 'Could not retrieve maze from server at route /maze. \
                    Error Status Code ' + r.status_code
            return None

        num_tries += 1

    return None

def is_open_position(x, y, maze_id):

    num_tries = 0
    check_position_addr = server + 'maze/' + maze_id + \
                        '/check?x=' + str(x) + '&y=' + str(y)

    ## Handle 'spaced out for a second' error
    while (True):

        r = requests.get(check_position_addr)
        if (r.status_code == 200 or r.status_code == 403):
            print r.content
            break

        elif (num_tries >= 100):
            print 'is_open_position failed retrieving info from server'
            return False

    if (r.status_code == 200):
        return True
    else:
        return False
