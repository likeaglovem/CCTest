# Google Sheet Structure Update

## Updated Column Mapping

The dashboard has been updated to match your new Google Sheet structure with the following columns:

### Original Columns (0-18):
1. Original Filename
2. New Filename
3. Date Filmed
4. Duration
5. Orientation
6. Resolution
7. Type
8. Location
9. Weather
10. Main Subject
11. Visual Tags
12. Content Tags
13. Mood
14. Color Palette
15. Audio
16. Transcript
17. Key Quotes
18. Topics
19. Use Cases

### New Columns Added (19-28):
20. **Platform Suitability** - Which platforms this video works best for
21. **Time of Day** - Morning, afternoon, evening, night
22. **Season** - Spring, summer, fall, winter
23. **People Count** - Number of people in the video
24. **Energy Level** - High, medium, low energy
25. **Camera Movement** - Static, pan, tilt, zoom, handheld, etc.
26. **Audio Quality** - Quality of the audio track
27. **Drive Link** (moved from position 19 to 26)
28. **Notes** (moved from position 20 to 27)
29. **Analysis Date** (moved from position 21 to 28)

## What's Changed in the Dashboard

### Data Loading
✅ Updated column mapping to read all 29 columns
✅ New fields are now captured in the video objects

### Modal Display
✅ Added display of new fields in the Details section:
- Time of Day
- Season
- People Count
- Energy Level
- Camera Movement
- Audio Quality
- Platform Suitability

✅ All new fields only display if they have values (not "N/A")

## To Deploy

```bash
cd /Users/mmitten/ClaudeCode
git add index.html SHEET_STRUCTURE_UPDATE.md
git commit -m "Update dashboard to match new Google Sheet structure with additional columns"
git push origin main
```

Wait 1-2 minutes, then refresh: https://likeaglovem.github.io/CCTest/

## Notes

- All new fields are optional and will only show if they contain data
- The dashboard will filter out "N/A" values automatically
- Search functionality will continue to work across all fields
- Existing filters (Type, Location, Weather) remain functional
