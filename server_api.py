import requests
import json

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

def is_open_position(node, maze_id):

    num_tries = 0
    x, y = node[0], node[1]
    check_position_addr = server + 'maze/' + maze_id + \
                        '/check?x=' + str(x) + '&y=' + str(y)

    ## Handle 'spaced out for a second' error
    while (True):

        r = requests.get(check_position_addr)
        if (r.status_code == 200 or r.status_code == 403):
            break

        elif (num_tries >= 100):
            print 'is_open_position failed retrieving info from server'
            return False

        num_tries += 1

    if (r.status_code == 200):
        return True
    else:
        return False

## solution has the format [[0, 0], [0, 1], ..., [n, n]]
def format_solution(solution):
    
    if (solution != None):
        converted_solution = [{'x': loc[0], 'y': loc[1]} for loc in solution]
    else:
        converted_solution = []

    return json.dumps(converted_solution)

def submit_solution(solution, maze_id):

    num_tries = 0
    submit_sol_addr = server + 'maze/' + maze_id + '/solve'
    solution_formatted = format_solution(solution)
    
    while (True):

        r = requests.post(submit_sol_addr, data=solution_formatted)
        if (r.status_code == 200):
            print 'Solution for maze is correct!'
            print r.content
            return
        elif (r.status_code != 503):
            print 'Solution INCORRECT!'
            print r.content
            return
        elif (num_tries >= 100):
            print 'Could not submit solution... There is probably a server problem'
            return

        num_tries += 1

    print r.status_code
    print r.content
