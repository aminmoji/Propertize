# Propertize

**Propertize** is a collaborative Django property marketplace project built by Amin, Caleb, and Connor during boot camp in 2023.

The project explores a direct seller/buyer workflow: sellers can publish property listings and buyers can browse listings, save favorites, and schedule showings.

## Features

- Custom user accounts
- Property listings
- Property image uploads
- Favorite properties
- Showing/open-house scheduling
- Seller/buyer-oriented property browsing

## Screenshots

![Propertize screenshot](https://user-images.githubusercontent.com/126698422/236488569-b1efbc74-d5ea-436c-b2cc-8ed3d47311ab.png)

![Propertize screenshot](https://user-images.githubusercontent.com/126698422/236489708-deae7a6e-f626-459e-a094-178da94f9803.png)

## Tech stack

- Python
- Django 4.2
- PostgreSQL
- HTML
- CSS
- Materialize CSS
- Django authentication

## Original project material

- [Pitch deck](https://my.visme.co/view/4d1n9eok-propertize-pitch-deck-presentation)
- [Trello board](https://trello.com/b/YDxYEXII/propertize)

## Local setup

```bash
git clone https://github.com/aminmoji/Propertize.git
cd Propertize

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
```

Export the variables from `.env`, then:

```bash
cd propertize
python manage.py migrate
python manage.py runserver
```

## Configuration

Database credentials and the Django secret key are not meant to be committed to the repository.

See `.env.example` for the required values.

## Future ideas from the original project

- Direct chat between buyers and sellers
- Interactive virtual showings
- User/listing reviews
- Nearby places and neighborhood information
- Social-media integration
- Side-by-side property comparison

## Project status

Historical collaborative portfolio / learning project.

The repository is intentionally kept recognizable as the original team project. Cleanup work focuses on security, reproducibility, documentation, and clear bugs rather than rewriting the application.
