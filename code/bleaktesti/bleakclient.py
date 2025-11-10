import asyncio

from bleak import BleakClient
from bleak.exc import BleakCharacteristicNotFoundError

char_uuid = "00001526-1212-EFDE-1523-785FEABCD123"
address = "D7:38:E3:1C:21:EF" 


def notif_callback(sender, data: bytearray):
    print(f"Lähetetty data: {data}")


async def main():
    try:
        async with BleakClient(address, pair=True) as client:
            print(f"Connected to {client.name}")
            print(f"Services: {client.services}")
            await client.start_notify(char_uuid, notif_callback)
            print("Listening for notifications...")
            await asyncio.sleep(60)  # Kuuntele 30 sekuntia
            await client.stop_notify(char_uuid)
    except BleakCharacteristicNotFoundError:
        print("Characteristic not found")
    except Exception as e:
        print(f"Connection failed: {e}")

asyncio.run(main())
