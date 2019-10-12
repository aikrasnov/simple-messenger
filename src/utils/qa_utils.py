def check_response(response, endpoint=None, status_code=200):
    message = f" in {endpoint}" if endpoint else ""
    assert (
        response.status_code == status_code
    ), f"invalid status code: {response.status_code}{message}"
    assert response.is_json, f"has no json in body{endpoint}"
