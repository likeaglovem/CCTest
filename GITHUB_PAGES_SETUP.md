# GitHub Pages Setup Guide

This guide will help you host your Content Dashboard on GitHub Pages, solving the CORS issue.

## Steps to Deploy

### 1. Add and Commit Files

```bash
git add index.html content-dashboard/ content-system/
git commit -m "Add content dashboard for GitHub Pages"
git push origin main
```

### 2. Enable GitHub Pages

1. Go to your repository on GitHub: https://github.com/likeaglovem/CCTest
2. Click **Settings** (top menu)
3. Click **Pages** (left sidebar)
4. Under "Source", select **main** branch
5. Click **Save**

### 3. Wait for Deployment

GitHub will take 1-2 minutes to deploy your site. You'll see a message like:
```
Your site is live at https://likeaglovem.github.io/CCTest/
```

### 4. Access Your Dashboard

Once deployed, visit:
```
https://likeaglovem.github.io/CCTest/
```

## Important Notes

✅ **CORS Issue Solved** - The dashboard will now work without local server
✅ **Always Accessible** - Access from any device with internet
✅ **Auto-Updates** - Every time you push changes, GitHub Pages updates automatically

## Making Updates

Whenever you want to update the dashboard:

1. Edit `index.html` locally
2. Commit and push:
   ```bash
   git add index.html
   git commit -m "Update dashboard"
   git push origin main
   ```
3. Wait 1-2 minutes for GitHub to redeploy

## Google Sheet Requirements

Remember, your Google Sheet must still be:
- **Publicly shared** ("Anyone with the link can view")
- The correct **Sheet ID** in the HTML

Current Sheet ID: `1gyW5t2U5wu0Rd1ujDkgiau4ZJXkZhd15mx2WShchOok`

## Troubleshooting

### Dashboard shows old version
- GitHub Pages caches content. Wait 2-3 minutes or hard-refresh (Ctrl+F5)

### Still getting errors
- Check browser console (F12) for specific error messages
- Verify Google Sheet is publicly accessible
- Ensure Sheet ID is correct in index.html
