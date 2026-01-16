# Geometry Dash Demon List Website - Deployment Guide

## 🎮 What This Is

This is a Geometry Dash Demon List website with embedded YouTube videos for each level. All YouTube links have been converted to iframes that play directly on the page.

## 🚀 Quick Start - 3 FREE Hosting Options

### Option 1: GitHub Pages (RECOMMENDED - Easiest & Free Forever)

**Step-by-step:**

1. **Create a GitHub account** (if you don't have one):
   - Go to https://github.com
   - Click "Sign up" and follow the instructions

2. **Create a new repository**:
   - Click the "+" icon in the top right
   - Select "New repository"
   - Name it: `gddl-website` (or anything you want)
   - Set to "Public"
   - Click "Create repository"

3. **Upload your files**:
   - Click "uploading an existing file"
   - Drag and drop ALL files from the `gddl-website` folder
   - Scroll down and click "Commit changes"

4. **Enable GitHub Pages**:
   - Go to your repository Settings
   - Click "Pages" in the left sidebar
   - Under "Source", select "main" branch
   - Click "Save"
   - Wait 1-2 minutes

5. **Get your link**:
   - Your site will be live at: `https://YOUR-USERNAME.github.io/gddl-website/`
   - Click the link at the top of the Pages settings to visit it!

**Pros:**
- ✅ 100% Free forever
- ✅ No credit card required
- ✅ Custom domain support
- ✅ Automatic HTTPS
- ✅ No server management needed
- ✅ Link never expires

---

### Option 2: Netlify (Also Great & Free)

**Step-by-step:**

1. **Create a Netlify account**:
   - Go to https://www.netlify.com
   - Click "Sign up" (you can use GitHub, email, etc.)

2. **Deploy your site**:
   - Drag and drop the entire `gddl-website` folder onto the Netlify dashboard
   - That's it! Netlify will give you a URL instantly

3. **Get your link**:
   - You'll get a URL like: `https://random-name-12345.netlify.app`
   - You can change this in Site settings > Domain management > Options > Edit site name

**Pros:**
- ✅ 100% Free forever
- ✅ Instant deployment (drag & drop)
- ✅ Automatic HTTPS
- ✅ Easy to update (just drag new files)
- ✅ Link never expires

---

### Option 3: Vercel (Modern & Fast)

**Step-by-step:**

1. **Create a Vercel account**:
   - Go to https://vercel.com
   - Click "Sign Up" (use GitHub, GitLab, or email)

2. **Deploy your site**:
   - Click "Add New..." → "Project"
   - Click "Browse" and select your `gddl-website` folder
   - Or drag and drop the folder
   - Click "Deploy"

3. **Get your link**:
   - You'll get a URL like: `https://your-project.vercel.app`
   - Can be customized in Settings

**Pros:**
- ✅ 100% Free forever
- ✅ Very fast performance
- ✅ Automatic HTTPS
- ✅ Easy updates
- ✅ Link never expires

---

## 📝 Files Included

- `index.html` - Main demon list page
- `leaderboard.html` - Leaderboard page
- `documentation.html` - API documentation
- Individual level pages (acheron.html, amethyst.html, etc.)
- All images (.jpg, .jpeg, .png files)
- CSS files (style.css, style2.css)
- All YouTube links converted to embedded iframes

## 🎥 YouTube Embedding

All level pages now show YouTube videos directly on the page using iframes instead of external links. Videos will play without leaving your site!

## 🔧 Local Testing (Optional)

If you want to test the website on your computer first:

1. Install Python (it's usually pre-installed on Mac/Linux)
2. Open Terminal/Command Prompt
3. Navigate to the website folder:
   ```bash
   cd path/to/gddl-website
   ```
4. Run a local server:
   ```bash
   python3 -m http.server 8000
   ```
5. Open browser and go to: `http://localhost:8000`

## 🌐 Custom Domain (Optional)

All three hosting options support custom domains:

**GitHub Pages:**
- Go to Settings → Pages → Custom domain
- Enter your domain name
- Add CNAME record in your domain provider

**Netlify/Vercel:**
- Go to Domain settings
- Click "Add custom domain"
- Follow the DNS instructions

## 💡 Why These Are Better Than ngrok

**ngrok issues:**
- ❌ Link expires when you close your computer
- ❌ Requires keeping your computer running 24/7
- ❌ Random URLs that change
- ❌ Limited free hours per month
- ❌ Slower performance

**GitHub Pages/Netlify/Vercel benefits:**
- ✅ Always online, even when your computer is off
- ✅ Free forever
- ✅ Professional URLs
- ✅ Fast global CDN
- ✅ No maintenance required
- ✅ Automatic HTTPS/SSL
- ✅ No technical knowledge needed

## 🆘 Troubleshooting

**Videos not loading?**
- Make sure you have internet connection
- Check if YouTube is accessible in your country
- Try a different browser

**Site not loading?**
- Wait 2-3 minutes after deployment
- Clear browser cache (Ctrl+F5 or Cmd+Shift+R)
- Check if all files were uploaded

**Want to update the site?**
- GitHub Pages: Commit and push new files
- Netlify: Drag and drop new files to dashboard
- Vercel: Push to repository or redeploy

## 📧 Need Help?

- GitHub Pages docs: https://docs.github.com/pages
- Netlify docs: https://docs.netlify.com
- Vercel docs: https://vercel.com/docs

---

**Recommendation:** Use GitHub Pages for the best free hosting experience!
