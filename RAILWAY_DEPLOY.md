# Railway Deployment for Puch AI MCP Server

## 🚂 **Deploy to Railway Steps:**

### **1. Create Railway Account**
- Go to [railway.app](https://railway.app)
- Sign up with GitHub account

### **2. Install Railway CLI (Optional)**
```bash
npm install -g @railway/cli
```

### **3. Deploy via GitHub (Recommended)**

#### **Option A: GitHub Integration**
1. Create a new GitHub repository
2. Push your code to GitHub
3. Connect Railway to your GitHub repo
4. Deploy automatically

#### **Option B: Railway CLI**
1. Login: `railway login`
2. Initialize: `railway init`
3. Deploy: `railway up`

### **4. Set Environment Variables**
In Railway dashboard, set:
- `AUTH_TOKEN` = `5079b331ef08`
- `PHONE_NUMBER` = `9516326057`

### **5. Get Your Railway URL**
Railway will provide a URL like:
`https://your-app-name.railway.app`

Your MCP endpoint will be:
`https://your-app-name.railway.app/mcp`

### **6. Update Puch Connection**
```
/mcp connect https://your-app-name.railway.app/mcp 5079b331ef08
```

## 📁 **Files Ready for Deployment:**
- ✅ `dummy.py` (updated for Railway)
- ✅ `requirements.txt`
- ✅ `Procfile`
- ✅ `runtime.txt`
- ✅ `resume.md`

## 🔧 **What Changed:**
- Added environment variable support
- Dynamic port configuration for Railway
- Production-ready configuration

Ready to deploy! 🚀
