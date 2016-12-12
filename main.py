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

while True:
    print(kernel.respond(raw_input(">: ")))
    
