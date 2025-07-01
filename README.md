# GitHub Streak Helper

> ⚠️⚠️⚠️ **Important Disclaimer**: This tool is designed for educational purposes and genuine streak maintenance when you haven't had time to code, not for artificial contribution inflation. Use responsibly and remember that real coding and learning should always be your priority!

A simple Python script to maintain your GitHub contribution streak by automatically creating commits when you haven't done any real work for the day.

## What it does

- Makes random changes to README.md with timestamps
- Creates commits with meaningful messages
- Pushes to your private repository
- Keeps your GitHub contribution graph green! 🟢

## Quick Start

### Prerequisites
- Python 3.x installed
- Git configured with your GitHub credentials
- A private GitHub repository

### Setup

1. **Clone or create your private repository:**
   ```bash
   # Option 1: Clone existing repo
   git clone https://github.com/yourusername/your-private-repo.git
   cd your-private-repo
   
   # Option 2: Create new local repo
   mkdir my-streak-repo
   cd my-streak-repo
   git init
   ```

2. **Connect to GitHub (for new repos):**
   ```bash
   # Add your GitHub repo as remote
   git remote add origin https://github.com/yourusername/your-private-repo.git
   
   # Or using SSH
   git remote add origin git@github.com:yourusername/your-private-repo.git
   ```

3. **Download the script:**
   - Copy `streak_keeper.py` into your repository folder
   - Make sure it's in the same directory as your `.git` folder

4. **Initial setup (for new repos):**
   ```bash
   git add .
   git commit -m "Initial commit with streak keeper"
   git push -u origin main
   ```

## Usage

### Basic Usage
```bash
# Navigate to your repository
cd your-repo-folder

# Run the streak keeper
python streak_keeper.py
```

### Multiple Commits
Want to make multiple commits in one run? Edit the script:

```python
# In streak_keeper.py, change this line:
num_commits = 3  # This will make 3 commits
```

Then run:
```bash
python streak_keeper.py
```

## Configuration

### Customizing Number of Commits
Open `streak_keeper.py` and modify:
```python
num_commits = 1  # Change this number
```

### Customizing Commit Messages
The script generates random activity messages. You can modify the `activities` list in the script:
```python
activities = [
    "Daily commit",
    "Keeping the streak alive", 
    "Your custom message here"
]
```

## File Structure
```
your-repo/
├── README.md
├── streak_keeper.py
├── .git/
└── (other files...)
```

## 🛠️ Troubleshooting

### Common Issues

**"Not in a git repository" error:**
```bash
# Make sure you're in the right folder
pwd
ls -la  # Should see .git folder

# If no .git folder, initialize:
git init
git remote add origin https://github.com/yourusername/repo.git
```

**Authentication errors:**
```bash
# For HTTPS (will prompt for username/token)
git remote set-url origin https://github.com/yourusername/repo.git

# For SSH (requires SSH key setup)
git remote set-url origin git@github.com:yourusername/repo.git

# Test connection
git remote -v
```

**Python not found:**
```bash
# Try different Python commands
python3 streak_keeper.py
py streak_keeper.py
```

**Permission denied:**
```bash
# Make script executable (Linux/Mac)
chmod +x streak_keeper.py
```

##  Example Output

```
🚀 GitHub Streak Keeper Started
📊 Number of commits to make: 1
==================================================

--- Making Commit #1 ---
Modified README.md: Added 'Daily commit' at 2025-07-01 15:30:25
Success: git add README.md
Success: git commit -m "Daily update 2025-07-01 15:30"
Success: git push origin main
✅ Commit #1 completed successfully!

==================================================
🎉 Completed! Made 1/1 commits
🔥 Your GitHub streak is safe for today!
```

## Best Practices

1. **Use a private repository** - Keep your streak maintenance private
2. **Run manually daily** - Don't automate it completely; maintain the discipline of daily engagement
3. **Use responsibly** - This is for genuine streak maintenance, not artificial inflation
4. **Keep backups** - Your actual code should be in separate repositories

## Important Notes

- **GitHub streaks are consecutive days only** - You can't backfill missed days
- **Run before midnight** - Make sure to run the script before your day ends
- **Private repos recommended** - Keep your streak maintenance discrete
- **Manual execution** - Run it yourself to maintain daily coding discipline

## Contributing

This is a simple utility script. Feel free to:
- Fork and customize for your needs
- Add features like different file modifications
- Create pull requests for improvements

---

Made with 💙 by Jal Bafana
