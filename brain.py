#this file speedup the loading AIML file
import aiml

    # Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("krips.xml")
kernel.respond("LOAD AIML B")

    # Press CTRL-C to break this loop
while True:
    print kernel.respond(raw_input("Enter your message >> "))
