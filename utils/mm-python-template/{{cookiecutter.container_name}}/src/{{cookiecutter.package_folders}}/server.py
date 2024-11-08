from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse 
from pydantic import BaseModel, Field 
from pathlib import Path 
import uvicorn
import mimetypes

from {{cookiecutter.plugin_package}}.{{cookiecutter.package_name}} import (
    {{cookiecutter.package_name}},
)

# Initialize the FastAPI app
app = FastAPI()
