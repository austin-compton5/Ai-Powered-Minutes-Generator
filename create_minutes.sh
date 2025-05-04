#!/bin/bash

read -p "Enter the commission video URL: " video_url

# Check if a URL was provided
if [ -z "$video_url" ]; then
  echo "No URL provided. Exiting."
  exit 1
fi

output_dir="downloads"
mkdir -p "$output_dir"

video_title=$(yt-dlp --get-title "$video_url")
safe_title=$(echo "$video_title" | tr ' ' '_' | tr -dc '[:alnum:]_-')

output_file="$output_dir/${safe_title}.mp3"

echo "Downloading audio..."
yt-dlp -x --audio-format mp3 -o "${output_dir}/${safe_title}.%(ext)s" "$video_url"

# Check if the download was successful
if [ $? -eq 0 ]; then
  echo "Download complete!"
  echo "Creating AI generated minutes"
  python3 src/app.py "$output_file"
else
  echo "Download failed."
fi

rm $output_file

exit 0
