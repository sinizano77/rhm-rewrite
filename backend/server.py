from flask import Flask
import rhythm_game_API
 
# Initializing flask app 
app = Flask(__name__)
 
# Route for seeing a data
@app.route('/data')
def get_rhythm_game():
    query_result = rhythm_game_API.get_rhythm_game()
    # Returning an api for showing in reactjs
    return {
        "game_id":f"{query_result[0]}", 
        "game_name":f"{query_result[1]}",
        "group_id":f"{query_result[2]}",
        "game_platform":f"{query_result[3]}",
        "point_meter":f"{query_result[4]}",
        "skill_star":f"{query_result[5]}",
        "two_player":f"{query_result[6]}",
        "image_file":f"{query_result[7]}",
        "difficulty":f"{query_result[8]}",
        }

# Running app
if __name__ == '__main__':
    app.run()
