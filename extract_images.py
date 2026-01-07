#!/usr/bin/env python3
"""
Extract base64 images from HTML and create a static website structure.
"""

import re
import os
import base64
from pathlib import Path
from bs4 import BeautifulSoup
import hashlib

def extract_base64_images(html_file, output_dir='portfolio'):
    """
    Extract base64 images from HTML and save them as separate files.
    Update HTML to reference the extracted images.
    """
    # Create output directory structure
    output_path = Path(output_dir)
    images_dir = output_path / 'images'
    images_dir.mkdir(parents=True, exist_ok=True)
    
    # Read HTML file
    print(f"Reading HTML file: {html_file}")
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all img tags with base64 data
    img_tags = soup.find_all('img', src=re.compile(r'^data:image'))
    
    print(f"Found {len(img_tags)} base64 images to extract")
    
    # Extract and save images
    image_counter = 0
    for img in img_tags:
        src = img.get('src', '')
        
        # Extract base64 data
        match = re.match(r'data:image/(\w+);base64,(.+)', src)
        if match:
            image_format = match.group(1)
            base64_data = match.group(2)
            
            # Decode base64
            try:
                image_data = base64.b64decode(base64_data)
                
                # Generate filename (use hash for uniqueness, or counter)
                image_hash = hashlib.md5(base64_data[:100].encode()).hexdigest()[:8]
                filename = f"image_{image_counter:03d}_{image_hash}.{image_format}"
                filepath = images_dir / filename
                
                # Save image
                with open(filepath, 'wb') as img_file:
                    img_file.write(image_data)
                
                # Update img src to relative path
                img['src'] = f'images/{filename}'
                
                print(f"  Extracted: {filename} ({len(image_data)} bytes)")
                image_counter += 1
                
            except Exception as e:
                print(f"  Error extracting image: {e}")
                continue
    
    # Save updated HTML
    output_html = output_path / 'index.html'
    
    # Add basic HTML structure if needed
    if not soup.find('html'):
        # Wrap content in proper HTML structure
        html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flight Sentry - Portfolio Demo</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .notebook-content {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        img {{
            max-width: 100%;
            height: auto;
        }}
    </style>
</head>
<body>
    <div class="notebook-content">
{soup.prettify()}
    </div>
</body>
</html>"""
        with open(output_html, 'w', encoding='utf-8') as f:
            f.write(html_doc)
    else:
        with open(output_html, 'w', encoding='utf-8') as f:
            f.write(str(soup))
    
    print(f"\n✓ Successfully extracted {image_counter} images")
    print(f"✓ Updated HTML saved to: {output_html}")
    print(f"✓ Images saved to: {images_dir}")
    print(f"\nYour static website is ready in: {output_path}/")
    print(f"  - index.html (main HTML file)")
    print(f"  - images/ (extracted images)")
    
    return output_path

if __name__ == '__main__':
    import sys
    
    html_file = 'FP_Phase_3_Project_Notebook_Team_4_4.html'
    if len(sys.argv) > 1:
        html_file = sys.argv[1]
    
    if not os.path.exists(html_file):
        print(f"Error: File not found: {html_file}")
        sys.exit(1)
    
    extract_base64_images(html_file)

