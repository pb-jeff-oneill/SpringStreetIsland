from flask import Flask, render_template, request, redirect
from flask_talisman import Talisman

csp = {
    'default-src': [
        "'self'",
        'https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css'
    ]
}

app = Flask(__name__)
talisman = Talisman(app, content_security_policy=csp)

supporters = sorted([
    ("Ben Ewen-Campen, Ward 3 City Councilor", "https://www.benforward3.com/"),
    ("Jake Wilson, Councilor-At-Large", "https://www.jakeforsomerville.org/"),
    ("Earthwise Aware", "https://www.earthwiseaware.org/"),
    ("Somerville Alliance for Safe Streets", "https://sass-somerville.org/"),
    ("Green & Open Somerville", "https://www.greenopensomerville.org/"),
    ("Claire & Jeff O'Neill, 50 Spring St.", ""),
    ("Jeff Gentry, 10 Spring St.", ""),
    ("Jenn & Charlie Clifford, 146 Summer St.", ""),
    ("Ariane & Jess Torres, 50 Spring St.", ""),
    ("Greg Stanton Marra, 25 Atherton St.", ""),
    ("Renée & David Scott, 63 Boston St.", ""),
    ("Amy Mertl, 68 Mount Vernon St.", ""),
    ("Leigh Meunier", ""),
    ("Mark Chase, 13 Belmont St.", ""),
    ("Michelle A. & John D., 46 Spring St.", ""),
    ("Stephanie Galaitsi", ""),
    ("Matt Gage, 59 Oxford St.", ""),
    ("Nancy Lynn Goldberg, 25 Atherton St.", ""),
    ("Cam Grosser, 22 Belmont St.", ""),
    ("Laura de la Torre Bueno, 21 Spring Hill Terr.", ""),
    ("Lee Ann Walsh, 18 Spring St.", ""),
    ("Jane Gillooly, 61 Atherton St.", ""),
    ("Rob Lasell & Nicky Gonzalez, 4 Phillips Pl.", ""),
    ("Lynne Hartwell, 155 Summer St.", ""),
    ("Steve Pomeroy, 16 Spring St.", ""),
    ("Brian Thurber, 16 Spring St.", ""),
    ("Eva Breitenbach, 16 Spring St.", ""),
    ("Kathleen & Ed Froehlich, 58 Pitman St.", ""),
    ("Amanda Johnson, Elm Place", ""),
    ("Uschi & Dan Stoutenbugh, 16 Monmouth St.", ""),
    ("Evan & Joanna Bernstein, Cleveland St.", ""),
    ("Will Mbah, Councilor At-Large", "https://www.willmbah.com/"),
    ("Iris Haley, 24 Spring St.", ""),
])

@app.route('/')
def homepage():
    return render_template('home.html', supporters=supporters)

@app.before_request
def before_request():
    if request.url.startswith('https://spring'):
        url = request.url.replace('https://spring', 'https://www.spring', 1)
        return redirect(url, code=301)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
