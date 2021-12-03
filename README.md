# Argon2id Password Hashing
Hashes and stores passwords with the salt under a username.

## Todo
- Password requirements
- - Figure out best requirements to enforce.
- HIBP API check
- - Need a key to test with.
- Actual DB implementation.
- Arguments for #Usage.
- Separate into different files.
- pip package?

## Usage
```console
// Login
$ passhash login <username> <password>

// Add
$ passhash add <username> <password>

// Remove
$ passhash remove <username> <password>

// List
$ passhash list
```
