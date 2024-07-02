import aiohttp
from bot.config import RUST_BACKEND_URL

# class APIClient:
#     @staticmethod
#     async def register_user(user_id: int):
#         async with aiohttp.ClientSession() as session:
#             async with session.post(f"{RUST_BACKEND_URL}/register", json={"user_id": user_id}) as response:
#                 if response.status == 200:
#                     return await response.json()
#                 else:
#                     # Handle error
#                     return None

#     @staticmethod
#     async def export_key(user_id: int, api_key: str):
#         async with aiohttp.ClientSession() as session:
#             async with session.get(f"{RUST_BACKEND_URL}/export_key/{user_id}", headers={"x-api-key": api_key}) as response:
#                 if response.status == 200:
#                     return await response.json()
#                 else:
#                     # Handle error
#                     return None

    # Add other API methods here

class MockAPIClient:
    @staticmethod
    async def register_user(user_id: int):
        # Simulate a successful registration
        return {
            "solana_public_key": f"mock_solana_key_{user_id}",
            "api_key": f"mock_api_key_{user_id}"
        }

    @staticmethod
    async def export_key(user_id: int, api_key: str):
        # Simulate key export
        return {
            "private_key": f"mock_private_key_{user_id}"
        }

# Use this instead of the real APIClient in your handlers