from pathlib import Path
import gdown

URLS = {
    "https://drive.google.com/uc?id=1nezR0u6r9sMpikYYw3jMkfF14EVnmi72": "data/saved_models/fine_tuned_model_with_regularization/config.json",
    "https://drive.google.com/uc?id=1mK6XxrWy682CBkhX4cqEPVNdP-bqzEzS": "data/saved_models/fine_tuned_model_with_regularization/generation_config.json",
    "https://drive.google.com/uc?id=1LFrJeIkvmkCLmRwUV0AU9ESW7QynGMq3": "data/saved_models/fine_tuned_model_with_regularization/model.safetensors",
}


def main():
    path_gzip = Path("data/saved_models/fine_tuned_model_with_regularization").absolute().resolve()
    path_gzip.mkdir(exist_ok=True, parents=True)

    for url, path in URLS.items():
        gdown.download(url, path)


if __name__ == "__main__":
    main()