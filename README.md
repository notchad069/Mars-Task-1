So, I learned quite a lotta stuff with this task. THe major challenges/roadblocks that i faced through this task was the debugging part. I wanted to make every single code errorless and that was the challenging part. Lemme explain my exp with task 1 through each quests.

#Light Dose
  So, this was kinda easy for me as i've been usin ubuntu for around 5 months now. But that doesn't mean i know everythin. I still didnt know how to write a bash script as i havent used that before. I had to learn about that. Light dose was easy but that wasn't really the case for others.

  #Medium Dose
    **The Rover, Brick, has a simple task — detect a Red circle marker on the ground, reach its location, and perform a 360-degree turn**
   This was easy after figuring out the frame of reference. It would've been a little bit more challenging if y'all didnt give that hint tbh. I used a sketch to get an overview of the problem but i dont know where i sketched it. At first i thought of simulatin this in real time but yea that isn't really a good idea cuz i had to wait for a couple of minutes to get the output.
    **The Mars rover communicates with Earth using Morse code**
      This one was easy but it took a while to create that dictionary for morse code to english. Cuz i had to type in every single character manually. 
      **The Mars rover transmits encrypted messages to Earth using a special encoding method. Your task is to decode the message by reversing this pattern.**
        This was similar to the morse code one. The only difference was that, i didnt have to type in every single char like morse code as this was just a pattern where every nth letter was moved n times in the alphabet. 
      **Sunitha Williams rescue mission**
        Well this one was a bit interesting cuz at first i thought, this seems too real to be in a hypothetical question. And then i looked it up and yep, that was true. I'm quite bad at knowin real world news and stuff. Anyways, my approach to this wouldn't be the best cuz i only used those two filters separately and didnt use a hybrid one cuz i thought of updating the code later but i didnt get the time to do that. Ig i might update this after submission.
      **Euler to Quaternions**
        THis was the most interesting task of all cuz the concept of Quaternions is kinda intriguing. I spent quite some time in this. I tried to solve the actual equations for converting euler angles to quaternions. It was kinda hard and i just left it half way down the road and just got the conversion equation from https://inertiallabs.com/euler-and-quaternion-angles-differences-and-why-it-matters/ and for further stuff, i used deepseek cuz the equations from that websites were kinda complex. 
  #Hard Dose
    **Rover Brick — the King of the Arena**
      This one took me a lotta time. My approach is that, after i upload the .txt file which contains info regardin the placement of obstacles across the arena, i'd analyse every single line separately. Also i wanted to work only at the positive region. So i made south and west as positive by takin the negative of those coordinates. While, brick was navigating the arena, I'd mark those coords which it had already reached as 0. For finding the shortest path, i used BFS. I thought of using A* but that seemed a bit too complex. Anyways, that's how i did this.
  #Final Words:
    THat's all the quests that i did. I wanted to try the other two hard dose probs but i didnt get the time to try those. The second one from hard dose might have taken all my time as i dont know opencv but i'll still learn it. That's pretty much it.
    
