import time
import requests

MESH_SERVER = "http://172.105.103.52:8080"

def send_heartbeat():
    while True:
        print("💓 Sending heartbeat to NovaMesh...")
        try:
            response = requests.post(f"{MESH_SERVER}/heartbeat", json={
                "node_id": "gpu-verification-node-01",
                "gpu": "GTX 1660 S",
                "performance": "3.6 TFLOPS",
                "temperature": "69C"
            })
            print("✅ Status:", response.status_code, "-", response.text)
        except Exception as e:
            print("❌ Error:", e)
        time.sleep(30)

if __name__ == "__main__":
    send_heartbeat()
