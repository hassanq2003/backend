# Backend Project

This is a Django backend project connected to a MongoDB cluster.

## Setup Instructions

1. **Install Dependencies**:
   Ensure you have Python 3.10+ installed. Install the requirements using:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables**:
   Create a `.env` file in this directory based on the `.env.example` file. 
   Add your MongoDB database password:
   ```env
   DB_PASSWORD=your_mongodb_password_here
   ```

3. **Run the Server**:
   Start the Django development server:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

## API Routes

The backend uses Django REST Framework. The following routes are available:

- `GET /api/phones/` - List all phone synchronization records.
- `POST /api/phones/` - Create a new phone synchronization record.
- `GET /api/phones/{id}/` - Retrieve a specific phone record.
- `PUT /api/phones/{id}/` - Update a specific phone record.
- `DELETE /api/phones/{id}/` - Delete a specific phone record.

### Example Phone Record JSON
```json
{
  "name": "John's iPhone",
  "sync_time": "2026-09-28T12:00:00Z"
}
```
Note: `created_at` is generated automatically when the record is saved.

## Replit Deployment

This project is configured for seamless deployment on Replit.
It includes a `.replit` configuration file that will automatically provision the correct Python environment and start the Django server. Ensure you set the `DB_PASSWORD` secret in your Replit workspace's Secrets panel.
