# Azure Machine Learning
This is a repository of Azure Machine Learning examples demonstrating various aspects ranging from setting up the infrastructure up to creating and managing ML lifecycle through MLOps.

## Getting Started
These scripts and notebooks are recommended for use in an Azure Machine Learning [Compute Instance](https://docs.microsoft.com/azure/machine-learning/concept-compute-instance), where you can run them without any additional set up.

However, it can be run in any development environment with the correct `azureml` packages installed.

You can create a new conda environment through:

```bash
conda create --name azure_cloud python=3.8.12
```

which installs a specific version of python at the same time.

Now install the `azureml.core` Python package:

```bash
pip install azureml-core
```

Install additional packages as needed:

```bash
pip install azureml-mlflow
pip install azureml-dataset-runtime
pip install azureml-automl-runtime
pip install azureml-pipeline
pip install azureml-pipeline-steps
```

If you start with Azure Machine Learning, [here](azure-ml-quickstarts) are some resources to get started.

