#!/usr/bin/env python3
import time
import socket
import requests
import random

MESH_SERVER = "http://172.105.103.52:8080"

NODE_ID = f"nova-node-{random.randint(1000, 9999)}"
GPU_MODEL = "GTX 1660 S"
TFLOPS = 3.6

def register_node():
    try:
        response = requests.post(f"{MESH_SERVER}/register", json={
            "node_id": NODE_ID,
            "gpu_model": GPU_MODEL,
            "tflops": TFLOPS,
            "ip": socket.gethostbyname(socket.gethostname())
        })
        print("📡 Registration:", response.status_code, response.text)
    except Exception as e:
        print("⚠️ Registration failed:", e)

def send_heartbeat():
    try:
        while True:
            usage = round(random.uniform(0.3, 0.9), 2)
            temperature = random.randint(60, 78)
            response = requests.post(f"{MESH_SERVER}/heartbeat", json={
                "node_id": NODE_ID,
                "gpu_utilization": usage,
                "temperature": temperature
            })
            print("💓 Heartbeat:", response.status_code, response.text)
            time.sleep(30)
    except Exception as e:
        print("❌ Heartbeat error:", e)

if __name__ == "__main__":
    print(f"🔧 Nova GPU Worker: {NODE_ID}")
    register_node()
    send_heartbeat()
