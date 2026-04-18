import requests


class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.content   # ✅ MUST be bytes

    def load_json(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.json()


if __name__ == "__main__":
    URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

    requester = GetRequester(URL)

    print("Fetching raw response...\n")
    raw_data = requester.get_response_body()
    print(raw_data[:200])

    print("\nLoading JSON data...\n")
    people = requester.load_json()
    print(people)
    print("\nData type:", type(people))