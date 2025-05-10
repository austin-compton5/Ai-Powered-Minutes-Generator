import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DOWNLOADS_DIR = BASE_DIR / "downloads"

def download_audio(youtube_url: str, output_dir: Path = DOWNLOADS_DIR) -> Path:
    output_dir.mkdir(exist_ok=True)
    
    # Define output path template
    output_template = str(output_dir / "%(title)s.%(ext)s")
    
    # Build and run yt-dlp command
    result = subprocess.run([
        "yt-dlp",
        "-x",  # extract audio
        "--audio-format", "mp3",
        "-o", output_template,
        youtube_url
    ], capture_output=True, text=True)
    
    if result.returncode != 0:
        raise RuntimeError(f"yt-dlp failed: {result.stderr}")
    
    # Optional: parse filename from output or glob the directory
    files = list(output_dir.glob("*.mp3"))
    if not files:
        raise FileNotFoundError("Audio download failed.")
    
    return files[0]  # Return path to downloaded audio
