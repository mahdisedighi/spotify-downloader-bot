from models import *
import secrets
from asgiref.sync import sync_to_async




@sync_to_async
def add_user(user_id):
    existing_user = session.query(User).filter_by(user_id=user_id).first()
    if existing_user:
        return False
    referral_code = secrets.token_urlsafe(8) 
    new_user = User(user_id=user_id, referral_code=referral_code)
    session.add(new_user)
    session.commit()
    return new_user

@sync_to_async
def update_user(user_id, new_user_id):
    user = session.query(User).filter_by(user_id=user_id).first()
    if not user:
        return True

    user.user_id = new_user_id
    session.commit()
    return True




@sync_to_async
def is_user_exist(user_id):
    user = session.query(User).filter_by(user_id=user_id).first()
    return user is not None



@sync_to_async
def get_referral_link(user_id):
    user = session.query(User).filter_by(user_id=user_id).first()

    if not user:
        session.close()
        return

    referral_link = f"https://t.me/YOUR_BOT_USERNAME?start={user.referral_code}"
    session.close()
    return referral_link



@sync_to_async
def get_referral_count(user_id):
    user = session.query(User).filter_by(user_id=user_id).first()
    if not user:
        return 0
    referral_count = session.query(User).filter_by(referrer_id=user.id).count()
    return referral_count



@sync_to_async
def add_referral(user_id, referrer_code):
    referrer = session.query(User).filter_by(referral_code=referrer_code).first()
    if not referrer:
        session.close()
        return False

    existing_user = session.query(User).filter_by(user_id=user_id).first()
    if existing_user:
        session.close()
        return False

    new_referral_code = secrets.token_urlsafe(8)
    new_user = User(user_id=user_id, referral_code=new_referral_code, referrer_id=referrer.id)

    session.add(new_user)
    session.commit()
    session.close()
    return True


@sync_to_async
def get_user(user_id):
    user = session.query(User).filter_by(user_id=user_id).first()
    return user