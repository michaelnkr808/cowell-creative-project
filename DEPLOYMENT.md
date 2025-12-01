# 🚀 Deployment Guide

This guide covers deploying your AI Tenant Rights chatbot to production.

## Architecture Overview

```
┌─────────────────┐         ┌─────────────────┐
│  Vercel         │         │  Render/Railway │
│  (Frontend)     │ ───────▶│  (Backend API)  │
│  React App      │  HTTPS  │  Python/FastAPI │
└─────────────────┘         └─────────────────┘
                                    │
                                    ▼
                            ┌─────────────────┐
                            │  Google Gemini  │
                            │  API            │
                            └─────────────────┘
```

---

## Part 1: Deploy Backend (Python/FastAPI)

### Option A: Deploy to Render (Recommended)

**Step 1: Prepare Your Backend**

The backend is already ready! Just make sure:
- ✅ `requirements.txt` exists in `backend/`
- ✅ `app.py` is in `backend/`

**Step 2: Create Render Account**

1. Go to https://render.com
2. Sign up with GitHub
3. Authorize Render to access your repositories

**Step 3: Create Web Service**

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository
3. Configure the service:

```
Name: tenant-rights-backend
Region: Oregon (or closest to you)
Branch: main
Root Directory: backend
Runtime: Python 3

Build Command:
pip install -r requirements.txt

Start Command:
uvicorn app:app --host 0.0.0.0 --port $PORT
```

**Step 4: Add Environment Variables**

In the Render dashboard, go to "Environment" tab and add:

```
GOOGLE_API_KEY=your_actual_gemini_api_key_here
```

**Step 5: Deploy!**

Click "Create Web Service" and wait ~5 minutes for deployment.

You'll get a URL like: `https://tenant-rights-backend.onrender.com`

**Step 6: Test Your Backend**

Visit: `https://your-app-name.onrender.com/`

You should see: `{"status":"ok","message":"Tenant Rights Chatbot API is running"}`

---

### Option B: Deploy to Railway

1. Go to https://railway.app
2. Sign in with GitHub
3. "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway auto-detects Python
6. Add environment variable: `GOOGLE_API_KEY`
7. Deploy!

---

## Part 2: Deploy Frontend (React) to Vercel

**Step 1: Update Frontend to Use Production Backend**

Currently your React app points to `http://localhost:8000`. We need to make it dynamic.

**Step 2: Push to GitHub**

```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

**Step 3: Deploy to Vercel**

1. Go to https://vercel.com
2. Sign in with GitHub
3. Click "Add New..." → "Project"
4. Import your GitHub repository
5. Configure:
   - **Framework Preset**: Vite
   - **Root Directory**: `./` (leave default)
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
6. Click "Deploy"

**Step 4: Add Environment Variable**

In Vercel dashboard, go to:
- Settings → Environment Variables
- Add: `VITE_API_URL` = `https://your-render-backend-url.onrender.com`

---

## Part 3: Connect Frontend to Backend

We need to update your React app to use the production backend URL.

**Update `src/App.tsx`:**

Instead of hardcoding `http://localhost:8000`, use an environment variable:

```typescript
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

// In your fetch call:
const response = await fetch(`${API_URL}/chat`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ message: input }),
})
```

**Create `.env.local` for local development:**

```
VITE_API_URL=http://localhost:8000
```

This way:
- Locally: Uses `http://localhost:8000`
- Production: Uses the Vercel environment variable

---

## Part 4: Update Backend CORS

Your backend needs to allow requests from your Vercel domain.

In `backend/app.py`, update CORS:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",           # Local dev
        "https://your-app.vercel.app",     # Production
        "https://*.vercel.app",            # All Vercel preview URLs
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 📊 Cost Breakdown (Free Tiers)

| Service | Free Tier | What You Get |
|---------|-----------|--------------|
| **Vercel** | ✅ Free | Unlimited bandwidth, 100GB/month |
| **Render** | ✅ Free | 750 hours/month, sleeps after inactivity |
| **Railway** | ✅ $5 credit/month | Good for small apps |
| **Gemini API** | ✅ Free | 60 requests/minute |

**Total Cost: $0/month** for moderate usage!

---

## 🔧 Troubleshooting

### Backend "Service Unavailable" on Render

**Problem**: Render free tier puts apps to sleep after 15 minutes of inactivity.

**Solution**: 
- First request wakes it up (takes ~30 seconds)
- Consider upgrading to paid tier ($7/month for always-on)
- Or use Railway which has better free tier

### CORS Errors

**Problem**: Frontend can't connect to backend.

**Solution**: Check that:
1. Backend CORS includes your Vercel URL
2. You're using HTTPS (not HTTP) for production URLs
3. Environment variables are set correctly

### API Key Not Working

**Problem**: 500 errors from backend.

**Solution**:
1. Check Render/Railway environment variables
2. Make sure `GOOGLE_API_KEY` is set correctly
3. Check backend logs in Render dashboard

---

## 🎓 Development vs Production

```
┌──────────────────────────────────────────────┐
│ DEVELOPMENT (Your Computer)                  │
├──────────────────────────────────────────────┤
│ Frontend: http://localhost:5173              │
│ Backend:  http://localhost:8000              │
│ Database: None (using AI only)               │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ PRODUCTION (Internet)                        │
├──────────────────────────────────────────────┤
│ Frontend: https://your-app.vercel.app        │
│ Backend:  https://your-api.onrender.com      │
│ Database: None (using AI only)               │
└──────────────────────────────────────────────┘
```

---

## ✅ Deployment Checklist

**Backend:**
- [ ] Push code to GitHub
- [ ] Create Render/Railway account
- [ ] Deploy backend service
- [ ] Add `GOOGLE_API_KEY` environment variable
- [ ] Test backend URL in browser
- [ ] Update CORS to allow frontend domain

**Frontend:**
- [ ] Update API URL to use environment variable
- [ ] Push code to GitHub
- [ ] Create Vercel account
- [ ] Deploy to Vercel
- [ ] Add `VITE_API_URL` environment variable
- [ ] Test the app!

---

## 📱 Next Steps After Deployment

1. **Custom Domain** (optional)
   - Buy a domain (e.g., `tenantrightsai.com`)
   - Connect to Vercel for frontend
   - Connect to Render for backend API

2. **Analytics** (optional)
   - Add Google Analytics
   - Track usage and popular questions

3. **Monitoring** (optional)
   - Use Render's built-in monitoring
   - Set up error alerts

4. **Add RAG** (future enhancement)
   - Upload California tenant rights PDFs
   - Implement document retrieval
   - More accurate, cited responses

---

**Need help with deployment? Let me know which service you choose!** 🚀

