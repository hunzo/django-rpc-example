from nameko.rpc import rpc 

class reader:
    name =  "reader_01"
    @rpc
    def get_data(self):
        print("GET DATA RPC 01")
        return {
            "reader_id": 1,
            "data": "reader data from reader 01"
        }
