# Documentation
# Project title: Blog
# Table of contents:
- [Introduction](#introduction)
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)


## Introduction
The purpose of the document is to give a detailed description of the specific web project in terms of idea, goals, functionalities, requirements and others.
## Overview
The project is a small blogging application with some rudimentary features. Authors can write many posts. Posts are separated by categories. Each post can have one or more categories. Comments section is available beneath every post page.
## Features
- Extended user model.
- Cloud storage.
- Password change.
- Password reset via email.
- Pagination.
- Create, read, update and delete blog posts.
- Categorization of blog posts.
- Search blog posts by title, author or category.
- Search for category from list of categories.
- Create, read, update and delete comments for a given post.
- Post likes.
- CKeditor (rich text editor) available upon post content creation.
- Update user's own profile page.
- View other user's profiles.
- Dark mode??? TODO
- Comments likes ??? TODO

## Additional
- Amazon AWS S3 cloud for uploading files such as profile pictures.
- Resize??? TODO

## Object specific information
### User model
- Not authenticated users have only get() (read) permissions. These include viewing the list of blog posts, the given post's details page with the related comments, viewing the author's profile page, performing all the search functionality and requesting email for password reset.
- Admin user has all the CRUD permissions by default upon the 'createsuperuser' command.
- Regular user (non staff & non superuser) has all the CRUD permissions over personal content and read permissions just like the non authenticated user over non-personal content.
### Comments model
- Comments model has ManyToOne relationships with an user model and a post model. Each post can have many comments and each user can write many comments to one or more posts.
- Fields:
  - author
  - name
  - content
  - post
  - date_published
  - date_modified
### Post model
- A Post model has ManyToOne relationship with the user model in terms of the post author and ManyToMany relationship with the user model in terms of blog post likes. Each post can have only one author but an author can write many posts. Each post can have many comments but a comment can be assigned to only one post.
- Model fields:
  - title
  - author
  - content
  - date_published
  - category
  - likes
  - snippet
- Custom Methods:
  - likes_count() - returns the number of the users who liked the post.
### Category
- As explained above, the Category model has a ManyToMany relationship with the Post model. It's purpose is to order and categorize posts so they can be easily searched.
- Model fields:
  - name 
### Profile model
- Profile model's purpose is to extend the base user model's functionality by providing the user's to upload additional information about themselves such as profile picture, social media links, bio, birth date and location.
- A profile is automatically created upon successfull user registration by using django signals. OneToOneField relationship is implemented between the two classes.
- Model Fields:
  - user
  - profile_picture
  - location
  - birth_date
  - bio
  - facebook_url
  - linkedin_url
  - instagram_url
  - twitter_url
  - github_url
- Custom Methods:
  - get_domain_name_url(), where domain_name = [facebook, instagram, github, twitter, linkedin]
  - get_profile_picture() - returns the path where the file is located.
  - get_absolute_url()
  - create_profile() - 
  - save_profile() -
## Requirements
- Softuni project requirements:
- Mandatory
  - The application must be implemented using Django Framework.
  - The application must have at least 10 endpoints.
  - The application must have login/register functionality.
  - The application must have public part (A part of the website, which is accessible by everyone - un/authenticated users and admins).
  - The application must have private part (accessible only by authenticated user and admins)
  - The application must have admin part (accessible only to admins).
  - Unauthenticated users (public part) have only get permissions e.g., lading page, details, about page.
  - Authenticated users (private part) have full CRUD for all their created content.
  - Admins have full CRUD functionalities.
  - Form Validations.
  - To avoid crashes, implement Error Handling and Data Validations.
  - Use PostgreSQL as a database.
  - Write tests for at least 60% coverage on your business logic.
  - Templates (your controllers/views must return HTML files) - one and the same template could be re-used/used multiple times (with the according adjustments, if such needed).
  - Use a source control system by choice - Github or Gitlab. You must have at least 5 commits + README.
- Optional
  - Responsive web design.
  - Class-based views.
  - Extended django user.
  - Documentation/Swagger
  - Use a file storage cloud API e.g., Cloudinary, Dropbox, Google Drive or other for storing the files.
  - Implement Microservice architecture in your application.
  - Additional functionality, not explicitly described in this section, will be counted as a bonus if it has practical usage.

## Tests Coverage

## Demonstration
