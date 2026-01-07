#!/usr/bin/env python3
"""
Extract base64 images from HTML using only standard library.
No external dependencies required.
"""

import re
import os
import base64
from pathlib import Path
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
    
    # Pattern to find base64 images
    # Matches: data:image/format;base64,base64data...
    pattern = r'data:image/(\w+);base64,([A-Za-z0-9+/=]+)'
    
    image_counter = 0
    replacements = []
    
    def replace_image(match):
        nonlocal image_counter
        image_format = match.group(1)
        base64_data = match.group(2)
        
        try:
            # Decode base64
            image_data = base64.b64decode(base64_data)
            
            # Generate filename
            image_hash = hashlib.md5(base64_data[:100].encode()).hexdigest()[:8]
            filename = f"image_{image_counter:03d}_{image_hash}.{image_format}"
            filepath = images_dir / filename
            
            # Save image
            with open(filepath, 'wb') as img_file:
                img_file.write(image_data)
            
            # Store replacement
            old_src = match.group(0)
            new_src = f'images/{filename}'
            replacements.append((old_src, new_src))
            
            print(f"  Extracted: {filename} ({len(image_data)} bytes)")
            image_counter += 1
            
            return new_src
            
        except Exception as e:
            print(f"  Error extracting image: {e}")
            return match.group(0)  # Return original if error
    
    # Find and replace all base64 images
    print("Extracting base64 images...")
    updated_html = re.sub(pattern, replace_image, html_content)
    
    # Ensure proper HTML structure
    if '<!DOCTYPE html>' not in updated_html and '<html' not in updated_html:
        # Wrap in basic HTML structure
        html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flight Sentry - Portfolio Demo</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .notebook-content {
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 10px 0;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }
        table th, table td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        table th {
            background-color: #f2f2f2;
        }
        pre {
            background: #f4f4f4;
            padding: 15px;
            border-radius: 4px;
            overflow-x: auto;
        }
        code {
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
        }
    </style>
</head>
<body>
    <div class="notebook-content">
{content}
    </div>
</body>
</html>"""
        updated_html = html_template.format(content=updated_html)
    
    # Save updated HTML
    output_html = output_path / 'index.html'
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(updated_html)
    
    print(f"\n✓ Successfully extracted {image_counter} images")
    print(f"✓ Updated HTML saved to: {output_html}")
    print(f"✓ Images saved to: {images_dir}")
    print(f"\nYour static website is ready in: {output_path}/")
    print(f"  - index.html (main HTML file)")
    print(f"  - images/ (extracted images)")
    print(f"\nTo view: Open {output_html} in a web browser")
    
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




