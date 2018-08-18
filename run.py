from app import app

if __name__ == '__main__':
    # app.config['TESTING'] = True
    with app.app_context():
        app.run(debug = True)