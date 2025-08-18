# OLLAMA + gpt-oss Model
```bash
# start docker
colima start --memory 16 --cpu 6 --disk 100 --vm-type vz --mount-type virtiofs

# start ollama
docker-compose up -d

# open
http://localhost:3000

# clean up
docker-compose down
colima stop && colima delete
```