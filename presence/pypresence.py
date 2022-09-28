from pypresence import Presence
import tim

client_id = '2399023920329030992'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect()  # Start the handshake loop

print(RPC.update(state="...", details="...", large_image="...", small_image="...", start="...", buttons=[
      {"label": "...", "url": "..."}, {"label": "...", "url": "..."}], party_size=[2, 3], party_id="...",))  # Set the presence


while True:  # The presence will stay on as long as the program is running
    time.sleep(15)  # Can only update rich presence every 15 seconds
