import os
import subprocess

def call_dotnet_app(txt_file):
    # Path to the .NET 6 app (DLL)
    dotnet_app_path = "/home/chaithanya/Documents/DotnetFromPython/linux-x64/CallDotnetFromPython.dll"  # Update this path in linux vm
    
    # Call the .NET app with the txt file as an argument
    result = subprocess.run(['dotnet', dotnet_app_path, txt_file], 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE, 
                            text=True)
    
    # Print the result from the .NET app
    if result.returncode == 0:
        print(f"Successfully processed: {txt_file}")
        print(result.stdout)
    else:
        print(f"Error processing: {txt_file}")
        print(result.stderr)

def process_txt_files(folder_path):
    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                txt_file_path = os.path.join(root, file)
                print(f"Found text file: {txt_file_path}")
                call_dotnet_app(txt_file_path)

if __name__ == "__main__":
    folder_to_search = "/home/chaithanya/Documents/DotnetFromPython/Python"  # Update this path in linux vm
    process_txt_files(folder_to_search)
