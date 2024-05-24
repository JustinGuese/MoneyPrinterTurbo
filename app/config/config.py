import os
import shutil
import socket

import toml
from loguru import logger

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
config_file = f"{root_dir}/config.toml"

# i dont want to use config files, use env instead
_cfg = {
    "app": {
        "video_source": "pexels",
        "pexels_api_keys": os.environ.get("PEXELS_API_KEYS", "").split(","),
        "llm_provider": "openai",
        "openai_api_key": os.environ["OPENAI_API_KEY"],
        "openai_model_name": os.environ.get("OPENAI_MODEL_NAME", "gpt-4-turbo"),
        "openai_base_url": os.environ.get(
            "OPENAI_BASE_URL", "https://api.openai.com/v1"
        ),
        "subtitle_provider": "edge",
        "endpoint": os.environ.get("ENDPOINT", "http://localhost:8000"),
        "material_directory": "/storage",
    }
}


app = _cfg.get("app", {})
whisper = _cfg.get("whisper", {})
proxy = _cfg.get("proxy", {})
azure = _cfg.get("azure", {})
ui = _cfg.get("ui", {})

hostname = socket.gethostname()

log_level = _cfg.get("log_level", "DEBUG")
listen_host = _cfg.get("listen_host", "0.0.0.0")
listen_port = _cfg.get("listen_port", 8080)
project_name = _cfg.get("project_name", "MoneyPrinterTurbo")
project_description = _cfg.get(
    "project_description",
    "<a href='https://github.com/harry0703/MoneyPrinterTurbo'>https://github.com/harry0703/MoneyPrinterTurbo</a>",
)
project_version = _cfg.get("project_version", "1.1.9")
reload_debug = False

imagemagick_path = app.get("imagemagick_path", "")
if imagemagick_path and os.path.isfile(imagemagick_path):
    os.environ["IMAGEMAGICK_BINARY"] = imagemagick_path

ffmpeg_path = app.get("ffmpeg_path", "")
if ffmpeg_path and os.path.isfile(ffmpeg_path):
    os.environ["IMAGEIO_FFMPEG_EXE"] = ffmpeg_path

logger.info(f"{project_name} v{project_version}")
