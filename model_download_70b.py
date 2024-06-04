from huggingface_hub import hf_hub_download
all_files=[
    ".gitattributes",
    "added_tokens.json",
    "config.json",
    "gap-replay.png",
    "generation_config.json",
    "model-00001-of-00008.safetensors",
    "model-00002-of-00008.safetensors",
    "model-00003-of-00008.safetensors",
    "model-00004-of-00008.safetensors",
    "model-00005-of-00008.safetensors",
    "model-00006-of-00008.safetensors",
    "model-00007-of-00008.safetensors",
    "model-00008-of-00008.safetensors",
    "model.safetensors.index.json",
    "special_tokens_map.json",
    "tokenizer_config.json",
    "tokenizer.json",
    "tokenizer.model"
    ]

token = ""
for items in all_files:
    print(f"Started downloading of the following item: {items}")
    hf_hub_download(local_dir="./meditron-70b",repo_id="epfl-llm/meditron-70b", filename=items, use_auth_token=token)
