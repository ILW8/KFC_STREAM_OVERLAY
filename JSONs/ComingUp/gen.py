import io
import csv


# copy this from the ref sheet
# ,stage,id,date,time,red team,,score,,,blue team,referee,streamer,commentator,commentator,mp link,intro json,,,,W,L,ID1,ID2,mp,bans,,,
SHEET_CSV = """
,F,25,Apr 1 (Sat),19:00,seal,•   ✦,,,✦   •,PEKORA LOVERS,[K],Xpekade,Tycani,shiba,,"{""time"": 1680375600000, ""red_team"": ""seal"", ""blue_team"": ""PEKORA LOVERS""}",,L,,,,23,22,,,,,
,F,26,Apr 1 (Sat),14:00,zeisendash,•   ✦,6,2,✦   •,Polish Hunxin,HuTaoMyMommy,affirmedcheese,shiba,Crystal Enjoyer,MP Link,"{""time"": 1680357600000, ""red_team"": ""zeisendash"", ""blue_team"": ""Polish Hunxin""}",,L,,zeisendash,Polish Hunxin,24,21,,,,,
,F,27A,Apr 2 (Sun),03:00,seal,•   ✦,,,✦   •,zeisendash,A secret,ilw8,Tycani,,,"{""time"": 1680404400000, ""red_team"": ""seal"", ""blue_team"": ""zeisendash""}",,P,,,,25,26,,,,,
,F,27B,Apr 2 (Sun),03:00,seal,•   ✦,,,✦   •,Polish Hunxin,A secret,ilw8,Tycani,,,"{""time"": 1680404400000, ""red_team"": ""seal"", ""blue_team"": ""Polish Hunxin""}",,P,,,,25,26,,,,,
,F,27C,Apr 2 (Sun),16:00,PEKORA LOVERS,•   ✦,,,✦   •,zeisendash,A secret,affirmedcheese,Crystal Enjoyer,affirmedcheese,,"{""time"": 1680451200000, ""red_team"": ""PEKORA LOVERS"", ""blue_team"": ""zeisendash""}",,P,,,,25,26,,,,,
,F,27D,Apr 2 (Sun),16:00,PEKORA LOVERS,•   ✦,,,✦   •,Polish Hunxin,A secret,affirmedcheese,Crystal Enjoyer,affirmedcheese,,"{""time"": 1680451200000, ""red_team"": ""PEKORA LOVERS"", ""blue_team"": ""Polish Hunxin""}",,P,,,,25,26,,,,,
,F,28,Apr 1 (Sat),16:00,Hotline Bling,•   ✦,,,✦   •,FLOPINSKI,[K],Xpekade,Crystal Enjoyer,shiba,,"{""time"": 1680364800000, ""red_team"": ""Hotline Bling"", ""blue_team"": ""FLOPINSKI""}",,W,,,,23,24,,,,,
"""

RELEASE_TAG_NAME = "F"


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
