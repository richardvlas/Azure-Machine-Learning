# What is an Azure Machine Learning component?
An Azure Machine Learning component (previously known as a module) is a self-contained piece of code that does one step in a machine learning pipeline. Components are the building blocks of advanced machine learning pipelines (see [Create and run machine learning pipelines with the Azure Machine Learning CLI](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-create-component-pipelines-cli)). Components can do tasks such as data processing, model training, model scoring, and so on.

A component is analogous to a function - it has a name, parameters, expects input, and returns output. For more information on creating a component, see [create a component](https://docs.microsoft.com/en-us/azure/machine-learning/concept-component#define-a-component-preview).

## Why should I use a component?
Components let you manage and reuse common logic across pipelines.

- **Composable**: Components let developers hide complicated logic behind a simple interface. Component users don't have to worry about the underlying logic, they only need to provide parameters.

- **Share and reuse**: Components are automatically shared with users in the same workspace. You can reuse components across pipelines, environments, workspaces, and subscriptions. Built-in version-tracking lets you keep track of changes and reproduce results.

- **CLI support**: Use components to create pipelines in the CLI (v2).

## Define a component
To define an Azure Machine Learning component, you must provide two files:

- A component specification in the valid [YAML component specification format](https://docs.microsoft.com/en-us/azure/machine-learning/reference-yaml-component-command). This file specifies the following information:
  - Metadata: name, display_name, version, type, and so on.
  - Interface: inputs and outputs
  - Command, code, & environment: The command, code, and environment used to run the component
- A script to provide the actual execution logic.

## Component specification
The component specification file defines the metadata and execution parameters for a component. The component spec tells Azure Machine Learning how to run the Python script that you provide.

The following YAML example is a component specification for a training component.

```yaml
name: Example_Train
display_name: Example Train
version: 20
type: command
description: Example of a torchvision training component
tags: {category: Component Tutorial, contact: user@contoso.com}
inputs:
  training_data: 
    type: path
    description: Training data organized in torchvision structure
  max_epochs:
    type: integer
    description: Maximum epochs for training
  learning_rate: 
    type: number
    description: Learning rate, default is 0.01
    default: 0.01
  learning_rate_schedule: 
    type: string
    default: time-based 
outputs:
  model_output:
    type: path
code:
  local_path: ./train_src
environment: azureml:AzureML-Minimal:1
command: >-
  python train.py 
  --training_data ${{inputs.training_data}} 
  --max_epochs ${{inputs.max_epochs}}   
  --learning_rate ${{inputs.learning_rate}} 
  --learning_rate_schedule ${{inputs.learning_rate_schedule}} 
  --model_output ${{outputs.model_output}}
```

The following table explains the fields in the example. For a full list of available fields, see the [YAML component specification reference page](https://docs.microsoft.com/en-us/azure/machine-learning/reference-yaml-component-command).

| Name  | Type | Required | Description |
| ------------- | ------------- | ------------- | ------------- |
| name  | string | Yes | Name of the component. Must be a unique identifier of the component. Must start with number or letter, and only contain letters, numbers, `_`, and `-`. Maximum length is 255 characters. |
| version |	string | Yes | Version of the component. Must be a string.|
| display_name | string |	No | Display name of the component. Defaults to same as `name`. |
| type | string |	No | The type of the component. Currently, this value must be `command`. |
| description | string | No |	Detailed description of the component. |
| tags | Dictionary<string>	| No | A list of key-value pairs to describe different perspectives of the component. Each tag's key and value should be one word or a short phrase, for example, `Product:Office`, `Domain:NLP`, `Scenario:Image Classification`. |
| is_deterministic | boolean | No |	Whether the component will always generate the same result when given the same input data. The default is `True`. Should be set to `False` for components that will load data from external resources, for instance, importing data from a given url, since the data may be updated. |
| inputs | Dictionary<string, Input> | No |	Defines input ports and parameters of the component. The string key is the name of the input, which must be a valid Python variable name. |
| outputs | Dictionary<string, Output> | No |	Defines output ports of the component. The string key is the name of the output, which must be a valid Python variable name. |
| code | string |	No | Path to the source code. |
| environment |	Environment	| No | The runtime environment for the component to run. |
| command |	string | No |	The command to run the component code. |





