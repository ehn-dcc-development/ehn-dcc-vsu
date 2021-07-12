import requests

from repeat_timer import RepeatTimer
from time import sleep


class VsuClient:

    VSU_SERVER = "http://localhost:9010"

    @staticmethod
    def latest() -> str:
        r = requests.get(f"{VsuClient.VSU_SERVER}/vsc_most_recent")
        r.raise_for_status()
        return r.text


def show_latest(vsu_client: VsuClient):
    print(f"Latest Value-Set timestamp: {vsu_client.latest()}")


if __name__ == "__main__":
    vsu = VsuClient()
    SECONDS_BETWEEN_CALLS = 5
    MAX_CLIENT_SECONDS = 26
    rep_timer = RepeatTimer(SECONDS_BETWEEN_CALLS, show_latest, args=(vsu,))
    rep_timer.start()
    sleep(MAX_CLIENT_SECONDS)
    rep_timer.cancel()
