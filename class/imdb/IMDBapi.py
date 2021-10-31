import json
import http.client
import secrets


class IMDB:
    def get_movie(self, imdb_code):
        if (self == 1):
            # --Run using IMDB API
            conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")
            headers = {
                'x-rapidapi-host': "imdb8.p.rapidapi.com",
                'x-rapidapi-key': secrets.imdb_api_key
            }
            conn.request("GET", "/title/get-overview-details?tconst=" + imdb_code, headers=headers)
            data = json.loads(conn.getresponse().read().decode("utf-8"))
            print("Running IMDB API")

        else:
            # --- Testmode
            with open('../../../IMDB/testData.json') as json_file:
                data = json.load(json_file)
            print("pretending to run IMDB API")

        # --- JSON to DICT
        result = {}
        result["year"] = data["title"]["year"]
        result["title"] = data["title"]["title"]
        result["length"] = data["title"]["runningTimeInMinutes"]
        result["rating"] = data["ratings"]["rating"]
        result["genres"] = data["genres"]
        return result
