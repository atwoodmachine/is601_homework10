## Readme

## Closed Issues
### Issue 1: API inaccuracy
In the video, an issue was demonstrated where the API documentation displayed inconsistent information in the nickname fields of the user registration where mismatched. This was originally due to the fact that in the user_schemas.py file, the nickname examples all called generate_nickname(), which randomly assigned a nickname every time the docs page was viewed. This was fixed by changing the example text to a consistent value, which helps developers by making the API clearer and accurate to its actual functionality. Here is the link to the [closed issue](https://github.com/atwoodmachine/is601_homework10/issues/1).

### Issue 2
When first running the project, several tests fail because there is a mismatch in testing fixtures and the given schema. Particularly, the attributes "full_name" and "username" are used instead of the accurate "first_name", "last_name", and "nickname" fields. These were renamed and the tests pass with expected behavior. Here is the link to the [closed issue](https://github.com/atwoodmachine/is601_homework10/issues/3)

### Issue 3
When first running the program, several missing fixtures cause errors when attempting to run tests. These fixtures were added and the tests passed as expected. Here is the link to the [closed issue](https://github.com/atwoodmachine/is601_homework10/issues/5)

### Issue 4
The CI/CD workflow in github checks to ensure used libraries are secure and warns if libraries are not up to date and have known vulnerabilities. To fix this, libraries are upgraded to their most recent versions. Here is the link to the [closed issue](https://github.com/atwoodmachine/is601_homework10/issues/8)

### Issue 5
It is important to use strong passwords in order to avoid security problems. However, there was no validation for strong passwords in the user schema. A validator was added to check when a user is being created that they enter a strong password containg a digit, a special character, and an uppercase letter at a minimum. Here is the link to the [closed issue](https://github.com/atwoodmachine/is601_homework10/issues/12)

### Issue 6
There exist real world scenarios in which a user might want to update a number of fields in their account at the same time. At the start there were no tests to ensure these changes were handled as expected, so additional tests were added in order to test updating combinations of fields so if anything broke because of changes made they would be detected easily. Here is the link to the [closed issue](https://github.com/atwoodmachine/is601_homework10/issues/14)

## Dockerhub Image
Here is the dockerhub image for this project: [link](https://hub.docker.com/repository/docker/senizozso9/is601_homework10/general) 

## Reflection
This assignment provided valuable insights into source control practices such as github issues and CI/CD pipelines. Issues were an effective way to communicate errors with the project and solve them in an organized manner. The ability to create branches directly based off of an issue was especially convenient and provided for clearer organization of what was being worked on and an easy way to see how those issues were solved. 
<br>
It was also important to see how unit testing affects real production environments and how it helps in development. Unit testing provides a quick and easy way to see exactly where issues arise in order to fix them. They're also critical when making changes to how the program is structured or how it functions in order to ensure changes that break what used to work don't get missed. For example, the existing tests were critical when initially setting up the project, since several did not function "out of the box" and edits needed to be made in order to get the program working as intended before any changes were made to subsequently break the program ourselves.