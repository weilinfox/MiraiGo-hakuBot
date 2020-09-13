# 此源代码的使用受 GNU AFFERO GENERAL PUBLIC LICENSE version 3 许可证的约束, 您可以在下面的链接找到该许可证.
# https://github.com/weilinfox/MiraiGo-CQHTTP-hakuBot/blob/master/LICENSE

import time
from hakuCore.botApi import *

recordMsg = []
heartbeats = []
lock = False

def msgRate():
    global recordMsg
    return len(recordMsg)

def heartRate():
    global heartbeats
    return len(heartbeats)

def main (msgDict):
    msgList = list(msgDict['raw_message'].split())
    if len(msgList) > 1 and msgList[1].strip() == 'help':
        helpMsg = '可以查看小白的状态哦~'
        if msgDict['message_type'] == 'private':
            send_private_message(msgDict['user_id'], helpMsg)
        elif msgDict['message_type'] == 'group':
            send_group_message(msgDict['group_id'], helpMsg)
        return

    global lock, recordMsg, heartbeats
    while lock:
        pass
    lock = True
    if msgDict['message_type'] == 'private':
        send_private_message(msgDict['user_id'], '流量: ' + str(msgRate())+'/min\n心跳: ' + str(heartRate()*5))
    elif msgDict['message_type'] == 'group':
        send_group_message(msgDict['group_id'], '流量: ' + str(msgRate())+'/min\n心跳: ' + str(heartRate()*5))
    lock = False


def check():
    global lock, recordMsg
    while lock:
        pass
    lock = True
    ntime = time.time()
    while len(recordMsg) > 0:
        if ntime - min(recordMsg) >= 60:
            recordMsg.remove(min(recordMsg))
        else:
            break
    while len(heartbeats) > 0:
        if ntime - min(heartbeats) >= 60:
            heartbeats.remove(min(heartbeats))
        else:
            break
    lock = False

def insert():
    global lock, recordMsg
    ntime = time.time()
    while lock:
        pass
    lock = True
    recordMsg.append(ntime)
    lock = False

def heartBeats():
    global lock, heartbeats
    ntime = time.time()
    while lock:
        pass
    lock = True
    heartbeats.append(ntime)
    lock = False
