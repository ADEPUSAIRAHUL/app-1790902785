import unittest
import asyncio
from httpx import AsyncClient, ASGITransport

from main import app


class TestHealthEndpoint(unittest.TestCase):
    def test_health_returns_200_and_healthy_status(self):
        async def _run():
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as client:
                response = await client.get("/health")
                return response

        response = asyncio.run(_run())
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data.get("status"), "healthy")


class TestItemsEndpoint(unittest.TestCase):
    def test_items_returns_200_and_array(self):
        async def _run():
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as client:
                response = await client.get("/items")
                return response

        response = asyncio.run(_run())
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 1)
        for item in data:
            self.assertIn("id", item)
            self.assertIn("name", item)


if __name__ == "__main__":
    unittest.main()
