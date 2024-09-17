import asyncio
import edge_tts
import pygame
import os
import randfacts
import random

async def amain(text_content):
    communicate = edge_tts.Communicate(text_content, VOICE, pitch=TTS_PITCH, rate=TTS_RATE) #reads with a pitch
    # communicate = edge_tts.Communicate(text_content, VOICE) #reads with a pitch
    await communicate.save(OUTPUT_FILE)

    pygame.mixer.init(devicename=OUTPUT_DEVICE) #Outputs audio source to VB Audio Cablle to be catched in OBS as it's own source
    pygame.mixer.music.load(OUTPUT_FILE)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


    pygame.mixer.quit()
    os.remove(OUTPUT_FILE)

async def main():
    while True:
        # Get a random fact
        fact = randfacts.get_fact(filter_enabled=False)
        # fact = randfacts.get_fact(only_unsafe=True)

        # Write the fact to the speech file
        with open("speech.txt", "w") as file:
            intro_speech = [
    "The Jellyfish Fields gossip columnist once whispered, 'Did you know...'",
    "Mr. Krabs's pet snail, Gary, confided in me, 'The secret is...'",
    "The Flying Dutchman's ghost pirate crew whispered among themselves, 'Imagine this...'",
    "The Chum Bucket's secret menu has a surprising twist:...",
    "The Bikini Bottom Library's dusty old books revealed, 'It turns out that...'",
    "Plankton's secret lab experiments uncovered, 'The truth is...'",
    "The Goofy Goober's comedy routine once mentioned, 'Get ready for this...'",
    "Squidward's clarinet solo was interrupted by a sudden realization, 'Can you believe that...'",
    "The Krusty Krab's secret recipe for Krabby Patties includes a surprising ingredient:...",
    "Mermaid Man's old comic book collection has a hidden secret:...",
    "Barnacle Boy once bragged, 'I know something you don't...'",
    "The Bikini Bottom Chum Bucket's secret ingredient is something unexpected:...",
    "The Flying Dutchman's treasure map has a hidden clue:...",
    "The Jellyfish Fields' annual beauty pageant winner revealed, 'The secret is...'",
    "Mr. Krabs's secret safe contains a surprising secret:...",
    "The Goofy Goober's latest comedy routine has a shocking twist:...",
    "Squidward's clarinet solo was interrupted by a sudden realization, 'Can you believe that...'",
    "The Krusty Krab's secret ingredient is something unexpected:...",
    "Mermaid Man's old comic book collection has a hidden secret:...",
    "Barnacle Boy once bragged, 'I know something you don't...'",
    "The Bikini Bottom Chum Bucket's secret ingredient is something unexpected:...",
    "The Flying Dutchman's treasure map has a hidden clue:...",
    "The Jellyfish Fields' annual beauty pageant winner revealed, 'The secret is...'",
    "Mr. Krabs's secret safe contains a surprising secret:...",
    "The Goofy Goober's latest comedy routine has a shocking twist:...",
    "Squidward's clarinet solo was interrupted by a sudden realization, 'Can you believe that...'",
    "The Krusty Krab's secret ingredient is something unexpected:...",
    "Mermaid Man's old comic book collection has a hidden secret:...",
    "Barnacle Boy once bragged, 'I know something you don't...'",
    "The Bikini Bottom Chum Bucket's secret ingredient is something unexpected:...",
    "The Flying Dutchman's treasure map has a hidden clue:...",
    "The Jellyfish Fields' annual beauty pageant winner revealed, 'The secret is...'",
    "Mr. Krabs's secret safe contains a surprising secret:...",
    "The Goofy Goober's latest comedy routine has a shocking twist:...",
    "Squidward's clarinet solo was interrupted by a sudden realization, 'Can you believe that...'",
    "The Krusty Krab's secret ingredient is something unexpected:...",
    "Mermaid Man's old comic book collection has a hidden secret:...",
    "Barnacle Boy once bragged, 'I know something you don't...'",
    "The Bikini Bottom Chum Bucket's secret ingredient is something unexpected:...",
    "The Flying Dutchman's treasure map has a hidden clue:...",
    "The Jellyfish Fields' annual beauty pageant winner revealed, 'The secret is...'",
    "Mr. Krabs's secret safe contains a surprising secret:...",
    "The Goofy Goober's latest comedy routine has a shocking twist:...",
    "Squidward's clarinet solo was interrupted by a sudden realization, 'Can you believe that...'",
    "The Krusty Krab's secret ingredient is something unexpected:...",
    "Mermaid Man's old comic book collection has a hidden secret:...",
    "Barnacle Boy once bragged, 'I know something you don't...'",
    "The Bikini Bottom Chum Bucket's secret ingredient is something unexpected:...",
    "The Flying Dutchman's treasure map has a hidden clue:..."
]

            file.write(fact)
            combined_text = random.choice(intro_speech) + fact
            print(combined_text)

        # Play the fact using amain
        await amain(combined_text)

        # # Check if the user wants to stop
        # if input("Press 'q' to quit, or any other key to continue: ") == 'q':
        #     break

        interval = random.randint(5, 10)
        print(f"Waiting {interval} seconds...")
        await asyncio.sleep(interval)

if __name__ == "__main__":
    VOICE = "en-GB-RyanNeural"
    OUTPUT_FILE = "test.mp3"
    OUTPUT_DEVICE = "CABLE Input (VB-Audio Virtual Cable)"
    TTS_PITCH = "+25Hz"
    TTS_RATE = "-5%"

    asyncio.run(main())