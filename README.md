# What this is
This is an in-development python module being tailored to the requirements of the restore portion of the Requiem project. The purpose of this is to aid in securing the game client from malicious SWF content. A proxying solution in the ambassador that we release will be made to use this library for scanning requests/responses and deciding weather or not they should be allowed to go to the client. **Examples of malicious content include**:
- SWF data uploaded where other data should be e.g. cdn.example.com/user/example_user_id/profile_picture.png containing SWF data which could hypothetically be uploaded put in its place.
- SWF files that use certain packages that are not expected to be loaded which could be used in XSS attacks e.g. flash.net.
  - The restore portion of the project will load various SWF assets for portions of the client which contain art, these are not expected to use various packages that could be malicious, and if they do it means that content has potentially been maliciously uploaded/modified and blocking them is acceptable.

**Capabilities**
- This solution will be capable of scanning pairs of HTTP requests/responses to determine if they are fit for the restore client to receive.
  - A proxying solution will be able to use this to decide if it should send a response to the client and even to "modify" a response to be safe for sending to the client.

# What this is not

This is **not a general purpose solution** to scanning/restricting access to SWF files. This is something that is intended to go with an HTTP proxying solution shipped with the restore client, where requests go through the proxying solution, a response is retrieved by the proxy, and the proxy solution can pass the request/response into the firewalling solution to decide if they the response is suitable for the client, and modify them in any way deemed necessary to make them safe. i.e. **this solution is tailored to the requiem project, and it will be limited to the features required for the project, added when they are required.**

