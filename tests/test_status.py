from api_requests import request_status


class TestStatus:

    def test_status_api(self):
        response = request_status.get_status()
        assert response.status_code == 200
        assert response.json()["status"] == "OK"