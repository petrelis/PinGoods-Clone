# Software Engineering project "PinGoods"
# Group II
PinGoods is a local goods platform dedicated to easily connecting vendors with their customers.

## Purpose

There was once a potato lover who wanted to buy fresh potatoes straight from the farm (because Maxima potatoes are not so tasty). Unfortunately, he didn‘t know anyone who could sell them to him :( He looked for them on Facebook, but couldn‘t find a single person. He searched the entire internet but was not able to find a place to contact a potato grower. We would make a new Facebook (but with superior search algorithms of course :))))), but we're too cool for that. Besides, we have a better idea. On the other side, it‘s not all sunshine and rainbows either. Potato sellers also have a hard time finding someone to buy from them (not because they can‘t navigate Facebook, but because there is no good platform for such things). And that‘s where we come in. We will create a platform that will easily connect the buyers and potato sellers, and they will both live in great prosperity.

## High-Overview

The aim of the system is to ensure that goods from the villages of all Lithuanian regions can display their purchase location on the map, and when the customer selects the result in the search bar, he gets teleported to the seller's location. The system will provide the best environment for small businesses to showcase their high-quality products and services, and there will be no unrelated ads, so you can disable your AdBlock. Product prices will be clearly stated including Value-added tax (PVM). Customers will also be able to take advantage of our intuitive sorting system, thanks to a great variety of colors as if van Gogh drew it. All available functions can be seen in the diagram below.

