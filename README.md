# URL Shortener 🚀

## Tech Stack 🛠️

- **Backend:** Flask (Python)
- **Database:** Redis (In-Memory Storage)
- **Containerization:** Docker

---

## Prerequisites ✅

Ensure you have the following installed:

- **Python 3.8+**
- **Docker & Docker Compose**
- **Redis** (if running locally without Docker)

---

## Week 1 Deliverables 📌

- Set up a **Flask** API to shorten URLs.
- Store short URLs in **Redis**.
- Implement **redirect functionality**.
- Containerize the application with **Docker**.

---

## Run with Docker 🐳

#### **1️⃣ Build the Docker Image**

```sh
docker build -t url-shortener .
```
#### **2️⃣ Start the Containers**

```sh
docker-compose up -d
```
#### **3️⃣ Check Running Containers**

```sh
docker ps
```

## Usage 📌

### **Shorten a URL**

Make a **POST** request:

```sh
curl -X POST http://localhost:5000/shorten \
     -H "Content-Type: application/json" \
     -d '{"url": "https://example.com"}'
```
Response:
```json
{
  "short_url": "http://localhost:5000/abc123"
}
```

#### Redirect to original URL:
Visit the short URL in the browser or use curl
```sh
curl -L http://localhost:5000/abc123
```
