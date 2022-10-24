build:
	mamba env create -f environment.yml

remove:
	conda deactivate
	mamba env remove -n pytorch_env -y

activate:
	conda activate pytorch_env

deactivate:
	conda deactivate