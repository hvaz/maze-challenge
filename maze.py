import requests

server = 'http://52.27.140.147:9099/'

## Tries 100 times to get a maze from the server.
## Returns maze payload upon first success
## Return None upon failure
def getmaze():

    get_maze_addr = server + 'maze'
    num_tries = 0
    while (True):
        
        r = requests.post(get_maze_addr)

        if (r.status_code == 201):
            return r.content

        elif (num_tries >= 100):
            return None

        num_tries += 1

    return None

print getmaze()
