# CRUD Web Application

A complete CRUD (Create, Read, Update, Delete) web application built with Flask, SQLAlchemy, and SQLite.

## Project Structure

```
CRUD/
├── app.py
├── data.db (auto-created)
├── requirements.txt
├── README.md
├── templates/
│   ├── index.html
│   └── edit.html
├── static/
│   └── style.css
```

## Features

- **Create**: Add new persons with name and age
- **Read**: View all records in a responsive table
- **Update**: Edit existing records
- **Delete**: Remove records from the database
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Modern UI**: Gradient background, card-based layout, smooth animations
- **Automatic Database**: SQLite database created on first run

## Installation

1. Navigate to the project directory:
   ```
   cd "CRUD operations"
   ```

2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Run the Flask application:
   ```
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Database

The application uses SQLite with SQLAlchemy ORM. The database is automatically created on first run with a `Person` table containing:
- **id**: Primary key (auto-increment)
- **name**: String field for person's name
- **age**: Integer field for person's age

## Available Routes

- `GET /` - Display all records and add form
- `POST /add` - Add a new record
- `GET /edit/<id>` - Edit page for a specific record
- `POST /update/<id>` - Update a record
- `GET /delete/<id>` - Delete a record

## UI Components

### Main Page
- **Add Form**: Input fields for name and age with green Add button
- **Records Table**: Displays all persons with ID, Name, Age and action buttons
- **Edit Button** (Blue): Navigates to edit page
- **Delete Button** (Red): Removes record with confirmation

### Edit Page
- **ID Field**: Read-only display of record ID
- **Name Field**: Editable text input
- **Age Field**: Editable number input
- **Update Button** (Blue): Saves changes
- **Cancel Button**: Returns to main page

## Styling

- **Color Scheme**: Purple gradient background with white cards
- **Layout**: Center-aligned responsive container
- **Effects**: Smooth animations, hover effects, box shadows
- **Buttons**:
  - Green (#4caf50) for Add
  - Blue (#2196f3) for Edit/Update
  - Red (#f44336) for Delete
  - Gray (#757575) for Cancel

## Browser Support

Works on all modern browsers:
- Chrome/Chromium
- Firefox
- Safari
- Edge

## Requirements

- Python 3.7+
- Flask 2.3+
- Flask-SQLAlchemy 3.0+
- SQLAlchemy 2.0+

## Notes

- The database file `data.db` is created automatically in the project root
- Deletion requires confirmation to prevent accidental data loss
- Age input is restricted to values between 1 and 150
- The application runs in debug mode for development

## License

This project is open source and available for educational purposes.
