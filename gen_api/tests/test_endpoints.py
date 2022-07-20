import json
from tests.utils import make_token


def test_gen(client):

    token = make_token(2)
    response = client.post(
        "/api/gen"
    )

    assert json.dumps(response.json, sort_keys=True) == json.dumps(
        gen, sort_keys=True
    )


gen = {
    "generator": {
        "results": "SUCCESS"
    },
}
