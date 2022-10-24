## An all-around data science conda environment focused on pytorch with GPU support
*Only tried in Windows 10
Use of mamba is highly recommended over the out-of-box conda for creating and removing the environment, since its significantly faster and works as a drop-in replacement, but be careful not to use to activate or deactivate the environment itself:
```
conda install mamba -n base -c conda-forge
```
### Create environment:
```
mamba env create -f environment.yml
conda activate pytorch_env
```
### Re-create (first deactivate and remove, then create and activate with the previous steps)
```
conda deactivate
mamba env remove -n pytorch_env -y
```
### To test the correct configuration run (needs pytest to be installed in the base environment):
```
pytest
```
### To install pretrained models:
```
python -m spacy download en_core_web_sm
python -m spacy download es_core_news_sm
python -m nltk.downloader popular
python -m textblob.download_corpora
```