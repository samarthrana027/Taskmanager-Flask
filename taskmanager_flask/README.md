# Task Manager Flask Application

A sleek, modern task management application built with Flask. This project provides a clean interface for managing tasks with priority levels, due dates, and status tracking.

## 📋 Overview

This task manager application is a full-featured web application built with **Flask** (backend) and **HTML/CSS** (frontend). The project includes two main implementations:

1. **taskmanager_app.py** - Pure Flask application with inline HTML/CSS
2. **taskmanager_flask1.py** - Streamlit-based interface with API integration

## ✨ Features

### Core Functionality
- ✅ Create, read, update, and delete (CRUD) tasks
- 📌 Assign priority levels: **High**, **Medium**, **Low**
- 📅 Set due dates with overdue tracking
- 🏷️ Task status management: **Pending** and **Completed**
- 🔍 Filter tasks by:
  - Status (Pending/Completed)
  - Priority level (High/Medium/Low)
  - All tasks view

### User Interface
- 🎨 Modern dark theme with vibrant accent colors
- ⚡ Smooth animations and transitions
- 📱 Responsive design
- 🎯 Intuitive task management interface
- 📊 Dashboard with task statistics

### Visual Design
- **Accent Color**: Bright yellow-green (#e8ff47)
- **Priority Colors**:
  - 🔴 High: Red (#ff5252)
  - 🟠 Medium: Orange (#ffaa47)
  - 🟢 Low: Green (#4dff91)
- **Custom Fonts**: Syne (headings), DM Sans (body)

## 📁 Project Structure

```
taskmanager_flask/
├── taskmanager_app.py          # Main Flask application
├── taskmanager_flask1.py        # Streamlit frontend application
├── templates/                   # HTML template files
│   ├── index.html               # Task list page
│   ├── add.html                 # Add task form
│   └── edit.html                # Edit task form
└── README.md                    # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Flask
- Streamlit (for taskmanager_flask1.py)
- Requests library

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/samarthrana027/Flask-Project.git
   cd Flask-Project/taskmanager_flask
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask streamlit requests
   ```

## 🏃 Running the Application

### Option 1: Flask Application (taskmanager_app.py)

```bash
python taskmanager_app.py
```

The application will start on `http://localhost:5000`

**Features:**
- Pure Flask backend with embedded HTML/CSS
- In-memory task storage
- No external dependencies beyond Flask
- Full CRUD operations via web interface

### Option 2: Streamlit Interface (taskmanager_flask1.py)

First, ensure the Flask API is running (see Option 1), then:

```bash
streamlit run taskmanager_flask1.py
```

The Streamlit app will open in your browser (typically `http://localhost:8501`)

**Features:**
- Modern Streamlit UI
- Communicates with Flask backend API
- Dashboard with statistics
- Side navigation with filters

## 📖 Usage Guide

### Adding a Task

1. Click **"New Task"** button (Flask app) or navigate to **"➕ Add Task"** (Streamlit)
2. Enter task title (required)
3. Select priority level:
   - 🔴 High
   - 🟠 Medium (default)
   - 🟢 Low
4. Optionally set a due date
5. Click **"Add Task"** to create

### Viewing Tasks

- **All Tasks**: View all tasks on the main page
- **Filters**: Use filter buttons to view by:
  - Status: Pending, Completed
  - Priority: High, Medium, Low
- **Statistics**: Quick stats showing:
  - Total tasks
  - Pending tasks
  - Completed tasks
  - Overdue tasks

### Managing Tasks

**Mark as Complete:**
- Click the **"Done"** button (green checkmark icon) next to a task
- Completed tasks appear with reduced opacity and strikethrough text

**Reopen Task:**
- Click the **"Reopen"** button (circular arrow icon) on completed tasks
- Status reverts to pending

**Edit Task:**
- Click the **"Edit"** button (pencil icon)
- Modify title, priority, status, or due date
- Click **"Save Changes"** to update

**Delete Task:**
- Click the **"Delete"** button (trash icon)
- Confirm deletion in the popup

## 💻 API Endpoints (Flask Backend)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Display all tasks with filters |
| GET | `/?filter=<filter>` | Filter tasks by status or priority |
| POST | `/add` | Create a new task |
| GET | `/edit/<task_id>` | Display edit form |
| POST | `/edit/<task_id>` | Update a task |
| GET | `/toggle/<task_id>` | Toggle task completion status |
| GET | `/delete/<task_id>` | Delete a task |

## 🎨 Customization

### Colors
Edit the `STYLES` variable in `taskmanager_app.py` to customize:
```python
PRIORITY_META = {
    "high":   {"color": "#ff5252", "dim": "rgba(255,82,82,0.12)",  "label": "High"},
    "medium": {"color": "#ffaa47", "dim": "rgba(255,170,71,0.12)", "label": "Medium"},
    "low":    {"color": "#4dff91", "dim": "rgba(77,255,145,0.12)", "label": "Low"},
}
```

### Fonts
CSS variables in the style section:
```css
--bg: #0f0f0f;           /* Dark background */
--accent: #e8ff47;       /* Bright yellow-green */
--text: #f0f0f0;         /* Light text */
```

## 🔧 Technical Details

### Data Structure
Tasks are stored in-memory as dictionaries:
```python
{
    "id": 1,
    "title": "Task title",
    "status": "pending",        # pending or completed
    "priority": "medium",        # high, medium, or low
    "due_date": "2024-12-31"    # Optional, format: YYYY-MM-DD
}
```

### Key Functions (taskmanager_app.py)

- `fmt_date()` - Format and validate dates, check if overdue
- `build_task_row()` - Generate HTML for individual task items
- `base_page()` - Template for all pages with consistent styling

### Routing

- **Index** (`/`) - Main task list with filtering
- **Add** (`/add`) - Create new tasks
- **Edit** (`/edit/<id>`) - Modify existing tasks
- **Toggle** (`/toggle/<id>`) - Mark tasks complete/pending
- **Delete** (`/delete/<id>`) - Remove tasks

## 📊 Database Notes

Currently uses **in-memory storage** (Python list). To persist data:
- Add SQLite integration
- Use SQLAlchemy ORM
- Implement JSON file storage
- Deploy with a production database

## 🐛 Known Limitations

- Tasks are stored in memory and lost on app restart
- Single-user application (no authentication)
- No sorting options (displays in creation order)
- No task descriptions in Flask version
- No recurring tasks

## 🚀 Future Enhancements

- [ ] Persistent database storage (SQLite/PostgreSQL)
- [ ] User authentication and authorization
- [ ] Task categories/tags
- [ ] Recurring tasks
- [ ] Due date reminders/notifications
- [ ] Task search functionality
- [ ] Collaborative task management
- [ ] Mobile app
- [ ] Dark/Light theme toggle

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📧 Contact

For questions or suggestions, please reach out via GitHub issues.

---

**Built with ❤️ using Flask and Python**
