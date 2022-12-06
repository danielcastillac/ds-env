def test_torch_gpu():  # TODO
    import torch

    assert torch.cuda.is_available() == True

def test_tf_gpu():
    import tensorflow as tf

    assert tf.config.list_physical_devices('GPU') 


def test_transformers():  # TODO
    from transformers import pipeline

    classifier = pipeline("sentiment-analysis")
    output = classifier("I wouldn't want to wait for a disgusting HuggingFace course")
    assert output == [{"label": "NEGATIVE", "score": 0.9670306444168091}]
