from database import Database
import Blog

'''
post = Post(blog_id = "123", title = "Awesome", content = "Nothing is true, everything is permited",
            author = "Anonymous")

post.save_to_mongo()

blog = Blog(author = "Joao ninguem", title = "Isso e um titulo", description = "E ae man kkk")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())
'''
Database.initialize()

menu = Menu()

menu.run_menu()
