from playwright.sync_api import sync_playwright

from utils.config import google_url_es, session_path
from utils.utils import (
    get_cookies,
    store_cookies,
    path_exists,
    read_input,
    generate_inputs_search,
    check_gdpr,
    generate_inputs_search_stop_words,
    store_output,
)


def main():
    with sync_playwright() as playWright:
        words_input = read_input()
        browser = playWright.chromium.launch(headless=False)
        context = browser.new_context(no_viewport=True, bypass_csp=True)

        if path_exists(session_path):
            context.add_cookies(get_cookies())

        page = context.new_page()
        page.goto(google_url_es)
        check_gdpr(page)
        input = page.query_selector("[aria-label='Buscar']")
        list_output = []
        for word in words_input:
            print(f"Working on: {word}")
            terms_search = generate_inputs_search(word) + generate_inputs_search_stop_words(word)
            for term in terms_search:
                input.fill(term)
                page.wait_for_timeout(100)
                suggested_search = page.query_selector("[role='presentation']")
                suggested = suggested_search.query_selector_all("li")
                list_output += list(filter(lambda x: x not in list_output, [item.inner_text() for item in suggested]))

        store_output(list_output)

        store_cookies(context.cookies())
        browser.close()


if __name__ == "__main__":
    main()
