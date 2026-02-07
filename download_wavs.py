import pandas as pd
import subprocess
from pathlib import Path
import sys
OUTPUT_DIR = "downloaded_wav"

def download_as_wav(url, output_dir):
    cmd = [
            "yt-dlp",
            "-x",  
            "--audio-format", "wav", 
            "--output", f"{output_dir}/%(uploader)s/%(title)s.%(ext)s",  
            url
        ]
    result = subprocess.run(cmd, capture_output=True, text=True)

def main():

    Path(OUTPUT_DIR).mkdir(exist_ok=True)
    df=pd.read_excel('Book1.xlsx')
    urls=df.url
    for url in urls:
        download_as_wav(url,OUTPUT_DIR)

if __name__=='__main__':
    main()