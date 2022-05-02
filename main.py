import tkinter as tk
import requests
win = tk.Tk()
try:
  def get_weather():
    city = cityInput.get()
    key='3b557df1ad7d0220a04961bb4d1186e4'
    url= 'http://api.openweathermap.org/data/2.5/weather'
    query = {'q': city ,'units': 'metric', 'type': 'like', 'APPID': key}
    res = requests.get(url, params=query)
    #pieprasa datus no laikapstaklu vietnes, ar savu atslēgu
    #dabū datus json veidā, paņem tikai vajadzīgos un attēlo saskarnē
    #izmantotā datu stuktūra vārdnīca, piekļūst datu vērtībām caur atslēgu
    data = res.json()
    print(data)
    print("conditions:", data['weather'][0]['description'])
    print("temp:", data['main']['temp'])
    print("temp_min:", data['main']['temp_min'])
    print("temp_max:", data['main']['temp_max'])
    title1['text'] = f'{str(data["name"])}: {data["main"]["temp"]}'
except Exception as e:
    print("Exception (weather):", e)
    pass
win.geometry(f"400x300+10+20")
win['bg'] = '#7C51A0'
win.title('Laikapstākļi')
win.wm_attributes('-alpha', 0.9)
frame1 = tk.Frame(win, bg = 'orange')
frame1.place(relx=0.15, rely=0.15, relwidth = 0.7, relheight=0.20)
frame2 = tk.Frame(win, bg = 'orange')
frame2.place(relx=0.15, rely=0.55, relwidth = 0.7, relheight=0.10)
cityInput = tk.Entry(frame1, bg='white')
cityInput.pack()
btn = tk.Button(frame1, text='Skatīties laikapstākļus', bg='yellow', command=get_weather)
btn.pack()
title1 = tk.Label(frame2, text='Laikapstaklu informacija', bg = 'orange')
title1.pack()
win.mainloop()



