import pygame

print("Setup Start")
pygame.init()
window = pygame.display.set_mode(size=(600, 450))
print("Setup Finish")

print("Loop Start")

while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close the window
            quit()  # Finish the pygame
