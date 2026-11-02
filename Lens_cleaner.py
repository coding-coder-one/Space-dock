telescope_veiw = ["bodes galaxy", "rosette nebula", "turantula nebula", "dust"]
for x in telescope_veiw:
    if "dust" in telescope_veiw:
        telescope_veiw.remove("dust")
        print("dust removed")
    elif x not in telescope_veiw:
        print("not in list")
print(telescope_veiw)
