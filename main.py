import telebot
import random
import re
from time import sleep

admin_id = [管理员TG_ID]
channel_link = '你的频道链接，比如https://t.me/fffffx2'
channel_name = '你的频道名称'
channel_id = '你的频道ID'
TOKEN = '你的BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

auto_replies = {}


@bot.message_handler(commands=['start'])
def start_auto_reply(message):
    identifier = message.text.replace('/start ', '').strip()
    if identifier in auto_replies:
        if is_subscribed(channel_id, message.from_user.id):
            reply_text = f'{auto_replies[identifier]}\n\n✅订阅来源<a href=\"{channel_link}\"><strong>{channel_name}</strong></a>，搬运转发请带来源！'
            bot.reply_to(message, reply_text, parse_mode='HTML', disable_web_page_preview=True)

        else:
            reply_markup = telebot.types.InlineKeyboardMarkup()
            url_button = telebot.types.InlineKeyboardButton(
                text='👉点击关注频道',
                url=f'{channel_link}'
            )
            reply_markup.add(url_button)
            bot.reply_to(message, '请先点击下方按钮关注频道后再尝试获取订阅：', reply_markup=reply_markup)
    else:
        bot.reply_to(message, f'请从<a href=\"{channel_link}\"><strong>{channel_name}</strong></a>获取邀请链接！', parse_mode='HTML', disable_web_page_preview=True)


@bot.message_handler(commands=['add'], chat_types=['private'])
def add_auto_reply(message):
    if message.from_user.id in admin_id:
        auto_reply_text = message.text.replace('/add', '').strip()
        if len(auto_reply_text) > 0:
            identifier = ''.join(random.choices('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=8))
            auto_replies[identifier] = auto_reply_text
            message_raw = message.text
            start_link = f'https://t.me/{bot.get_me().username}?start={identifier}'
            url_pattern = r'https?://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]'
            url_match = re.search(url_pattern, message_raw)
            if url_match:
                message_raw = re.sub(url_pattern, start_link, message_raw)
                message_raw = message_raw.replace('/add', '')
                url_pattern = r'https://t.me/yige_bot\?start=[\w-]+'
                url_match = re.search(url_pattern, message_raw)
                try:
                    url = url_match.group(0)
                    message_raw = re.sub(url_pattern, f'<a href="{url}"><strong>【点击这里获取】</strong></a>', message_raw)
                except Exception as t:
                    bot.reply_to(message, f'出错了：{t}')
            bot.send_message(chat_id=channel_id, text=message_raw, parse_mode='HTML', disable_web_page_preview=True)
        else:
            bot.reply_to(message, '请提供要添加的自动回复内容')
    else:
        bot.reply_to(message, '您没有权限进行此操作')


def is_subscribed(chat_id, user_id):
    if user_id in admin_id:
        return True
    else:
        chat_member = bot.get_chat_member(chat_id, user_id)
        return chat_member.status == 'member' or chat_member.status == 'administrator'


@bot.message_handler(commands=['help'], chat_types=['private'])
def help_doc(message):
    doc = '''
【务必将bot拉到频道并给与*发布消息*的权限】
管理员使用 `/add `[空格]内容（比如订阅流量信息），会自动帮您把第一个链接转换为 *【点击这里获取】*形式的超链接发送频道
作者 @KKAA2222 
        '''
    bot.send_message(message.chat.id, doc, parse_mode='Markdown' )


if __name__ == '__main__':
    print('=====程序已启动=====')
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            sleep(30)
