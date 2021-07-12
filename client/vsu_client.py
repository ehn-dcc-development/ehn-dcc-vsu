import requests


class VsuClient:

    VSU_SERVER = "http://localhost:9010"

    @staticmethod
    def latest() -> str:
        r = requests.get(f"{VsuClient.VSU_SERVER}/vsc_most_recent")
        r.raise_for_status()
        return r.text


if __name__ == "__main__":
    vsu = VsuClient()
    print(f"Latest Value-Set timestamp: {vsu.latest()}")
