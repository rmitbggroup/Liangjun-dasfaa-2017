class microblog:
    """ microblogs (v,t)"""
    dist=0.0
    content = ""
    post_time = ""
    reply = ""
    usr = ""
    def __init__(self,con,ti):
        self.content=con
        self.post_time=ti
    def rep(self,us,re):
        self.usr = us
        self.reply = re