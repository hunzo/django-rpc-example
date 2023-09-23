# django with nameko rpc
## start app
```sh 
docker compose up -d
```
## ex. start client
- client 01
```
nameko rpc rpc-02 --broker amqp://guest:guest@localhost
```
- client 02
```
nameko rpc rpc-02 --broker amqp://guest:guest@localhost
```

