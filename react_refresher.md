# ReactJS Refresher

### Creating a ReactJS App:
#### Step 1: create-react-app
  * [create-react-app github](https://github.com/facebook/create-react-app)
  * In your terminal use `create-react-app example-app-name`.
  * Enter the directory `cd example-app-name`.
  * Make sure you initialize the repository:
  ~~~
  git init
  ~~~
  * Create the repo in Github and copy the link provided there to connect this repo with it:
  ~~~
  git remote add origin your-url-here
  ~~~
  * Lastly, make sure you add, commit and push your boilerplate:
  ~~~
  git add .
  git commit -m "Inital commit, boilerplate"
  git push origin master
  ~~~

  * If you are planning on hosting a demo on Heroku, you can do so using:
  ~~~
  heroku create
  git push heroku master
  ~~~

#### Step 2: Adding React-Routes
  * [react-router github](https://github.com/ReactTraining/react-router)
  * We will be using `react-router-dom` for reference.
  * We will now be adding React Routes to our App to create a seamless SPA (Single Page App).
  * I use *yarn* instead of *npm*, so all examples will be in *yarn* only:
  ~~~
  yarn add react-router-dom
  ~~~
  * Now we are going to alter the text to include our routing options:
  * Open both "Index.js" & "App.js" in Atom or another text editor.
  * In "Index.js" replace line 4 with:
  ~~~
  import Routing from './Routing';
  ~~~
  * And replace line 7 with:
  ~~~
  ReactDOM.render(<Routing />, document.getElementById('root'));
  ~~~

  * Now we will created **`Routing.js`** in the **`src`** folder and add this to it:
  ~~~
  import React, { Component } from 'react';
  import { BrowserRouter, Route } from 'react-router-dom'
  import App from './App';

  class Routing extends Component {
    render() {
      return (
        <BrowserRouter>
          <div>
            <Route exact path="/" component={App} />
          </div>
        </BrowserRouter>
      );
    }
  }

  export default Routing;
  ~~~
  * The important bits here are `<BrowserRouter>` & `<Route exact path="/" component={App} />`.
    * We tell React that we are using Routes by encompassing our Routing section in `<BrowserRouter>`
    * We tell React the exact url and component we want to use using: `<Route exact path="/" component={App} />`.
    * Provided we have components called *"ComponentA"*, *"ComponentB"*, & *"ComponentC"* we can connect those using the following example:
    ~~~
    import React, { Component } from 'react';
    import { BrowserRouter, Route } from 'react-router-dom'
    import App from './App';
    import ComponentA from './ComponentA';
    import ComponentB from './ComponentB';
    import ComponentC from './ComponentC';

    class Routing extends Component {
      render() {
        return (
          <BrowserRouter>
            <div>
              <Route exact path="/" component={App} />
              <Route exact path="/PageOne" component={ComponentA} />
              <Route exact path="/AnyPathTwo" component={ComponentB} />
              <Route exact path="/YouSeeWhatIMean" component={ComponentC} />
            </div>
          </BrowserRouter>
        );
      }
    }

    export default Routing;
    ~~~
    * As it implies, if we were to visit "http://localhost:3000/YouSeeWhatIMean" we would load *"ComponentC"*.

  * Lastly, while you likely won't need it right away, your are able to implement links to other components.
  * It will go to the URL associated with the link as well as load the component.
  ~~~
  import { Link } from 'react-router-dom';

  . . .

  <Link to="/"><p>Home Page</p></Link>
  ~~~
  * This example would bring you to the root directory, which in our example above would be *"App.js"*.

#### Step 3: File Structure (Opinionated)
  > As a warning, there is no "perfect" way to set up your file structure & the following step is entirely my opinion on the matter.
  There are some conventions, but it comes down to how you enjoy sorting files as well as future developer readability.

  * Now that we have used `create-react-app` & added our `react-routes-dom` updates to the code, we should have a file structure like this:
  ~~~
  example-app-name
    => .git
    => node_modules
    => public
    => src
    => .gitignore
    => package.json
    => README.md
    => yarn.lock
  ~~~

  * We are almost exclusively interested in the `src` folder.
  * After expanding that we should see:
  ~~~
  example-app-name
    => src
      => App.css
      => App.js
      => App.test.js
      => Index.css
      => Index.js
      => logo.svg
      => registerServiceWorker.js
      => Routing.js
  ~~~

  * I like to create a `components` folder to hold everything I'll be working on inside of the `src` folder.
  * Inside the `components` folder, I like to have a top level set of components such as: *`Navigation.js`*, *`Header.js`*, *`Body.js`*, & *`Footer.js`*
  ~~~
  example-app-name
    => src
      => components
        => Navigation.js
        => Navigation.css
        => Header.js
        => Header.css
        => Body.js
        => Body.css
        => Footer.js
        => Footer.css
      => App.css
      => App.js
      => App.test.js
      => Index.css
      => Index.js
      => logo.svg
      => registerServiceWorker.js
      => Routing.js
  ~~~

  * Using this template for structuring your components and CSS files will go a long way towards maintaining organization in larger codebases.

###### Bonus Individual File Setup:
  * For each new component I create, I use the same templates when I begin.
  * Prior to designing a website, I choose a set of colors and add them as CSS variables for easy access from any `.css` file:
  ~~~
  /* Color Palette provided to all other .css */
  :root {
    --TheNameOfTheVariable: #2C7D42;
    --Gunmetal: #2B2D42;
    --GrayBlue: #8D99AE;
    --AntiFlashWhite: #EDF2F4;
    --Khaki: #CCAD8F;
    --Lust: #E2161A;
    --Footer: #383838;
    --Highlightes: #428bca;
    --Backdrops: #7bb1e0;
  }
  ~~~
  * using `:root` as the element just allows us to call it from any `.css` file.
  * In order to call that variable to another file you use the normal call for an element, but instead of using a color or hex code, you call `var(--TheNameOfTheVariable)`:
  ~~~
  background-color: var(--Gunmetal)
  color: var(--AntiFlashWhite)
  border-color: var(--Lust)
  ~~~

  * For all other `.css`:
  ~~~
  /* Color Palette provided in App.css */

  * {
    margin: 0;
    padding: 0;
  }
  #NewComponent-wrapper {
    min-height: 100vh; /* Allows the footer to exist in the proper place */
  }
  ~~~

  * For `.js`:
  ~~~
  import React, { Component } from 'react';
  import logo from './logo.svg';
  import './NewComponent.css';
  import Navigation from './components/Navigation';
  import Footer from './components/Footer';

  class NewComponent extends Component {
    render() {
      return (
        <div id="NewComponent">
          <div id="NewComponent-Navigation"><Navigation /></div>

          <div id="NewComponent-wrapper"> {/* Flexboxed Body while maintaining the Navigation and Footer */}
          </div>

          <div id="NewComponent-Footer"><Footer /></div>
        </div>
      );
    }
  }

  export default NewComponent;
  ~~~

#### Step 4: Setting Up Responsive Design Using react-responsive
* [react-responsive](https://github.com/contra/react-responsive)
* We will be using a combination of react-responsive & CSS @media queries in order to make the site responsive.
* To use react-responsive you must import it into any page you use it on:
~~~
import MediaQuery from 'react-responsive';
~~~
* Every site is a little different, so the breakpoints won't usually match up every time.
* However, this is a good mobile-first baseline to follow when your starting out:
~~~
/*==========  Mobile First Method  ==========*/

/* Custom, iPhone Retina */
@media only screen and (min-width : 320px) {
  body {
    background-color: red;
  }
}

/* Extra Small Devices, Phones */
@media only screen and (min-width : 480px) {
  body {
    background-color: blue;
  }
}

/* Small Devices, Tablets */
@media only screen and (min-width : 768px) {
  body {
    background-color: green;
  }
}

/* Medium Devices, Desktops */
@media only screen and (min-width : 992px) {
  body {
    background-color: yellow;
  }
}

/* Large Devices, Wide Screens */
@media only screen and (min-width : 1200px) {
  body {
    background-color: purple;
  }
}
~~~
* I, personally, want it to transition smoothly when changing queries, and all you have to do is add this little snippet to your .css sheets:
~~~
* {
    transition:all .2s linear;
    -o-transition:all .2s linear;
    -moz-transition:all .2s linear;
    -webkit-transition:all .2s linear;
}
~~~
* For reference's sake, here is the full .css sheet to copy and paste:
~~~
/* Color Palette provided in App.css */

* {
  margin: 0;
  padding: 0;
  transition:all .2s linear;
  -o-transition:all .2s linear;
  -moz-transition:all .2s linear;
  -webkit-transition:all .2s linear;
}

/*==========  Mobile First Method  ==========*/

/* Custom, iPhone Retina */
@media only screen and (min-width : 320px) {
  body {
    background-color: red;
  }
}

/* Extra Small Devices, Phones */
@media only screen and (min-width : 480px) {
  body {
    background-color: blue;
  }
}

/* Small Devices, Tablets */
@media only screen and (min-width : 768px) {
  body {
    background-color: green;
  }
}

/* Medium Devices, Desktops */
@media only screen and (min-width : 992px) {
  body {
    background-color: yellow;
  }
}

/* Large Devices, Wide Screens */
@media only screen and (min-width : 1200px) {
  body {
    background-color: purple;
  }
}
~~~

# Full list of Atom Packages as of 5-18-18
 My Themes (Great highlighting, easy on the eyes):
   UI: steam-pirate-ui
     https://atom.io/themes/steam-pirate-ui
   Syntax: steam-pirate-syntax
     https://atom.io/themes/steam-pirate-syntax

 Core MUST HAVES:
   atom-beautify
     https://atom.io/packages/atom-beautify
   auto-detect-indentation
     https://atom.io/packages/auto-detect-indentation
   auto-update-packages
     https://atom.io/packages/auto-update-packages
   autoclose-html
     https://atom.io/packages/autoclose-html
   busy-signal
     https://atom.io/packages/busy-signal
   emmet
     https://atom.io/packages/emmet
   file-icons
     https://atom.io/packages/file-icons
   highlight-selected
     https://atom.io/packages/highlight-selected
   jquery-snippets
     https://atom.io/packages/jquery-snippets
   neon-selection
     https://atom.io/packages/neon-selection
   pigments
     https://atom.io/packages/pigments
   teletype
     https://atom.io/packages/teletype

 Core Rails/Ruby Specific:
   rails-snippets
     https://atom.io/packages/rails-snippets
   ruby-block
     https://atom.io/packages/ruby-block

 Core React/Javascript Specific:
   language-babel
     https://atom.io/packages/language-babel
   linter
     https://atom.io/packages/linter
   react-es6-snippets
     https://atom.io/packages/react-es6-snippets
   react-snippets
     https://atom.io/packages/react-snippets

 Not Core But Highly Recommended:
   atom-clock
     https://atom.io/packages/atom-clock
   color-picker
     https://atom.io/packages/color-picker

 Funs Side Ones:
   activate-power-mode
     https://atom.io/packages/activate-power-mode
   rainbow-delimiters
     https://atom.io/packages/rainbow-delimiters
