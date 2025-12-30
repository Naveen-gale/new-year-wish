from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

# --- REQUIRED: Secret Key for Error Messages ---
app.secret_key = "naveen_new_year_secret_key" 

# Name → photo mapping
friends = {
    
    "akash": "akash.png",
    "prajwal": "prajwal.png",
    "niranjan":"nirangen.png",
    "vivek":"vivek.png",
    "usha":"usha.png",
    "sohil":"memmor.png",
     "sneha":"sneha.png",
     "kavay":"kavay.png",
     "":"memmor.png",
     "":"memorr.png",
     "":"memory2.png",
     "prince":"prince.png",
      "praveen":"praveen.png",
      "vineet":"vineet.png",
     "subhashani":"subashine.png",
     "johnglenn":"jhone.png",
     "sachin":"sacine.png",
     "sufiyan":"sufiyan.png",
     "trish":"trish.png",
     "steeven":"steven.png",
     "kaushalya":"kaushly.png",
     "yashwath":"yeshwant.png",
      "girijamma":"antti1.png",
      "akshita":"antti2.png",


}

@app.route("/")
def loading():
    return render_template("loading.html")

@app.route("/enter-name")
def enter_name():
    return render_template("index.html")

@app.route("/wish", methods=["POST"])
def wish():
    # 1. Get name and clean it (lowercase, no spaces)
    name = request.form.get("name").strip().lower()

    # 2. CHECK: Is the name in the dictionary?
    if name in friends:
        photo = friends[name]
        display_name = name.capitalize()

        return render_template(
            "wish.html",
            name=display_name,
            photo=photo
        )
    
    # 3. IF NOT FOUND:
    else:
        # Save an error message to show on the next page
        flash("🚫 Name not found! Ask Naveen your name .", "error")
        # Send user back to the Entry Page
        return redirect(url_for('enter_name'))

@app.route("/gallery")
def gallery():
    return render_template("gallery.html", friends=friends)

if __name__ == "__main__":
    app.run()
