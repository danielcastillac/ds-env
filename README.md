## An all-around data science conda environment focused on either pytorch or tensorflow with GPU support
*Only tried in Pop_OS (Ubuntu 22.04 LTS) 
Use of mamba is highly recommended over the out-of-box conda for creating and removing the environment, since its significantly faster and works as a drop-in replacement, but be careful not to use to activate or deactivate the environment itself:
```
conda install mamba -n base -c conda-forge
```
## Note: Makefile currently not working due to conda issues, see [here](https://stackoverflow.com/questions/53382383/makefile-cant-use-conda-activate).

### Create environment:
```
mamba env create -f environment_{torch or tf}.yml
conda activate {torch or tf}_env
```
### Re-create (first deactivate and remove, then create and activate with the previous steps)
```
conda deactivate
mamba env remove -n {torch or tf}_env -y
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
### TO-DO:
- [ ] Rewrite makefile for automatic build and remove
- [X] ~~Add option to makefile for tensorflow alternative~~
- [X] ~~Add tests for gpu availability for each library~~
