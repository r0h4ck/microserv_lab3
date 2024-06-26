from nameko.rpc import rpc
import json



class LoggingService:
    name = "logging_service"
    
    logs= []

    @rpc
    def log_message(self,message,message_id):
        
        log_dict = {"uuid": message_id, "msg": message}
        self.logs.append(log_dict)

        print(json.dumps({'Gut it logged': log_dict}))

    @rpc
    def get_messages(self):
        print(json.dumps({'Gets all msg': self.logs}))
        return json.dumps(self.logs)
        



