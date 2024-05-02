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
    -   [Navigation (header and footer)](#navigation-header-and-footer)
    -   [Home Page](#home-page)
    -   [About Us Page](#about-us-page)
    -   [Sign up Page](#sign-up-page)
    -   [Sign in Page](#sign-in-page)
    -   [Log out Page](#log-out-page)
    -   [Profile Page](#profile-page)
    -   [Order History Page](#order-history-page)
    -   [Products Page](#products-page)
    -   [Product Details Page](#product-details-page)
    -   [Add Product Page](#add-product-page)
    -   [Edit Product Page](#edit-product-page)
    -   [Basket page](#basket-page)
    -   [Checkout Page](#checkout-page)
    -   [Checkout Success Page](#checkout-success-page)
    -   [Privacy Policy Page](#privacy-policy-page)
    -   [Contact Us Page](#contact-us-page)
    -   [Error pages](#error-pages)
    -   [Password reset page](#password-reset-page)
    -   [Password change page](#password-change-page)
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

| Page                                                                                                                                                                                              | Pass     | Note                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | -------------------------------- |
| [Index](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2F)                                                                          | &#10004; |                                  |
| [Products](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fproducts%2F)                                                                           | &#10004; |                                  |
| [Product details](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fproducts%2F2%2F)                                                                | &#10004; | error                            |
| [Add product](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fproducts%2Fadd%2F)                                                   | &#10004; | error if pasted from view source |
| [Edit product](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fproducts%2Fedit%2F62%2F)                                                           | &#10004; | error if pasted from view source |
| [Basket](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fbasket%2F)                                                                | &#10004; |                                  |
| [Checkout](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fcheckout%2F)                                                                           | &#10004; |                                  |
| [Checkout success](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fcheckout%2Fcheckout_success%2F2543D203B41D4F24B9A926EDFD6A7474) | &#10004; |                                  |
| [Profile](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fprofiles%2F)                                                             | &#10004; | error if pasted from view source |
| [Order history](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fprofiles%2Forder_history%2F2A6469C5547F4CF09CD5F0FEA4BBDE3C%2F)    | &#10004; |                                  |
| [Login](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Faccounts%2Flogin%2F)                                                       | &#10004; |                                  |
| [Log out](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Faccounts%2Flogout%2F)                                                    | &#10004; |                                  |
| [Register](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Faccounts%2Fsignup%2F)                                                   | &#10004; |                                  |
| [About us](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fabout_us%2Fabout_us%2F)                                                 | &#10004; |                                  |
| [Contact_us](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fcontact_us%2Fcontact%2F)                                              | &#10004; |                                  |
| [Privacy Policy](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fpokemon-tcg-ireland-ad52d37e70f9.herokuapp.com%2Fprivacy_policy%2Fprivacy_policy%2F)                               | &#10004; |                                  |

</details>

The error which occurred on the product details page when validating the html code has nothing to do with my code. This error was produced by the |safe. When the safe filter is applied to the product description the error gets introduced because the safe filter adds an addition closing p tag. When the safe filter is not used there are no errors on the HTML page. I tried various methods to work around this trying to target the description with JavaScript and modify it, trying to make it safe in the view first and sanitising it using bleach before it was sent to the template, trying various filters such as striptags, but did not have any success with this. The issue with this was that if I did not use the safe filter on the description, it would display with all of the element tags that summernote adds to it when it is created in the editor. I discussed this issue with my mentor and cohort facilitator and they advised that it would be ok to leave in as the error is not introduced by any code I wrote. Due to the fact that the safe filter is so important to the functionality of my website I agreed and left it in, as without it the product description would not be readable.

When I inspected the pages in my browser, selected view source and then copied the source code directly into the HTML checker it flagged an error on the profile page and errors on the add and edit product pages.
The error on the profile page was caused by how crispy forms renders the password change form tips. I had this issue with my last project as well and again like then I was advised that it was fine to leave in the code, as the issue was not in code I wrote. The issues is caused because it places a ul inside a small element when rendering the password tips. I tried to combat this by viewing the source code, extracting the form that crispy forms renders and then fixing the issue by changing the small to a div. When I did this, although the form worked correctly it lost its validation. This was due to the fact that it was no longer being created based on the allauth form. Due to this and after discussion with my mentor I decided that I would leave the crispy form library code as it was and put up with the validation error as the validation functionality gained by using the allauth form to generate the sign in form outweighed it.

The errors flagged on the edit and add product page were caused by the summernote editor and again had nothing to do with my code. If I removed the line of code from my view that sets the description as a summernote widget (description = forms.CharField(widget=SummernoteWidget()) there were no errors on either page. Again the issue here is that I needed the text editor on the front end to allow the admin to add and edit products. If I removed the summernote editor and displayed a simple charfield, all the tags would be shown from its creation in summernote and the admin would not be able to edit or add products correctly. Again I discussed this with my mentor and facilitator and they advised that it was fine to leave in and would not effect my grade as it is not caused by any code I wrote.

## CSS

The projects CSS was validated using [W3C CSS validator](https://jigsaw.w3.org/css-validator/). The projects code was input manually into the validator under the advice of my mentor. My css passed with no errors or warnings and the test results can be seen below.

<details>

<summary style="font-size: 20px; font-weight: bold;">Checkout</summary>

![CSS test results checkout](/documentation/testing/validation/css/checkout-css-validation.png).

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Profile</summary>

![CSS test results profile](/documentation/testing/validation/css/profile-css-validation.png).

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Styles</summary>

![CSS test results styles](/documentation/testing/validation/css/styles-css-validation.png).

</details>

## JavaScript

The projects JavaScript was testing using [jshint](https://jshint.com/). The code passed with no errors. I piece of JavaScript did display a warning which was that Functions declared within loops referencing an outer scoped variable may lead to confusing semantics. I updated my code to use let instead of var to ensure the code would behave correctly but the warning was still shown. I discussed this issue with my mentor and was advised that it was only a warning and once the code worked correctly and I mentioned it in this readme I could Ignore it. The results can be seen below.

<details>

<summary style="font-size: 20px; font-weight: bold;">Add & Edit product, image script</summary>

![JavaScript results image script](/documentation/testing/validation/js/add-edit-product-img-script-validation.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Base, mailchimp and toast scripts</summary>

![JavaScript results mailchimp and toast scripts](/documentation/testing/validation/js/base-mailchimp-toast-script-validation.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Basket, button control script</summary>

![JavaScript results button control script](/documentation/testing/validation/js/basket-button-control-script-validation.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Checkout, icon collapse script</summary>

![JavaScript results icon collapse script](/documentation/testing/validation/js/checkout-icon-collapse-script-validation.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Product card, buttons script</summary>

![JavaScript results buttons script](/documentation/testing/validation/js/product-card-btns-js-validation.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Products script</summary>

![JavaScript products script](/documentation/testing/validation/js/products-script-validation.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Stripe elements JS file</summary>

![JavaScript results Stripe elements](/documentation/testing/validation/js/stripe-elements-js-validation.png)

</details>

[Return to Table of Contents](#table-of-contents)
[Return to README.md](README.md)

# Lighthouse testing

Lighthouse testing was carried out using chrome developer tools. Overall scores we excellent with accessibility, best practices and SEO almost 100% across all pages. On mobile the scores for performance were less impressive but I was still very happy with them. There were 2 pages on mobile that score lower than others due to their use of the summernote editor. Again this was a requirement for the websites functionality and there was very little I could do to improve it. Summernote editor was also originally on the contact us page and scored around 60% for performance, so to prove a point I removed it as it was not necessary for the functionality of that page. The pages score for performance increased to almost 90% without it. To improve my scores I did the following

-   Reduced the image size from 1200px X 1200px to 500px by 500px
-   Compressing the images multiple times.
-   Using block tags to remove the lightbox css and related scripts from base and only using them in html files that require them.
-   Carried out extensive wave testing and made improvement to ensure no errors were present from an accessibility point of view.
-   Carried out a lot of work to ensure the SEO of the site was excellent. This is detailed in the Marketing section of the read me document.

## Desktop

<details>

<summary style="font-size: 20px; font-weight: bold;">About Us</summary>

![About Us lighthouse desktop](/documentation/testing/lighthouse/desktop/about-us-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Add Product</summary>

![Add Product lighthouse desktop](/documentation/testing/lighthouse/desktop/add-product-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Basket</summary>

![Basket lighthouse desktop](/documentation/testing/lighthouse/desktop/basket-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Checkout</summary>

![Checkout lighthouse desktop](/documentation/testing/lighthouse/desktop/checkout-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Checkout Success</summary>

![Checkout Success lighthouse desktop](/documentation/testing/lighthouse/desktop/checkout-success-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Contact Us</summary>

![Contact Us lighthouse desktop](/documentation/testing/lighthouse/desktop/contact-us-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;"> Edit Product</summary>

![Edit Product< lighthouse desktop](/documentation/testing/lighthouse/desktop/edit-product-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Index</summary>

![Index lighthouse desktop](/documentation/testing/lighthouse/desktop/index-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Login</summary>

![Login lighthouse desktop](/documentation/testing/lighthouse/desktop/log-in-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Logout</summary>

![Logout lighthouse desktop](/documentation/testing/lighthouse/desktop/log-out-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Order History</summary>

![Order History lighthouse desktop](/documentation/testing/lighthouse/desktop/order-history-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Privacy Policy</summary>

![Privacy Policy lighthouse desktop](/documentation/testing/lighthouse/desktop/privacy-policy-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Product Details</summary>

![Product Details lighthouse desktop](/documentation/testing/lighthouse/desktop/product-detail-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Products</summary>

![Products lighthouse desktop](/documentation/testing/lighthouse/desktop/products-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Profile</summary>

![Profile lighthouse desktop](/documentation/testing/lighthouse/desktop/profile-desktop-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Register</summary>

![Register lighthouse desktop](/documentation/testing/lighthouse/desktop/register-desktop-lighthouse.png)

</details>

## Mobile

<details>

<summary style="font-size: 20px; font-weight: bold;">About Us</summary>

![About Us lighthouse mobile](/documentation/testing/lighthouse/mobile/about-us-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Add Product</summary>

![Add Product lighthouse mobile](/documentation/testing/lighthouse/mobile/add-product-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Basket</summary>

![Basket lighthouse mobile](/documentation/testing/lighthouse/mobile/basket-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Checkout</summary>

![Checkout lighthouse mobile](/documentation/testing/lighthouse/mobile/checkout-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Checkout Success</summary>

![Checkout Success lighthouse mobile](/documentation/testing/lighthouse/mobile/checkout-success-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Contact Us</summary>

![Contact Us lighthouse mobile](/documentation/testing/lighthouse/mobile/contact-us-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;"> Edit Product</summary>

![Edit Product< lighthouse mobile](/documentation/testing/lighthouse/mobile/edit-product-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Index</summary>

![Index lighthouse mobile](/documentation/testing/lighthouse/mobile/index-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Login</summary>

![Login lighthouse mobile](/documentation/testing/lighthouse/mobile/log-in-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Logout</summary>

![Logout lighthouse mobile](/documentation/testing/lighthouse/mobile/log-out-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Order History</summary>

![Order History lighthouse mobile](/documentation/testing/lighthouse/mobile/order-history-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Privacy Policy</summary>

![Privacy Policy lighthouse mobile](/documentation/testing/lighthouse/mobile/privacy-policy-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Product Details</summary>

![Product Details lighthouse mobile](/documentation/testing/lighthouse/mobile/product-detail-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Products</summary>

![Products lighthouse mobile](/documentation/testing/lighthouse/mobile/products-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Profile</summary>

![Profile lighthouse mobile](/documentation/testing/lighthouse/mobile/profile-mobile-lighthouse.png)

</details>

<details>

<summary style="font-size: 20px; font-weight: bold;">Register</summary>

![Register lighthouse mobile](/documentation/testing/lighthouse/mobile/register-mobile-lighthouse.png)

</details>

# Manual testing

The tests for this app listed below were conducted to ensure it correct operation. All tests passed successfully. For the purpose of the test results below user refers to a logged in user and admin refers to a logged in super user

## Navigation (header and footer)

<details>

<summary style="font-size: 20px; font-weight: bold;">Tests</summary>

| Item tested                                        | Test action | Expected Result                                                                                                                   | Pass     |
| -------------------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Pokemon TCG Home Logo                              | Click       | Redirects to home page                                                                                                            | &#10004; |
| Nav links                                          | Hover       | Colour change                                                                                                                     | &#10004; |
| Nav dropdown links                                 | Hover       | Background colour change                                                                                                          | &#10004; |
| Search bar (populated)                             | Submit      | Filter products based on search term query to name and description                                                                | &#10004; |
| Search bar (empty)                                 | Submit      | Displays the product page with all products and message informing user no word was entered                                        | &#10004; |
| Search bar button                                  | Hoover      | Brightness increases                                                                                                              | &#10004; |
| Search bar button                                  | Click       | Filter products based on search term query to name and description                                                                | &#10004; |
| My account icon                                    | Click       | Displays a dropdown containing signup and login links                                                                             | &#10004; |
| My account icon (user)                             | Click       | Displays a dropdown containing my profile and logout links                                                                        | &#10004; |
| My account icon (admin)                            | Click       | Displays a dropdown containing add products, my profile and logout links                                                          | &#10004; |
| Login link                                         | Click       | Redirects to login page                                                                                                           | &#10004; |
| Sign Up link                                       | Click       | Redirects to sign up page                                                                                                         | &#10004; |
| Add products link (admin)                          | Click       | Redirects to add products page                                                                                                    | &#10004; |
| My profile link                                    | Click       | Redirects to the profile page                                                                                                     | &#10004; |
| Log out link                                       | Click       | Redirects to the log out page                                                                                                     | &#10004; |
| Shopping Basket Icon                               | Click       | Redirects to basket page                                                                                                          | &#10004; |
| Shopping Basket Icon (products in)                 | Display     | Displays a badge with total number of items in basket                                                                             | &#10004; |
| Shopping Basket Icon (products in)                 | Display     | Displays total cost of items in basket                                                                                            | &#10004; |
| All products menu                                  | Click       | Displays a dropdown containing by price, by rating, by category and all products                                                  | &#10004; |
| All products menu (by price)                       | Click       | Displays the products page with products filtered by price asc                                                                    | &#10004; |
| All products menu (by rating)                      | Click       | Displays the products page with products filtered by rating desc                                                                  | &#10004; |
| All products menu (by category)                    | Click       | Displays the products page with products filtered by category A-Z                                                                 | &#10004; |
| All products menu (all products)                   | Click       | Displays the products page with all available products                                                                            | &#10004; |
| Pokemon cards menu                                 | Click       | Displays a dropdown containing booster packs, booster bundles, booster boxes, boxed sets, elite trainer boxes, tins and all cards | &#10004; |
| Pokemon cards menu (booster packs)                 | Click       | Displays the products page with products filtered by booster pack category                                                        | &#10004; |
| Pokemon cards menu (booster bundles)               | Click       | Displays the products page with products filtered by booster bundles category                                                     | &#10004; |
| Pokemon cards menu (booster boxes)                 | Click       | Displays the products page with products filtered by booster boxes category                                                       | &#10004; |
| Pokemon cards menu (boxed sets)                    | Click       | Displays the products page with products filtered by boxed sets category                                                          | &#10004; |
| Pokemon cards menu (elite trainer boxes)           | Click       | Displays the products page with products filtered by elite trainer boxes category                                                 | &#10004; |
| Pokemon cards menu (tins)                          | Click       | Displays the products page with products filtered by tins category                                                                | &#10004; |
| Pokemon cards menu (all cards)                     | Click       | Displays the products page with products with all available cards                                                                 | &#10004; |
| Accessories menu                                   | Click       | Displays a dropdown containing binders, sleeves, toploaders and all accessories                                                   | &#10004; |
| Accessories menu (binders)                         | Click       | Displays the products page with products filtered by binders category                                                             | &#10004; |
| Accessories menu (sleeves)                         | Click       | Displays the products page with products filtered by sleeves category                                                             | &#10004; |
| Accessories menu (toploaders)                      | Click       | Displays the products page with products filtered by toploaders category                                                          | &#10004; |
| Accessories menu (all accessories)                 | Click       | Displays the products page with products with all available accessories                                                           | &#10004; |
| Toys & Collectables menu                           | Click       | Displays a dropdown containing figures, pins, plushes and all toys and collectables                                               | &#10004; |
| Toys & Collectables menu (figures)                 | Click       | Displays the products page with products filtered by figures category                                                             | &#10004; |
| Toys & Collectables menu (pins)                    | Click       | Displays the products page with products filtered by pins category                                                                | &#10004; |
| Toys & Collectables menu (plushes)                 | Click       | Displays the products page with products filtered by plushes category                                                             | &#10004; |
| Toys & Collectables menu (all toys & collectables) | Click       | Displays the products page with all available toys & accessories displayed                                                        | &#10004; |
| Sale menu                                          | Click       | Displays the products page with products which are marked as on sale                                                              | &#10004; |
| Footer about us                                    | Click       | Redirects to the about us page                                                                                                    | &#10004; |
| Footer contact us                                  | Click       | Redirects to the contact us page                                                                                                  | &#10004; |
| Footer privacy policy                              | Click       | Redirects to the privacy policy page                                                                                              | &#10004; |
| Footer Facebook link                               | Click       | Pokemon TCG Ireland facebook business page opens in a new tab                                                                     | &#10004; |
| Footer Instagram link                              | Click       | Instagram home page opens in a new tab                                                                                            | &#10004; |
| Footer Tiktok link                                 | Click       | Tiktok home page opens in a new tab                                                                                               | &#10004; |
| Footer Youtube link                                | Click       | Youtube home page opens in a new tab                                                                                              | &#10004; |
| FooterX link                                       | Click       | X home page opens in a new tab                                                                                                    | &#10004; |
| Footer All social links                            | Hover       | Increase in size and brightness                                                                                                   | &#10004; |
| Footer Newsletter valid input                      | Submit      | Emailed added to mailchimp and success message displayed                                                                          | &#10004; |
| Footer Newsletter invalid input                    | Submit      | Error message displayed                                                                                                           | &#10004; |
| Collapsed mobile menu                              | Display     | At mid size screens and smaller this menu is displayed                                                                            | &#10004; |
| Collapsed mobile menu                              | Click       | Displays full navigation menu which now included a home links                                                                     | &#10004; |
| Search bar icon                                    | Display     | At mid size screens and smaller this icon is displayed                                                                            | &#10004; |
| Search bar icon                                    | Click       | Displays search bar input                                                                                                         | &#10004; |

</details>

## Home Page

<details>

<summary style="font-size: 20px; font-weight: bold;">Tests</summary>

| Item tested                             | Test action | Expected Result                                                                                                       | Pass     |
| --------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------- | -------- |
| Hero image                              | Display     | Hero image rendered correctly                                                                                         | &#10004; |
| Shop now link                           | Hover       | Brightness decreased                                                                                                  | &#10004; |
| Shop now link                           | Click       | Displays the product page with all available products                                                                 | &#10004; |
| Latest products                         | Display     | 4 Products displayed in order on date added                                                                           | &#10004; |
| Popular products                        | Display     | 4 Products displayed in order of highest review rating                                                                | &#10004; |
| Product card                            | Display     | Cards displayed correctly in grid                                                                                     | &#10004; |
| Product card image                      | Hover       | Brightness increase                                                                                                   | &#10004; |
| Product card image                      | Click       | Redirects to product details page for that product                                                                    | &#10004; |
| Product card links                      | Hover       | Colour change                                                                                                         | &#10004; |
| Product card category                   | Click       | Redirects to product page, filtering by associated category                                                           | &#10004; |
| Product card card set                   | Click       | Redirects to product page, filtering by associated card set                                                           | &#10004; |
| Product card expansion                  | Click       | Redirects to product page, filtering by associated expansion                                                          | &#10004; |
| Product card buttons (admin)            | Display     | Two additional buttons displayed, edit and delete                                                                     | &#10004; |
| Product card buttons                    | Hover       | Decrease in brightness                                                                                                | &#10004; |
| Product card add to basket button       | Click       | All add to basket buttons disabled, item added to basket, upon page reload buttons enabled, success message displayed | &#10004; |
| Product card add to basket toast        | Display     | Toast is displayed containing success message, basket summary, total, shipping message and checkout button            | &#10004; |
| Product card add to basket toast button | Hover       | Brightness decrease                                                                                                   | &#10004; |
| Product card edit button (admin)        | Click       | Redirects user to the edit product page                                                                               | &#10004; |
| Product card delete button (admin)      | Click       | Displays confirmation modal                                                                                           | &#10004; |
| Product card on sale                    | Display     | On Sale badge displayed, Pre sale price red and struck through                                                        | &#10004; |

</details>

## About Us Page

<details>

<summary style="font-size: 20px; font-weight: bold;">Tests</summary>

| Item tested | Test action | Expected Result                                                           | Pass     |
| ----------- | ----------- | ------------------------------------------------------------------------- | -------- |
| Images      | Display     | Images are displayed correctly                                            | &#10004; |
| Content     | Display     | All text content displayed correctly                                      | &#10004; |
| Google maps | Display     | Map is rendered in the find us section                                    | &#10004; |
| Google maps | Function    | Map can be moved, locations can be selected, larger view can be triggered | &#10004; |

</details>

## Sign up Page

<details>

<summary style="font-size: 20px; font-weight: bold;">Tests</summary>

| Item tested    | Test action | Expected Result                                                                                                  | Pass     |
| -------------- | ----------- | ---------------------------------------------------------------------------------------------------------------- | -------- |
| Valid form     | Submit      | User logged into newly created account, new profile created , redirected to home page, success message displayed | &#10004; |
| Invalid form   | Submit      | Form validation triggered and indicates reason for failure                                                       | &#10004; |
| Sign in button | Hover       | Brightness decrease                                                                                              | &#10004; |
| Sign in button | Click       | Form submission attempt                                                                                          | &#10004; |
| Sign up link   | Hover       | Colour change                                                                                                    | &#10004; |
| Sign up link   | Click       | Redirected to the sign in page                                                                                   | &#10004; |

</details>

## Sign in Page

<details>

<summary style="font-size: 20px; font-weight: bold;">Tests</summary>

| Item tested    | Test action | Expected Result                                                    | Pass     |
| -------------- | ----------- | ------------------------------------------------------------------ | -------- |
| Valid form     | Submit      | User logged in, redirected to home page, success message displayed | &#10004; |
| Invalid form   | Submit      | Form validation triggered and indicates reason for failure         | &#10004; |
| Sign in button | Hover       | Brightness decrease                                                | &#10004; |
| Sign in button | Click       | Form submission attempt                                            | &#10004; |
| Sign up link   | Hover       | Colour darkens                                                     | &#10004; |
| Sign up link   | Click       | Redirected to the sign up page                                     | &#10004; |

</details>

## Log out Page

<details>

<summary style="font-size: 20px; font-weight: bold;">Tests</summary>

| Item tested     | Test action | Expected Result                                                    | Pass     |
| --------------- | ----------- | ------------------------------------------------------------------ | -------- |
| Sign out button | Hover       | Decrease in brightness                                             | &#10004; |
| Sign out button | Click       | User logged out, redirected to the home page and message displayed | &#10004; |

</details>

## Profile Page

<details>

<summary style="font-size: 20px; font-weight: bold;">Tests</summary>

| Item tested                              | Test action | Expected Result                                                                | Pass     |
| ---------------------------------------- | ----------- | ------------------------------------------------------------------------------ | -------- |
| Collapsed sections                       | Display     | All 5 sections are collapsed on entry                                          | &#10004; |
| Collapsed sections                       | Hover       | Colour change border displayed                                                 | &#10004; |
| Collapsed sections                       | Click       | Section expands                                                                | &#10004; |
| Account info form button                 | Hover       | Decrease brightness                                                            | &#10004; |
| Account info form button (data invalid)  | Click       | Form validation triggers indicating the issue                                  | &#10004; |
| Account info form button (data valid)    | Click       | Success message, info update, section collapsed                                | &#10004; |
| Shipping info form button                | Hover       | Decrease brightness                                                            | &#10004; |
| Shipping info form button (data invalid) | Click       | Form validation triggers indicating the issue                                  | &#10004; |
| Shipping info form button (data valid)   | Click       | Success message, info update, section collapsed                                | &#10004; |
| Password form button                     | Hover       | Decrease brightness                                                            | &#10004; |
| Password form button (data invalid)      | Click       | Form validation triggers indicating the issue                                  | &#10004; |
| Password form button (data valid)        | Click       | Success message, info update, section collapsed                                | &#10004; |
| Form submit failure                      | Submit      | Page rendered, section that validation is expanded                             | &#10004; |
| Order history                            | Display     | Order all displayed in scrollable section                                      | &#10004; |
| Order history order number               | Click       | Redirects use to Order history page for that specific order                    | &#10004; |
| Wishlist (empty)                         | Display     | Message displayed to inform the user, Products button rendered                 | &#10004; |
| Wishlist (empty) button                  | Hover       | Brightness decrease                                                            | &#10004; |
| Wishlist (empty) button                  | Click       | Redirects user to products page                                                | &#10004; |
| Wishlist (populated)                     | Display     | Products in wishlist are displayed, with image, name, price and wishlist icon. | &#10004; |
| Wishlist (populated) image               | Click       | Redirects to product details page for the specific product                     | &#10004; |
| Wishlist (populated) on sale             | Display     | On sale badge displayed, price in red.                                         | &#10004; |
| Wishlist icon                            | Hoover      | Tooltip displayed with "Remove from wishlist" text                             | &#10004; |
| Wishlist icon                            | Click       | Item removed from wishlist, page reloaded, success message displayed           | &#10004; |
| Success toast (products in basket)       | Display     | Success message will only display message text, no basket summary              | &#10004; |

</details>

## Order History Page

<details>

<summary style="font-size: 20px; font-weight: bold;">Tests</summary>

| Item tested          | Test action | Expected Result                                                        | Pass     |
| -------------------- | ----------- | ---------------------------------------------------------------------- | -------- |
| Order history        | Display     | Info notification displayed                                            | &#10004; |
| Order history        | Display     | All order details rendered correctly, back to profile button displayed | &#10004; |
| Order history button | Hover       | Brightness Decrease                                                    | &#10004; |
| Order history button | Click       | Redirected to profile page                                             | &#10004; |

</details>

## Products Page

<details>

<summary style="font-size: 20px; font-weight: bold;">Tests</summary>

| Item tested                             | Test action | Expected Result                                                                                                       | Pass     |
| --------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------- | -------- |
| Products page                           | Display     | Products displayed correctly in grid                                                                                  | &#10004; |
| Product card image                      | Hover       | Brightness increase                                                                                                   | &#10004; |
| Product card image                      | Click       | Redirects to product details page for that product                                                                    | &#10004; |
| Product card links                      | Hover       | Colour change                                                                                                         | &#10004; |
| Product card category                   | Click       | Redirects to product page, filtering by associated category                                                           | &#10004; |
| Product card card set                   | Click       | Redirects to product page, filtering by associated card set                                                           | &#10004; |
| Product card expansion                  | Click       | Redirects to product page, filtering by associated expansion                                                          | &#10004; |
| Product card buttons (admin)            | Display     | Two additional buttons displayed, edit and delete                                                                     | &#10004; |
| Product card buttons                    | Hover       | Decrease in brightness                                                                                                | &#10004; |
| Product card add to basket button       | Click       | All add to basket buttons disabled, item added to basket, upon page reload buttons enabled, success message displayed | &#10004; |
| Product card add to basket toast        | Display     | Toast is displayed containing success message, basket summary, total, shipping message and checkout button            | &#10004; |
| Product card add to basket toast button | Hover       | Brightness decrease                                                                                                   | &#10004; |
| Product card edit button (admin)        | Click       | Redirects user to the edit product page                                                                               | &#10004; |
| Product card delete button (admin)      | Click       | Displays confirmation modal                                                                                           | &#10004; |
| Product card on sale                    | Display     | On Sale badge displayed, Pre sale price red and struck through                                                        | &#10004; |
| Product count (all products)            | Display     | Displays correct num or products on page                                                                              | &#10004; |
| Product count (search)                  | Display     | Displays product home link, count and search term                                                                     | &#10004; |
| Product count (search) - home link      | Click       | Redirects to products page, displaying all products                                                                   | &#10004; |
| Sort dropdown                           | Click       | Displays drop down menu with available search options                                                                 | &#10004; |
| Sort dropdown (by price low to high)    | Select      | Sorts all products on page by price low to high                                                                       | &#10004; |
| Sort dropdown (by price high to low)    | Select      | Sorts all products on page by price high to low                                                                       | &#10004; |
| Sort dropdown (by rating low to high)   | Select      | Sorts all products on page by rating low to high                                                                      | &#10004; |
| Sort dropdown (by rating high to low)   | Select      | Sorts all products on page by rating high to low                                                                      | &#10004; |
| Sort dropdown (by name A-Z)             | Select      | Sorts all products on page by name A-Z                                                                                | &#10004; |
| Sort dropdown (by name Z-A)             | Select      | Sorts all products on page by name Z-A                                                                                | &#10004; |
| Sort dropdown (by category A-Z)         | Select      | Sorts all products on page by category A-Z                                                                            | &#10004; |
| Sort dropdown (by category Z-A)         | Select      | Sorts all products on page by category Z-A                                                                            | &#10004; |
| Products page back to top button        | Hover       | Brightness increase                                                                                                   | &#10004; |
| Products page back to top button        | Click       | Returned to top of page                                                                                               | &#10004; |

</details>

## Product Details Page

<details>

<summary style="font-size: 20px; font-weight: bold;">Tests</summary>

| Item tested                                         | Test action | Expected Result                                                                                                                                                                       | Pass     |
| --------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Product details                                     | Display     | Image, detail section, add review section and review section displayed                                                                                                                | &#10004; |
| Product details (on sale)                           | Display     | Image, detail section, add review section and review section displayed, on sale badge overlayed on image, pre sale displayed red and struck through                                   | &#10004; |
| Image                                               | Click       | Opens image with lightbox                                                                                                                                                             | &#10004; |
| Detail section (no user)                            | Display     | Displays name, price, review status, description, category, card set, expansion, qty input, add to basket button and back to products link                                            | &#10004; |
| Detail section (user)                               | Display     | Displays name, price, wishlist icon, review status, description, category, card set, expansion, qty input, add to basket button and back to products link                             | &#10004; |
| Detail section (admin)                              | Display     | Displays name, price, wishlist icon, review status, description, category, card set, expansion, qty input, add to basket button and back to products link, edit button, delete button | &#10004; |
| Detail section review status                        | Click       | Moves user to review section                                                                                                                                                          | &#10004; |
| Wishlist icon (not in wishlist)                     | Hoover      | Tooltip displayed with "Add from wishlist" text                                                                                                                                       | &#10004; |
| Wishlist icon (not in wishlist)                     | Click       | Item added to wishlist, page reloaded, success massage displayed, Icon now red                                                                                                        | &#10004; |
| Wishlist icon (in wishlist)                         | Hoover      | Tooltip displayed with "Remove from wishlist" text                                                                                                                                    | &#10004; |
| Wishlist icon (in wishlist)                         | Click       | Item removed from wishlist, page reloaded, success message displayed, Icon now empty                                                                                                  | &#10004; |
| Product card links                                  | Hover       | Colour change                                                                                                                                                                         | &#10004; |
| Product card category                               | Click       | Redirects to product page, filtering by associated category                                                                                                                           | &#10004; |
| Product card card set                               | Click       | Redirects to product page, filtering by associated card set                                                                                                                           | &#10004; |
| Product card expansion                              | Click       | Redirects to product page, filtering by associated expansion                                                                                                                          | &#10004; |
| Quantity selector (in range)                        | Input       | Product added to the basket, page reloaded, success message displayed                                                                                                                 | &#10004; |
| Quantity selector (above range range)               | Input       | Form validation stops submission and informs the user of the issue                                                                                                                    | &#10004; |
| Quantity selector (below range)                     | Input       | Form validation stops submission and informs the user of the issue                                                                                                                    | &#10004; |
| Quantity selector (above max of product per basket) | Submit      | Qty added to basket adjusted to only add qty that will make item in basket reach max 99. So if 50 in basket and 99 submitted, 49 added, user informed via message                     | &#10004; |
| Quantity selector (max of product in basket)        | Submit      | Qty adjusted to 0 and no more products added to basket. So if 99 in basked and 99 added, qty will be adjusted to 0 and user informed 0 were added and 99 in basket                    | &#10004; |
| Back to products button                             | Click       | Redirects to products page                                                                                                                                                            | &#10004; |
| Add Review (no user)                                | Display     | Login and sign up to leave review message rendered, links redirect to relevant pages                                                                                                  | &#10004; |
| Add Review (user review already)                    | Display     | Thank you message displayed                                                                                                                                                           | &#10004; |
| Add review (user not reviewed)                      | Display     | Start rating selection and review textfield displayed                                                                                                                                 | &#10004; |
| Start rating                                        | Hover       | Start will turn yellow as they are hovered, As stars are hovered 1-5 the previous stars remain solid                                                                                  | &#10004; |
| Start rating                                        | Click       | Start before selected and selected stars will turn solid                                                                                                                              | &#10004; |
| Submit review (invalid)                             | Submit      | Form validation triggered, user informed of issues.                                                                                                                                   | &#10004; |
| Submit review (valid)                               | Submit      | Review submitted for approval, page reloaded, success message displayed                                                                                                               | &#10004; |
| Review section empty                                | Display     | Message displayed reading there are no reviews for this product yet                                                                                                                   | &#10004; |
| Review section reviews                              | Display     | Reviews displayed in a list. Each contains username of reviewer, dated and time of review, review rating and review text                                                              | &#10004; |
| Review section owner                                | Display     | Delete button displayed                                                                                                                                                               | &#10004; |
| Delete button                                       | click       | Review deleted, page reloaded, user informed via message                                                                                                                              | &#10004; |

</details>

## Add Product Page

<details>

<summary style="font-size: 20px; font-weight: bold;">Tests</summary>

| Item tested                     | Test action | Expected Result                                                                    | Pass     |
| ------------------------------- | ----------- | ---------------------------------------------------------------------------------- | -------- |
| Add product (admin)             | Display     | Only displays for super user (even with direct url access)                         | &#10004; |
| Add product form                | Display     | Form displays correctly with all fields displayed and required fields labeled      | &#10004; |
| Add product form                | Display     | Summernote text editor rendered correctly                                          | &#10004; |
| Add Product form (invalid data) | Submit      | Validation triggered indicating issue to user                                      | &#10004; |
| Add Product form (invalid data) | Submit      | Error message displayed                                                            | &#10004; |
| Add Product form (image added)  | Select      | message below image button displays name of image file to be added                 | &#10004; |
| Add Product form buttons        | Hover       | Brightness decrease                                                                | &#10004; |
| Add Product form cancel button  | Click       | Redirected to the product page                                                     | &#10004; |
| Add Product form (valid data)   | Submit      | Product is added, redirected to added products details page, success msg displayed | &#10004; |

</details>

## Edit Product Page

<details>

<summary style="font-size: 20px; font-weight: bold;">Tests</summary>

| Item tested                      | Test action | Expected Result                                                                    | Pass     |
| -------------------------------- | ----------- | ---------------------------------------------------------------------------------- | -------- |
| Edit product (admin)             | Display     | Only displays for super user (even with direct url access)                         | &#10004; |
| Edit product form                | Display     | Info message is displayed                                                          | &#10004; |
| Edit product form                | Display     | Form displays correctly with all fields displayed and required fields labeled      | &#10004; |
| Edit product form                | Display     | Summernote text editor rendered correctly                                          | &#10004; |
| Edit product form                | Display     | All fields are pre populated with current product info                             | &#10004; |
| Edit product form                | Display     | Current image is displayed                                                         | &#10004; |
| Edit Product form (invalid data) | Submit      | Validation triggered indicating issue to user                                      | &#10004; |
| Edit Product form (invalid data) | Submit      | Error message displayed                                                            | &#10004; |
| Edit Product form (image added)  | Select      | message below image button displays name of image file to be added                 | &#10004; |
| Edit Product form buttons        | Hover       | Brightness decrease                                                                | &#10004; |
| Edit Product form cancel button  | Click       | Redirected to the product page                                                     | &#10004; |
| Edit Product form (valid data)   | Submit      | Product is added, redirected to added products details page, success msg displayed | &#10004; |

</details>

## Basket page

<details>

<summary style="font-size: 20px; font-weight: bold;">Tests</summary>

| Item tested                              | Test action | Expected Result                                                                                                                                                 | Pass     |
| ---------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Basket                                   | Display     | Product summaries and basket summary displayed                                                                                                                  | &#10004; |
| Product summaries                        | Display     | Summary for each product contain an image, name, sku, qty input sub total and total                                                                             | &#10004; |
| Product summaries sale                   | Display     | Summary for each product contain an image, name, sku, qty input sub total and total, on sale badge overlayed in image, pre sale price in res and struck through | &#10004; |
| Basket summary                           | Display     | Displays subtotal, shipping, total shipping message, product and checkout button, each redirect to relevant page                                                | &#10004; |
| Product summaries image                  | Click       | Redirects to product details page of selected product                                                                                                           | &#10004; |
| Product summaries qty - button           | Clicked     | Decrements qty by one and reloads page, success message shown                                                                                                   | &#10004; |
| Product summaries qty - button (qty=1)   | Clicked     | Button disabled                                                                                                                                                 | &#10004; |
| Product summaries qty + button           | Clicked     | Increments qty by one and reloads page, success message shown                                                                                                   | &#10004; |
| Product summaries qty + button (qty= 99) | Clicked     | Button disabled                                                                                                                                                 | &#10004; |
| Quantity selector (in range)             | Input       | Product added to the basket, page reloaded, success message displayed                                                                                           | &#10004; |
| Quantity selector (above range range)    | Input       | Qty adjusted to 99 and added to basket, success message shown                                                                                                   | &#10004; |
| Quantity selector (below range)          | Input       | Qty adjusted to 1 and added to basket, success message shown                                                                                                    | &#10004; |

</details>

## Checkout Page

<details>

<summary style="font-size: 20px; font-weight: bold;">Tests</summary>

| Item tested                 | Test action | Expected Result                                                                                                                                         | Pass     |
| --------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Checkout                    | Display     | Form, your items and payment summary displayed                                                                                                          | &#10004; |
| Form                        | Display     | Form displays correctly with all fields displayed and required fields labeled                                                                           | &#10004; |
| Form                        | Display     | from is pre populated with all available user data if signed in                                                                                         | &#10004; |
| Form (invalid data)         | Submit      | Triggers form validation, user is informed of issue                                                                                                     | &#10004; |
| Form (invalid payment data) | Submit      | Page overlay and loading icon are displayed, page reloads with error/validation messages for user                                                       | &#10004; |
| Form (valid data)           | Submit      | Page overlay and loading icon are display, checkout success is displayed, user received mail confirmation, order is niw available in order confirmation | &#10004; |
| Your items                  | Display     | Collapsed by default                                                                                                                                    | &#10004; |
| Your items                  | Click       | Expand to show product summary for each product in the basket (image, name, qty and subtotal).                                                          | &#10004; |
| Your items on sale          | Click       | Expand to show product summary for each product in the basket (image, name, qty and subtotal). Image is overlayed with on sale badge, price in red      | &#10004; |
| Product image               | Click       | Redirects user to product details page of specific product                                                                                              | &#10004; |

</details>

## Checkout Success Page

<details>

<summary style="font-size: 20px; font-weight: bold;">Tests</summary>

| Item tested   | Test action | Expected Result                      | Pass     |
| ------------- | ----------- | ------------------------------------ | -------- |
| Order details | Display     | Info notification displayed          | &#10004; |
| Order details | Display     | All order details rendered correctly | &#10004; |

</details>

## Privacy Policy Page

<details>

<summary style="font-size: 20px; font-weight: bold;">Tests</summary>

| Item tested | Test action | Expected Result                      | Pass     |
| ----------- | ----------- | ------------------------------------ | -------- |
| Content     | Display     | All text content displayed correctly | &#10004; |

</details>

## Contact Us Page

<details>

<summary style="font-size: 20px; font-weight: bold;">Tests</summary>

| Item tested         | Test action | Expected Result                                                               | Pass     |
| ------------------- | ----------- | ----------------------------------------------------------------------------- | -------- |
| Form                | Display     | Form displays correctly with all fields displayed and required fields labeled | &#10004; |
| Form                | Display     | Inputs pre populated with available user info                                 | &#10004; |
| Form (invalid data) | Submit      | Validation triggered, user informed of issues                                 | &#10004; |
| Form (valid data)   | Submit      | contact created, page reloaded, success message displayed                     | &#10004; |

</details>

## Error pages

<details>

<summary style="font-size: 20px; font-weight: bold;">Tests</summary>

| Item tested | Test action | Expected Result                 | Pass     |
| ----------- | ----------- | ------------------------------- | -------- |
| Home button | Hover       | Increase in size and brightness | &#10004; |
| Home button | Click       | Redirect user to home page      | &#10004; |

</details>

## Password Reset Page

<details>

<summary style="font-size: 20px; font-weight: bold;">Tests</summary>

| Element      | Action | Expected Result            | Pass/Fail |
| ------------ | ------ | -------------------------- | --------- |
| Form (valid) | Submit | Sends reset password email | &#10004;  |
| Login Button | Click  | Displays loin pag          | &#10004;  |

</details>

## Password Change Page

<details>

<summary style="font-size: 20px; font-weight: bold;">Tests</summary>

| Element       | Action | Expected Result                                    | Pass/Fail |
| ------------- | ------ | -------------------------------------------------- | --------- |
| Form Valid    | Submit | Updates the users password, success message        | &#10004;  |
| Form(Valid)   | Submit | Change Password Notification received              | &#10004;  |
| Form(Invalid) | Submit | Form validation triggered, user informed of issues | &#10004;  |

</details>

[Return to Table of Contents](#table-of-contents)
[Return to README.md](README.md)

# Responsive design testing

The Responsive design testing was carried out during and after the development of the website. Firefox's development tools were used to ensure that all webpages not only looked good at the bootstrap breakpoints, but at all points in between. This was accomplished by altering the screen width from 320px up and and making changes to the code using bootstraps grid system. In cases where the grid system could not achieve the desired sizing or layout custom media queries were added. After the website was completed it was tested on my Huawei P30 pro and all pages passed responsive testing.

[Return to Table of Contents](#table-of-contents)
[Return to README.md](README.md)

# Bugs

During testing I found three bugs based on code I used fom the Boutique Ado walkthrough and wrote some code to fix each one. I also found some bugs in my own code during testing and all were fixed. The links below go to the github bug reports for each bug and give the full details on what the bug were, why they occurred and how I fixed each, please follow the links for more details.

| Bugs                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------- |
| [Unlimited items in basket](https://github.com/GaryDolan/ci-p5-pokemon-tcg-ireland/issues/93)                          |
| [App breaking bug (orderline item data error)](https://github.com/GaryDolan/ci-p5-pokemon-tcg-ireland/issues/92)       |
| [Basket qty button spamming](https://github.com/GaryDolan/ci-p5-pokemon-tcg-ireland/issues/90)                         |
| [Save info checkbox](https://github.com/GaryDolan/ci-p5-pokemon-tcg-ireland/issues/89)                                 |
| [Basket qty issue](https://github.com/GaryDolan/ci-p5-pokemon-tcg-ireland/issues/88)                                   |
| [Product cards footer mismatched style](https://github.com/GaryDolan/ci-p5-pokemon-tcg-ireland/issues/87)              |
| [Basket details showing in success toast when empty](https://github.com/GaryDolan/ci-p5-pokemon-tcg-ireland/issues/86) |
| [Custom button transparent on press](https://github.com/GaryDolan/ci-p5-pokemon-tcg-ireland/issues/85)                 |
| [Sort selector issue](https://github.com/GaryDolan/ci-p5-pokemon-tcg-ireland/issues/83)                                |

[Return to Table of Contents](#table-of-contents)
[Return to README.md](README.md)
