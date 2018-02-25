from apps.user.models import *
from apps.account.models import *
from apps.account.utils import *
import requests

profile = Profile.objects.last()
Account.objects.all().delete()


def new_account():
		a = Account.objects.create(address="Account-1", profile=profile, category=3)
		broadcast_new_user_account(a)


def new_buyer_account():
		a = Account.objects.create(address="Buyer-1", profile=profile, category=3)
		broadcast_new_user_account(a)


def new_contract():
		c = Account.objects.create(address="Contract-1", contract={"name": "buy"}, category=2)
		broadcast_new_contract(c)


def new_content():
		entities = {
				"content_owner": {
						"address": [Account.objects.filter(category=3).first().address],
						"req": True
				},
				"content": {
						"address": ["Content-1"]
				}
		}
		c = Account.objects.create(address="Content-1", content={"entities": entities, "meta": {}, "actions": {}}, category=1)
		broadcast_new_content(c)


def update_content():
		c = Account.objects.filter(category=1)
		if c:
				c = c[0]
				c.content["actions"] = {
						"buy": {
								"contract": "Contract-1",
								"params": {
										"price": 10
								}
						}
				}
				c.save()
				broadcast_updated_content(c)


new_account()
new_buyer_account()
new_contract()
new_content()
update_content()


def get_all_contents():
		all_contents = requests.get("http://localhost:8000/content/").json()
		print(all_contents)
		return all_contents

all_contents = get_all_contents()

# Search for a content with an action
# for content in all_contents:
for content in all_contents:
		actions = content.get("data", {}).get("content", {}).get("actions")
		for action in actions.keys():
				content_id = content.get("index")
				requests.post("http://localhost:8000/content/{}/{}/".format(content_id, action), json={
						"buyer": "Buyer-1",
				})
				break

