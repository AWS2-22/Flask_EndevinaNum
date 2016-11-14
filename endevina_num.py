# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
app = Flask(__name__)
num_random = 66
 
# el decorator (@) estableix la ruta (URL). A mes, activem el mètode POST
@app.route("/endevina_num", methods=["GET","POST"])
def endevina_num():
    import random
    from random import randint
    global num_random
    miss = ""
    trobat=0
    if request.method == "POST":
        num = request.form["num"]
        num = int(num)
        if num > num_random:
            miss = "El numero <b>" + str(num) + u"</b> és més gran que el que estic pensant"
        elif num < num_random:
            miss = "El numero <b>" + str(num) + u"</b> és més petit que el que estic pensant"
        elif num == num_random:
            miss = "Has trobat el numero! <b>" + str(num) + "</b>"
            num_random = randint(1,100)
    return render_template( "template_endevina_num.html", missatge=miss )
 
if __name__ == "__main__":
    app.run()