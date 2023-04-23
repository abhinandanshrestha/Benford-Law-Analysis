from wsgiref.simple_server import make_server
from pyramid.config import Configurator

if __name__ == '__main__':
    with Configurator() as config:
        config.include('pyramid_jinja2')  # include the Jinja2 package
        config.include('pyramid_debugtoolbar')
        config.add_static_view(name='static',path='static')
        config.add_route('home', '/')
        config.add_route('benford', '/benford')
        config.scan('views')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    print("Server running at http://localhost:6543")
    server.serve_forever()


# can directly work with .html also
# config.add_jinja2_renderer('.html')