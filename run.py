from app import create_app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        from app import db
        db.create_all()  # Crea las tablas si no existen
    app.run(debug=True)