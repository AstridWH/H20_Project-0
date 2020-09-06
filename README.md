# Project 0
https://github.com/AstridWH/Project-0.git
https://github.uio.no/IN1910/H20_project0_astridwh.git

First. I forgot to make my repo as a UiO user, and
made it in my own profile instead. I tried to 
change the link, but I couldn't push after that.
So I changed the link back. The uppermost link is
the original. The 2nd one is the uio one that I may
or may not have maneaged to change it to. We'll 
only know after I've changed it, and then I can't 
commit. Sorry about this.

My main problem with this whole thing was pytest.
It refused to work. I've spendt hours trying to fix
it. First I got 
"bash: /c/Users/astri/AppData/Local/Microsoft/WindowsApps/python: Permission denied"
Then I "fixed it" and got
"bash: /c/Users/astri/AppData/Local/Microsoft/WindowsApps/python: No such file or directory"
instead. So I have no clue if this code actually
works as it should. All the tests (except 
parametrize) worked fine before I changed the 
variables to be more descriptive and changed the 
"return"s to "assert"s. This is the "help" branch.
Then I had to add @pytest.mark.parametrize. Wich 
didn't work at all. I even got a friend to try it
on his computer. There the "help" branch worked 
fine with pytest, but @pytest.mark.parametrize 
still didn't work. The squared test from the task
also didn't work. 
So I have no idea what's wrong with pytest, and I
have no idea if most of my code actually works as
it should. But I have no way of testing it. So all
I can do is hope that it works. 

I also tried the optional exercise, but I have
no idea if it worked, due to pytest refusing to 
cooperate.

Under are some notes I made while doing the tasks.
I don't know if they are relevant or not. 



- The test_add_Exercise_1 should be fine for 
	stings. But need to add a tolerance for 
	floats. test_add_float_Exercise_2 should
	work for int and float. 

- Have problems with exercise 4, factorial.
	It takes ages to run the test, and I have 
	no idea why. 
	P.S; I figured it out. Now I feel silly. 

- Exercise 4, sin can't take too high N. 85 seems
	to be the highest it can go. 

- Exersice 4, I button mashed for the test number,
	And accidentally found 5821 as a prime
	number. I know this isn't relevant, but
	it made me happy. 

- Exercise 5: My biggest problem with this whole 
	thing is git and pytest. I've been coding
	in spyder, so I have very little experience
	with teminals, and I just can't get it to
	do what I want to to do. (eks, I created
	a branch called help while trying to 
	figure out how to move from in-progress
	to master)
	Update: I've gotten to master, but when 
	trying to pytest "Permission denied" comes 
	up.
- Just looked at github. Looks like it hasn't 
	registered master as a branch. Great. 

- It's two days and multiple hours of trying to fix
	pytest later. No progress.

- I've pretty much given up. I'm just writing stuff
	And hope it works.
