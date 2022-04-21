import sys
import torch
import os

is_colab = False
is_drive = False

pyt_version_str=torch.__version__.split("+")[0].replace(".", "")
version_str="".join([
    f"py3{sys.version_info.minor}_cu",
    torch.version.cuda.replace(".",""),
    f"_pyt{pyt_version_str}"
])

root_path = f'.'

sys.path.append('./pytorch3d-lite')
import pathlib, shutil
from os.path import exists as path_exists
import wget
  
if not path_exists(f'{root_path}/MiDaS/midas_utils.py'):
  os.rename("MiDaS/utils.py", "MiDaS/midas_utils.py")

if not path_exists(f'{root_path}/glid-3-xl/jack_guided_diffusion'):
  os.rename('glid-3-xl/guided_diffusion', 'glid-3-xl/jack_guided_diffusion')
shutil.copyfile("mindseye/.streamlit/config.toml", ".streamlit/config.toml")
shutil.copyfile("mindseye/app.py", "app.py")
shutil.copyfile("mindseye/disco_streamlit_run.py", "disco_streamlit_run.py")
shutil.copyfile("mindseye/hypertron_streamlit_run.py","hypertron_streamlit_run.py")
shutil.copyfile("mindseye/latent_streamlit_run.py", "latent_streamlit_run.py")
shutil.copyfile("mindseye/streamlit_nested_expanders.py", "streamlit_nested_expanders.py")
if not path_exists(f'{root_path}/disco_xform_utils.py'):
  shutil.copyfile("disco-diffusion/disco_xform_utils.py", "disco_xform_utils.py")

#sys.path.append('./mindseye')
sys.path.append('./guided-diffusion')
sys.path.append('./latent-diffusion')
sys.path.append(".")
sys.path.append('./taming-transformers')
sys.path.append('./disco-diffusion')
sys.path.append('./AdaBins')
