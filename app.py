import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("I will start debug ...")
        a = 123
        a += 456
        print("a:{}\n".format(a))
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/hello", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
