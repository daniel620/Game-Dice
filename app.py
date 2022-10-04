
from flask import Flask, request, render_template
from Player import player
import numpy as np
# import joblib
app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        dice_in_hand = str(request.form.get("dice_in_hand"))
        last_input = dice_in_hand 
        try:
            dice_in_hand = np.array(dice_in_hand.replace(' ','').split(','),dtype=int).tolist()
            if len(dice_in_hand) != 5:
                return render_template("index.html", result1 = 'Please enter 5 dices in hand', result2='')
        except:
            # throw error
            Exception('Invalid input')
            return render_template("index.html", result1 = 'Invalid input', result2='')

        my_player = player(dice_in_hand)
        player_num = int(request.form.get("player_num"))
        game_dice_num = int(request.form.get("game_dice_num"))
        game_point_chosen = int(request.form.get("game_point_chosen"))

        r1, r2 = my_player.technical_analysis(player_num, game_dice_num, game_point_chosen)
        return(render_template("index.html", result1 = r1, result2=r2, last_input = last_input,last_player_num=player_num, last_game_dice_num=game_dice_num, last_game_point_chosen=game_point_chosen))
    else:
        return(render_template("index.html", result1 = "Waiting", result2="Waiting", last_input = '',last_player_num=None, last_game_dice_num=None, last_game_point_chosen=None))

if __name__ == "__main__":
    from gevent import pywsgi
    server = pywsgi.WSGIServer(('127.0.0.1', 5000), app)
    server.serve_forever()
    # app.run()
