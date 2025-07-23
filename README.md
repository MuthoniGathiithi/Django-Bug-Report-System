# Bug Reporting System 🐛

A comprehensive Django-based bug tracking and reporting system with role-based access control. This system allows users to submit bug reports while providing administrators with tools to manage and resolve issues efficiently.

## 📋 Table of Contents

- [Features](#features)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [User Roles](#user-roles)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### Core Functionality
- **Bug Submission**: Users can submit detailed bug reports with title, description, and priority levels
- **Status Tracking**: Track bugs through their lifecycle (Open → In Progress → Resolved → Closed)
- **Priority Management**: Categorize bugs by priority (Low, Medium, High, Critical)
- **Assignment System**: Assign bugs to specific team members for resolution

### Advanced Features
- **Role-Based Access Control**: Three-tier user system (User, Admin, Super Admin)
- **Admin Request System**: Users can request admin privileges with approval workflow
- **Search & Filter**: Advanced filtering by status, priority, and text search
- **Pagination**: Efficient handling of large bug databases
- **Admin Dashboard**: Comprehensive overview with statistics and recent activity
- **User Profiles**: Personal dashboards showing submitted bugs and role requests

### Technical Features
- **Django Admin Integration**: Full administrative interface for all models
- **Responsive Design**: Bootstrap-powered responsive UI
- **User Authentication**: Secure login/registration system
- **Signal-based Profile Creation**: Automatic user profile generation
- **Form Validation**: Comprehensive client and server-side validation

## 🏗️ System Architecture

### Models
- **Bug**: Core bug report model with status, priority, and assignment tracking
- **UserProfile**: Extended user model with role management
- **AdminRequest**: Role elevation request system

### User Roles
1. **Regular User**: Can submit bugs and request admin privileges
2. **Admin**: Can manage bugs, update statuses, assign tasks, and request super admin
3. **Super Admin**: Full system access including approving admin requests

## 🚀 Installation

### Prerequisites
- Python 3.8+
- Django 4.0+
- Git

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/bug-reporting-system.git
   cd bug-reporting-system
   ```

2. **Create project structure**
   ```bash
   mkdir BUGreporting_system
   cd BUGreporting_system
   ```

3. **Set up virtual environment**
   ```bash
   # Windows
   python -m venv bug_env
   bug_env\Scripts\activate
   
   # Mac/Linux
   python -m venv bug_env
   source bug_env/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install django
   ```

5. **Create Django project**
   ```bash
   django-admin startproject bugreporting .
   cd bugreporting
   python manage.py startapp bugs
   ```

6. **Configure settings**
   - Add `'bugs'` to `INSTALLED_APPS` in `settings.py`
   - Copy all model, view, form, and template files from the repository

7. **Set up database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

8. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

9. **Run the server**
   ```bash
   python manage.py runserver
   ```

10. **Access the application**
    - Main application: `http://127.0.0.1:8000/`
    - Admin interface: `http://127.0.0.1:8000/admin/`

## 📖 Usage

### For Regular Users
1. **Register**: Create an account using the registration form
2. **Submit Bugs**: Use the "Submit Bug" form to report issues
3. **Track Progress**: View your submitted bugs and their current status
4. **Request Admin**: Apply for admin privileges through your profile

### For Admins
1. **Dashboard Access**: Access the admin dashboard for system overview
2. **Bug Management**: Update bug statuses, assign team members
3. **User Management**: View user profiles and submitted bugs
4. **Request Super Admin**: Apply for elevated privileges

### For Super Admins
1. **Full System Control**: Access all administrative functions
2. **Role Management**: Approve or reject admin role requests
3. **User Oversight**: Manage all user accounts and permissions
4. **System Statistics**: View comprehensive system analytics

## 🔐 User Roles

| Role | Permissions |
|------|-------------|
| **User** | Submit bugs, view own submissions, request admin role |
| **Admin** | All user permissions + manage bugs, assign tasks, update statuses |
| **Super Admin** | All admin permissions + approve role requests, full system access |

## 📁 Project Structure

```
BUGreporting_system/
├── bugreporting/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── bugs/
│   ├── migrations/
│   ├── templates/
│   │   ├── bugs/
│   │   │   ├── base.html
│   │   │   ├── home.html
│   │   │   ├── bug_list.html
│   │   │   ├── bug_detail.html
│   │   │   ├── submit_bug.html
│   │   │   ├── update_bug.html
│   │   │   ├── profile.html
│   │   │   ├── admin_dashboard.html
│   │   │   ├── register.html
│   │   │   └── request_admin.html
│   │   └── registration/
│   │       └── login.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── signals.py
│   ├── views.py
│   └── urls.py
└── manage.py
```

## 🎯 Key Features Demonstrated

### Django Skills
- **Models & Relationships**: Complex model relationships with foreign keys
- **Forms**: Custom forms with validation and widgets
- **Views**: Function-based views with permissions and filtering
- **Templates**: Responsive template system with inheritance
- **Admin Interface**: Customized Django admin with inline editing
- **Signals**: Automated profile creation using Django signals
- **Authentication**: Custom user registration and role management

### Web Development Skills
- **Responsive Design**: Bootstrap integration for mobile-friendly interface
- **User Experience**: Intuitive navigation and feedback systems
- **Security**: Role-based access control and permission checking
- **Database Design**: Efficient queries with filtering and pagination

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📋 Future Enhancements

- [ ] Email notifications for bug assignments
- [ ] File attachments for bug reports
- [ ] Comment system for bug discussions
- [ ] API endpoints for mobile app integration
- [ ] Advanced reporting and analytics
- [ ] Bug categories and tagging system
- [ ] Integration with external tools (Slack, Jira)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/MuthoniGathiithi)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/muthoni-gathiithi)

## 🙏 Acknowledgments

- Django Documentation and Community
- Bootstrap for responsive design components
- Contributors and testers

---

### 📞 Support

If you encounter any issues or have questions, please [open an issue](https://github.com/MuthoniGathiithi/bug-reporting-system/issues) on GitHub.

**Happy Bug Hunting! 🐛🔍**
