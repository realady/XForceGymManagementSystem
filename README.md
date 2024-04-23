# XForce Gym Management System 💪

## Overview 📝

This Python script connects to a MySQL database to manage a gym's operations. It allows administrators to perform various tasks such as adding trainers and members, removing trainers and members, modifying information, and viewing lists of trainers and members.

## Prerequisites 🛠️

- [Python 3.x](https://www.python.org/downloads/)
- [MySQL](https://dev.mysql.com/downloads/)
- MySQL Connector (`pip install mysql-connector-python`)
- Tabulate (`pip install tabulate`)

## Usage 🚀

1. Make sure you have Python installed along with the required packages.
2. Set up a MySQL database for the gym with the following tables:

   ```sql
   CREATE DATABASE IF NOT EXISTS GYM;
   USE GYM;
   CREATE TABLE IF NOT EXISTS FEES(SILVER INT, GOLD INT, PLATINUM INT);
   CREATE TABLE IF NOT EXISTS LOGIN(USERNAME VARCHAR(25), PASSWORD VARCHAR(25) NOT NULL);
   CREATE TABLE IF NOT EXISTS MEMBER(ID INT, NAME VARCHAR(25), GENDER CHAR(1), CATEGORY VARCHAR(25), AMOUNT INT);
   CREATE TABLE IF NOT EXISTS SNO(ID INT, DID INT);
   CREATE TABLE IF NOT EXISTS TRAINER(ID INT, NAME VARCHAR(25), AGE VARCHAR(25), GENDER CHAR(1), SALARY INT);
   ```
3. Clone the repository:

   ```bash
   git clone https://github.com/not-adarsh/gym-management.git
   ```

4. Navigate to the project directory:

   ```bash
   cd gym-management
   ```

5. Run the script and follow the prompts:

   ```bash
   python gym_management.py
   ```

## Features ✨

- Add and remove trainers
- Add and remove members
- Modify trainer and member information
- View lists of trainers and members

## Contribution 🤝

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## Collaborators 👥

- Adarsh
- Yashvardhan Dhaka
- Kavit Shukla

## GitHub Repository 🌐

[GitHub Repository](https://github.com/not-adarsh/gym-management/tree/main)
