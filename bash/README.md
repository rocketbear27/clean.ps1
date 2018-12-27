# Cleanscript for Linux
## Installation
To install cleanscript for Linux, simply clone the repo:
`git https://github.com/rocketbear27/cleanscript.git`

Then, `cd` into that directory and run these commands in order:
```
cd bash
chmod +x install.sh
sudo ./install.sh
```

You should be greeted by a welcome message.

## Usage
To clean a desired folder, simply run:
`cleanscript /absolute/path/to/desired/folder`

This will eliminate heavy or useless files and folders automatically.


## Making the most of cleanscript
For the best results, we recommend running cleanscript automatically on startup. 

To do this, you must add it to your `.bashrc`:

```
cd ~
nano .bashrc
```

In the file, add the line `cleanscript /absolute/path/to/desired/folder`. 

Now it will run automatically on login!
