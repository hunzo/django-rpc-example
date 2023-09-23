from nameko.rpc import rpc 

class reader:
    name =  "reader_02"
    @rpc
    def get_data(self):
        print("GET DATA RPC 02")
        return {
            "reader_id": 2,
            "data": "reader data from reader 02"
        }
