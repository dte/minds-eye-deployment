#!/bin/bash

pwd
ls -la
cd / 
mkdir .streamlit
pwd

pip install xattr
pip install streamlit==1.7.0
pip install wget
pip install fvcore iopath lpips datetime timm ftfy
pip install pytorch-lightning
pip install omegaconf
pip install einops
pip install stqdm
pip install kora
pip install imageio
pip install kornia
pip install pathvalidate
pip install dalle_pytorch


git clone https://github.com/MSFTserver/pytorch3d-lite.git
git clone "https://github.com/CompVis/latent-diffusion.git"
git clone "https://github.com/shariqfarooq123/AdaBins.git"
git clone "https://github.com/alembics/disco-diffusion.git"
git clone "https://github.com/Jack000/glid-3-xl"
git clone "https://github.com/CompVis/taming-transformers.git"
git clone "https://github.com/openai/CLIP.git"
git clone "https://github.com/crowsonkb/guided-diffusion.git"
git clone "https://github.com/assafshocher/ResizeRight.git"
git clone "https://github.com/isl-org/MiDaS.git"
git clone "https://github.com/multimodalart/mindseye.git"

cp mindseye/app.py /app.py


export PATH="$PATH:/repo/pytorch3d-lite"
export PATH="$PATH:/repo/guided-diffusion"
export PATH="$PATH:/repo/latent-diffusion"
export PATH="$PATH:/repo/taming-transformers"
export PATH="$PATH:/repo/disco-diffusion"
export PATH="$PATH:/repo/AdaBins"
export PATH="$PATH:/repo/"

python main.py

  
