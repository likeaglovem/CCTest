# Dashboard Setup Guide

## Step 1: Download the Dashboard

Download the `content-dashboard.html` file to your computer.

## Step 2: Make Your Google Sheet Public

1. Open your Content Database Google Sheet
2. Click "Share" button (top right)
3. Click "Change to anyone with the link"
4. Make sure it's set to "Viewer" (not Editor)
5. Click "Copy link"

## Step 3: Get Your Sheet ID

From the URL you just copied, extract the Sheet ID:

```
https://docs.google.com/spreadsheets/d/1a2b3c4d5e6f7g8h9i0j/edit
                                       ^^^^^^^^^^^^^^^^^
                                       This is your Sheet ID
```

Copy the long string between `/d/` and `/edit`

## Step 4: Configure the Dashboard

1. Open `content-dashboard.html` in a text editor (TextEdit, VS Code, Sublime, etc.)
2. Find this line near the top of the `<script>` section:

```javascript
const SHEET_ID = 'YOUR_GOOGLE_SHEET_ID_HERE';
```

3. Replace `YOUR_GOOGLE_SHEET_ID_HERE` with your actual Sheet ID:

```javascript
const SHEET_ID = '1a2b3c4d5e6f7g8h9i0j';
```

4. Save the file

## Step 5: Open the Dashboard

**Double-click `content-dashboard.html`** 

It will open in your default browser and automatically load your videos from the Google Sheet!

## Usage

### Search:
- Type anything in the search box to filter videos
- Searches across: filenames, subjects, tags, topics, transcripts

### Filter:
- Use the dropdowns to filter by Type, Location, or Weather
- Combine multiple filters

### View Details:
- Click any video card to see full details
- View transcript, all tags, notes
- Click "Open in Drive" to view the actual video

### Stats:
- Top section shows total videos, duration, and breakdown by type
- Updates automatically as you filter

## Sharing with Your Editor

### Option 1: Send them the file
1. Send `content-dashboard.html` to your editor
2. They double-click to open it
3. Works immediately - no setup needed on their end

### Option 2: Host it online (5 minutes)
**Using Netlify (easiest):**
1. Go to https://app.netlify.com/drop
2. Drag `content-dashboard.html` onto the page
3. Get a URL like: `matthew-content.netlify.app`
4. Share this URL with your editor

**Using GitHub Pages:**
1. Create a new GitHub repo
2. Upload `content-dashboard.html`
3. Go to Settings → Pages
4. Enable Pages
5. Get a URL like: `matthew.github.io/content-dashboard`

## Updating

The dashboard automatically refreshes data from your Google Sheet whenever you reload the page. 

**To see new videos:**
1. Process videos with your Python script
2. Refresh the dashboard page
3. New videos appear automatically!

## Customization

Want to change colors or layout? The dashboard is a single HTML file with all CSS and JavaScript included. Just edit and save!

### Quick Color Changes:

Find this section in the `<style>` tag:

```css
:root {
    --bg-primary: #0a0a0a;
    --accent-1: #00ff88;  /* Change this for different accent color */
    --accent-2: #0088ff;  /* And this */
}
```

Change the hex codes to your preferred colors!

## Troubleshooting

**"No videos found"**
- Check that your Sheet ID is correct
- Make sure the Sheet is publicly viewable
- Verify the Sheet has data in it

**Videos not loading**
- Check browser console for errors (F12 → Console tab)
- Make sure you're connected to the internet
- Verify the Sheet URL works when you paste it in a browser

**Looks broken**
- Make sure you saved the file after editing the Sheet ID
- Try opening in a different browser
- Clear your browser cache

## Features

✅ Real-time search across all fields
✅ Multiple filters (type, location, weather)
✅ Click to view full video details
✅ Direct links to Drive files
✅ Responsive design (works on phone/tablet)
✅ No login required
✅ Works offline after first load
✅ Automatically updates when you refresh

## Next Steps

Once you're happy with the dashboard:
1. Process your existing video library
2. Share dashboard with your editor
3. Use search/filters to find footage quickly
4. Build content faster! 🚀

---

**Questions?** The dashboard is just HTML/CSS/JavaScript - you can customize it however you want!
