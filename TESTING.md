# Pokemon TCG Ireland

Testing of app was ongoing throughout the development process. I used the developer tools in chrome and firefox to test all aspect of the app.

![Preview of website on various devices](documentation/images/responsive-design-screenshot.png)

# Table of Contents

-   [User story testing](#user-story-testing)
    -   [Owner/Admin & Developer goals](#owneradmin--developer-goals)
    -   [First time visitor goals](#first-time-visitor-goals)
    -   [Returning visitor goals](#returning-visitor-goals)
-   [Automated testing](#automated-testing)
    -   [Python](#python)
    -   [HTML](#html)
    -   [CSS](#css)
    -   [JavaScript](#javascript)
-   [Lighthouse testing](#lighthouse-testing)
-   [Manual testing](#manual-testing)
    -   [Header brand](#header-brand)
    -   [Navigation](#navigation)
    -   [Footer](#footer)
    -   [Home Page](#home-page)
    -   [About Us Page](#about-us-page)
    -   [Sign up Page](#sign-up-page)
    -   [Sign in Page](#sign-in-page)
    -   [Log out Page](#log-out-page)
    -   [Profile Page](#profile-page)
    -   [Empty Profile](#empty-profile)
    -   [Edit Info Page](#edit-info-page)
    -   [Edit Profile Page](#edit-profile-page)
    -   [Edit Booking Page](#edit-booking-page)
    -   [Delete Booking Modal](#delete-booking-modal)
    -   [Visit Users Profiles](#visit-users-profiles)
    -   [Book A Class Page](#book-a-class-page)
    -   [Club News Page](#club-news-page)
    -   [News Post Page](#news-post-page)
    -   [Contact Us Page](#contact-us-page)
    -   [Error pages](#error-pages)
-   [Responsive design testing](#responsive-design-testing)
-   [Bugs](#bugs)

# User story testing

# Owner/Admin & Developer goals

<details>

<summary style="font-size: 20px; font-weight: bold;">Results</summary>

| Test                                                                                                                                                                                               | Expected Result                                                             | Pass     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | -------- |
| As a developer I can carry out project planning so that the website has a clear development direction going forward.                                                                               | Project planning completed and plans created                                | &#10004; |
| As a developer I can create user stories and epics so that the projects work is well planned out and prioritised before coding begins.                                                             | User stories and epics created, prioritising must haves etc.                | &#10004; |
| As a developer I can select a colour scheme so that the websites colouring creates a positive user experience and also meets the stakeholders aesthetic goals.                                     | Colour scheme created in line with user story                               | &#10004; |
| As a developer I can select the websites fonts so that I can provide a good user experience, highlighting readability and stakeholder branding goals.                                              | Fonts selected in line with user story                                      | &#10004; |
| As a developer I can construct wire-frames so that I have details of the website layout, features and style before coding begins.                                                                  | Wireframes constructed before coding began                                  | &#10004; |
| As a developer I can create an entity relationship diagram so that I can define all database entities, the information they will store and their relationship to one another.                      | ERD created detailing all models and relationships                          | &#10004; |
| As a developer I can decided on what individual apps my project will contain so that I can separate my code into different apps based on their functionality.                                      | List of apps generated                                                      | &#10004; |
| As a developer I can setup my IDE so that I can develop a Django based project.                                                                                                                    | IDE setup with all necessary modules etc.                                   | &#10004; |
| As a developer I can setup a new Django project and apps so that I can create the basic project structure.                                                                                         | Basic project structure created                                             | &#10004; |
| As a developer I can setup my database so that my data can be stored using the database.                                                                                                           | Both local and online DB created                                            | &#10004; |
| As a developer I can deploy my project to Heroku so that I can confirm correct operation early in the project.                                                                                     | Initial Heroku deployment carried out                                       | &#10004; |
| As a developer I can add styling to the website so that it is visually appealing to the user, easy to use and all content is accessible and readable.                                              | Styled to be visually appealing and has high accessibility scores site wide | &#10004; |
| As a developer I can create custom error templates for common errors so that the user is provided with a safe way to return to our website if an error occurs and the website maintains a good UX. | Error templates created for 400, 401, 403, 404, 500 and 503                 | &#10004; |
| As a developer I can create a robots.txt so that I can control the access search engine crawlers have to parts of my website.                                                                      | Robots.txt created                                                          | &#10004; |
| As a developer I can create an SEO sitemap so that search engine crawlers can effectively crawl and index the pages on my website.                                                                 | Sitemap created from deployed project                                       | &#10004; |
| As a developer I can create a facebook page for marketing, promoting and showcasing my website to potential customers so that I can direct potential customers to my website.                      | Facebook Business page created                                              | &#10004; |
| As a developer I can ensure meta tags keywords etc are used so that the correct content can be easily accessed.                                                                                    | Keyword used in meta tags and in semantic HTML and site text                | &#10004; |
| As a developer I can add comments and docs strings so that at a glance the reader will understand the functions of various elements of the code.                                                   | Comment and doc strings added in all relevant places                        | &#10004; |
| As a developer I can carry out user story testing so that I can confirm the finished project meets the user story requirements.                                                                    | Story testing completed successfully                                        | &#10004; |
| As a developer I can carry out validation of my code so that I can ensure it complies to coding guidelines.                                                                                        | All validation carried out                                                  | &#10004; |
| As a developer I can carry out manual site testing so that I can confirm the correct operation of the website.                                                                                     | Manual testing complete and documented                                      | &#10004; |
| As a developer I can carry out lighthouse testing on all my webpages so that I can assess my websites performance and accessibility.                                                               | Lighthouse testing complete with excelling scores                           | &#10004; |
| As a developer I can carry out responsive design testing so that I can ensure my website works on a variety of screen sizes, from mobile to large desktop.                                         | Responsive testing complete-no issues found                                 | &#10004; |
| As a developer I can add messaging to the website so that I can provide the user with feedback regarding the action they have performed.                                                           | Messaging shown for all user interaction with the website                   | &#10004; |
| As a developer I can carry out wave testing on all my webpages so that my websites accessibility is excellent and free of errors.                                                                  | Wave testing completed, all errors corrected                                | &#10004; |
| As a superuser I can add a product so that I can add products to my online store.                                                                                                                  | Add product functionality available on front and back end                   | &#10004; |
| As a superuser I can edit a product so that I can change the details of an existing product, including name, description, images, price, product code, category and others.                        | Edit product functionality available on front and back end                  | &#10004; |
| As a superuser I can delete a product so that I can remove items which are no longer available to purchase.                                                                                        | Delete product functionality available on front and back end                | &#10004; |
| As a superuser I can perform CRUD operations on user profiles so that I can manage and where applicable delete or edit user profiles.                                                              | Admin panel provides full crud functionality for all user models            | &#10004; |

</details>

# First time visitor goals

<details>

<summary style="font-size: 20px; font-weight: bold;">Results</summary>

| Test                                                                                                                                                                                                   | Expected Result                                                                    | Pass     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- | -------- |
| As a user I can navigate through the website with ease understanding layout and calls to action so that I can make use of the websites various functionality, allowing me to easily purchase products. | Easy to use responsive navbar implemented. Uniform calls to action used site wide  | &#10004; |
| As a user I can view the website on multiple devices with different screen sizes so that I can have an excellent viewing experience regardless of the device I use.                                    | Website is fully responsive from 320px up.                                         | &#10004; |
| As a user I can sign up and create an account so that I can have an account and view my personal profile.                                                                                              | Sign in via allauth implemented.                                                   | &#10004; |
| As a user I can receive a sign up confirmation email so that I can verify my account sign up was successful.                                                                                           | Confirmation email sent on user sign up                                            | &#10004; |
| As a user I can view a home page so that I can be introduced to the store and its products.                                                                                                            | Home page implemented in line with user story                                      | &#10004; |
| As a shopper I can view a list products so that I can choose whats ones I would like to purchase.                                                                                                      | Products page available with multiple filter and sort options                      | &#10004; |
| As a shopper I can click on a product in the list so that I can view full details such as price, features, description, images, warnings, reviews.                                                     | Product details complete and provide full product info                             | &#10004; |
| As a shopper I can quickly and easily view discounted items so that I can take advantage of special offers on items I would like to purchase.                                                          | Sale link available from main nav menu                                             | &#10004; |
| As a shopper I can view the current total of my items in my basket so that I can ensure I do not spend more than expected.                                                                             | Basket total displayed below icon in header                                        | &#10004; |
| As a shopper I can add products to my wish-list so that I can save products that I wish to purchase at a later date.                                                                                   | Wishlist available on user profile, products can be added via product details page | &#10004; |
| As a shopper I can search and sort products so that I can quickly and easily find the products I wish to purchase.                                                                                     | Search bar in header, many filter and sort options available on products page      | &#10004; |
| As a shopper I can sort the list of available products so that I can view products based on a number of criteria such as name price, rating, category, set, expansion.                                 | Sort options available on products page                                            | &#10004; |
| As a shopper I can filter a product category so that I can find items in a specific category.                                                                                                          | Category filtering available via nav menu                                          | &#10004; |
| As a shopper I can sort multiple product categories at the same time so that I can find items in multiple categories at the same time.                                                                 | Sorting available from dropdown on products page                                   | &#10004; |
| As a shopper I can search for products by name and description so that I can find a products which I would like to purchase.                                                                           | Search bar operational and available from header                                   | &#10004; |
| As a shopper I can see my search results and the number of them so that I can see if a product I have searched for is available.                                                                       | Search results displayed including search word and number of results               | &#10004; |
| As a shopper I can select the quantity of a product so that I can purchase the correct number of products.                                                                                             | Quantity selection available on product detail page and from basket                | &#10004; |
| As a shopper I can view the items I have added to my cart so that I can see a summary of my intended purchases.                                                                                        | Basket available from icon, displays all products added                            | &#10004; |
| As a shopper I can change the quantity of items in my shopping bag so that I can make adjustments to the products I wish to purchase before I checkout.                                                | Basket contains quantity adjustment functionality                                  | &#10004; |
| As a shopper I can enter my payment information so that I can pay for my items at checkout.                                                                                                            | Form to enter payment details available on checkout page                           | &#10004; |
| As a shopper I can be sure my information is secure so that I am happy to provide all information to make a purchase.                                                                                  | Stripe secure payment system used                                                  | &#10004; |
| As a shopper I can view my order confirmation after checkout so that I can ensure my order is correct.                                                                                                 | Order confirmation displayed upon successful checkout                              | &#10004; |
| As a shopper I can receive a confirmation emails after a purchase so that I know my order has been placed and I have a copy of my purchases.                                                           | Confirmation email sent upon successful purchase                                   | &#10004; |
| As a user I can see messages whenever I perform an action so that I can know if my actions were successful, caused errors etc.                                                                         | Messaging implemented site wide for all user actions                               | &#10004; |

</details>

# Returning visitor goals

<details>

<summary style="font-size: 20px; font-weight: bold;">Results</summary>

| Test                                                                                                                                           | Expected Result                                                            | Pass     |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------- |
| As a user I can click on the website social links in the footer so that I can visit the stores various social networks and interact with them. | Social icons available from footer and open social networks in new tab     | &#10004; |
| As a user I can login so that I can access my account, order history etc.                                                                      | Returning user can login and access their account, view order history etc. | &#10004; |
| As a user I can logout so that I can no longer access my account and associated functionality.                                                 | Log out functionality implemented using allauth                            | &#10004; |
| As a user I can recover my password so that regain access to my personal account.                                                              | Password recovery available from log in menu                               | &#10004; |
| As a user I can view my profile page so that I can edit my account info (address etc.).                                                        | Profile page displays all user info                                        | &#10004; |
| As a user I can edit all of my profile details so that keep my account information up to date.                                                 | Profile allows editing of user and shipping info, as well as password      | &#10004; |
| As a user I can edit my password so that I can keep my account secure.                                                                         | Password can be changed from user profile                                  | &#10004; |
| As a user I can view my order history so that I can check items which I have previously purchased.                                             | Order history available on user profile                                    | &#10004; |
| As a user I can view my wish-list so that I can purchase item which I saved to it earlier.                                                     | Wishlist functionality implemented                                         | &#10004; |
| As a user I can I can sign up to the newsletter so that I can be kept up to date with the latest product releases and offers.                  | Newsletter signup in footer                                                | &#10004; |
| As a user I can view the websites privacy policy so that I can understand how my information is used.                                          | Privacy policy available from footer                                       | &#10004; |
| As a user I can view an about us page so that I can learn all about the company.                                                               | About up page available from the footer                                    | &#10004; |
| As a user I can fill out a contact form so that I can communicate with the website owner directly.                                             | Contact form working, from content sent to admin via backend model         | &#10004; |
| As a user I can submit a review on a product so that other site users can quickly gauge my opinion of the product.                             | Review functionality implemented                                           | &#10004; |

</details>

[Return to Table of Contents](#table-of-contents)
[Return to README.md](README.md)

# Automated testing

## Python

The [Code institutes Pep8 linter](https://pep8ci.herokuapp.com/) was used to ensure the python code conformed to Pep8 style guidelines. The results of these can be seen below.

<details>

<summary style="font-size: 20px; font-weight: bold;">About us URL's</summary>

![About us URL's](/documentation/testing/validation/python/about-us-urls-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">About us Views</summary>

![About us Views](/documentation/testing/validation/python/about-us-views-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Basket Context</summary>

![Basket Context](/documentation/testing/validation/python/basket-context-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Basket URL's</summary>

![Basket URL's](/documentation/testing/validation/python/basket-urls-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Basket Views</summary>

![Basket Views](/documentation/testing/validation/python/basket-views-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Checkout Admin</summary>

![Checkout Admin](/documentation/testing/validation/python/checkout-admin-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Checkout Forms</summary>

![Checkout Forms](/documentation/testing/validation/python/checkout-forms-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Checkout Models</summary>

![Checkout Models](/documentation/testing/validation/python/checkout-models-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Checkout Signals</summary>

![Checkout Signals](/documentation/testing/validation/python/checkout-signals-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Checkout URL's</summary>

![Checkout URL's](/documentation/testing/validation/python/checkout-urls-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Checkout Views</summary>

![Checkout Views](/documentation/testing/validation/python/checkout-views-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Checkout Webhook Handler</summary>

![Checkout Webhook Handler](/documentation/testing/validation/python/checkout-webhook-handler-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Checkout Webhooks</summary>

![Checkout Webhooks](/documentation/testing/validation/python/checkout-webhooks-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Contact Us Admin</summary>

![Contact Us Admin](/documentation/testing/validation/python/contact-us-admin-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Contact Us Forms</summary>

![Contact Us Forms](/documentation/testing/validation/python/contact-us-forms-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Contact Us Models</summary>

![Contact Us Models](/documentation/testing/validation/python/contact-us-models-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Contact Us URL's</summary>

![Contact Us URL's](/documentation/testing/validation/python/contact-us-urls-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Contact Us Views</summary>

![Contact Us Views](/documentation/testing/validation/python/contact-us-views-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Home URL's</summary>

![Home URL's](/documentation/testing/validation/python/home-url-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Home Views</summary>

![Home Views](/documentation/testing/validation/python/home-views-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Main Settings</summary>

![Main Settings](/documentation/testing/validation/python/main-settings-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Main URL's</summary>

![Main URL's](/documentation/testing/validation/python/main-urls-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Main Views</summary>

![Main Views](/documentation/testing/validation/python/main-views-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Privacy Policy URL's</summary>

![Privacy Policy URL's](/documentation/testing/validation/python/privacy-policy-urls-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Privacy Policy Views</summary>

![Privacy Policy Views](/documentation/testing/validation/python/privacy-policy-views-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Products Admin</summary>

![Products Admin](/documentation/testing/validation/python/products-admin-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Products Forms</summary>

![Products Forms](/documentation/testing/validation/python/products-forms-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Products Models</summary>

![Products Models](/documentation/testing/validation/python/products-models-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Products URLS</summary>

![Products URLS](/documentation/testing/validation/python/products-urls-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Products Views</summary>

![Products Views](/documentation/testing/validation/python/products-views-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Products Widgets</summary>

![Products Widgets](/documentation/testing/validation/python/products-widgets-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Profiles Admin</summary>

![Profiles Admin](/documentation/testing/validation/python/profiles-admin-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Profile Forms</summary>

![Profile Forms](/documentation/testing/validation/python/profiles-forms-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Profile Models</summary>

![Profile Models](/documentation/testing/validation/python/profiles-models-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Profile URL's</summary>

![Profile URL's](/documentation/testing/validation/python/profiles-urls-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Profile Views</summary>

![Profile Views](/documentation/testing/validation/python/profiles-views-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Wishlist Admin</summary>

![Wishlist Admin](/documentation/testing/validation/python/wishlist-admin-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Wishlist Models</summary>

![Wishlist Models](/documentation/testing/validation/python/wishlist-models-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Wishlist URL's</summary>

![Wishlist URL's](/documentation/testing/validation/python/wishlist-urls-pep8ci.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Wishlist Views</summary>

![Wishlist Views](/documentation/testing/validation/python/wishlist-view-pep8ci.png)

</details>

## HTML

The automated testing of this projects HTML code was carried out using [Validator w3](https://validator.w3.org/nu/), the results are shown below,

<details>

<summary style="font-size: 20px; font-weight: bold;">Results</summary>

| Page                                                                                                                                                                                              | Pass     | Note  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ----- |
| [Index](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2F)                                                                          | &#10004; |       |
| [Products](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fproducts%2F)                                                                           | &#10004; |       |
| [Product details](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fproducts%2F2%2F)                                                                | &#10004; | error |
| [Add product](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fproducts%2Fadd%2F)                                                   | &#10004; |       |
| [Edit product](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fproducts%2Fedit%2F62%2F)                                                           | &#10004; |       |
| [Basket](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fbasket%2F)                                                                | &#10004; |       |
| [Checkout](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fcheckout%2F)                                                                           | &#10004; |       |
| [Checkout success](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fcheckout%2Fcheckout_success%2F2543D203B41D4F24B9A926EDFD6A7474) | &#10004; |       |
| [Profile](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fprofiles%2F)                                                             | &#10004; |       |
| [Order history](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fprofiles%2Forder_history%2F2A6469C5547F4CF09CD5F0FEA4BBDE3C%2F)    | &#10004; |       |
| [Login](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Faccounts%2Flogin%2F)                                                       | &#10004; |       |
| [Log out](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Faccounts%2Flogout%2F)                                                    | &#10004; |       |
| [Register](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Faccounts%2Fsignup%2F)                                                   | &#10004; |       |
| [About us](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fabout_us%2Fabout_us%2F)                                                 | &#10004; |       |
| [Contact_us](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fcontact_us%2Fcontact%2F)                                              | &#10004; |       |
| [Privacy Policy](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fprivacy_policy%2Fprivacy_policy%2F)                               | &#10004; |       |

</details>
