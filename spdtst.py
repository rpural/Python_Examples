#! /usr/bin/env python3

import speedtest

st = speedtest.Speedtest()

st.get_servers([])

print("Testing download speed...")
download = st.download()

print("Testing upload speed...")
upload = st.upload()

print(f"Your Download speed is {round(download / 1_000_000.0, 2)} mHz.")
print(f"Your Upload speed is {round(upload / 1_000_000.0, 2)} mHz.")

ping = st.results.ping
print(f"Your ping is {ping}")
