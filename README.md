# SHA-512 Password Hashing
Hashes and stores passwords with the salt under a username.

## Todo
- Password requirements
- - Figure out best requirements to enforce.
- HIBP API check
- - Need a key to test with.
- May be a better way to generate the salt.
- Actual DB implementation.
- Arguments for #Usage.
- Remove users.
- List users.
- Separate into different files.
- pip package?

## Usage
```
// Login
$ passhash login <username> <password>

// Add
$ passhash add <username> <password>

// Remove
$ passhash remove <username> <password>

// List
$ passhash list
```
