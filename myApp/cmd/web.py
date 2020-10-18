import myApp


def main():
    app = myApp.create_app()

    app.run(debug=True)
