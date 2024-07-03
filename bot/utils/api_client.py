import aiohttp
from bot.config import RUST_BACKEND_URL

class APIClient:
    @staticmethod
    async def register_user(user_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{RUST_BACKEND_URL}/register", json={"user_id": user_id}) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(response)# Handle error
                    return None

    @staticmethod
    async def decrypt_keys(api_key: str):
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{RUST_BACKEND_URL}/decrypt_keys",json={"api_key": api_key}) as response:
                if response.status == 200:
                    return await response.json()
                elif response.status == 404:
                    return {"error": "User not found"}
                else:
                    # Handle other errors
                    return {"error": "Failed to decrypt keys"}
                  
    @staticmethod
    async def export_key(api_key: str):
        # This method now uses decrypt_keys
        return await APIClient.decrypt_keys(api_key)
#     # Add other API methods here

# class MockAPIClient:
#     @staticmethod
#     async def register_user(user_id: int):
#         # Simulate a successful registration
#         return {
#             "solana_public_key": f"mock_solana_key_{user_id}",
#             "api_key": f"mock_api_key_{user_id}"
#         }

#     @staticmethod
#     async def export_key(user_id: int, api_key: str):
#         # Simulate key export
#         return {
#             "private_key": f"mock_private_key_{user_id}"
#         }

# Use this instead of the real APIClient in your handlers