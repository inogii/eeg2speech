# eeg2speech

eeg2speech is a speech generation model conditioned on an EEG signal. It proposes using an architecture based on a latent diffusion model for audio generation, conditioned on EEG signals. The eeg2speech model is based on AudioLDM's architecture, a text-to-audio generation system that uses Latent Diffusion Models (LDM). AudioLDM relies on the contrastive pretraining model CLAP, which trains an Audio encoder and a Text encoder so that the text and audio embeddings from the same pair are as similar as possible, while those from different pairs are as distinct as possible. During the training phase, AudioLDM is conditioned only with audio embeddings to learn how to denoise latent representations of audio signals. However, during inference, the model can be conditioned with text embeddings to guide audio generation. In the case of eeg2speech, the Audio and Text encoder pair from CLAP are replaced with a pair of EEG and Audio encoders obtained from the brainmagick project.

<p align="center">
<img src="./imgs/architecture.png"
     alt="eeg2speech architecture."
     width="700px">
</p>  

## computational requirements
in order to run the project, the following setup has been proven to work. other setups with worse requirements of cpu and ram may work, although a gpu with 80 gb vram is encouraged. 
- 1x A100 SXM4 (80 GB)
- AMD Epyc 7j13 64 core (32cpu)
- 258 GB RAM

at the time of writing this, you can get a similar setup in [vast-ai](https://cloud.vast.ai/?ref_id=144332) for around 0.8$/h

## prepare python environment
in a shell with anaconda installed:
```shell 
# Create conda environment
conda create -n audioldm_train python=3.10
conda activate audioldm_train
# Install running environment
pip install poetry
poetry install
```

## other dependencies

to run the project, you need to install the following dependencies using your preferred package manager:
- libx11-6
- libx11-dev

additionally, an unzip tool is required to download and extract the dataset.

it is also recommended to use a resource monitoring tool like top, btop, or htop to track system performance during the experiments.

```shell
apt install -y unzip libx11-6 libx11-dev btop
```

## prepare dataset download

the dataset is publicly available on Hugging Face. It is a modified version of the AudioCaps dataset, which includes both EEG embeddings for a subject and additional audio embeddings. You will also need to download certain checkpoints for the AudioLDM project, which are also available on Hugging Face.
- [audioEEG Dataset in Huggingface](https://huggingface.co/datasets/inogii/audioeeg)
- [audioLDM Checkpoints](https://huggingface.co/datasets/inogii/audioldm_checkpoints)

to simplify the download process, you can use the following commands. These commands utilize the [hfdownloader](https://github.com/bodaay/HuggingFaceModelDownloader) tool, which allows for faster, multithreaded downloads from Hugging Face.

```shell
./hfdownloader -d inogii/audioeeg -c 10 -s /root/AudioLDM-training-finetuning/data/dataset
./hfdownloader -d inogii/audioldm_checkpoints -c 10 -s /root/AudioLDM-training-finetuning/data/checkpoints
python merge_chunks.py
unzip -o -d data/dataset/ data/dataset/inogii_audioeeg/audioeeg.zip
unzip -o -d data/ data/checkpoints/reassembled_checkpoints.zip
rm -rf data/checkpoints/inogii_audioldm_checkpoints
rm -rf data/dataset/inogii_audioeeg
rm -rf data/__MACOSX
rm data/checkpoints/reassembled_checkpoints.zip
```

## training the model

to train the model, you can run the following command:

```shell
python audioldm_train/train/latent_diffusion.py -c audioldm_train/config/2023_08_23_reproduce_audioldm/audioldm_eeg.yaml
```