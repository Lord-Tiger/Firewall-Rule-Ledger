### User Stories & Acceptance Criteria:
- As a user, I want to be able to securely login and logout and be able to only view the features that are relevant to my assigned role.
	- Acceptance criteria: All users are met with a login page to enter their credentials, once authenticated, they’d be taken to a specific dashboard based on their assigned role. A requester will see a list of their own requests and a button to start a new request. If a user enters wrong credentials, they’re met with an error and they’re not allowed to login.

- As a requester, I want to be able to login and submit firewall rules requests with enough detail so that my requests can be reviewed and processed in a timely manner.
	- Acceptance criteria: When a requester tries to enter a new request, they are presented with multiple fields that are required to be completed in order for an admin to review and approve the request. If a user enters incorrect values or doesn’t fill out all the required fields, they’re met with an error that prevents the request from being submitted.

- As a requester, I want to be able to track my submissions so I can find out when they’re actioned so the project can continue or address any missing data or rejections. This includes historic requests and the ability to track expiry dates if any.
	- Acceptance criteria: The requester dashboard presents a list of requests that belong to the logged in user (if any), it’s a table and it shows each request and its current status.

- As an admin/reviewer, I want to be able to review, approve and reject firewall rule requests in accordance with our standards and policies so I can ensure compliance with our organization and industry standards. This includes a comment box with the justification for the taken action.
	- Acceptance criteria: With an admin view that shows pending requests, and admin can see all such requests with complete detail, source IP, destination IP and so on. Each status update also requires a justification comment, not having such comment prevents the status change from happening and an error is presented until the box is populated.

- As an admin/reviewer, I want to be able to apply specific flags on each rule to specific risk and even function, such as “Disaster Recovery”, a specific application or client.
	- Acceptance criteria: The admin rule requests dashboard allows the admin to select and add specific flags that signify risk or function (such as DR) to each request.

- As an admin/reviewer, I want to be able to add users to the applications and assign roles to them so each user can only execute actions that are needed for their role.
	- Acceptance criteria: Once logged in, the application enforces roles and permissions based on defined criteria and database stored accounts that match the account that logs in.

- As an admin/reviewer, I want to be able to remove users who are no longer with the organization or don’t need access anymore.
	- Acceptance criteria: The admin dashboard allows an admin to navigate to a users page and manage these users and remove them if needed. The deleted user can no longer login.

- As an auditor, I want to be able to review work logs with read-only access to ensure compliance and that proper process was followed from submission to approval.
	- Acceptance criteria: An auditor user is presented with an auditor view that features logs pulled from the database, it includes dates, status changes, actions taken and so on.

- As an auditor, I want to have the ability to parse the logs in a meaningful way so that I can filter entries by user, date and action.
	- Acceptance criteria: The auditor view allows the auditor user to use a search box and filters to filter entries by specific items such as date ranges, usernames and actions.

### Misuser stories & Mitigations:
- As a malicious requester, I might want to approve my own submitted requests and bypass the proper review process by an admin.
	- Mitigation criteria: A user who is not assigned an admin role cannot approve requests and is met with an error if attempted. The attempts are also logged.

- As a malicious requester, I may try to manipulate my requests so I can pass some approved status token as an injection with my submission.
	- Mitigation criteria: The status is set up as read only in the serializer so all attempts will be ignored.

- As malicious requester, or just curious one, I may want to manipulate the URL in such way to change IDs and other attributes so I can view changes submitted by others.
	- Mitigation criteria: Requesters may only see requests made by them. Attempts to do otherwise will be presented with an error.

- As any user, including an admin, I may attempt to delete or modify audit logs to hide risky or approved requests without exceptions.
	- Mitigation criteria: No ability to modify or delete audit logs on the web application itself.

- As an attacker, I want to brute force my way into the application especially to get into an admin account.
	- Mitigation criteria: Login attempts are limited, there are strong password requirements and a lockout for repeated login failure.

- As a malicious requester, or an attacker who managed to compromise a requester’s account, I want to elevate my privileges by changing my role to admin.
	- Mitigation criteria: Roles can only be modified by accounts with an admin role.

- As a malicious requester, I want to edit my requests after approval so I can make it more permissive after it was already approved without further review.
	- Mitigation criteria: Once a request has been submitted, it cannot by modified by the requester and they’ll have to submit a new request.

- As an attacker, I want to run injection strings into the input fields in order to extract data from the database that I shouldn’t have access to.
	- Mitigation criteria: The fields do not accept just any query it receives; inputs are validated first.
