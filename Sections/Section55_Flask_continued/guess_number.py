from flask import Flask

app = Flask(__name__)

import random
number = random.randint(0,9)
print('number is ', number)


def h1(funct):
    def wrapper(*args):
        return f"<h1>{args[0]}</h1>"
    return wrapper

@h1
def home_title(text):
    return text


@app.route("/")
def home():
    # return "<h1>Guess a Number</h1> <img src=\"https://tenor.com/bAasa.gif\" width=\"500\" height=\"500\"></img>"

    # number = random.randint(0,9)
    # print('number is ', number)

    return home_title('Guess a Number') + \
        """
        <!-- <h1>Guess a Number</h1> -->
        <p>guess a number 0 through 9</p>

        <!-- the gif -->
        <div class="tenor-gif-embed" data-postid="20973980" data-share-method="host" data-aspect-ratio="1" data-width="25%">
        <a href="https://tenor.com/view/number-gif-20973980">Number GIF</a>from <a href="https://tenor.com/search/number-gifs">Number GIFs</a>
        </div> 
        <script type="text/javascript" async src="https://tenor.com/embed.js"></script>

        """



@app.route("/<gn>")
def guess_number(gn):
    global number

    # print(type(gn),gn)
    # print(type(number),number)

    try:
        if int(gn) == number:
            number = random.randint(0,9)
            print('the new number is ', number)
            return """
                <h1>YAY, You Won!</h1>

                <div class="tenor-gif-embed" data-postid="26009901" data-share-method="host" data-aspect-ratio="1.24514" data-width="25%">
                <a href="https://tenor.com/view/mika-noah-raj-yay-cheer-gif-26009901">Mika Noah GIF</a>from <a href="https://tenor.com/search/mika-gifs">Mika GIFs</a>
                </div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>

                """


        elif int(gn) > number:
            return """
                <h1 style="color:Red">Too High</h1>

                <div class="tenor-gif-embed" data-postid="10410151" data-share-method="host" data-aspect-ratio="1.29515" data-width="25%">
                <a href="https://tenor.com/view/jimmy-mcmillan-too-damn-high-high-gif-10410151">Too Damn High GIF</a>from <a href="https://tenor.com/search/jimmy+mcmillan-gifs">Jimmy Mcmillan GIFs</a>
                </div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>

                """
        elif int(gn) < number:
            return """
                <h1 style="color:Red">Too Low</h1>

                <div class="tenor-gif-embed" data-postid="13374826" data-share-method="host" data-aspect-ratio="1.78771" data-width="25%">
                <a href="https://tenor.com/view/no-thats-too-low-scared-threat-gif-13374826">No Thats Too Low GIF</a>from <a href="https://tenor.com/search/no-gifs">No GIFs</a>
                </div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>

                """
    except Exception as ex:
        print(str(ex))
        return """
            <h1 style="color:Red">What?</h1>
            <p>guess a number 0 through 9</p>

            <div class="tenor-gif-embed" data-postid="21870111" data-share-method="host" data-aspect-ratio="0.934375" data-width="25%">
            <a href="https://tenor.com/view/wait-what-gif-21870111">Wait What GIF</a>from <a href="https://tenor.com/search/wait+what-gifs">Wait What GIFs</a>
            </div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>

            """

if __name__ == "__main__":
    app.debug = True
    app.run()    

# run in terminal
"""
flask --app guess_number run
"""

