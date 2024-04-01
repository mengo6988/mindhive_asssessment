from playwright.sync_api import sync_playwright
import json

from model.outlets import Outlet


def scrape_subway():
    url = "https://www.subway.com.my/find-a-subway"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        search_bar = page.locator("#fp_searchAddress")
        search_bar.fill("Kuala Lumpur")

        submit_button = page.locator("#fp_searchAddressBtn")
        submit_button.click()

        page.wait_for_selector(".fp_listitem", timeout=5000)

        divs = page.query_selector_all("div.fp_listitem")

        results = []

        for div in divs:
            info = div.query_selector(".location_left")
            links = div.query_selector(".location_right").query_selector_all("a")
            name = info.query_selector("h4").inner_text()
            add_box = info.query_selector(".infoboxcontent").query_selector_all("p")
            add_info = [
                x.inner_text()
                for x in add_box
                if not x.get_attribute("class") == "infoboxlink"
                and len(x.inner_text()) != 0
            ]
            # for i, adds in enumerate(add_box):
            #     if len(adds.inner_text()) != 0:
            #         add_info.append(adds.inner_text())

            # address = add_box[0].inner_text()
            # outlet_hours = add_box[2].inner_text()
            lat = div.get_attribute("data-latitude")
            long = div.get_attribute("data-longitude")
            link = links[1].get_attribute("href")
            outlet = {
                "name": str(name),
                "latitude": float(lat),
                "longitude": float(long),
                "waze": str(link),
                "add_info": add_info,
            }
            # outlet = Outlet(name, add_info, link, lat, long)
            results.append(outlet)
            # print(
            #     f"name = {name} | lat = {lat} | long = {long} | {address} | hours: {outlet_hours}"
            # )
            # print(f"lat = {lat}")
            # print(f"long = {long}")
            # print(div.inner_html())
        # print(results)
        return results


if __name__ == "__main__":
    outlets = scrape_subway()
    for i, outlet in enumerate(outlets):
        print(i, outlet)
        if i == 10:
            break
