# Personal Gallery

## Getting Started
These instructions will get you a copy of the project up and running on your local machine

## Prerequisites
These are the things you need to make all the installations needed

## Installations
1. First clone this project to your device and run the following command
  ```
  python3.6 -m venv virtual
  ```
  You can specify the version of python you are using but make sure its compatible with venv
2. Then install pip
  ```
  python3.6 -m install pip
  ```
  Then install all the dependencies needed.Open the requirements file and make sure the following dependency is not there
  ```
  pkg-resources==0.0.0
  ```
  Then run
  ```
  pip install -r requirements.txt
  ```
## Running the project
  ```
  python manage.py runserver
  ```

## User Stories
1. View different photos that interest me.
2. Click on a single photo to expand it and also view the details of the photo.
3. Search for different categories of photos. (ie. Travel, Food)
4. Copy a link to the photo to share with my friends.
5. View photos based on the location they were taken.

## Built With
* [Django](https://www.djangoproject.com/) - The python web framework used
* [PostgreSQL](https://www.postgresql.org/) - Primary relational database
* [Heroku](https://signup.heroku.com/login) - Used to deploy the website live

## Author
This was built by **Andrew Kimani** - [Personal Gallery](https://github.com/andykimchris/Unsplash)

## License
This project is licensed under the [MIT license](https://opensource.org/licenses/MIT) - see the [LICENSE.md](LICENSE.md) file for further details
