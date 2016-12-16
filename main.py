#created by Nishad A
#copyright protected
import aiml
import os
kernel = aiml.Kernel()
#if os.path.isfile("krips.brn"):
 #   kernel.bootstrap(brainFile = "krips.brn")
#else:
kernel.bootstrap(learnFiles = "krips.xml", commands = "LOAD AIML B")
kernel.saveBrain("krips.brn")
print  "\n*************BlueRabbit*************"
print "\nHi I am krips v 1.0... Happy to help you\n"

while True:
    print("you  : "+kernel.respond(raw_input("krips: ")))
    
