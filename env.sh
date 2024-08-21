sudo apt install -y unzip libx11-6 libx11-dev btop
# Create conda environment
conda create -n audioldm_train python=3.10 -y
conda activate audioldm_train
# Clone the repo
git clone https://github.com/haoheliu/AudioLDM-training-finetuning.git; cd AudioLDM-training-finetuning
bash <(curl -sSL https://g.bodaay.io/hfd) -h
# Install running environment
pip install poetry
poetry install
