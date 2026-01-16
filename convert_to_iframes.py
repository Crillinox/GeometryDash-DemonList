import os
import re
from pathlib import Path

def extract_video_id(url):
    """Extract YouTube video ID from URL"""
    patterns = [
        r'(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})',
        r'youtube\.com/embed/([a-zA-Z0-9_-]{11})',
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def convert_youtube_link_to_iframe(html_content):
    """Convert YouTube anchor tags to iframes"""
    # Pattern to find YouTube links
    pattern = r'<a href="(https://www\.youtube\.com/watch\?v=[^"]+)"[^>]*>\s*<img src="([^"]+)"[^>]*>\s*</a>'
    
    def replace_with_iframe(match):
        url = match.group(1)
        img_src = match.group(2)
        video_id = extract_video_id(url)
        
        if video_id:
            return f'''<div class="video-container">
        <iframe width="600" height="338" src="https://www.youtube.com/embed/{video_id}" 
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen></iframe>
      </div>'''
        return match.group(0)  # Return original if can't extract video ID
    
    return re.sub(pattern, replace_with_iframe, html_content, flags=re.DOTALL)

# Get all HTML files except index, leaderboard, and documentation
html_files = [f for f in os.listdir('.') if f.endswith('.html') 
              and f not in ['index.html', 'leaderboard.html', 'documentation.html']]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Convert YouTube links to iframes
    updated_content = convert_youtube_link_to_iframe(content)
    
    # Write back
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"Updated {filename}")

print(f"\nTotal files updated: {len(html_files)}")
