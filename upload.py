from huggingface_hub import HfApi

USERNAME = "oschan77"
MODEL_NAME = "OpenPipe-7B-slerp"
HF_TOKEN = "xxx"

api = HfApi(token=HF_TOKEN)
api.create_repo(repo_id=f"{USERNAME}/{MODEL_NAME}", repo_type="model")
api.upload_folder(
    repo_id=f"{USERNAME}/{MODEL_NAME}",
    folder_path="merge",
)
