# DevOps Unit 4 Workshop

Welcome to the Unit 4 Workshop!

## Our objectives
The objectives for today are:

- Get familiar and comfortable with the TDD workflow
- Get comfortable and capable writing code backed by tests
- Gain insight into what good tests look like
- Understand how good tests enable you to write code more confidently
- Understand how good tests enable you to refactor code more confidently

## Pre-flight checks
This workshop requires you to have a working Python environment on your computer, or if not on your computer, then you can use an ACG environment.

If you're using ACG, you'll need to install VS Code on your ACG instance. We want to see the visual test suite as well as use the debugger today, so we want to be using VS Code regardless of our development setup.

Fortunately, running VS Code on ACG is a relatively simple matter.

### Installing VS Code on ACG
#### Step 1: Spin up an ACG instance
As normal, spin up an ACG cloud server instance using Ubuntu 22.04.

#### Step 2: Add Microsoft keyring
We'll be installing VS Code from Microsoft, and so we need your ACG instance to trust Microsoft's repository. You can do this by running the following 5 commands in your ACG environment:
```bash
sudo apt-get install wget gpg
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" |sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null
rm -f packages.microsoft.gpg
```

#### Step 3: Install VS Code
Once that's done, you can install VS Code:
```bash
sudo apt install apt-transport-https
sudo apt update
sudo apt install -y code
```

#### Step 4: Run VS Code tunnel
We need to run VS Code, but in a way that allows you to access it via a web browser. You can do this by running the following command:
```bash
code tunnel
```

You should then be able to open up the provided link, sign in to GitHub (you may need to do this a couple times), and then be good to go!

## Morning
We are going to start by implementing the rules of Chess in a chess app that has almost everything working apart from the rules of the game itself. 

Please follow these instructions on the repo (which will include cloning the repo to your machine / ACG instance): https://github.com/corndeladmin/DevOps-Chessington-Python/blob/master/during_the_workshop.md

## Afternoon
We'll do a bit more Chessington this afternoon, but we're going to take a detour to practice refactoring code. 
Now we have more of an idea how TDD works, how unit tests work, and how they help you write code to begin with, we want to explore how tests in general can help you refactor code. 
We're going to look at this through the lens of a different kind of test - a snapshot test. 

This test will look and work differently from the Chessington ones - instead of being pytest tests that VS Code integrates with, we have a simple Python script that executes the snapshot test. Running it will tell you if your code complies with the requirements or not.

Please clone this repo to your local machine/ACG server, using the instructions to run it: https://github.com/corndeladmin/DevOps-Gilded-Rose-Python

### Gilded Rose
#### Goal
The Gilded Rose is a popular exercise, originally created by Terry Hughes.
Our principal motivation is that we'd eventually like to be able to add a new feature to some existing code.
But… the code starts off as a bit of a mess. Adding the new feature now is going to be tricky.
So our actual immediate goal is to refactor the code first, and let’s do so with pair programming.
If you get far enough, then as a stretch goal, try adding the new feature in.

#### The Brief
Before we do anything, let's read the brief for Gilded Rose.
> Hi and welcome to team Gilded Rose. 
> As you know, we are a small inn with a prime location in a prominent city run by a friendly innkeeper named Allison. We also buy and sell only the finest goods.
> Unfortunately, our goods are constantly degrading in quality as they approach their sell by date. 
> We have a system in place that updates our inventory for us. It was developed by a no-nonsense type named Leeroy, who has moved on to new adventures.
> First an introduction to our system:
> - All items have a “sell_in” value which denotes the number of days we have to sell the item
> - All items have a “quality” value which denotes how valuable the item is
> - At the end of each day our system lowers both values for every item
> Pretty simple, right? Well this is where it gets interesting:
> - Once the sell by date has passed, Quality degrades twice as fast
> - "Aged Brie" actually increases in Quality the older it gets
> - "Backstage passes" also increase in Quality as its sell_in value approaches but with these rules:
>   - Increases by 1 when there are more than 10 days
>   - Increases by 2 when there are 10 days or less
>   - Increases by 3 when there are 5 days or less but
>   - Quality drops to 0 after the concert
> - "Sulfuras", being a legendary item, doesn’t age or decrease in Quality
> - The Quality of an item is never negative
> - The Quality of an item cannot increase over 50
> 
> Feel free to make any changes to the “update_quality” method in gilded_rose.py.
> 
> Add any new code you like, as long as everything still works correctly - refactor in small steps and run the test frequently.
>
> To keep things simple, do not alter the Item class or “items” property.

#### Step 1: Get set up
- Clone the repo to your machine or ACG instance if you haven't already.
- Follow the instructions in the README to get set up and run the test.

#### Step 2: Refactor the code
We want to add a new feature, but right now it's tricky to figure out what is going on.

Before we add anything new, we should refactor the code.

Remember to:
- Keep each refactor small
- Run your test after each refactor
- Commit after each refactor
- Swap pairing roles frequently

**Hints**
- It’s hard to understand everything at once… is there a small piece that you can start with?
- What makes it hard to understand at first? Can you fix that?
- Check out the next slides for some potential concerns to observe
- It’s a really long method… would it be possible to split it up at all?

*...Still stuck on what to refactor first?*

You want to make changes that make the code easier to read.

So try:
- Renaming variables to be more descriptive
- Introducing more variables - it can simplify how the logic reads
- Extracting functions - if you see a block of code that does something, especially if it's done in multiple places, it can be extracted to a named function, and doing so can often make your code more readable. Experiment! If you don't like the result, you can always undo it.

#### Step 3: Stretch goal: Add the new feature
If you've refactored the code and you're feeling confident, try adding the new feature.

> We have recently signed a supplier of conjured items. This requires an update to our system:
> - "Conjured" items degrade in Quality twice as fast as normal items

Have a go at implementing this now – it should be easier having refactored the code.
Your Golden Master test checks that the behaviour doesn’t change… but in this case we have changed the behaviour, so your test is going to fail.

Try fixing the test.

This is one of the downsides of this style of testing. Different kinds of tests have advantages and disadvantages - reflect on this, as we generally need to use a variety of tests to meet all your needs with the minimum of downsides!
