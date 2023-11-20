import asyncio
import json
import websockets
import httpx

async def fetch_weather_data(api_url):
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
        return response.text

async def handle_client(websocket, path):
    try:
        while True:
            # Nhận yêu cầu tìm kiếm từ client
            search_query = await websocket.recv()
            
            # Gửi yêu cầu API thời tiết
            api_url = f"http://api.weatherapi.com/v1/current.json?key=768512e15ecf4ceca73102703231311&q={search_query}&aqi=yes"
            weather_data = await fetch_weather_data(api_url)
            
            # Gửi thông tin thời tiết về client
            await websocket.send(weather_data)
    except websockets.exceptions.ConnectionClosedError:
        pass

async def main():
    server = await websockets.serve(handle_client, "localhost", 2905)
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
