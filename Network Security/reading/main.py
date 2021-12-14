from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
# Go to IMDB Sign In Page
time.sleep(10)
driver.get('https://www.imdb.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fregistration%2Fap-signin-handler%2Fimdb_us&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl91cyIsInJlZGlyZWN0VG8iOiJodHRwczovL3d3dy5pbWRiLmNvbS8_cmVmXz1sb2dpbiJ9&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&tag=imdbtag_reg-20')

driver.find_element_by_id('ap_email').send_keys('aldehf420@naver.com') # Enter Email
driver.find_element_by_id('ap_password').send_keys('na00879090') # Enter PW
driver.find_element_by_id('signInSubmit').click() # Click Sign In button
time.sleep(5) # Wait

fake_reviews = [
	("tt4154796","It was Good",10,"One of the other reviewers has mentioned that after watching just 1 Oz episode you'll be hooked. They are right, as this is exactly what happened with me. The first thing that struck me about Oz was its brutality and unflinching scenes of violence, which set in right from the word GO. Trust me, this is not a show for the faint hearted or timid. This show pulls no punches with regards to drugs, sex or violence. Its is hardcore, in the classic use of the word. It is called OZ as that is the nickname given to the Oswald Maximum Security State Penitentary. It focuses mainly on Emerald City, an experimental section of the prison where all the cells have glass fronts and face inwards, so privacy is not high on the agenda. Em City is home to many..Aryans, Muslims, gangstas, Latinos, Christians, Italians, Irish and more....so scuffles, death stares, dodgy dealings and shady agreements are never far away. I would say the main appeal of the show is due to the fact that it goes where other shows wouldn't dare. Forget pretty pictures painted for mainstream audiences, forget charm, forget romance...OZ doesn't mess around. The first episode I ever saw struck me as so nasty it was surreal, I couldn't say I was ready for it, but as I watched more, I developed a taste for Oz, and got accustomed to the high levels of graphic violence. Not just violence, but injustice (crooked guards who'll be sold out for a nickel, inmates who'll kill on order and get away with it, well mannered, middle class inmates being turned into prison bitches due to their lack of street skills or prison experience) Watching Oz, you may become comfortable with what is uncomfortable viewing....thats if you can get in touch with your darker side."),
	("tt1843866","It was Bad",8,"I thought this was a wonderful way to spend time on a too hot summer weekend, sitting in the air conditioned theater and watching a light-hearted comedy. The plot is simplistic, but the dialogue is witty and the characters are likable (even the well bread suspected serial killer). While some may be disappointed when they realize this is not Match Point 2: Risk Addiction, I thought it was proof that Woody Allen is still fully in control of the style many of us have grown to love. This was the most I'd laughed at one of Woody's comedies in years (dare I say a decade?). While I've never been impressed with Scarlet Johanson, in this she managed to tone down her \"sexy\" image and jumped right into a average, but spirited young woman. This may not be the crown jewel of his career, but it was wittier than \"Devil Wears Prada\" and more interesting than \"Superman\" a great comedy to go see with friends.")
]

for fk in fake_reviews:
	driver.get(f'https://www.imdb.com/title/{fk[0]}/reviews') # Go to movie's Review by Movie's ID
	time.sleep(2)
	driver.find_element_by_class_name('user-reviews').click() # Open Review input tab
	time.sleep(5)
	review_frame = driver.find_element_by_class_name('cboxIframe') 
	driver.switch_to.frame(review_frame) # Move Frame
	
	driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div/div[1]/div[3]/div[1]/div/a[{fk[2]}]').click() # Click Star Point
	driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[5]/div[1]/input').send_keys(fk[1]) # Enter Title
	driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[5]/div[2]/textarea').send_keys(fk[3]) # Enter Description
	driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[5]/div[3]/div/ul/li[2]/span[1]').click() # No spoiler Radio

	driver.switch_to.default_content() # Move default frame
	time.sleep(1)


