# Cookie Manager

Cookie Manager is a simple Flask-based web application that allows users to manage cookie recipes and a guestbook. Users can add and view cookie recipes as well as leave their names in the guestbook.

## Features

- Add and list cookie recipes.
- Add and list guestbook entries.
- Simple and intuitive web interface.

## Project Structure

```
app.py
requirements.txt
static/
    guestbook.html
    index.html
    styles.css
    images/
```

- `app.py`: The main Flask application.
- `requirements.txt`: Contains the Python dependencies.
- `static/`: Contains static files like HTML, CSS, and images.

## Prerequisites

- Python 3.7 or higher
- Flask

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd cookie-manager
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   - `http://127.0.0.1:5000/` for the home page.
   - `http://127.0.0.1:5000/guestbook` for the guestbook page.

## API Endpoints

### Cookie Recipes

- **Add a Cookie Recipe**
  - Endpoint: `/cookie/add`
  - Method: `POST`
  - Payload: `{ "recipe": "<recipe-details>" }`
  - Response: `200 OK`

- **List Cookie Recipes**
  - Endpoint: `/cookie/list`
  - Method: `GET`
  - Response: JSON array of cookie recipes.

### Guestbook

- **Add a Guestbook Entry**
  - Endpoint: `/guestbook/add`
  - Method: `POST`
  - Payload: `{ "name": "<guest-name>" }`
  - Response: `200 OK`

- **List Guestbook Entries**
  - Endpoint: `/guestbook/list`
  - Method: `GET`
  - Response: JSON array of guest names.

## License

This project is licensed under the MIT License.