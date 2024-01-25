#from flask import Flask, render_template
from flask import Flask, render_template, request, redirect, url_for
from exercises import get_exercise_by_id
import sys
sys.path.insert(0,"")
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthdata.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    blood_test_results = db.Column(db.String(200), nullable=True)
    weight = db.Column(db.Float, nullable=True)
    height = db.Column(db.Float, nullable=True) 

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')
@app.route('/healthdata', methods=['GET', 'POST'])
def healthdata():
    if request.method == 'POST':
        blood_test_results = request.form['blood_test_results']
        weight = request.form['weight']
        height = request.form['height']
        # Assuming the user is already logged in
        user = User.query.filter_by(username=session['username']).first()
        user.blood_test_results = blood_test_results
        user.weight = weight
        user.height = height
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('healthdata.html')    
def calculate_diet_preferencesuser():
    height = user.height / 100  # Convert height from cm to m
    weight = user.weight
    bmi = weight / (height * height)

    diet_preferences = {}

    if bmi < 18.5:
        diet_preferences['preference'] = 'underweight'
        diet_preferences['recommendations'] = ['foods high in calories and protein', 'healthy fats']
    elif bmi >= 18.5 and bmi < 24.9:
        diet_preferences['preference'] = 'normal weight'
        diet_preferences['recommendations'] = ['maintain balanced diet', 'focus on whole foods']
    elif bmi >= 25 and bmi < 29.9:
        diet_preferences['preference'] = 'overweight'
        diet_preferences['recommendations'] = ['foods low in calories and high in fiber', 'reduce portion sizes']
    else:
        diet_preferences['preference'] = 'obese'
        diet_preferences['recommendations'] = ['low-calorie and high-fiber foods', 'consult a healthcare professional']

    return diet_preferences

    foods = {
    'high_calorie': ['avocado', 'nuts', 'whole milk', 'eggs', 'bananas'],
    'high_protein': ['chicken breast', 'fish', 'lentils', 'greek yogurt', 'quinoa'],
    'healthy_fats': ['olive oil', 'coconut oil', 'flaxseeds', 'chia seeds', 'walnuts'],
    'low_calorie': ['broccoli', 'spinach', 'celery', 'cucumber', 'tomatoes'],
    'high_fiber': ['beans', 'berries', 'apples', 'oats', 'popcorn']
}
@app.route('/healthdata', methods=['GET', 'POST'])
def healthdata():
    if request.method == 'POST':
        blood_test_results = request.form['blood_test_results']
        weight = request.form['weight']
        height = request.form['height']
        # Assuming the user is already logged in
        user = User.query.filter_by(username=session['username']).first()
        user.blood_test_results = blood_test_results
        user.weight = weight
        user.height = height
        db.session.commit()

        diet_preferences = calculate_diet_preferences(user)

        food_list = []
        for food_type, foods in diet_preferences['recommendations'].items():
            food_list += foods

        return render_template('healthdata.html', food_list=food_list)
    return render_template('healthdata.html')
def get_food_nutritional_info(food):
    food_nutritional_info = {}
    # Assuming there is a table 'foods' in the database with columns 'name', 'calories', 'protein', 'fat', and 'fiber'
    result = Food.query.filter_by(name=food).first()
    if result:
        food_nutritional_info['name'] = result.name
        food_nutritional_info['calories'] = result.calories
        food_nutritional_info['protein'] = result.protein
        food_nutritional_info['fat'] = result.fat
        food_nutritional_info['fiber'] = result.fiber
    return food_nutritional_info
def calculate_diet_preferences(user):
    diet_preferences = {}
    # Assuming you have some algorithm to calculate the diet preferences based on the user's blood test results, weight, and height
    diet_preferences['recommendations'] = recommend_foods(user)
    return diet_preferences
def recommend_foods(user):
    # Assuming you have a database table 'foods' with columns 'name', 'food_type', and 'preference_level'
    recommended_foods = {}
    result = Food.query.filter_by(preference_level=user.preference_level).all()
    for food in result:
        if food.food_type not in recommended_foods:
            recommended_foods[food.food_type] = []
        recommended_foods[food.food_type].append(food.name)
    return recommended_foods
def recommend_foods(user):
    recommended_foods = {}
    # Assuming you have a list of nutrient preferences, like ['calories', 'protein', 'carbohydrates', 'fat']
    for nutrient in user.nutrient_preferences:
        result = Food.query.filter_by(nutrient=nutrient).all()
        for food in result:
            if food.food_type not in recommended_foods:
                recommended_foods[food.food_type] = []
            recommended_foods[food.food_type].append(food.name)
    return recommended_foods
def on_nutrient_preferences_changed(user):
    # This function can be triggered whenever the user's nutrient preferences are changed
    # Then, the `recommend_foods` function is called to update the recommended food list
    user.recommended_foods = recommend_foods(user)
    
"""from flask import Flask, render_template, request, redirect, url_for
from exercises import get_exercise_by_id"""

app = Flask(__name__)

# Add a list of users and their exercise habits here
users = {
    'user1': {'exercise_id': 'exercise1', 'frequency': '5', 'duration': '30'},
    'user2': {'exercise_id': 'exercise2', 'frequency': '3', 'duration': '45'},
    # ... more users ...
}

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/exercise', methods=['GET', 'POST'])
def exercise():
    if request.method == 'POST':
        user_id = request.form['user_id']
        exercise_id = request.form['exercise_id']
        frequency = request.form['frequency']
        duration = request.form['duration']
        
        # Add the new user's exercise habit data to the users dictionary
        users[user_id] = {'exercise_id': exercise_id, 'frequency': frequency, 'duration': duration}
        
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/exercise', methods=['GET', 'POST'])
def exercise():
    if request.method == 'POST':
        user_id = request.form['user_id']
        exercise_id = request.form['exercise_id']
        frequency = request.form['frequency']
        duration = request.form['duration']
        
        # Check if the user already exists in the 'users' dictionary
        if user_id in users:
            # Update the user's exercise habit data
            users[user_id]['exercise_id'] = exercise_id
            users[user_id]['frequency'] = frequency
            users[user_id]['duration'] = duration
        else:
            # Add the new user's exercise habit data to the users dictionary
            users[user_id] = {'exercise_id': exercise_id, 'frequency': frequency, 'duration': duration}
        
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    user_id = session.get('user_id')
    user = User.query.filter_by(id=user_id).first()
    articles = Article.query.all()
    return render_template('dashboard.html', user=user, articles=articles)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))


        
    






