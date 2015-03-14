from behave import given, when, then
from hamcrest.core import assert_that
from hamcrest.core.core.isequal import equal_to

@given(u"I am on thecatapi's homepage")
def step_homepage(context):
	context.home.go()
	# save this for later use
	context.initial_cat_img_src = context.home.get_cat_image_src()
	
@when(u'I click the "love it" button')
def step_click_love_it(context):
	context.home.get_love_it_button().click()


@then(u'a new cat image should be loaded into the page')
def step_assert_new_cat_image(context):
	context.home.wait_for_image_to_reload(context.initial_cat_img_src)
	assert context.initial_cat_img_src != context.home.get_cat_image_src()