from cocoapi import *
import json, codecs, traceback
data_dir = "data/"
authsOpen = codecs.open(data_dir + "Auths.json","r","utf-8")
loginOpen = codecs.open(data_dir + "Logins.json","r","utf-8")
auths = json.load(authsOpen)
Login = json.load(loginOpen)
Bot = []
Botmid = []
for client_name in auths:
	i = 0
    for auth in auths[client_name]:
        try:
            Bot.append(LINE(auth))
            print("【Login OK】{}".format(Bot[len(Bot)-1].getProfile().displayName))
            Botmid.append(Bot[len(Bot)-1].getProfile().mid)
        except:
            try:
                Bot.append(LINE(Login[client_name]["0"+str(i)]["mail"], Login[client_name]["0"+str(i)]["passwd"]))
                Bot[len(Bot)-1].log("Auth Token : " + str(Bot[len(Bot)-1].authToken))
                print(str(Bot[len(Bot)-1].getProfile().displayName))
                Botmid.append(Bot[len(Bot)-1].getProfile().mid)
            except BaseException as e:
                print("[Login] %s[%s] Error %s" % (client_name, str(len(Bot)-1), str(e),))
                traceback.print_exc()
                exit(0)
        i += 1
print("======登入成功=====")
def Sync(Objlist, Midlist):
	invlist = []
	for x in Objlist:
		grouplist = x.getGroupIdsJoined()
		print(x.getProfile().displayName + " 群組取得階段")
		for xx in grouplist:
			group = x.getGroup(xx)
			memberlist = [member.mid for member in group.members]
			print(x.getProfile().displayName + " 成員取得階段")
			for xxx in Midlist:
				print(x.getProfile().displayName + " 成員判別階段")
				if xxx not in memberlist:
					invlist.append(xxx)
				else:
					pass
			print(x.getProfile().displayName + " 邀請階段")
			x.inviteIntoGroup(xx, invlist)
			invlist.clear()
def Accept(Objlist):
	for x in Objlist:
		for xx in x.getGroupIdsInvited():
			x.acceptGroupInvitation(xx)
			print(x.getProfile().displayName + " 加入 " + x.getGroup(xx).name)

