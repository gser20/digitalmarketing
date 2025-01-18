campaigns = {}


def create_campaign(clients):
    campaign_id = input("Enter campaign ID: ")
    client_id = input("Enter client ID: ")

    if client_id not in clients:
        print("Client ID does not exist. Please add the client first.")
        return

    campaign_name = input("Enter campaign name: ")
    impressions = int(input("Enter initial impressions: "))
    clicks = int(input("Enter initial clicks: "))
    conversions = int(input("Enter initial conversions: "))

    if campaign_id in campaigns:
        print("Campaign ID already exists. Please use a unique ID.")
    else:
        campaigns[campaign_id] = {
            "client_id": client_id,
            "name": campaign_name,
            "impressions": impressions,
            "clicks": clicks,
            "conversions": conversions
        }
        print("Campaign created successfully!")


def track_campaign_performance():
    campaign_id = input("Enter campaign ID: ")

    if campaign_id not in campaigns:
        print("Campaign ID does not exist.")
        return

    new_impressions = int(input("Enter new impressions: "))
    new_clicks = int(input("Enter new clicks: "))
    new_conversions = int(input("Enter new conversions: "))

    campaigns[campaign_id]["impressions"] = new_impressions
    campaigns[campaign_id]["clicks"] = new_clicks
    campaigns[campaign_id]["conversions"] = new_conversions

    print("Campaign performance updated successfully!")


def generate_report():
    campaign_id = input("Enter campaign ID: ")

    if campaign_id not in campaigns:
        print("Campaign ID does not exist.")
        return

    campaign = campaigns[campaign_id]
    print("Campaign Report:")
    print(f"- Campaign Name: {campaign['name']}")
    print(f"- Impressions: {campaign['impressions']}")
    print(f"- Clicks: {campaign['clicks']}")
    print(f"- Conversions: {campaign['conversions']}")
