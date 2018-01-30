import socket
import string

FREENODE = "irc.freenode.net"

alphanumeric = string.ascii_uppercase + string.ascii_lowercase + string.digits
nick = "heibot"

class Bot(object):
	client = None
	connected = False
	command_trigger = "!"
	commands = {}
	channel = None
	joined = False

	def __init__(self, trigger=None):
		self.client = socket.socket()
		if trigger and len(trigger) == 1 and trigger not in alphanumeric:
			self.command_trigger = trigger

	def connect(self, host, port=6667, channel=None):
		print "Connecting to %s..." % str((host, port))
		self.client.connect((host, port))
		self.connected = True
		self.send("NICK %s" % nick)
		self.send("USER %s %s %s :%s" % (nick, nick, nick, nick))
		while True:
			line = self.client.recv(1024)
			if line.find("PING") != -1:
				self.send("PONG :" + line.split(":")[1])
				if self.joined != True and channel is not None:
					self.send("JOIN %s" % channel)
					self.channel = channel
					self.joined = True

			if line[0] == self.command_trigger:
				command = line[1:].split(" ")[0].lower()
				args = line[2+len(command):]
				if command in self.commands:
					self.commands[command](args)

	def send(self, message):
		if self.connected:
			self.client.send("%s\n" % message)

	def add_command(self, keyword, handler):
		self.commands[keyword.lower()] = handler
		print self.commands

	def disconnect(self):
		self.client.close()
		self.connected = False