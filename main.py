import requests
import matplotlib.pyplot as plt

response = requests.get('https://monolithtracker.com/json-export')
data = response.json()

for item in data[0]:

  arraydata = []
  output = []

  labels = []
  sizes = []

  notallowed = ["nid","uuid","vid","langcode","type","revision_timestamp","revision_uid","revision_log","uid","status","title","created","changed","promote","sticky","revision_translation_affected","moderation_state","content_translation_source","content_translation_outdated","body","field_articles_media","field_disappearance_date","field_height","field_location","field_monolith_image","field_multiple_monoliths","field_notes","field_related_monoliths","field_spotted_date","field_text_symbols","defualt_langcode"]

  if item is item in notallowed:
    continue;
  else:
    collecting=item

  for number in range(0,len(data)):
    if (len(data[number][collecting]))==0:
      arraydata.append("No Data")
    if (len(data[number][collecting]))>=1:
      arraydata.append(data[number][str(collecting)][0]["value"])

  for x in arraydata:
    if x not in output:
          output.append(x)

  for i in output:
    sizes.append(arraydata.count(i)/len(data))
    labels.append(str(i)+"\n"+str(round(arraydata.count(i)/len(data)*100,2))+"%")

  fig1, ax1 = plt.subplots()
  fig1.suptitle('Monolith Tracker '+collecting+' data availability', fontsize=16)
  ax1.pie(sizes, labels=labels,shadow=False, startangle=90, labeldistance=1.1)
  ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

  #for number in range(0,len(output)):
    #print(labels[number],(round(sizes[number],5)*100),"%")

  plt.savefig(fname='plots/'+collecting)
