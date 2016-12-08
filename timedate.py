from datetime import datetime
import optparse

def main():
    now = datetime.now()
    mm = str(now.month)
    dd = str(now.day)
    yy = str(now.year)
    hour = str(now.hour)
    mi = str(now.minute)
    ss = str(now.second)

    parser = optparse.OptionParser()
    parser.add_option('-m','--month', dest='month',action='store_true', help='displays month')
    parser.add_option('-d', '--day', dest='day', action='store_true', help='displays day')
    parser.add_option('-y', '--year', dest='year', action='store_true', help='displays year')
    parser.add_option('-t', '--time', dest='time', action='store_true', help='Displays time')

    (options, args) = parser.parse_args()
    day = options.day
    month = options.month
    year = options.year
    time = options.time

    if options.day :
        print(dd)

    elif options.month :
        print(mm)

    elif options.year :
        print(yy)

    elif options.time :
        print(hour + ":" + mi + ":" + ss)

    else :
        print("Display the correct arguement")
if __name__ == "__main__" :
    main()




