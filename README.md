# Easy-OpenAI

## Installation
```bash
pip install git+https://github.com/jdf-prog/easy-openai
```

## Features

- support automatic retrying
- multi-threading to increase the speed
- auto cache annotations under `~/.easy-openai`, no recomputation if the input is the same
- support both official OpenAI API and Azure OpenAI API
- support API key pools


## Usage
```python
prompts = ["Respond with one digit: 1+1=", "Respond with one digit: 2+2="]
chatmls = [[{"role":"system","content":"You are an AI assistant that helps people find information."},
            {"role":"user","content": prompt}] for prompt in prompts]
openai_completions(chatmls, model_name="ChatGPT", max_tokens=50) # change model_name to your desired model
```


### environment variable

By default, we read the OpenAI API configuration from the environment variable

#### Official OpenAI API 
```
export OPENAI_API_KEY="..." # replace ... with your API key
```
set `model_name` to openai official model name

#### Azure OpenAI API
```
export OPENAI_API_KEY="..." 
export AZURE_OPENAI_ENDPOINT="https://{your_endpoint}.openai.azure.com/"
export OPENAI_API_TYPE="azure"
export OPENAI_API_VERSION="..."
```
set `model_name` to your Azure deployed model name

#### API key pools
```
export OPENAI_API_KEYS="key1,key2,key3" # replace key1,key2,key3 with your API keys
```
Not only support official OpenAI API
