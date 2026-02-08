from app import app


def test_header_present(dash_duo):
	dash_duo.start_server(app)
	dash_duo.wait_for_element("h1", timeout=10)


def test_visualisation_present(dash_duo):
	dash_duo.start_server(app)
	dash_duo.wait_for_element("#pink-morsel-sales-graph", timeout=10)


def test_region_picker_present(dash_duo):
	dash_duo.start_server(app)
	dash_duo.wait_for_element("#region-selector", timeout=10)
