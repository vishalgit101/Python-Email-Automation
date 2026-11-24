# Python Email Automation 📧

A simple Python-based email automation project that allows you to send emails to multiple recipients using Gmail SMTP.

The project uses environment variables to securely store Gmail credentials and a text file (`emails.txt`) to manage recipient email addresses.

## 🚀 Features

- Send emails to multiple recipients using Gmail SMTP.
- Securely store Gmail credentials using a `.env` file.
- Manage recipient email addresses through `emails.txt`.
- Use Google App Passwords for authentication.
- Keep sensitive credentials separate from source code.
- Lightweight setup with minimal dependencies.

## 📁 Project Structure

```text
Python-Email-Automation/
│
├── main.py              # Main Python script
├── emails.txt           # Recipient email addresses
├── requirements.txt     # Python dependencies
├── .env                 # Your Gmail credentials (create this)
├── .env.example         # Example environment configuration
├── .gitignore           # Files excluded from Git
└── README.md            # Project documentation
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone git@github.com:vishalgit101/Python-Email-Automation.git
```

Navigate into the project directory:

```bash
cd Python-Email-Automation
```

### 2. Create a Virtual Environment (Recommended)

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

**Windows (Git Bash):**

```bash
source venv/Scripts/activate
```

**Windows (Command Prompt):**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python package:

```bash
pip install -r requirements.txt
```

The project uses Python's built-in libraries such as `os`, `smtplib`, `pathlib`, and `email.message`. These do not require separate installation.

The only external dependency is:

- `python-dotenv`

## 🔐 Gmail Configuration

To send emails through Gmail, you need to configure your Gmail account using a Google App Password.

**Do not use your regular Gmail account password.**

### Step 1: Enable 2-Step Verification

1. Visit [Google Account Security](https://myaccount.google.com/security).
2. Sign in to your Google account.
3. Enable **2-Step Verification** if it is not already enabled.

### Step 2: Generate a Google App Password

1. Visit [Google App Passwords](https://myaccount.google.com/apppasswords).
2. Sign in to your Google account.
3. Enter an app name, for example: `Python Email Automation`.
4. Click **Create**.
5. Google will generate a 16-character App Password.
6. Copy the generated password and keep it secure.

**Note:** App Passwords may not be available for every Google account. Certain organizational accounts and accounts enrolled in Advanced Protection may have restrictions.

### Step 3: Create Your `.env` File

In the root directory of the project, create a file named:

```text
.env
```

Add the following variables:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_16_character_app_password
```

Replace the example values with your own Gmail address and Google App Password.

**Important:**

- `EMAIL_ADDRESS` should contain your Gmail address.
- `EMAIL_PASSWORD` should contain your Google App Password.
- Do not use your regular Gmail login password.
- Do not share your `.env` file.
- Never upload your `.env` file to GitHub.

## 📩 Adding Recipient Email Addresses

Create or open the `emails.txt` file in the project root.

Add the email addresses of the people you want to send emails to.

Example:

```text
user1@gmail.com
user2@gmail.com
user3@example.com
user4@gmail.com
```

**Important:**

- Add one email address per line.
- Make sure the email addresses are valid.
- Remove addresses you no longer want to contact.
- Only send emails to recipients who have agreed to receive them.

The application reads the recipient addresses from this file.

## ▶️ Running the Project

After completing the installation and configuration:

Run the main Python script:

```bash
python main.py
```

The application will use the Gmail credentials stored in `.env` and the recipient addresses listed in `emails.txt`.

## 📦 Requirements

Python 3 and the following external package are required:

```text
python-dotenv
```

All other imports used by this project are part of Python's standard library.

## 🔒 Security & Privacy

Please follow these security practices:

1. Never upload your `.env` file to GitHub.
2. Never share your Google App Password.
3. Keep your recipient email list private.
4. If your App Password is exposed, revoke it through your Google Account and generate a new one.
5. Do not send unsolicited bulk emails or spam.

Make sure your `.gitignore` contains:

```gitignore
.env
.env.*
!.env.example
emails.txt
venv/
.venv/
__pycache__/
*.pyc
```

### Optional: Create a `.env.example` File

You can create a `.env.example` file to show other users which environment variables are required.

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

This example file can safely be committed to GitHub because it contains placeholder values, not actual credentials.

## 🛠️ Technologies Used

- Python
- Gmail SMTP
- Python-dotenv

## 👨‍💻 Author

**Vishal**

GitHub: [@vishalgit101](https://github.com/vishalgit101)

Project Repository: [Python-Email-Automation](https://github.com/vishalgit101/Python-Email-Automation)

---

If you find this project useful, consider giving the repository a ⭐ star!
