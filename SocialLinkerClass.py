import json


def write_json(data, filename='test.json'):
    with open(filename, "w") as outfile:
        json.dump(data, outfile)


def get_new_id(uid):
    inp = {
        "id": uid,
        "twitch_link": "",
        "twitter_link": "",
        "groups": ""
    }
    return inp


class SocialLinker:
    def __init__(self, json_key, link_comparator):
        self.key = json_key
        self.link_comparator = link_comparator

    # Returns True on success
    def create_link(self, ctx, link):
        file_users = open("test.json")
        users = json.load(file_users)
        file_users.close()
        user_found = False

        if self.link_comparator in link:
            for keyval in users['members']:
                if str(ctx.author.id) == str(keyval['id']):
                    keyval[self.key] = link
                    user_found = True
                    break

            if not user_found:
                new_entry = get_new_id(ctx.author.id)
                new_entry[self.key] = link
                users['members'].append(new_entry)

            write_json(users)
            return True
        else:
            return False

    def retrieve_link(self, ctx, member_id):
        file_users = open("test.json")
        users = json.load(file_users)
        file_users.close()

        for keyval in users['members']:
            if str(member_id) == str(keyval['id']):
                if len(keyval[self.key]) == "":
                    return None
                else:
                    return keyval[self.key]

        return None