![Use-Case Matrix](https://user-images.githubusercontent.com/47245874/135151107-f3b1b202-6b2b-44f3-bc39-605a59cab5e9.png)

## The Great Gang

Each project member chose a working team in which is most comfortable. This was done to save time and improve efficiency. As a well-coordinated team, we will collaborate with the rest of the team. We selected these specific teams as a part of our project. Why? Because the big guys on the internet said these specific teams should be enough for any project. And we decided to go for it.

**Lead: Sahak Ivašauskas @sahiva**

- **Front-End**
  - **Sara Sánchez @SaraSanGar (Sub-Lead)**
  - Gustas Petkevičius @FlooPeriS
  - Danielius Miškinis @Segulx
  - Pablo Santana @pablosanttanaa
  - Liudas Kraujalis @Liudaskr
  - David Kisel @DavidK14
  
- **Back-End**
  - **Marius Raupelis @mariusraupel (Sub-Lead)**
  - Martynas Jakučionis @Jaku12345
  - Gustas Strimaitis @Radorkan
  - Aurimas Miliauskas @AuriTheGreat
  - Petras Rudys @petrelis
  - Faustas Baltrušaitis @FaustasYe
  - Yeeun Lee @Atay36
  - Chiara Satta @chiarasatta

- **Server**
  - **Sahak Ivašauskas @sahiva (Sub-Lead)**
  - Taha Abakar Samir @samir737
  
- **Graphics**
  - David Kisel @DavidK14
  - Martynas Jakučionis @Jaku12345

- **Documentation**
  - Sahak Ivašauskas @sahiva

## Mandatory Functionality

One of the key functionalities that our project will consist:

**HOMEPAGE** 

This is the page that the user sees once he visits the website. 
- At the top, there is the primary button. Clicking it leads you to the main page, which includes the following functionalities:
  - Search bar 
  - Map 
  - Options Bar 
- Under the button, the description of the website is displayed.

**REGISTRATION WINDOW**

At the top-right of the home page, there are "Login" and "Registration" fields. Clicking the "Log in" button opens the "Log in" window. In that window, the user will have to enter his username or e-mail address in the "Username or e-mail address" field and the password in the "Password" field. That window will also have a button titled "Log in" and a text box as "If you are not registered, register." where "Register" is the text associated with the registration window. After clicking on the main page "Register" button - you'll see a window where you can register, whether you are registering as a seller or a buyer. If you are registering as a seller, a window will appear with the required fields to fill in: 
- Username
- First/Last name
- Phone number (optional as instead, it'll be next to the product) 
- City of residence 
- Address (optional as instead, it'll be next to the product)
- Password 
- Repeat password

If you register as a customer, a window will appear with a required fields to fill in: 
- Username
- City of residence (optional)
- Password 
- Retype password 

Some other information may be added later on to be filled in. Upon registration, **noreply@pingoods.com** will send a message with confirmation to the user.

**MAP** 

It is located in the center of the home page on the right side of the search bar. After submitting a search query to the search bar: 
- In the enlarged window, the user sees all the results that best match the search criteria. 
- When zoomed in, the user sees all the products in the area that match the criteria. 
- Clicking on one of the search results will take you to that seller on the map.

**SEARCH BAR** 

Clicking the primary button on the homepage leads you to the main page with the Search Bar. It'll be located at the top-left of the page. After the search, the search bar will list the most relevant results for the products, and the goods and services tax (PVM) adjusted prices will be displayed. The most suitable product is determined by the combination of your preferred results (vendor's subscription products will be at top), selected categories (product color), keyword best match, and closest customer distance.

**OPTIONS BAR**

If the user has logged in to the system, it's located at the top-right of the Main Page. Otherwise, it's not so. When the registered user clicks the button, it'll display for **Vendors**:
- Subscription 
  - Buy subscription
  - Check subscription history 
- Edit product posts
  -  Edit location 
  -  Edit price
  -  Delete the post
    - Once the remove button is clicked, a confirmation screen will appear in the center. 
  - Change Phone Number
  - Change City of Living  
  - Change Address 
  - Change Password

If it's clicked by a **Customer**, then he'll get displayed with:
  - History of Purchases 
  - Change Phone Number 
  - Change City of Living 
  - Change Address 
  - Change Password

## Non-Functional Requirements

We, as a team, are expecting that the following non-functional requirements won't cause stress to our users. The software program will have a clear-as sky (not like what we see every day) interface mixed with bright colors! Our login and registration system will be as simple as putting on your pants (although sometimes it can be complicated, especially on Monday mornings). But it'll have high data protection and will give security to its users. Nobody desires to be spied on. For sure, the database won't be accessible to external people other than administrators, the email or postal address will not be visible in the profile of consumers. Also, the software will detect the existence of two customers with the same ID (so that you cannot buy from yourself). Don't worry, we'll have an age limit to prevent your kids from spending the savings buying potatoes. In addition, the software program may be so optimized that it may even run on a grandmother's cell phone. Lastly, the loading time won't exceed 4 seconds, so you will not get bored surfing our webpage (because who likes to wait more than 4 seconds?)

## Documentation

   The provided information must be referred by the developers in their workflow to prevent disorder and misunderstandings.

   ### GitHub formatting

   GitHub formatting [syntaxes](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) should be known for formatting your issue description and commits.

   ### Issues

   Issues are created for setting tasks and reporting bugs. All the Issues title must be as follows: "[**TEAMNAME**-**ISSUEID**] **ISSUENAME**", where **TEAMNAME** is the shortcut of the team that must handle this Issue, **ISSUEID** is a unique identification number for each team's Issue, **ISSUENAME** is the short title for the issue. Use uppercase letters appropriately in the title.

   [How We Write GitHub Issues](https://wiredcraft.com/blog/how-we-write-our-github-issues/)

   **Shortcuts for each team**

   - **Front-End** - **FRNT**
   - **Back-End** - **BACK**
   - **Server** - **SERV**
   - **Graphics** - **GFX**
   - **Documentation** - **DOCS**

   **Setting Issue fields**

   - **Assignee**: to solve this Issue, assign a specific developer list. Set to null if the problem is not someone's concern, especially
   - **Label**: select the appropriate label for the Issue, including the label of the team to which it is assigned. **If the Issue is a bug**, then **bug** label must be set as well
   - **Projects**: must be set to the team to which the Issue belongs
   - **Milestone**: set the Issue to an appropriate release


   **Issue Description**

   **If the Issue is a task**, then write a clear, atomic specification of the task. If needed, use visual content, checkboxes, etc.
   
   **If the Issue is a bug**, then shortly describe the problem and write down what is the **Expected result:** and the **Actual result:**.
   
  ### Gitflow Workflow

   This [article](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) contains the git-flow model that should be followed when creating, merging, and deleting branches. For naming branches, please refer to the git branch naming [convention](https://deepsource.io/blog/git-branch-naming-conventions/). **Important!: don't use the tracker ID in the branch name as it's provided in the article. We're not going to use it.**

  ### Coding conventions

  Each developer has a different coding style, and to avoid confusion, you should follow the Google Style Guide for each programming language.

  -  [**JavaScript**](https://google.github.io/styleguide/jsguide.html)
  -  [**HTML/CSS**](https://google.github.io/styleguide/jsguide.html)
  -  [**Java**](https://google.github.io/styleguide/javaguide.html)
  -  [**PHP**](https://www.php-fig.org/psr/psr-2/)

  
