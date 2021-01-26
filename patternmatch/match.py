import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def match(target, template, threshold):
    print(f'Start finding {template} in {target}')
    img_rgb = cv.imread(target)
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    
    template_rgb = cv.imread(template)
    template = cv.cvtColor(template_rgb, cv.COLOR_BGR2GRAY)
    
    w, h = template.shape[::-1]
    
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    
    # Set threshold to 0.95 for app galary icons
    # hreshold = 1
    
    loc = np.where( res >= threshold)
    
    if loc[0].size <= 0:
        print('Pattern Not Found')
    else:
        for pt in zip(*loc[::-1]):
            cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
        print(f'Template found at {pt}')
    
    cv.imshow('template',template_rgb)
    cv.imshow('target',img_rgb)
    cv.waitKey(0)

# match('appgalary.png', 'template_phone.png', 0.95)

# pending = np.array([['appgalary.png', 'template_phone.png', 0.95],
#            ['appgalary.png', 'template_theme.png', 0.95],
#            ['bluetooth.png', 'template_bluetooth.png', 0.95],
#            ['controlpanel.png', 'template_bluetooth2.png', 0.95],
#            ['main.png', 'template_phone.png', 0.95]])

# for case in pending:
#     threshold = case[2].astype(np.float)
#     match(case[0], case[1], threshold)

match('2app.png', 'template_phone.png', 0.65)