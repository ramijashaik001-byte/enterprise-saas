import os
import zipfile

def main():
    # Base directories
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    parent_dir = os.path.dirname(project_dir)
    zip_path = os.path.join(parent_dir, "enterprise-saas.zip")
    
    print(f"Project directory: {project_dir}")
    print(f"Target zip path: {zip_path}")
    
    # Exclude directories
    exclude_dirs = {".venv", "__pycache__", ".pytest_cache"}
    
    count = 0
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(project_dir):
            # Prune directory search to exclude virtual environment and git data
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in files:
                # Skip temporary local log files or database files if any, to keep zip pure
                if file in {"test_run.log", "saas_hrms.db"}:
                    continue
                filepath = os.path.join(root, file)
                # Compute path relative to parent_dir so it extracts inside a directory named enterprise-saas
                arcname = os.path.relpath(filepath, parent_dir)
                zipf.write(filepath, arcname)
                count += 1
                
    print(f"Success! Zipped {count} files into {zip_path}")

if __name__ == "__main__":
    main()
