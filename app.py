from flask import Flask, render_template

import praw

app = Flask(__name__)

r = praw.Reddit('OAuth testing example by u/kevinmrr ver 0.1 see '
                'https://praw.readthedocs.org/en/latest/'                           'pages/oauth.html for source')

r.set_oauth_app_info(client_id='ao_u3M0fXkxRyQ',
                    client_secret='WA3LY5nI1irCpwM-nsTWT1s_t70',
                   redirect_uri='http://127.0.0.1:5000/oauth/reddit/callback')

@app.route('/')
def index():
    return render_template('test_reddit.html',
                           connect_url='http://localhost:5000/oauth/reddit/connect')



@app.route('/oauth/reddit/connect')
def reddit_oauth():




    return "SUP"


@app.route('/oauth/reddit/callback')
def reddit_callback():

    return "YOSKI"



if __name__ == "__main__":
    app.run(debug=True)