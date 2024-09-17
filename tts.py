import asyncio
import edge_tts
import pygame
import os
import randfacts
import random
import introductions

async def amain(text_content):
    communicate = edge_tts.Communicate(text_content, VOICE, pitch=TTS_PITCH, rate=TTS_RATE) #reads with a pitch
    # communicate = edge_tts.Communicate(text_content, VOICE) #reads with a pitch
    await communicate.save(OUTPUT_FILE)

    # pygame.mixer.init(devicename=OUTPUT_DEVICE) #Outputs audio source to VB Audio Cablle to be catched in OBS as it's own source
    pygame.mixer.init() #Output to default when VB is missing
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
            intro_speech = introductions.get_tts_intro()

            file.write(fact)
            combined_text = random.choice(intro_speech) + fact
            print(combined_text)

        # Play the fact using amain
        await amain(combined_text)

        # # Check if the user wants to stop
        # if input("Press 'q' to quit, or any other key to continue: ") == 'q':
        #     break

        interval = random.randint(1, 5)
        print(f"Waiting {interval} seconds...")
        await asyncio.sleep(interval)

if __name__ == "__main__":
    VOICE = "en-GB-RyanNeural"
    OUTPUT_FILE = "test.mp3"
    OUTPUT_DEVICE = "CABLE Input (VB-Audio Virtual Cable)"
    TTS_PITCH = "+25Hz"
    TTS_RATE = "-5%"

    asyncio.run(main())