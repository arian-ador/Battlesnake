import typing
import random
import heapq
import copy

MAX_DEPTH = 2 # Maximum depth for the minimax algorithm

def info() -> typing.Dict: 
    print("INFO") 
    return { 
        "apiversion": "1",
        "author": "Naughtysnake",  # My Battlesnake Username
        "color": "#66b3ff",  # Choose color
        "head": "mlh-gene",  # Choose head
        "tail": "ice-skate",  # Choose tail
    }


# start is called when your Battlesnake begins a game
def start(game_state: typing.Dict):
    print("GAME START")

# end is called when your Battlesnake finishes a game
def end(game_state: typing.Dict):
    print("GAME OVER\n")

# is_safe is called when your Battlesnake is trying to move to a square and checks if it is safe to move there
def is_safe(pos, my_body, opponents, board_width, board_height):  
    x, y = pos[0], pos[1]
    new_pos = {"x": x, "y": y}
    if not (0 <= x < board_width and 0 <= y < board_height):  # Prevent your Battlesnake from moving out of bounds
        return False 
    if new_pos in my_body: # Prevent your Battlesnake from colliding with itself
        return False             
    for snake in opponents:
        if new_pos in snake['body']: # Prevent your Battlesnake from colliding with other Battlesnakes
            return False
# move is called on every turn and returns your next move
# Valid moves are "up", "down", "left", or "right"
def move(game_state: typing.Dict) -> typing.Dict:

    is_move_safe = {"up": True, "down": True, "left": True, "right": True}

    # We've included code to prevent your Battlesnake from moving backwards
    my_head = game_state["you"]["body"][0]  # Coordinates of your head
    my_neck = game_state["you"]["body"][1]  # Coordinates of your "neck"
    board_width = game_state['board']['width'] 
    board_height = game_state['board']['height'] 
    my_body = game_state['you']['body'] 
    opponents = game_state['board']['snakes'] 
    food_list = game_state["board"]["food"] # List of Food coordinates
    
    direction = { # Directions are based on coordinates of x and y
        "up": [my_head['x'], my_head['y'] + 1],
        "down": [my_head['x'], my_head['y'] - 1],
        "left": [my_head['x'] -1, my_head['y']],
        "right": [my_head['x'] + 1, my_head['y']]
    }
    safe_moves = []

    
    # Step 1 - Prevent your Battlesnake from moving out of bounds
   
    # Step 3 - Prevent your Battlesnake from colliding with other Battlesnakes
        collision = False
        for snake in opponents:
            if new_pos in snake['body']:
                collision = True
                break
        if collision:
            continue  # collision detected

        safe_moves.append(move) # move is safe
        

    if not safe_moves: # No safe moves, go down
        next_move = "down"
    else:
        if food_list: # If there is food on the board
            def manhattan_dist(p1, p2): 
                return abs(p1["x"] - p2["x"]) + abs(p1["y"] - p2["y"])  
                # Determine the direction to the nearest food   
        
            nearest_food = min(food_list, key=lambda f:manhattan_dist(my_head, f)) 
            # Find the move that brings the snake closest to the nearest food
            best_move = None 
            min_dist = float('inf')
            for move in safe_moves: 
                new_x, new_y = direction[move]  # Get the new position after the move
                dist = abs(new_x - nearest_food["x"]) + abs(new_y - nearest_food["y"]) # Calculate the distance to the nearest food
                if dist < min_dist: 
                    min_dist = dist
                    best_move = move
            next_move = best_move
        else:
            # Calculate the score of the move based on the space around it
            def space_score(move):  
                x, y = direction[move]  
                score = 0 
                for dx in [-1, 0, 1]:  
                    for dy in [-1, 0, 1]: 
                        if dx == 0 and dy == 0:
                            continue  # Skip the current cell
                            # Check if the cell is within the board boundaries
                        if 0 <= x + dx < board_width and 0 <= y + dy < board_height: 
                            if{"x": x + dx, "y": y + dy} not in my_body: # Check if the cell is empty
                                score += 1
                    return score

            next_move = max(safe_moves, key=space_score) # Choose the move with the highest score
            
        

    print(f"MOVE {game_state['turn']}: {next_move}")
    return {"move": next_move}


# Start server when `python main.py` is run
if __name__ == "__main__":
    from server import run_server

    run_server({"info": info, "start": start, "move": move, "end": end})
