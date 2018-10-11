# Cha1ns
Since a lot of my smart-home-events and actions happen locally on my raspberry pi, i wanted to have a simple-to-use and efficient framework to connect certain events to certain actions.
So, i tried to create such a framework,that takes care of the unique creation and destruction of Input- and Output- modules and a certain abstraction of connection rules ("Chains").

Basically, each Chain module tells the framework which input modules should trigger that Chain and which Output modules it needs.
The framework creates all of those module objects, imports them into that chain and binds that Chain to the given input module.
If, for instance, a Chain "telegram_echo" bind the input "telegram_input", the callback of telegram_echo get called whenever telegram_input 
signals an event.
telegram_echo can then process the message given by telegram_input and send a response using the telegram_output class is bound before.

I am fully aware that such a thing may already exist, yet i wanted to develop it for my own training and experience.
