# Coder Installation Guide
##### This Guide focus' on Rails & ReactJS + all associated technologies.

##### Authors Note:
  > I wrote this guide for my future self. My Mac had a complete crash, forcing me to reinstall my OS.
  > I was mid-project and hadn't done a full fledged installation in about a year. While I did look for a straightforward guide to see me through, I was unable to fine a simple and easy one.  
  > So I wrote my own!
  > I hope this helps some poor unfortunate soul who just wants to get back to coding :)

### All Technologies:
  * This guide was based on:
    * [Rails Guide](http://installrails.com/)

  * __Update__: Make sure your OS is fully updated via the App Store.

  * __Install__: [Iterm2](https://www.iterm2.com/)
    * (Recommendation): Update Terminal Display Name
      * Set `sudo scutil --set ComputerName <new_name>`
      * Set `sudo scutil --set LocalHostName <new_name>`
      * Set `sudo scutil --set HostName <new_name>`
      * Perform `dscacheutil -flushcache`
      * Restart Mac before continuing.
    * (Recommendation): Alter text & colors on the command line. (After Git Installation)
      * After installation you can make some edits to the colors and text provided in the shell. For example, you can have the line tell you the current Git status, or provide your HostName at the beginning of the line.
      * You'll need to alter two files using Atom (using `open <file-name>` won't work on one of the files we have to alter).
        * Go to your root directory and open `.git_prompt.sh`. If you don't have this file, create it.
          * Paste in the code provided [HERE](https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh).
          * Do not make changes without doing research!
          * This code provides "Bash Profile" all the mechanics to show Git status.
        * Now go to your root directory and open `.bash_profile`.
          * Paste in the following code at the bottom of the file:
          ```

          # store colors
          MAGENTA="\[\033[0;35m\]"
          YELLOW="\[\033[01;32m\]"
          BLUE="\[\033[00;34m\]"
          LIGHT_GRAY="\[\033[0;37m\]"
          CYAN="\[\033[0;36m\]"
          GREEN="\[\033[00m\]"
          RED="\[\033[0;31m\]"
          VIOLET='\[\033[01;35m\]'
          # Additional color options: https://misc.flogisoft.com/bash/tip_colors_and_formatting#terminals_compatibility

          function color_my_prompt {
            local __user_and_host="$GREEN\u@\h"
            local __cur_location="$BLUE\W"           # capital 'W': current directory, small 'w': full file path
            local __git_branch_color="$GREEN"
            local __prompt_tail="$VIOLET$"
            local __user_input_color="$GREEN"
            local __git_branch='$(__git_ps1)';

            # colour branch name depending on state
            if [[ "$(__git_ps1)" =~ "*" ]]; then     # if repository is dirty
                __git_branch_color="$RED"
            elif [[ "$(__git_ps1)" =~ "$" ]]; then   # if there is something stashed
                __git_branch_color="$MAGENTA"
            elif [[ "$(__git_ps1)" =~ "%" ]]; then   # if there are only untracked files
                __git_branch_color="$CYAN"
            elif [[ "$(__git_ps1)" =~ "+" ]]; then   # if there are staged files
                __git_branch_color="$YELLOW"
            fi

            # Build the PS1 (Prompt String)
            PS1="$__user_and_host $__cur_location$__git_branch_color$__git_branch $__prompt_tail$__user_input_color "
          }

          # configure PROMPT_COMMAND which is executed each time before PS1
          export PROMPT_COMMAND=color_my_prompt

          # if .git-prompt.sh exists, set options and execute it
          if [ -f ~/.git-prompt.sh ]; then
            GIT_PS1_SHOWDIRTYSTATE=true
            GIT_PS1_SHOWSTASHSTATE=true
            GIT_PS1_SHOWUNTRACKEDFILES=true
            GIT_PS1_SHOWUPSTREAM="auto"
            GIT_PS1_HIDE_IF_PWD_IGNORED=true
            GIT_PS1_SHOWCOLORHINTS=true
            . ~/.git-prompt.sh
          fi
          ```
          * Note that you can alter this file to your liking.
          * The provided code will show the branch with a symbol and color based on its current status:
            COLOR | SYMBOL | DESCRIPTION
            *GRAY* | __>__ | The file is currently unaltered.
            *RED* | __*__ | The file has been altered & `git add` __has not__ been used.
            *YELLOW* | __+__ | The file has been altered & `git add` __has__ been used.
            *MAGENTA* | __$__ | There are stashed changes.
            *CYAN* | __%__ | A file was created that `.gitignore` will not allow to be comitted.
          * I will also note I prefer to have a static name instead of my user or host name on the command line. I replace `$__user_and_host` with `\[\e[1;93mBlaines_Mac\]`

  * __Install__: [Atom](https://atom.io/)
    * After installation install the shell commands. I.E. `atom .` (Atom -> Install Shell Commands)
    * (Recommendation): Enable the Autosave Package that comes pre-installed:
      * Open Preferences (Atom -> Preferences)
      * Selected "packages" from the left side bar.
      * Input "autosave" and select "settings" when it appears.
      * Checkmark the "enable" box.
    * (Recommendation): Additional Packages (What I Use):
      * All the following package names can be copied and pasted into Atom's Package finder.
      * __Themes__ (Great highlighting, easy on the eyes):
        * UI: [steam-pirate-ui](https://atom.io/themes/steam-pirate-ui)
        * Syntax: [steam-pirate-syntax](https://atom.io/themes/steam-pirate-syntax)
      * __Core__:
        * [atom-beautify](https://atom.io/packages/atom-beautify)
        * [auto-detect-indentation](https://atom.io/packages/auto-detect-indentation)
        * [auto-update-packages](https://atom.io/packages/auto-update-packages)
        * [autoclose-html](https://atom.io/packages/autoclose-html)
        * [busy-signal](https://atom.io/packages/busy-signal)
        * [emmet](https://atom.io/packages/emmet)
        * [file-icons](https://atom.io/packages/file-icons)
        * [highlight-selected](https://atom.io/packages/highlight-selected)
        * [neon-selection](https://atom.io/packages/neon-selection)
        * [pigments](https://atom.io/packages/pigments)
        * [teletype](https://atom.io/packages/teletype)
        * [linter](https://atom.io/packages/linter)
      * __HTML/CSS__:
        * [linter-tidy](https://atom.io/packages/linter-tidy)
        * [css-snippets](https://atom.io/packages/css-snippets)
        * [linter-sass-lint](https://atom.io/packages/linter-sass-lint)
      * __Rails/Ruby__:
        * [rails-snippets](https://atom.io/packages/rails-snippets)
        * [ruby-block](https://atom.io/packages/ruby-block)
        * [linter-erb](https://atom.io/packages/linter-erb)
      * __React/Javascript__:
        * [language-babel](https://atom.io/packages/language-babel)
        * [react-es6-snippets](https://atom.io/packages/react-es6-snippets)
        * [jquery-snippets](https://atom.io/packages/jquery-snippets)
        * [react-snippets](https://atom.io/packages/react-snippets)
      * __Utility__:
        * [linter-jsonlint](https://atom.io/packages/linter-jsonlint)
        * [markdown-preview-plus](https://atom.io/packages/markdown-preview-plus)
        * [atom-clock](https://atom.io/packages/atom-clock)
        * [color-picker](https://atom.io/packages/color-picker)
      * __Fun__:
        * [activate-power-mode](https://atom.io/packages/activate-power-mode)

  * __Install__ : XCode
    * Via the App Store: [XCode](https://itunes.apple.com/us/app/xcode/id497799835?mt=12)
    * Via command line (Personal preference): `xcode-select —install`

  * __Create__: Global .gitignore
    * Head to the root directory (/Users/you-user-name).
    * Create a file called .gitignore: `touch .gitignore`.
    * Open the file and paste in this code:
      ```
      # Compiled source #
      ###################
      *.com
      *.class
      *.dll
      *.exe
      *.o
      *.so

      # Packages #
      ############
      # it's better to unpack these files and commit the raw source
      # git has its own built in compression methods
      *.7z
      *.dmg
      *.gz
      *.iso
      *.jar
      *.rar
      *.tar
      *.zip

      # Logs and databases #
      ######################
      *.log
      *.sql
      *.sqlite

      # OS generated files #
      ######################
      .DS_Store
      .DS_Store?
      ._*
      .Spotlight-V100
      .Trashes
      ehthumbs.db
      Thumbs.db

      # User generated files #
      ######################
      .env
      ```
      * Based on the `.gitignore` provided by [Octocat](https://gist.github.com/octocat/9257657)

  * __Install__: [HomeBrew](https://brew.sh/)
    * `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
    * Check that HomeBrew is functional: `brew doctor`

### Git Guide:
  * __Install__: [Git](https://git-scm.com/)
    * `brew install git`
    * `git config --global user.name "Your Actual Name"`
    * `git config --global user.email "Your Actual Email"`
    * Make sure they are correct: `git config -l`
    * (Recommendation): Setup Autocomplete':
      * This will allow you to press `tab` to autocomplete a branch name or git based command.
      * Go to your root directory and open `.git-completion.bash`. If you don't have this file, create it.
        * Paste in the code provided [HERE](https://github.com/git/git/blob/master/contrib/completion/git-completion.bash).
        * Do not make changes without doing research!
        * This code provides "Bash Profile" all the mechanics to autocomplete Git queries.
      * Now go to your root directory and open `.bash_profile`.
        * Paste in the following code at the top of the file:
        ```
        if [ -f ~/.git-completion.bash ]; then
          . ~/.git-completion.bash
        fi
        ```
        * Close and reopen your terminal for the changes to take effect.
        * Go and create a new branch in any project and use `tab` to autocomplete the name. Voila!
    * (Recommendation): Setup Alias':
      * An Alias is a 'shortcut' command such as `git co <Branch_Name>` instead of typing out `git checkout <Branch_Name>`
      * You can add an Alias using a command (Edit to fit your need alias)
      ```
      git config --global alias.co checkout
      ```
      * Or you can manually add it to `~/.gitconfig`
    * (Recommendation): Personal Access Tokens
      * Presuming you set up two-factor authorization for github (If you haven't shame on you, go do it NOW!), then added a PAT (Personal Access Token) will allow you to push and pull to any associated repo without having to retype your password in the terminal each time.
      * Go to Github and open settings, then PAT tokens. (Github -> Settings -> Tokens -> Personal access tokens)
      * Generate a new token and select all the options you require. (I did everything, but I dont leave my computer open for others to use).
      * Copy the PAT it provides and dont lose it, you'll have to delete it and make a new one if you lose it.
      * In terminal perform any action that requires credentials (Such as pushing a repo up). Enter your Github Username and instead of your password, enter the Personal Access Token.
        * You should now be able to perform any action on any repo without having to enter the damn user and password now!
    * (IF YOUR NOT USING Personal Access Tokens): Setup SSH Keys:
      * Check to see if you already have an SSH key (If you just flattened your OS, you shouldn't): `cd ~/.ssh `
      * If it replies with “No such file or directory” proceed with the following steps:
        * `ssh-keygen -t rsa -C "your_email@domain.com"`
        * When it asks you to enter a file name in which to save the key, just press return/enter (leave the prompt blank).
        * You will then be asked to enter a passphrase and confirm it. Use a password your comfortable with.
          * If you've messed up during these steps, you can cancel out using `control + C`.
        * You'll need the newly generated SSH key for github. Grab it using: `pbcopy < ~/.ssh/id_rsa.pub`
      * Now we need to add the key to your Github:
        * Open Github.
        * Click your profile and click on "Settings".
        * Click "SSH and GPG keys" on the left menu.
        * Select "New SSH Key" and enter a memorable computer name for the computer your using.
        * Paste the SSH key you copied from the terminal using `pbcopy < ~/.ssh/id_rsa.pub`.
        * Save (and likely re-enter your Github Password).
      * Authenticate in terminal (if required):
        * Enter `ssh -T git@github.com`
        * IF it replies with `The authenticity of host 'github.com (XXX.XX.XXX.XXX)' can't be established.` then:
          * Type `yes` you wish to continue connecting.
          * Enter your SSH password once more.
          * Success!

### Rails Guide:
  * __Install__: [RVM (Ruby Version Manager)](https://rvm.io/)
    * `\curl -L https://get.rvm.io | bash -s stable`
    * Close and reopen your terminal.
    * Make sure RVM is running properly with `rvm | head -n 1`
  * __Install__: [Ruby](https://www.ruby-lang.org/en/)
    * `rvm use ruby --install --default`
    * Make sure Ruby is running properly with `ruby -v`
  * __Install__: [Rails](https://rubyonrails.org/)
    * `gem install rails --no-ri --no-rdoc`
    * Make sure Rails is running properly with `rails --version`
  * __Verify Installation__:
    * Create a Rails app and start it on your local server using `rails server`
    * Navigate to "http://localhost:3000/".

### ReactJS Guide:
  * __Install__: [Yarn](https://yarnpkg.com/lang/en/docs/install/#mac-stable)
    * Yarn is a replacement for [NPM](https://www.npmjs.com/).
    * `brew install yarn`
    * `yarn init`
    * Make sure Yarn is running properly with `yarn --version`
  * __Install__: [NVM (Node Version Manager)](https://github.com/creationix/nvm)
    * `curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash`
    * Close and reopen terminal.
    * Head to the root directory (/Users/you-user-name).
    * Open `.bash_profile` and paste the following code at the bottom:
      ```
      export NVM_DIR="$HOME/.nvm"
      . "/usr/local/opt/nvm/nvm.sh"
      ```
    * Close and reopen terminal.
    * Make sure NVM is running properly with `command -v nvm` (It should reply with `npm`. If it does not, it was not installed properly. Check the [NVM Readme](https://github.com/creationix/nvm))
  * __Install__: [Node](https://nodejs.org/en/)
    * `nvm install node`
    * Make sure Node is running properly with `node -v`
  * __Install__ __{Not Required if you user create-react-app}__: [Babel](https://babeljs.io/)
    * `yarn add babel-cli --dev`
    * create a file called `.babelrc` and paste the following into it:
    ```
    {
      "presets" : ["es2015", "react"]
    }
    ```
  * __Install__: [create-react-app](https://github.com/facebook/create-react-app)
    * `yarn add create-react-app`
    * To create React Apps use: `yarn create-react-app (your-apps-name)`
  * __Install__: [create-react-native-app](https://github.com/react-community/create-react-native-app/)
    * `yarn add create-react-native-app`
    * To create React Native Apps use: `yarn create-react-native-app (your-apps-name)`
  * __Verify Installation__:
    * Create a ReactJS app and start it on your local server using `yarn start`
    * Navigate to "http://localhost:3000/".

### Suggested Refresher Courses (Provided by CodeCademy):
  * [CommandLine](https://www.codecademy.com/learn/learn-the-command-line)
  * [Git](https://www.codecademy.com/learn/learn-git)
  * [HTML](https://www.codecademy.com/learn/learn-html)
  * [CSS](https://www.codecademy.com/learn/learn-css)
  * [Ruby](https://www.codecademy.com/learn/learn-ruby)
  * [Rails](https://www.codecademy.com/learn/learn-rails)
  * [Javascript](https://www.codecademy.com/learn/introduction-to-javascript)
  * [ReactJS P1](https://www.codecademy.com/learn/react-101)
  * [ReactJS P2](https://www.codecademy.com/learn/react-102)
  * [Node/SQLite](https://www.codecademy.com/learn/learn-node-sqlite)
  * [JQuery](https://www.codecademy.com/learn/learn-jquery)
