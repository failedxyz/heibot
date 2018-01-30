import client

bot = None

def hei_handler(args):
	print args
	bot.send_msg("hei")

def main():
	bot = client.Bot()
	bot.add_command("hei", hei_handler)
	bot.connect(client.FREENODE, channel="#lasactf")

try:
	main()
except KeyboardInterrupt, e:
	bot.disconnect()
	print "[INTERRUPT] Client stopped by user."
except Exception, e:
	print "[ERROR] Error: %s" % str(e)