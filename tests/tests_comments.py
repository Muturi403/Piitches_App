from app.models import Comment, User
from app import db

def setUp(self):
  self.user_Faith = User(username = 'Faith',password = '123456', email = 'fayshiks123@gmail.com')
  self.new_comment = Comment(id=1,user_id=10,comment='Pitches', pitch_id = 12 )

def tearDown(self):
  Comment.query.delete()
  User.query.delete()
        
def test_check_instance_variables(self):
  self.assertEquals(self.new_comment.id,1)
  self.assertEquals(self.new_comment.user_id,10)
  self.assertEquals(self.new_comment.comment,'Pitches')
  self.assertEquals(self.new_comment.pitch_id,12)
        
def test_save_comment(self):
  self.new_comment.save_comment()
  self.assertTrue(len(Comment.query.all())>0)
        
def test_get_comment_by_id(self):
  self.new_comment.save_comment()
  got_comments = Comment.get_comments(12345)
  self.assertTrue(len(got_comments) == 1)