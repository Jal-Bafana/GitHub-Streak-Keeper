import subprocess
import datetime
import random
import os

num_commits = 1 

def run_git_command(command):
    """Run a git command and return the result"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error running command: {command}")
            print(f"Error: {result.stderr}")
            return False
        else:
            print(f"Success: {command}")
            if result.stdout:
                print(f"Output: {result.stdout.strip()}")
        return True
    except Exception as e:
        print(f"Exception running command {command}: {e}")
        return False

def modify_readme():
    """Make a small change to README.md to create a commit"""
    readme_file = "README.md"
    
    if not os.path.exists(readme_file):
        with open(readme_file, 'w') as f:
            f.write("# My Streak Repository\n\n")
            f.write("This repository helps maintain my GitHub contribution streak.\n\n")
    
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    activities = [
        "Daily commit",
        "Keeping the streak alive",
        "Maintenance update",
        "Auto contribution",
        "Streak preservation",
        "Daily touch"
    ]
    
    activity = random.choice(activities)
    
    # Append to README
    with open(readme_file, 'a') as f:
        f.write(f"- {activity} on {timestamp}\n")
    
    print(f"Modified README.md: Added '{activity}' at {timestamp}")

def make_commit(commit_number):
    """Make a single commit"""
    print(f"\n--- Making Commit #{commit_number} ---")
    
    # Step 1: Modify README
    modify_readme()
    
    # Step 2: Add changes
    if not run_git_command("git add README.md"):
        return False
    
    # Step 3: Commit
    commit_message = f"Daily update {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}"
    if not run_git_command(f'git commit -m "{commit_message}"'):
        return False
    
    # Step 4: Push
    if not run_git_command("git push origin main"):
        return False
    
    print(f"✅ Commit #{commit_number} completed successfully!")
    return True

def main():
    """Main function to run the streak keeper"""
    print("🚀 GitHub Streak Keeper Started")
    print(f"📊 Number of commits to make: {num_commits}")
    print("=" * 50)
    
    # Check if we're in a git repository
    if not os.path.exists('.git'):
        print("❌ Error: Not in a git repository!")
        print("Make sure you're running this script from your git repository folder.")
        return
    
    successful_commits = 0
    
    for i in range(1, num_commits + 1):
        if make_commit(i):
            successful_commits += 1
        else:
            print(f"❌ Failed to make commit #{i}")
            break
        
        # Small delay between commits if making multiple
        if i < num_commits:
            print("⏳ Waiting 2 seconds before next commit...")
            import time
            time.sleep(2)
    
    print("=" * 50)
    print(f"🎉 Completed! Made {successful_commits}/{num_commits} commits")
    print(f"🔥 Your GitHub streak is safe for today!")

if __name__ == "__main__":
    main()