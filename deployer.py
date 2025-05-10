import os
import asyncio

async def deploy_user_bot(user_id, token):
    try:
        with open(f"user_bot_{user_id}.py", "w") as f:
            with open("bot_template.py", "r") as template:
                bot_code = template.read().replace("USER_BOT_TOKEN_HERE", token)
                f.write(bot_code)
        os.system(f"nohup python3 user_bot_{user_id}.py &")
        return True
    except Exception as e:
        print(e)
        return False
