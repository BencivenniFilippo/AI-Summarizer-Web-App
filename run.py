from app.__init__ import create_app

app = create_app()

if __name__ == "__main__": # only runs if the file is run directly and not from imports
    app.run(debug=True) # run is a flask method, nothing to do with the filename