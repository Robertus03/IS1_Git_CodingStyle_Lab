import pygame,random
pygame.init()
def f():
 return [[(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for _ in range(10)] for _ in range(10)]
s=pygame.display.set_mode((500,500));pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)");data=f();r=True
while r:
 s.fill((0,0,0))
 for y in range(20):
  for x in range(10):pygame.draw.rect(s,data[y][x],(x*50,y*50,50,50))
 pygame.display.flip()
 for e in pygame.event.get():
  r=False if e.type==pygame.QUIT else r;data=f() if e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE else data
pygame.quit()
