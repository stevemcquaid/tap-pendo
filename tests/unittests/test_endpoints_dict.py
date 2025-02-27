from tap_pendo.streams import Endpoints, Stream

config = {'x_pendo_integration_key': "TEST_KEY"}
stream = Stream(config=config)
stream.endpoint = Endpoints("/api/v1/aggregation", "POST", {"headers": "headers"}, {"params": "params"})


def test_correct_values_passed_in_endpoint_object():
    assert stream.endpoint.endpoint == "/api/v1/aggregation"
    assert stream.endpoint.method == "POST"
    assert stream.endpoint.headers == {"headers": "headers"}
    assert stream.endpoint.params == {"params": "params"}

def test_correct_endpoint_url():
    stream.endpoint = Endpoints(
        "/api/v1/visitor/{visitorID}/history", "GET")
    formatted_url = stream.endpoint.get_url(visitorID='abc')
    assert formatted_url == 'https://app.pendo.io/api/v1/visitor/abc/history'