# Routines App

This app is developed for Users who wants create a routine with specific exercises for the gym.

# How I understanded the solution?

For me, the solution was create `User`, `Routine` and `Exercise` models with the relationships between `User` with `Routine` and `Routine` with `Exercise`. I focused my implementation in the creation of these models and the relationships. Then I focused my time to add `JWT Token` authentication, with respectives `APIs` to create and refresh a token. Finally I worked on the `UserView`, trying to shown my knowledgs of `Serializers` and `Viewsets` of `Django REST Framework`.

# What were my assumptions during development?

First of all I thought about the User registration and the login, so I supposed the unique field for the User registration was the `email`,
therefore, we couldn't create a User with same email in the app and the User could login with the email.

In the second place, I supposed to create a `Routine` with the `days` we need send a array of string with the number of the day, for example: `1` is for `Monday`, `2` is for `Tuesday`, etc. We send a array of strings and with the validation methods in the serializer, we could check if a allowed choice for the field. Then, I used a `ArrayField` in the `Routine` model, thinking use a PostgresSQL database for the developmet, unfortunately I had not more time to finish and the migrations don't work with this implementation.

Finally, I assume the risk to implement everything but I failed with the time.
