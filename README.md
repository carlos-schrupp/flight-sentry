# Flight Sentry - Portfolio Website

Static website version of the Flight Sentry project notebook for team collaboration.

## Repository Structure

```
.
├── index.html          # Main HTML file (portfolio website)
├── images/            # Extracted images (34 files)
└── README.md          # This file
```

## Quick Start

### Viewing Locally

Simply open `index.html` in any web browser:

```bash
# On Linux/Mac
open index.html
# or
xdg-open index.html

# On Windows
start index.html
```

## Team Collaboration

### Setting Up GitHub Repository

1. **Create a new repository on GitHub**
   - Go to [github.com](https://github.com) and create a new repository
   - Name it something like `flight-sentry-portfolio` or `team-4-4-portfolio`
   - Make it **private** (if you want) or **public**
   - Don't initialize with README (we already have one)

2. **Push your code to GitHub**
   ```bash
   cd /home/user/delay
   git add .
   git commit -m "Initial commit: Portfolio website"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

3. **Add team members as collaborators**
   - Go to repository Settings → Collaborators
   - Add team members by their GitHub usernames
   - They'll receive an email invitation

### Working with the Team

**For team members:**
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

# Make changes to index.html
# Then commit and push
git add index.html
git commit -m "Updated section X"
git push
```

**Best practices:**
- Always pull latest changes before editing: `git pull`
- Make small, focused commits with clear messages
- Communicate with team about major changes
- Consider using branches for larger features

## Deploying to GitHub Pages (Free Hosting)

1. **Enable GitHub Pages**
   - Go to repository Settings → Pages
   - Source: Deploy from a branch
   - Branch: `main` (or `master`)
   - Folder: `/` (root)
   - Click Save

2. **Your site will be live at:**
   ```
   https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/
   ```
   (Note: It may take a few minutes to go live)

3. **Custom domain (optional):**
   - Add a `CNAME` file in the portfolio folder with your domain
   - Configure DNS settings with your domain provider

## Alternative Hosting Options

### Netlify (Recommended - Easiest)
1. Go to [netlify.com](https://netlify.com)
2. Sign up/login with GitHub
3. Click "New site from Git"
4. Select your repository
5. Build settings:
   - Base directory: `/` (root)
   - Publish directory: `/` (root)
   - Build command: (leave empty)
6. Deploy!

### Vercel
1. Install Vercel CLI: `npm i -g vercel`
2. Navigate to repository root: `cd /path/to/repo`
3. Run: `vercel`
4. Follow the prompts

## File Information

- **Total images**: ~5.6 MB (34 files)
- **HTML file**: Large file (~21,000+ lines)
- **Dependencies**: MathJax (loaded from CDN for LaTeX rendering)

## Features

- ✅ Responsive table styling
- ✅ LaTeX formula rendering (MathJax)
- ✅ Clean, professional layout
- ✅ All images extracted and optimized
- ✅ Mobile-friendly design

## Notes

- All images are referenced with relative paths (`images/image_XXX.png`)
- MathJax loads from CDN (requires internet connection)
- The HTML is self-contained - no build process needed
- Team members can edit directly in GitHub web interface or locally

## Troubleshooting

**MathJax not rendering?**
- Check browser console for errors
- Ensure internet connection (MathJax loads from CDN)
- Try refreshing the page

**Images not showing?**
- Ensure `images/` folder is in the same directory as `index.html`
- Check image paths are relative (not absolute)

**Git conflicts?**
- Use `git pull --rebase` to avoid merge commits
- Communicate with team about concurrent edits
- Consider using feature branches for larger changes
