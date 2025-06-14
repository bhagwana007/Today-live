import os
import subprocess

# Environment से RTMP URL और video path लें
rtmp_url = os.getenv("RTMP_URL")
video_path = os.getenv("VIDEO_PATH", "video.mp4")

if not rtmp_url:
    print("🔴 RTMP_URL environment variable missing!")
    exit(1)

ffmpeg_cmd = [
    "ffmpeg",
    "-re",
    "-stream_loop", "-1",
    "-i", video_path,
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-maxrate", "3000k",
    "-bufsize", "6000k",
    "-pix_fmt", "yuv420p",
    "-g", "50",
    "-c:a", "aac",
    "-b:a", "160k",
    "-ar", "44100",
    "-f", "flv",
    rtmp_url
]

print("🔄 Starting FFmpeg with command:", " ".join(ffmpeg_cmd))
subprocess.call(ffmpeg_cmd)
