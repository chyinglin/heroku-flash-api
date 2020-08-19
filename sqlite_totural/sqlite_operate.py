from sqlite_totural import User
from sqlite_totural import db

#  實作類別
admin = User('admin', 'admin@abc.com')
user1 = User('user1', 'user1@abc.com')
#  寫入資料
db.session.add(admin)
db.session.add(user1)
db.session.commit()

#  全部取回
all_users = User.query.all()
# all_users
# [<User 'admin'>, <User 'user1'>]

# 查看一下型別
# >>> type(all_users)
# <class 'list'>

# 利用取回的資料找尋使用者資料
# >>> all_users[1]
# <User 'user1'>
# >>> all_users[1].id
# 2
# >>> all_users[1].username
# 'user1'
# >>> all_users[1].email
# 'user1@abc.com'

# 透過條件尋找使用者
query_admin = User.query.filter_by(username='admin').first()
# >>> query_admin
# <User 'admin'>
# 如果沒有first?
# query_admin = User.query.filter_by(username='admin')
# >>> query_admin
# <flask_sqlalchemy.BaseQuery object at 0x03631E90>

# #  透過delete刪除
db.session.delete(admin)
# >>> db.session.commit()
# #  commit之後查詢一下目前所有使用者
user_all = User.query.all()
# >>> user_all
# [<User 'user1'>]

#  變更使用者名稱
admin.username='newAdmin'
db.seesion.add(admin)
db.session.commit()
all_user = User.query.all()
# >>> all_user
# [<User 'newAdmin'>, <User 'guest'>]

# 在view中如果希望搜尋不到值的時候拋出404而不是None的話
# 可透過get_or_404()、first_or_404()來設置
# 再利用app_errorhandler來做異常處理
# @app.route('/user/<username>')
# def get_user(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     return render_template('Yourpage.html', user=user)
