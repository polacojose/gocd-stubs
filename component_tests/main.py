import os

from gocd import Configuration

configuration = Configuration(
    host=os.getenv("HOST"),
    access_token=os.getenv("ACCESS_TOKEN"),
)


def main():
    print("Hello from integration-tests!")


if __name__ == "__main__":
    main()
