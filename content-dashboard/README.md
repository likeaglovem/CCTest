# Content Dashboard Setup Guide

## The Problem
Opening the HTML file directly (`file://` protocol) causes CORS errors because Google Sheets doesn't allow requests from local files.

## The Solution
Run a local web server to serve the HTML file over HTTP.

---

## How to Start the Dashboard

### Windows:
1. Double-click `START_SERVER.bat`
2. A command window will open showing the server is running
3. Open your browser and go to: **http://localhost:8000/content-dashboard.html**
4. Leave the command window open while using the dashboard
5. Press `Ctrl+C` in the command window to stop the server when done

### Mac/Linux:
1. Open Terminal
2. Navigate to this folder
3. Run: `./START_SERVER.sh`
4. Open your browser and go to: **http://localhost:8000/content-dashboard.html**
5. Press `Ctrl+C` in Terminal to stop the server when done

### Alternative (Any OS):
1. Open Terminal/Command Prompt
2. Navigate to this folder:
   ```
   cd path/to/content-dashboard
   ```
3. Run:
   ```
   python -m http.server 8000
   ```
   (or `python3 -m http.server 8000` on Mac/Linux)
4. Open browser to: **http://localhost:8000/content-dashboard.html**

---

## Troubleshooting

### "Python is not recognized"
- Install Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

### Still getting CORS errors?
1. Make sure your Google Sheet is publicly shared:
   - Open the Google Sheet
   - Click "Share" (top right)
   - Click "Change to anyone with the link"
   - Set permission to "Viewer"
   - Click "Done"

2. Verify the Sheet ID in `content-dashboard.html` matches your sheet URL

### Port 8000 already in use?
Change `8000` to another number like `8080` or `3000` in the command.

---

## Google Sheet Requirements

Your Google Sheet must be:
1. **Publicly accessible** ("Anyone with the link can view")
2. The correct **Sheet ID** must be in the HTML file
3. Data should be on the **first sheet/tab**

The Sheet ID is found in your Google Sheets URL:
```
https://docs.google.com/spreadsheets/d/SHEET_ID_HERE/edit
```

Current Sheet ID in dashboard: `1gyW5t2U5wu0Rd1ujDkgiau4ZJXkZhd15mx2WShchOok`
