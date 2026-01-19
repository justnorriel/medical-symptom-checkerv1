# 🚀 Deployment Guide

## Free Hosting Options

### 1. **Render** (Recommended)
**Steps:**
1. Push code to GitHub
2. Sign up at [render.com](https://render.com)
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Python Version**: `3.11`
6. Deploy! 🎉

**URL**: `https://your-app-name.onrender.com`

---

### 2. **Vercel** (Fastest Setup)
**Steps:**
1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel --prod`
3. Follow prompts
4. Deploy complete!

**URL**: `https://your-app-name.vercel.app`

---

### 3. **PythonAnywhere**
**Steps:**
1. Sign up at [pythonanywhere.com](https://pythonanywhere.com)
2. Create "Web" app
3. Set Flask app path
4. Upload files via web interface
5. Install requirements in console

**URL**: `https://yourusername.pythonanywhere.com`

---

### 4. **Railway**
**Steps:**
1. Sign up at [railway.app](https://railway.app)
2. Connect GitHub repo
3. Railway auto-detects Flask
4. Deploy with one click

**URL**: `https://your-app-name.up.railway.app`

---

## 📁 Files Created for Deployment

- ✅ `vercel.json` - Vercel configuration
- ✅ `Procfile` - Heroku/Railway process definition
- ✅ `requirements.txt` - All dependencies
- ✅ `Dockerfile` - Container deployment

---

## 🎯 Recommended: Render

**Why Render?**
- ✅ Most generous free tier
- ✅ Best Docker support
- ✅ Auto-deploys from GitHub
- ✅ Custom domains free
- ✅ No credit card required

---

## ⚡ Quick Deploy Commands

```bash
# For Vercel
npm i -g vercel
vercel --prod

# For Render (just push to GitHub)
git add .
git commit -m "Ready for deployment"
git push origin main
```

---

## 🔧 Production Considerations

- ✅ All hosting platforms support your pgmpy dependencies
- ✅ Gunicorn included for production server
- ✅ Environment variables supported
- ✅ SSL certificates automatic
- ✅ Global CDN on most platforms

---

## 📊 Resource Limits

| Platform | Free Tier | Sleep Time | Custom Domain |
|----------|-----------|------------|---------------|
| Render | 750h/mo | 15 min | ✅ |
| Vercel | Unlimited | None | ✅ |
| PythonAnywhere | 1 web app | None | ❌ |
| Railway | $5/mo credit | None | ✅ |

Your medical symptom checker is lightweight and will run perfectly on any free tier!
