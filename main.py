from PIL import Image, ImageDraw, ImageFont
import calendar
import datetime
now = datetime.datetime.now()

daysInMonth = calendar.monthrange(now.year, now.month)[1]
daySize = (90, 76);
txt = Image.new('RGB', (640,384),"white")

# get a font
DayNumber = ImageFont.truetype('arial.ttf', 20)
event = ImageFont.truetype('arial.ttf', 10)

# get a drawing context
d = ImageDraw.Draw(txt)
weekcount = -1
for daycount in range(0,daysInMonth-1):
    day = daycount+1
    if daycount%7 == 0:
        print(daycount%7)
        weekcount += 1
    dayPosition = ((daycount%7)*daySize[0], weekcount*daySize[1])
    print(dayPosition)
    dayRectCord = [dayPosition, (dayPosition[0]+daySize[0], dayPosition[1]+daySize[1])]
    d.rectangle(dayRectCord, outline=(0, 0, 0))
    sDayNumber = d.textsize(str(day), font=DayNumber)
    d.text(dayPosition, str(day), font=DayNumber, fill=(0, 0, 0))
    d.text((dayPosition[0]+sDayNumber[0]+2, dayPosition[1]+5), "Meeting with x", font=event, fill=(0, 0, 0))


txt.show()
