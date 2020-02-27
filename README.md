# Python-Projects
The following projects consist of python scripts, each with a specific function.
# WebCheck
This file automatically logins into a website by finding the email and password fields, which has data inputted into them to enter a specific account for the website. Afterwards, it fetches the next webpage and checks for a specific element on a webpage. If such does not exist, then an alert is made. There is optional code to hide the webdriver console which can be done following this tutorial: https://stackoverflow.com/a/48802883. 
> Replace these lines
```
self.process = subprocess.Popen(cmd, env=self.env,
                                            close_fds=platform.system() != 'Windows',
                                            stdout=self.log_file,
                                            stderr=self.log_file,
                                            stdin=PIPE)
```
> with 
```
if any("hide_console" in arg for arg in self.command_line_args()):
                self.process = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, creationflags=0x08000000)
            else:
                self.process = subprocess.Popen(cmd, env=self.env, close_fds=platform.system() != 'Windows', stdout=self.log_file, stderr=self.log_file, stdin=PIPE)
```
> Finally in your code, when you setup your driver:
```
args = ["hide_console", ]
driver = webdriver.Chrome("your-path-to-chromedriver.exe", service_args=args, ...)
```
> When editing the source code, be careful to PEP! Do not use tabs, just spaces!