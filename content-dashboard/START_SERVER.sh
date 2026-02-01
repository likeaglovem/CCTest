#!/bin/bash
echo "Starting local web server for Content Dashboard..."
echo ""
echo "The dashboard will be available at:"
echo "http://localhost:8000/content-dashboard.html"
echo ""
echo "Press Ctrl+C to stop the server when you're done."
echo ""
python3 -m http.server 8000
