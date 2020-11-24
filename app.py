from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('2xUaxaNQafEW5wa72jd8tp3pgKmHOdO65mZ6cwHqaJsmLPNo8y91bCUQlnwZa5ydb6O88PGD5Sx8SVUXXF6+OAOTB1xRnLxNOOnz30DZKAfBT6ONDZdtqpRQl7yVFnfzZ+icnyPulcz80QPZJUz98AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1d58682d8dc4f4d8b8f3f1a38771bd53')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '我他媽看不懂你在寫甚麼雞八毛'

    if msg in ['hi', 'Hi', '嗨']:
        r = 'hi'
    elif msg == '你吃飯了嗎':
        r = '還沒，乾你屁事'
    elif msg == '你是誰':
        r = '林老杯啦'
    elif '幹' in msg:
        r = '幹!是屁還喔!只會罵髒話'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= r))


if __name__ == "__main__":
    app.run()