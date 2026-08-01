import kagglehub

OWNER = ""
SLUG = ""


def download():
    if OWNER == "c":
        return kagglehub.competition_download(SLUG)
    return kagglehub.dataset_download(f"{OWNER}/{SLUG}")


if __name__ == "__main__":
    path = download()
    print(f"Dataset downloaded to: {path}")
