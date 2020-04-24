Learning Blender's new API
===========================

Currently learning the new API is quite tricky, because the API is new and docs are incomplete. Here's some tips I've worked out along the way:

* Open Blender in a terminal/ powershell/ commandline. This will let you debug Python projects properly (because errors are only displayed here).
* In Blender 2.82, select the `scripting` workspace on the top.
* you can press `tab` in the Blender python console for hints.
* in the Blender text editor, look at the code in `templates` -> `Python`.
* Install Blender 2.79 (or a version which lets you do what I mention next). This version lets you view code for certain "elements" by rightclicking -> "edit source" (to view code) or "online python reference" (to get python docs). While you can't guarantee this code will work with the new Blender API, the new version will work in a similar way and you can search for similar terms in the new API docs.
* Inside the Blender executable/ data folder, you can look inside `2.82/scripts` for code (and on a system with bash, you can search files with a term using `grep -rli "search term"`).
* Try to get as many sources as you can for code.
* Try getting simple, small pieces of code working with as few parts as possible. This is the only way to understand a new API.