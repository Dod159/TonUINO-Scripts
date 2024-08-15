import os
import subprocess

# Traverse through each subdirectory
for subdir, _, files in os.walk('.'):
    # Filter out mp3 files and sort them
    mp3_files = sorted([f for f in files if f.endswith('.mp3')])
    
    if mp3_files:
        # Change to the subdirectory
        os.chdir(subdir)
        
        # Create a temporary file list for ffmpeg
        with open('mylist.txt', 'w') as f:
            for mp3 in mp3_files:
                f.write(f"file '{os.path.join(os.getcwd(), mp3)}'\n")
        
        # Construct and execute the ffmpeg command
        command = ['ffmpeg', '-safe', '0', '-f', 'concat', '-i', 'mylist.txt', '-c', 'copy', 'alles-zusammen.mp3']
        
        try:
            # Execute the command
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
        
        # Clean up the temporary file
        os.remove('mylist.txt')
        
        # Return to the parent directory
        os.chdir('..')
