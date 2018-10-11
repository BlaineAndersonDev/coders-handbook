# Rails Refresher (Rails 5.0+)
___
##### Authors Note:
  > This guide is one of many written by [Blaine Anderson](https://github.com/BlaineAndersonDev).
  > You can find this and the rest of his guides in a special Github repository called [The Coders Handbook](https://github.com/BlaineAndersonDev/coders-handbook).
___

###### ------------------------------------------------------------------
#### Easily forgettable commands & amazing resources for using Rails:
###### Help Commands:
  * `rake -T`/`rails -T`: A useful command list

###### Local Database:
  * `rails db:drop`
  * `rails db:create`
  * `rails db:migrate`
  * `rails db:seed`
  * `rails db:migrate:reset`
  * `rails console` :Covered in-depth in it's own section.

###### Rails Console:
  * There are **many** SQL commands, but I will cover some of the more common ones and provide examples for each:
    * `Object.new` : Creates a new 'Object' with nil fields.
    * `Object.new(field: 'filler')` : Creates a new 'Object' filled with provided fields.
    * `Object.valid?` : Checks if the 'Object' is valid and returns a boolean.
    * `Object.[field]` : Returns the specified field from that specific 'Object'
    * `Object.created_at` : Returns the timestamp for when the 'Object' was created.
    * `Object.updated_at` : Returns the timestamp for when the 'Object' was last updated.
    * `Object.save` : Saves the 'Object' into the database as long as its 'valid'.
    * `Object.save!` : Saves the 'Object' into the database as long as its 'valid' else it returns an error. (Only use during debugging).
    * `Object.create` : Creates and saves the 'Object' into the database as long as its 'valid' and returns the 'Object'.
    * `Object.create!` : Creates and saves the 'Object' into the database as long as its 'valid' and returns the 'Object' else it returns an error. (Only use during debugging).
    * `Object.find(integer)` : Searches the database for the index (integer) of that 'Object' and returns it if it exists.
    * `Object.find_by(field: "field_entry")` : Searches the database for the field & field_entry of that 'Object' and returns the 'Object' if it exists.
    * `Object.first` : Searches the database returns the first indexed 'Object' if it exists.
    * `Object.all` : Searches the database returns every 'Object' if any exists.

    * These examples assume there is a "User" model with "Name" & "Email" fields:
    ~~~~
        >> User.new
        => #<User id: nil, name: nil, email: nil, created_at: nil, updated_at: nil>

        >> user = User.new(name: "Michael Hartl", email: "mhartl@example.com")
        => #<User id: nil, name: "Michael Hartl", email: "mhartl@example.com", created_at: nil, updated_at: nil>

        >> user.valid? #Returns a boolean value of true if valid.
        => #true

        >> user.save #Saves the user to the database provided the user is valid, and provides a boolean on success or failure.
         (0.1ms)  SAVEPOINT active_record_1
         SQL (0.8ms)  INSERT INTO "users" ("name", "email", "created_at",
         "updated_at") VALUES (?, ?, ?, ?)  [["name", "Michael Hartl"],
         ["email", "mhartl@example.com"], ["created_at", 2016-05-23 19:05:58 UTC],
         ["updated_at", 2016-05-23 19:05:58 UTC]]
         (0.1ms)  RELEASE SAVEPOINT active_record_1
        => true

        >> user.name #Returns the variable "user"'s name.
        => "Michael Hartl"

        >> user.email #Returns the variable "user"'s email.
        => "mhartl@example.com"

        >> user.updated_at #Returns the variable "user"'s updated_at timestamp.
        => Mon, 23 May 2016 19:05:58 UTC +00:00

        >> User.create(name: "A Nother", email: "another@example.org")
        #<User id: 2, name: "A Nother", email: "another@example.org", created_at: "2016-05-23 19:18:46", updated_at: "2016-05-23 19:18:46">

        >> foo = User.create(name: "Foo", email: "foo@bar.com")
        #<User id: 3, name: "Foo", email: "foo@bar.com", created_at: "2016-05-23 19:19:06", updated_at: "2016-05-23 19:19:06">

        >> User.find(1)
        => #<User id: 1, name: "Michael Hartl", email: "mhartl@example.com", created_at: "2016-05-23 19:05:58", updated_at: "2016-05-23 19:05:58">

        >> User.find(3)
        ActiveRecord::RecordNotFound: Couldn't find User with ID=3

        >> User.find_by(email: "mhartl@example.com")
        => #<User id: 1, name: "Michael Hartl", email: "mhartl@example.com",
        created_at: "2016-05-23 19:05:58", updated_at: "2016-05-23 19:05:58">

        >> User.first
        => #<User id: 1, name: "Michael Hartl", email: "mhartl@example.com",
        created_at: "2016-05-23 19:05:58", updated_at: "2016-05-23 19:05:58">

        >> User.all
        => #<ActiveRecord::Relation [#<User id: 1, name: "Michael Hartl",
        email: "mhartl@example.com", created_at: "2016-05-23 19:05:58",
        updated_at: "2016-05-23 19:05:58">, #<User id: 2, name: "A Nother",
        email: "another@example.org", created_at: "2016-05-23 19:18:46",
        updated_at: "2016-05-23 19:18:46">]>
    ~~~~

    * Manipulating/Updating "Objects" in database:
      * Keep in mind you **must** user `Object.save` when finished or the changes won't be permanently made to the "Object".
      * `Object.[field] = "new_field_value"` : Updates the specified field from that specific 'Object' to the "new_field_value".
      * `Object.update_attribute(name: "The Dude")` : Update a single value.
      * `Object.update_attributes(name: "The Dude", email: "dude@abides.org")` : Update multiple values at once.
      * `Object.errors.full_messages` : If the "Object" is invalid, this will provide a full error messages regarding why.
      ~~~~
          >> user.email = "mhartl@example.net"
          => "mhartl@example.net"
          >> user.save
          => true

          >> user.update_attribute(:name, "El Duderino")
          => true
          >> user.name
          => "El Duderino"

          >> user.update_attributes(name: "The Dude", email: "dude@abides.org")
          => true
          >> user.name
          => "The Dude"
          >> user.email
          => "dude@abides.org"

          >> user.errors.full_messages
          => ["Name can't be blank"]
      ~~~~

###### Branch Control:
  * `git reset --hard HEAD`: Resets the branch to the last commit. Use with caution!
  * `git checkout -b [BRANCH-NAME]`: The `-b` allows the creation of a new branch. `co` can be used in place of `checkout`.

###### Connecting Local & Remote Repos:
  * `git remote add origin [LINK TO NEW GITHUB REPO]`: Connect a remote repo to your local repo.

###### Heroku:
  * `heroku create`: Creates a Heroku repo for you to use.
  * `git push heroku master`: uploads the MASTER branch to Heroku to be deployed live.
  * `https://ancient-retreat-50009.herokuapp.com/`: Once done the link to the live site should be similar to this.
  * `heroku logs`: Shows the console activity (and errors) on the Heroku web server.

###### Rspec Installation & Commands:
  * [RSpec Matcher Guide](https://relishapp.com/rspec/rspec-expectations/v/3-7/docs/built-in-matchers)
  * Use `gem install rspec-rails` in the CLI or place `gem 'rspec-rails'` into the gemfile manually. The use `bundle install.`.
  * `rails g rspec:install`: Install RSpec via the Command Line AFTER implementing the gem using `bundle install`.
  * `be rspec -fd`: Runs the RSpec tests. `rspec` will also work but may prompt an error. `-fd` generates a more in-depth report.
  * `be rspec spec/[folder/filename] -fd`: Allows you to specify what folder or file you want to test individually.
  * [Rspec Spec Generator Guide](https://relishapp.com/rspec/rspec-rails/docs/generators)
    * `rails generate rspec:model [model name]`
    * `rails generate rspec:controller [controller name]`
  * [Rspec Model Test Guide](https://semaphoreci.com/community/tutorials/how-to-test-rails-models-with-rspec)
    * [**Ex**]: `let(:object) { User.new(name: => "Jane Doe", :email => "jane@doe.com", :password => "pw1234", :password_confirmation => "pw1234") }`
  * [Rspec View Test Guide](http://ruby-journal.com/how-to-write-rails-view-test-with-rspec/)
  * [Rspec Controller Test Guide](https://everydayrails.com/2012/04/07/testing-series-rspec-controllers.html)
  * [Rspec Route Test Guide](http://geekhmer.github.io/blog/2014/07/30/test-routes-with-rspec-in-ruby-on-rails/)

###### ------------------------------------------------------------------
#### Rails Generate Commands:
  * [RoR Generation Guide.](http://guides.rubyonrails.org/command_line.html#rails-generate)
  * `rails g` can be used as a shortcut command.
  * `rails d` can be used to destroy the generation if you need to redo it.

###### Controller Generation:
  * [Personal Preference Controller Generation Guide](https://www.sitepoint.com/building-your-first-rails-application-views-and-controllers/)
  * `rails g controller [Name of object in CamelCase] [Routes to include with options]`
  * `rails g controller StaticPages home help`

###### Model Generation:
  * [Personal Preference Model Generation Guide 1](https://railsguides.net/advanced-rails-model-generators/)
  * [Personal Preference Model Generation Guide 2](https://richonrails.com/articles/rails-model-generator-shortcuts)
  * `rails g model [model name] [field:fieldtype]`
  * `rails g controller user username email:string age:integer`
  * Each `field` may be assigned a field type. This defaults to `(field):string`.
  * Available field types are: `integer` `primary_key` `decimal` `float` `boolean` `binary` `string` `text` `date` `time` `datetime` `timestamp`.
  * Model Validations:
    * [RoR Validation Guide](http://guides.rubyonrails.org/active_record_validations.html)
    * [In-Depth Regex Email Validations](https://stackoverflow.com/questions/201323/using-a-regular-expression-to-validate-an-email-address)
    * If your "User" model has the fields "name" & "email" you can add required validations to ensure they are formatted properly.
    * `validates :[field]`: This is the simplest validation. It requires only that the field is not `nil`. (So `blank` is fine.)
    * `validates :[field], presence: [true/false]`: Requires that the field is not `blank`
    * `validates :[field], length: { maximum: 50 }`: Requires that the field be under the provided maximum length of characters.
    * `validates :[field]format: { with: [Regex_Formula] }`: Requires that the field successfully pass the Regex format.
    * `validates :[field]uniqueness: [true/false]`: Requires that the field be one of a kind.
    * `validates :[field]uniqueness: { case_sensitive: [true/false] }`: Allows you to set case_sensitive uniqueness. It is true by default.

    * User Migration Example:
    ~~~~
        class CreateUsers < ActiveRecord::Migration[5.1]
          def change
            create_table :users do |t|
              t.string :name
              t.string :email

              t.timestamps
            end
          end
        end
    ~~~~
    * User Model Example:
    ~~~~
        class User < ApplicationRecord
          validates :name,  presence: true, length: { maximum: 50 }
          validates :email, presence: true, length: { maximum: 255 }
        end
    ~~~~

###### ------------------------------------------------------------------
#### Adding Models/Views/Controllers Manually(Including Tests)(No Generators):
###### Models:
  *

###### Views:
  *

###### Controllers:
  * Using TDD(Test Driven Development) we will create a failing RSpec test to start with.
  * Open the RSpec spec file `spec/controllers/static_pages_controller_spec.rb` and create a test:
    ~~~~
      describe "GET #about" do
        it "returns http success" do
          get :about
          expect(response).to have_http_status(:success)
        end
      end
    ~~~~
  * [**RSpec**]: Run Rspec in Terminal.
  * [**Error**]: The error should now be: `No route matches {:action=>"about", :controller=>"static_pages"}`.
  * [**Solve**]: Add `get  'static_pages/about'` to `config/routes.rb`.
  * [**RSpec**]: Run Rspec in Terminal.
  * [**Error**]: The error should now be: `The action 'about' could not be found for StaticPagesController`.
  * [**Solve**]: Now add the route into the controller: `app/controllers/static_pages_controller.rb`
    ~~~~
      def about
      end
    ~~~~
  * [**RSpec**]: Run Rspec in Terminal.
  * [**Error**]:The error should now be: `StaticPagesController#about is missing a template for this request format and variant.`
  * [**Solve**]: Now create a view for the controller route: `touch app/views/static_pages/about.html.erb`
  * [**Side Note**]: While the controller is complete, you should also create a spec file for testing the view later in `spec/views/static_pages/about.html.erb_spec.rb`
  * [**Complete**]: The test should now be passing and you have a new route in your controller!


###### ------------------------------------------------------------------
#### Rails Helpers & Routing:
###### **Named** Route Examples:
~~~~
  Page	     URL	     Named route
  Home	     /	         root_path
  About	     /about	     about_path
  Help	     /help	     help_path
  Contact	 /contact	 contact_path
  Sign up	 /signup	 signup_path
  Log in	 /login	     login_path

  Using "resources :users" will provide:
  get "/users" # -- index on your controller
  get "/users/:id" # -- show on your controller
  get "/users/new" # -- new method on your controller
  post "/users" # -- create on your controller
  get "/users/:id/edit" # -- edit method on your controller
  put "/users/:id" # -- update on your controller
  patch "/users/:id" # -- update on your controller
  delete "/users/:id" # -- destroy on your controller
~~~~

##### Routing:
* [RESTful Routing](https://richonrails.com/articles/understanding-rails-routing)
* All routes are defined in `config/routes.rb`.
* `_path` is the normal route to use when using Rails Helpers.
* `_url` is generally only used for redirects with no exchange of information.
* The difference between `_path` & `_url` is the url version includes the entire url instead of a relative route.

  * **Root Route**
    * The root is a special route and therefore is slightly different than regular routes using "root" instead of "get" etc.
    * [**Normal Route**]: `get 'root 'static_pages#home'`.
    * [**Ex**]: `root_path -> '/'` - `root_url  -> 'http://www.example.com/'`
    * [**Rails Helper**] The root can be accessed as the route `root_path`. Ex: `<%= link_to "Home", root_path %>`
    * [**Rails Helper**] It can also be accessed as a route with `root_url`. Ex: `<%= link_to "Home", root_url %>`
    * [**HTML**] It can also be accessed as an HTML route `'/'`. Ex: `<a href="/">Home</a>`

  * **Normal Routes**
    * [**Normal Route**]: `get 'static_pages/help'`.
    * [**Ex**]: `help_path -> '/help'` - `help_url  -> 'http://www.example.com/static_pages/help'`
    * [**Rails Helper**] This route can be accessed with `help_path`. Ex: `<%= link_to "Help", help_path %>`
    * [**Rails Helper**] It can also be accessed with `help_url`. Ex: `<%= link_to "Help", help_url %>`
    * [**HTML**] It can also be accessed using HTML `'/static_pages/help'`. Ex: `<a href="/static_pages/help">Help</a>`

  * **Custom Routes**
    * Sometimes we want a page to be accessed via a different route than RESTful. You would then need a custom route.
    * Let's change our "Normal" route to a "Custom" route. This will change the `_path` & `_url`.
    * [**Normal Route**]: `get 'static_pages/help'` is originally access using:
      * `<%= link_to "Help", help_path %>`
      * `<a href="/static_pages/help">Help</a>`
    * [**Custom Route**]: `get  '/help', to: 'static_pages#help'` is now accessed using:
      * `<%= link_to "Help", help_path %>`
      * `<a href="/help">Help</a>`
      * [**Ex**]: `help_path -> '/help'` - `help_url  -> 'http://www.example.com/help'`


##### Rails Helpers:
  * **Link_To**:
    * [RoR link_to Guide](http://guides.rubyonrails.org/getting_started.html)
    * Creating a Link:
      * [**Rails Example**]: `<%= link_to "About", about_path %>`
      * [**HTML Example**]: `<a href="/static_pages/about">About</a>`
      * [**Rails Helper**]: `<%= link_to 'LinkName', http://LinkToPlace.org %>`
      * [**Rails Helper**]: `<%= link_to 'LinkName', any_routes_path %>`
      * [**Raw HTML**]: `<a href="http://LinkToPlace.org">LinkName</a>`
      * [**Raw HTML**]: `<a href="/ViewFolder/View">LinkName</a>`

    * Creating an Image as a Link:
      * [**Example**]: `<%= link_to image_tag("rails.png", alt: "Rails logo"), 'http://rubyonrails.org/' %>`
      * [**Rails Helper**]: `<%= link_to image_tag("ImageName.Extension", alt: "AlternateName"), 'http://LinkToPlace.org' %>`
      * [**Raw HTML**]: `<a href="http://LinkToPlace.org"><img alt="AlternateName" src="/ViewFolder/ImageName.Extension" /></a>`
      *

  * **Form_For**:
    * Creating a Form:
    * [Tutorial: Chapter 7.2 Signup form](https://www.railstutorial.org/book/sign_up#sec-signup_form)
    * [RoR form_for Guide](http://guides.rubyonrails.org/form_helpers.html)
    ~~~~
        <h1>Sign up</h1>

        <div class="row">
            <%= form_for(@user) do |f| %>
              <%= f.label :name %>
              <%= f.text_field :name %>

              <%= f.label :email %>
              <%= f.email_field :email %>

              <%= f.label :password %>
              <%= f.password_field :password %>

              <%= f.label :password_confirmation, "Confirmation" %>
              <%= f.password_field :password_confirmation %>

              <%= f.submit "Create my account", class: "btn btn-primary" %>
            <% end %>
        </div>
    ~~~~
      * `<%= form_for(@user) do |f| %>` The "@user" implies to Rails that we want to create namespaced data using "user[field]"
      * [**Ex**]: `<%= f.text_field :name %>` - NameSpaced: user[name]
      * [**Ex**]: `<%= f.email_field :name %>` - NameSpaced: user[email]
      * [**Ex**]: `<%= f.password_field :password %>` - NameSpaced: user[password]
      * [**Ex**]: `<%= f.password_field :password_confirmation %>` - NameSpaced: user[password_confirmation]
      * All these Namespaced fields together create a params hash: {name: user[name], email: user[email], password: user[password], password_confirmation: user[password_confirmation]}
      * The Rails Helper version VS. the HTML version:
      ~~~~
          #Rails:
            <%= f.label :name %>
            <%= f.text_field :name %>
          #html
            <label for="user_name">Name</label>
            <input id="user_name" name="user[name]" type="text" />
      ~~~~

##### Creating Sessions:
  * Sessions is the browser based "User ID" that allow a User to persistently be logged in on any given page of a website or program.
  * This requires you to already have a User database setup. The following steps provide a blueprint to expand on:
    * **Routes: `config/routes.rb`**:
      ~~~~
          get    '/login',   to: 'sessions#new'`
          post   '/login',   to: 'sessions#create'
          delete '/logout',  to: 'sessions#destroy'`
      ~~~~
    * **Sessions View: `app/views/sessions/new.html.erb`**
      ~~~~
          <h1>Log in</h1>

          <div class="row">
            <div class="col-md-6 col-md-offset-3">
              <%= form_for(:session, url: login_path) do |f| %>

                <%= f.label :email %>
                <%= f.email_field :email, class: 'form-control' %>

                <%= f.label :password %>
                <%= f.password_field :password, class: 'form-control' %>

                <%= f.submit "Log in", class: "btn btn-primary" %>
              <% end %>

              <p>New user? <%= link_to "Sign up now!", signup_path %></p>
            </div>
          </div>
      ~~~~
    * **Sessions Controller: `app/controllers/sessions_controller.rb`**
      ~~~~
          def new
          end

          def create
            user = User.find_by(email: params[:session][:email].downcase)
            if user && user.authenticate(params[:session][:password])
              # Log the user in and redirect to the user's show page.
            else
              # Create an error message.
              flash.now[:danger] = 'Invalid email/password combination'
              render 'new'
            end
          end

          def destroy
          end
      ~~~~
    * **FILLER**
      ~~~~
      ~~~~
    * **FILLER**
      ~~~~
      ~~~~

###### ------------------------------------------------------------------
#### Building your own Authentication System in Rails:
###### Basics:
  * Rails has a built in method called `has_secure_password` that when placed in a model (generally "User") provides the following:
    * The ability to save a securely hashed `password_digest` attribute to the database
    * A pair of virtual attributes (`password` and `password_confirmation`), including presence validations upon object creation and a validation requiring that they match
    * An authenticate method that returns the user when the `password` is correct (and false otherwise)
  * The only requirement for `has_secure_password` to work its magic is for the corresponding model (User) to have an attribute called `password_digest`.
  * You can generate a User model that includes it right off with the following command:
    * ``
  * Or you can add it to an already created User model by creating a new migration:
    * `rails generate migration add_password_digest_to_users password_digest:string`
    * This migration "`add_password_digest_to_users`" uses Rails methods to "`add_`" the "`password_digest_`" "`to_users`".
  * User Model


###### ------------------------------------------------------------------
#### Additional Resources:
###### Markdown:
  * [Markdown CheatSheet](https://en.support.wordpress.com/markdown-quick-reference/)
  * [Markdown Previewer](https://jbt.github.io/markdown-editor/)

###### CSS:
  * [Flexbox)](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
  * [Coolors.co](https://coolors.co/)
  * [Keep Footers Down](http://matthewjamestaylor.com/blog/keeping-footers-at-the-bottom-of-the-page)
  * []()

###### SASS:
  * [SASS Docs)](http://sass-lang.com/)
  * []()

###### Regex:
  * [Rublar)](http://www.rubular.com/)
  * []()
