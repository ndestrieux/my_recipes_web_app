# 2. Register ranking of recipes in db

Date: 2022-10-18

## Status

Proposed

## Context

The idea is to give the users the possibility to vote (up or down) for a recipe they liked. The importance is to track who give a vote and set a counter on the given recipe.

## Decision

The decision that we made is to set a relationship between a table in which all votes from users will be registered, this table will have a relationship between tables Recipe and User, and each time a vote is given a trigger will increment values in a separate table.
