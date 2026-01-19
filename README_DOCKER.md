# Medical Symptom Checker - Docker Setup

## 🐳 Docker Deployment

This setup includes everything you need to run the medical symptom checker in a Docker container with all dependencies properly isolated.

## 🚀 Quick Start

### Option 1: Using Docker Compose (Recommended)

```bash
# Build and run the container
docker-compose up --build

# Or run in detached mode
docker-compose up --build -d
```

The app will be available at: **http://localhost:5000**

### Option 2: Using Docker directly

```bash
# Build the image
docker build -t medical-symptom-checker .

# Run the container
docker run -p 5000:5000 medical-symptom-checker
```

## 📁 Docker Files

- **`Dockerfile`** - Main container definition with Python 3.11 slim base
- **`docker-compose.yml`** - Easy orchestration with port mapping
- **`.dockerignore`** - Excludes unnecessary files from the build context

## 🛠️ Container Details

- **Base Image**: Python 3.11-slim (lightweight and secure)
- **Working Directory**: `/app`
- **Exposed Port**: 5000
- **Environment**: Production Flask mode

## 🔄 Useful Commands

```bash
# View logs
docker-compose logs -f

# Stop the container
docker-compose down

# Rebuild after changes
docker-compose up --build --force-recreate

# Access container shell (for debugging)
docker-compose exec medical-symptom-checker /bin/bash
```

## 📊 Benefits of Docker Setup

✅ **Isolated Environment** - No conflicts with system Python  
✅ **Reproducible** - Same environment everywhere  
✅ **Portable** - Run on any machine with Docker  
✅ **Version Control** - Container image can be versioned  
✅ **Easy Deployment** - One command to start everything  

## 🔍 Troubleshooting

If port 5000 is already in use, modify the port mapping in `docker-compose.yml`:

```yaml
ports:
  - "8080:5000"  # Use port 8080 instead
```

Then access at: **http://localhost:8080**
