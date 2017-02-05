# colonbot
A simple bot for twitter. Responds to people who talk about hugging a guy and
smelling his "colon" (they probably mean "cologne") by saying "umm... you're
hugging him wrong".

## Inspiration
A chat in #retro (on irc.badnik.net):

```
22:28 < ImANoob> this is to all of the girls who tweet about smelling a guys "colon" when they hug them  
22:28 < ImANoob> ^ -_- you suck at spelling -_- ^  
...  
22:35 < Kradorex> ⦕ 2228.15 ◉ ImANoob ⦖ this is to all of the girls who tweet about smelling a guys "colon" when they hug them  
22:36 < Kradorex> Someone should write a twitter bot that automaticcally replies to posts containing "hug" and "colon" or the like with a message: "You're hugging them wrong."  
```

## Library?
Technically you could use this as a reply bot for anything. Change the
response (the `RESPONSE` variable in `bot.py`) and the check method
(`checker.check(text)`)

## keys.py
Copy the `keys-sample.py` file to `keys.py` and follow the directions laid out
in the comments.
