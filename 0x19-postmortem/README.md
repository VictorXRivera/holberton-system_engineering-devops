# Postmortem
By Victor X. Rivera

## Issue Summary
From 8:00 am EST to 10:00 am EST, my Robot named R.O.B was acting very strange when performing it's tasks. Being the only Robot performing simple tasks like stacking boxes or counting every item within an inventory, it had crashed during it's Stacking Boxes task and this was due to an Infinite Loop within it's programming.

## Timeline
- 8:00 am EST - Panicked for a brief moment, then went straight to debugging.
- 8:30 am EST - Discovered the issue by connecting R.O.B to my desktop and opening Microsoft Visual Studio to view its programming. The terminal highlighted the issues in red thanks to a custom coloring file when running the script.
- 8:30 am EST - Laughed out loud at the issue, attempted to correct it with simple code. It broke the programming further.
- 8:31 am EST - Deleted all of the current code.
- 9:00 am EST - Finished whiteboarding and mapping out what code I will implement to avoid issues.
- 9:30 am EST - After writing all of the new code, started performing testing. I had my sister help with discovering possible edge cases and more.
- 9:50 am EST - Most edge cases and bugs were found and taken care of.
- 10:00 am EST - R.O.B's programming was fixed thanks to new and better code.

## Root Cause and Resolution
So part of the issue was that I had hard coded quite a lot of actions and paths for R.O.B without an considerations for edge cases and scenarios like "what if there are no more Boxes to stack?". This morning it crashed because there was no more boxes to stack and the code telling it to perform this stacking action was stuck in an infinite loop due to that factor. It was beeping quite loudly with smoke emitting from it's head and even did this strange and glitchy dance or movement. It was hard to tell.
Me and my sister fixed the issue by rewriting the code to be more dynamic and fluid, implementing Recursive functions and Function Calls so that R.O.B can perform it's tasks fluidly and without issues. Now whenever R.O.B meets these cases like "what happens if it finishes one task?", it takes the best course of action. For example, whenever it stacks boxes it will announce how it is almost finished to give us an heads up and also let us know that it will move on to another available task. When R.O.B is finished with all tasks, it will bid farewell and go to sleep!

## Corrective and Preventative Measures
The code written to detail R.O.B's actions will use Recursion and Function Calls to create more dynamic and fluid code for it to follow.
Tasks:
- Check Syntax
- Whiteboard and list tasks before running R.O.B's programming
- Unitest
- Make sure loops are written correctly
- Implement recursion
- Implement Function Calls
- Always make sure R.O.B is okay

![Image of R.O.B with TEETH](https://memestatic.fjcdn.com/pictures/Rob+with+teeth_1d8038_7085855.jpg)
