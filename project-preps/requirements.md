# Software Requirements

## Vision

The vision of this product is to create a Python script that will enable the user to run one script which will open all of their desired applications for a particular purpose.

This project solves the pain point of spending several minutes every day opening all of the applications that you need for a particular task. For example, for software development you might want to have Google Chrome, VS Code, and Slack open. This script will open all of these applications at the same time.

You should care about our product because it will save you time! You can get started significantly quicker with our software because you only have to type in one command in one location in order to open your whole work/play set up.

## Scope

### In

- This product will open multiple applications/files with one command
- This script will be able to open a web browser to a specific website

### Out

- This script will not be housed in its own application
- This programm will not search the system for executable files

## Minimum Viable Product

Our minimum viable product (MVP) is to open all desired applications with one command in the terminal

Stretch goals:

- Add modes for different tasks and applications
- Add functionality for different operating systems

## Functional Requirements

1. User can manually add applications to open
2. User can create a new mode with different applications

## Data Flow

The user will enter one command to run a Python script which will open each application that is programmed to open.

## Non-Functional Requirements

1. Usability: The project will be a command line interface execution and will be simple and easy to use
2. Testability: Our project is easily tested. If the script is successful, the desired applications will open on the screen
3. Error Handling: Our project will handle errors such as an application not existing and produce a useful message to let the user know