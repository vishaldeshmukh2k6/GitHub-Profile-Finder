from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        choice = request.form['choice']

        base_url = f"https://api.github.com/users/{username}"
        user_data = requests.get(base_url).json()

        if choice == '1':
            return render_template('result.html', user=user_data, choice="account")
        
        elif choice == '2':
            repos = requests.get(base_url + '/repos', params={"page": 1, "per_page": 100}).json()
            return render_template('result.html', repos=repos, user=user_data, choice="repos")
        
        elif choice == '3':
            followers = requests.get(base_url + '/followers', params={"page": 1, "per_page": 100}).json()
            return render_template('result.html', followers=followers, user=user_data, choice="followers")
        
        elif choice == '4':
            following = requests.get(base_url + '/following', params={"page": 1, "per_page": 100}).json()
            return render_template('result.html', following=following, user=user_data, choice="following")
        
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True, port="5011")
