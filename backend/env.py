class SelectPort:
    local=8000
    cloud=80

class MyHost:
    local="localhost"
    cloud="db-instance-random.cq4k2yqospp0.us-east-1.rds.amazonaws.com"    

#SWITCH THESE VARIABLES BEFORE DEPLOYMENT
class MyCurrentEnv:
    host=MyHost.local
    port=SelectPort.local
