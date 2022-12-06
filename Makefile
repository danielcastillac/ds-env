build_torch:
	mamba env create -f environment_torch.yml

build_tensorflow:
	mamba env create -f environment_tf.yml

remove:
	conda deactivate
	mamba env remove -n pytorch_env -y

activate:
	conda activate pytorch_env

deactivate:
	conda deactivate