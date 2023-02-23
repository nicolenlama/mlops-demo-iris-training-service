FROM registry.fedoraproject.org/f33/python3
#COPY into image
COPY . /tmp
WORKDIR /tmp
# Install dependencies
RUN pip install -r ./requirements.txt
# Setting Persistent data
VOLUME ["/temp_models"]
# Running Python Application
CMD ["python" , "iris_model_training/train_iris.py"]
CMD ["python", "iris_test_inference/inference_iris.py"]
