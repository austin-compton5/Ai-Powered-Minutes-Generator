import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DOWNLOADS_DIR = BASE_DIR / "downloads"
DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)

def _get_video_id(url: str) -> str:
    res = subprocess.run(
        ["yt-dlp", "--no-playlist", "-O", "%(id)s", url],
        capture_output=True, text=True, check=True
    )
    vid = res.stdout.strip()
    if not vid:
        raise RuntimeError("yt-dlp: could not extract video id")
    return vid

def download_audio(youtube_url: str, output_dir: Path = DOWNLOADS_DIR) -> Path:
    """Return cached MP3 if present; otherwise download once and cache it."""
    video_id = _get_video_id(youtube_url)
    mp3_path = output_dir / f"{video_id}.mp3"

    # Fast path: already cached
    if mp3_path.exists() and mp3_path.stat().st_size > 0:
        return mp3_path

    # First time: download and transcode to mp3 (keeps rest of pipeline unchanged)
    cmd = [
        "yt-dlp", "--no-playlist",
        "-x", "--audio-format", "mp3",
        "-N", "4",                                # concurrent fragments
        "-o", str(output_dir / "%(id)s.%(ext)s"), # => downloads/<id>.mp3
        youtube_url,
    ]
    subprocess.run(cmd, check=True, text=True)

    if not mp3_path.exists() or mp3_path.stat().st_size == 0:
        raise FileNotFoundError(f"Expected file not found after download: {mp3_path}")

    return mp3_path
