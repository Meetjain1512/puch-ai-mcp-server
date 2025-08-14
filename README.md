# Puch AI MCP Server Setup Instructions

## ✅ Current Status
Your MCP server is successfully running on `http://localhost:8085/mcp`

## 📝 Next Steps to Complete Setup

### 1. Get Your Application Key
- Use this command with Puch: `/apply <TWITTER/LINKEDIN REPLY URL>`
- You will receive an application key

### 2. Update Your Token
- Open `dummy.py`
- Replace `"your_application_key_here"` with your actual application key
- Replace `"919189123456"` with your actual phone number in format `{country_code}{number}`
  - Example: `919876543210` for an Indian number (no + symbol)

### 3. Update Your Resume
- Edit `resume.md` with your actual resume content
- The file is already created with a sample resume

### 4. Make Server Publicly Accessible
For Puch to connect to your server, you need to make it publicly accessible. Options:

#### Option A: Using ngrok (Recommended for testing)
1. Install ngrok: `choco install ngrok` (if you have Chocolatey) or download from ngrok.com
2. Run: `ngrok http 8085`
3. Copy the public URL (e.g., `https://abc123.ngrok.io`)
4. Your server URL will be: `https://abc123.ngrok.io/mcp`

#### Option B: Using a Cloud Service
- Deploy to Heroku, Railway, or any cloud platform
- Make sure the port is configurable via environment variables

### 5. Connect with Puch
Use this command to connect Puch with your server:
```
/mcp connect <YOUR_PUBLIC_SERVER_URL>/mcp <YOUR_AUTH_TOKEN>
```

Example:
```
/mcp connect https://abc123.ngrok.io/mcp your_actual_application_key_here
```

## 🔧 Server Features
Your server includes:
- **Resume tool**: Returns your resume in markdown format
- **Validate tool**: Returns your phone number for validation
- **Fetch tool**: Fetches and converts web content to markdown

## 🚀 Running the Server
To start your server:
```powershell
python dummy.py
```

The server will be available at: `http://localhost:8085/mcp`

## 📞 Validation
Puch will validate:
1. Your auth token (application key)
2. Your phone number format: `{country_code}{number}` (no + symbol)

## 🔍 Testing
You can test your server locally by visiting: `http://localhost:8085/mcp`

Good luck with your Puch AI integration! 🎉
