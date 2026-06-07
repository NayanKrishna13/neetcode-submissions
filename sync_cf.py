import os
import requests

# 1. CHANGE THIS TO YOUR EXACT CODEFORCES HANDLE
CF_HANDLE = "The_dark_lord_1308"  

# Destination folder name inside your repo
SUBMISSIONS_DIR = "Codeforces_Submissions"

# Map Codeforces language strings to standard file extensions
LANG_MAP = {
    "cpp": ".cpp",
    "gnu c++": ".cpp",
    "java": ".java",
    "python": ".py",
    "c": ".c",
    "rust": ".rs",
    "go": ".go",
    "c#": ".cs"
}

def get_extension(lang_string):
    for key, val in LANG_MAP.items():
        if key in lang_string.lower():
            return val
    return ".txt"

def fetch_submissions():
    # Fetches your 50 most recent submissions from the Codeforces API
    url = f"https://codeforces.com{CF_HANDLE}&from=1&count=150"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"Codeforces API error: Status code {response.status_code}")
            return []
        data = response.json()
        if data.get("status") == "OK":
            return data["result"]
    except Exception as e:
        print(f"Network error connecting to Codeforces: {e}")
    return []

def sync():
    os.makedirs(SUBMISSIONS_DIR, exist_ok=True)
    submissions = fetch_submissions()
    
    if not submissions:
        print("No submissions retrieved.")
        return

    new_files_count = 0
    
    for sub in submissions:
        # Only pull solutions that passed all test cases
        if sub.get("verdict") == "OK":
            problem = sub["problem"]
            contest_id = problem.get("contestId", "Unknown")
            index = problem.get("index", "A")
            prob_name = problem.get("name", "Problem").replace(" ", "_")
            lang = sub.get("programmingLanguage", "Text")
            ext = get_extension(lang)
            submission_id = sub["id"]
            
            # Formats name like: Codeforces_Submissions/123A_Watermelon.cpp
            filename = f"{SUBMISSIONS_DIR}/{contest_id}{index}_{prob_name}{ext}"
            
            # Only create the file if it doesn't already exist in your repo
            if not os.path.exists(filename):
                with open(filename, "w", encoding="utf-8") as f:
                    # Header comments
                    if ext in [".cpp", ".java", ".c", ".rs", ".go", ".cs"]:
                        f.write(f"// Codeforces Problem: {contest_id}{index} - {prob_name}\n")
                        f.write(f"// Language: {lang}\n")
                        f.write(f"// Submission ID: {submission_id}\n\n")
                    elif ext == ".py":
                        f.write(f"# Codeforces Problem: {contest_id}{index} - {prob_name}\n")
                        f.write(f"# Language: {lang}\n")
                        f.write(f"# Submission ID: {submission_id}\n\n")
                    
                    # Note on raw code fetching: The public Codeforces API does not share 
                    # your raw source code string inside the JSON tracking payload.
                    # This saves the tracking entry so your repo maps your progress.
                    f.write("// Solution log template committed by automated action.\n")
                    f.write("// To keep things clean, paste your working code below if archiving manually!\n")
                
                print(f"Logged new solution: {filename}")
                new_files_count += 1
                
    print(f"Sync complete. Added {new_files_count} new submission logs.")

if __name__ == "__main__":
    sync()
