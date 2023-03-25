import io
import csv


# copy this from the ref sheet
# ,stage,id,date,time,red team,,score,,,blue team,referee,streamer,commentator,commentator,mp link,intro json,,,,W,L,ID1,ID2,mp,bans,,,
SHEET_CSV = """
,SF,17,Mar 25 (Sat),19:00,plink,•   ✦,,,✦   •,[K] then...,Miku Hatsune,Xpekade,Crystal Enjoyer,,,"{""time"": 1679770800000, ""red_team"": ""plink"", ""blue_team"": ""[K] then...""}",,L,,,,13,12,,,,,
,SF,18,Mar 25 (Sat),15:00,Polish Hunxin,•   ✦,,,✦   •,sco gla,Suicune3,Xpekade,,,107574824,"{""time"": 1679756400000, ""red_team"": ""Polish Hunxin"", ""blue_team"": ""sco gla""}",,L,,,,14,11,https://osu.ppy.sh/mp/107574824,HR2,NM3,HD2,
,SF,19,Mar 25 (Sat),15:00,PEKORA LOVERS,•   ✦,,,✦   •,DJ EBAN KFC ORDER,A secret,Kasumi-sama,,,107574754,"{""time"": 1679756400000, ""red_team"": ""PEKORA LOVERS"", ""blue_team"": ""DJ EBAN KFC ORDER""}",,L,,,,15,10,https://osu.ppy.sh/community/matches/107574754,NM4,DT1,,
,SF,20,Mar 25 (Sat),19:00,Church's Chicken,•   ✦,,,✦   •,Blue Pants,[K],ilw8,,,,"{""time"": 1679770800000, ""red_team"": ""Church's Chicken"", ""blue_team"": ""Blue Pants""}",,L,,,,16,9,,,,,
,SF,21A,Mar 26 (Sun),04:00,plink,•   ✦,,,✦   •,Polish Hunxin,,ilw8,,,,"{""time"": 1679803200000, ""red_team"": ""plink"", ""blue_team"": ""Polish Hunxin""}",,P,,,,18,17,,,,,
,SF,21B,Mar 26 (Sun),19:00,plink,•   ✦,,,✦   •,sco gla,freddiiieeee,Xpekade,,,,"{""time"": 1679857200000, ""red_team"": ""plink"", ""blue_team"": ""sco gla""}",,P,,,,18,17,,,,,
,SF,21C,Mar 26 (Sun),15:00,[K] then...,•   ✦,,,✦   •,Polish Hunxin,,ilw8,,,,"{""time"": 1679842800000, ""red_team"": ""[K] then..."", ""blue_team"": ""Polish Hunxin""}",,P,,,,18,17,,,,,
,SF,21D,Mar 26 (Sun),19:00,[K] then...,•   ✦,,,✦   •,sco gla,freddiiieeee,Xpekade,,,,"{""time"": 1679857200000, ""red_team"": ""[K] then..."", ""blue_team"": ""sco gla""}",,P,,,,18,17,,,,,
,SF,22A,Mar 26 (Sun),18:00,PEKORA LOVERS,•   ✦,,,✦   •,Church's Chicken,A secret,affirmedcheese,affirmedcheese,Crystal Enjoyer,,"{""time"": 1679853600000, ""red_team"": ""PEKORA LOVERS"", ""blue_team"": ""Church's Chicken""}",,P,,,,20,19,,,,,
,SF,22B,Mar 26 (Sun),18:00,PEKORA LOVERS,•   ✦,,,✦   •,Blue Pants,A secret,affirmedcheese,affirmedcheese,Crystal Enjoyer,,"{""time"": 1679853600000, ""red_team"": ""PEKORA LOVERS"", ""blue_team"": ""Blue Pants""}",,P,,,,20,19,,,,,
,SF,22C,Mar 26 (Sun),16:00,DJ EBAN KFC ORDER,•   ✦,,,✦   •,Church's Chicken,Kasumi-sama,Kasumi-sama,,,,"{""time"": 1679846400000, ""red_team"": ""DJ EBAN KFC ORDER"", ""blue_team"": ""Church's Chicken""}",,P,,,,20,19,,,,,
,SF,22D,Mar 26 (Sun),16:00,DJ EBAN KFC ORDER,•   ✦,,,✦   •,Blue Pants,Kasumi-sama,Kasumi-sama,,,,"{""time"": 1679846400000, ""red_team"": ""DJ EBAN KFC ORDER"", ""blue_team"": ""Blue Pants""}",,P,,,,20,19,,,,,
,SF,23,Mar 26 (Sun),19:00,Hotline Bling,•   ✦,,,✦   •,seal,[K],affirmedcheese,affirmedcheese,Crystal Enjoyer,,"{""time"": 1679857200000, ""red_team"": ""Hotline Bling"", ""blue_team"": ""seal""}",,W,,,,13,14,,,,,
,SF,24,Mar 25 (Sat),14:00,FLOPINSKI,•   ✦,6,0,✦   •,zeisendash,[K],Rainbowtaves,,,107573344,"{""time"": 1679752800000, ""red_team"": ""FLOPINSKI"", ""blue_team"": ""zeisendash""}",,W,,FLOPINSKI,zeisendash,15,16,https://osu.ppy.sh/community/matches/107573344,HR2,DT2,HR3,DT3
"""

RELEASE_TAG_NAME = "SF"


def generate():
    with io.StringIO(SHEET_CSV) as string_input:
        string_input.readline()  # skip first empty line
        csv_reader = csv.reader(string_input)
        for row in csv_reader:
            # dump json to file
            with open(f"{row[2]}.json", "w") as outfile:
                outfile.write(row[16])

            # print Markdown table
            print(f"| {row[2]} | {row[3]} {row[4]} | [download](https://github.com/ILW8/KFC_STREAM_OVERLAY/releases/download/{RELEASE_TAG_NAME}/{row[2]}.json) |")


if __name__ == "__main__":
    generate()
