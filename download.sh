./hfdownloader -d inogii/audioeeg -c 10 -s /root/AudioLDM-training-finetuning/data/dataset
./hfdownloader -d inogii/audioldm_checkpoints -c 10 -s /root/AudioLDM-training-finetuning/data/checkpoints
python merge_chunks.py
unzip -o -d data/dataset/ data/dataset/inogii_audioeeg/audioeeg.zip
unzip -o -d data/ data/checkpoints/reassembled_checkpoints.zip
rm -rf data/checkpoints/inogii_audioldm_checkpoints
rm -rf data/dataset/inogii_audioeeg
rm -rf data/__MACOSX
rm data/checkpoints/reassembled_checkpoints.zip