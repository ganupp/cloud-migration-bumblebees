import streamlit as st
from git import Repo
import os
import re

# Define a permanent download path

project_path = os.getcwd()
DOWNLOAD_DIR = project_path + "/cloud-migration-bumblebees/base-appl"
print(DOWNLOAD_DIR)

# Ensure the directory exists
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Function to sanitize GitHub URLs and clone the repository
def sanitize_and_clone(repo_url, download_path):
    # Remove any additional parts like /tree/main or /blob/main
    sanitized_url = re.sub(r"/(tree|blob)/.*", "", repo_url)
    
    if not sanitized_url.endswith(".git"):
        sanitized_url += ".git"  # Ensure the URL ends with .git

    try:
        Repo.clone_from(sanitized_url, download_path)
        return f"Downloaded repository from {sanitized_url}"
    except Exception as e:
        return f"Failed to download {sanitized_url}: {e}"

# Streamlit app
def main():
    st.header("GEN1 and GEN2 inputs")
    
    war_file = st.file_uploader("Upload a WAR file", type="war")
    if war_file is not None:
        # Define the path to save the uploaded file
        save_path = f"./cloud-migration-bumblebees/war-files/{war_file.name}"
        
        # Save the file
        with open(save_path, "wb") as f:
            f.write(war_file.getbuffer())
        st.write("WAR file saved successfully!")
        st.write("File path:", save_path)
    
    # Step 2: GitHub repository URLs input
    repo_urls = st.text_area("Enter GitHub repository URLs (one per line)", "")
    
    # Step 3: Process and download repositories
    if st.button("Download Repositories"):
        repo_urls_list = repo_urls.strip().splitlines()
        
        for repo_url in repo_urls_list:
            # Use the base name of the repo URL for the folder name
            repo_name = os.path.basename(repo_url)
            download_path = os.path.join(DOWNLOAD_DIR, repo_name)
            
            status = sanitize_and_clone(repo_url, download_path)
            st.write(status)
                
        st.success(f"Repositories download completed! Check the '{DOWNLOAD_DIR}' directory.")
    
if __name__ == "__main__":
    main()