import csv
albums = [('Welcome to my nightmare', 'Alice Cooper', 1975),
          ('Bad company', 'Bad Company', 1974),
          ('NightFlight', 'Budgie', 1981),
          ('More Mainheim', 'Imelda May', 2011),
          ('Ride the Lightening', 'Metallica', 1984),
]

keys = ['album', 'artist', 'year']

filename = 'albums.csv'
with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=keys)  
    writer.writeheader()  
    for row in albums:
        zib_object= zip(keys, row)
        # print(zib_object)
        # for thing in zip(keys, row):
        #     print('\t', thing)
        albums_dict = dict(zib_object)
        print(albums_dict)
        writer.writerow(albums_dict)