# Online Learning Platform

This project is an online learning platform built using Django. It offers various apps and functionalities to facilitate the learning process for students and instructors.

---

## Apps and Functionality

### 1. Signup

The Signup app handles the sign-up and login processes for students and instructors. Students can sign up or log in, while instructors can only log in. To create a new instructor, access the Django admin area.

### 2. Student Dashboard

The Student Dashboard app caters to all student-related activities. Students can register for new courses, upload assignment submissions, view assessments on submissions, and browse available courses.

### 3. Instructors Dashboard

The Instructors Dashboard app focuses on instructor-related tasks. Instructors can register courses, upload assignments, view student submissions, and assess them accordingly.

### 4. Forums

Each course has its own forum where students and instructors can post and engage in discussions. The Forums app manages all aspects of the forum, including creating new posts, replying to posts, and authentication to ensure access is limited to registered participants.

### 5. Notifications

The Notifications app includes the Notification model, which is integrated throughout the entire project. It allows users to receive and view notifications, and also provides a view to mark notifications as read.

---

## Getting Started

To explore and run this Online Learning Platform project, follow these steps:

1. **Clone the Repository:** Clone the repository from the following link:

   [Online Learning Platform Repository](https://github.com/SajeelHashmi/Online-Learning-Platform-Django)

2. **Install Requirements:** Install the required packages by executing the following command in the project directory:

        pip install -r requirements.txt

3. **Database Setup:** Configure the database settings in the project's `settings.py` file.

4. **Run Migrations:** Apply the database migrations by running the following command:

        python manage.py migrate

5. **Create a Superuser:** Create a superuser account to access the Django admin area and perform administrative tasks. Use the following command and follow the prompts:

        python manage.py createsuperuser

6. **Run the Development Server:** Start the development server by executing the following command:

        python manage.py runserver

7. **Access the Application:** Open your web browser and visit `http://localhost:8000` to access the Online Learning Platform.

---

For testing purposes, the repository currently includes the following users:

- Username: sajeelhashmi | Password: sajeelhashmi (Superuser, Instructor)
- Username: superuser2 | Password: changepass (Superuser)
- Username: testuser2 | Password: thisisatestuser (Student)

The superusers have access to the Django admin area.

---

Feel free to explore and experiment with this Online Learning Platform. It demonstrates various features and functionalities typically found in an online learning environment, providing students and instructors with a seamless experience.

If you have any questions or need assistance, please feel free to contact Sajeel Hashmi at sajeelhashmi.12@gmail.com.

---

Please note that the instructions provided here assume a basic understanding of Django and web development concepts.
