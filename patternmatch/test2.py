import numpy as np

pending = np.array([['appgalary.png', 'template_phone.png', 0.95],
           ['appgalary.png', 'template_theme.png', 0.95],
           ['bluetooth.png', 'template_bluetooth.png', 0.95],
           ['controlpanel.png', 'template_bluetooth2.png', 0.95],
           ['main.png', 'template_phone.png', 0.95]])

for case in pending:
    print(case[0], case[1], case[2])
    print(type(case[2]))