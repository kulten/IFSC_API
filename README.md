# IFSC_API
API that returns bank details when its IFSC code is given.
All of the tokens used in the curl commands is just for demonstration, the tokens have an expiration time of 5 days. If the API request is rejected make sure you have a valid authentication token.
Syntax for bank detail:
</br>
`curl https://my-ifsc-api.herokuapp.com/bank_detail?ifsc_code=<BANK IFSC CODE HERE>&token=<YOUR AUTHENTICATION TOKEN>`
Syntax for bank branch details with limit and offset:
`curl https://my-ifsc-api.herokuapp.com/bank_detail?city=<CITY>&bank_name=<BANK NAME>&limit=<LIMIT>&offset=<OFFSET>&token=<YOUR AUTHENTICATION TOKEN>`
Curl comand to fetch bank details given an ifsc code (WINDOWS): 
`curl https://my-ifsc-api.herokuapp.com/bank_detail?ifsc_code=abhy0065001^&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZ5bGUiLCJleHAiOjE1NzAyODIxNDh9.HTLyDZzzUsCSjyc_VS5y6s36RqIzkFayDutxbxiBBwg`
Curl command to fetch all bank branch details (WINDOWS):
`curl https://my-ifsc-api.herokuapp.com/branch_detail?city=mumbai^&bank_name=abhyudaya%20cooperative%20bank%20limited^&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZ5bGUiLCJleHAiOjE1NzAyODIxNDh9.HTLyDZzzUsCSjyc_VS5y6s36RqIzkFayDutxbxiBBwg`
Curl command to fetch all bank branch details with limit (WINDOWS):
`curl https://my-ifsc-api.herokuapp.com/branch_detail?limit=5^&city=mumbai^&bank_name=abhyudaya%20cooperative%20bank%20limited^&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZ5bGUiLCJleHAiOjE1NzAyODIxNDh9.HTLyDZzzUsCSjyc_VS5y6s36RqIzkFayDutxbxiBBwg`
Curl command to fetch all bank brach details with limit and offset (WINDOWS):
`curl https://my-ifsc-api.herokuapp.com/branch_detail?offset=1^&limit=5^&city=mumbai^&bank_name=abhyudaya%20cooperative%20bank%20limited^&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZ5bGUiLCJleHAiOjE1NzAyODIxNDh9.HTLyDZzzUsCSjyc_VS5y6s36RqIzkFayDutxbxiBBwg`
The curl command listed above are for systems running windows, the character `&` is a special character in the windows terminal and needs to be escaped.
The following commands are for UNIX like systems.
Curl comand to fetch bank details given an ifsc code (UNIX): 
`curl https://my-ifsc-api.herokuapp.com/bank_detail?ifsc_code=abhy0065001&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZ5bGUiLCJleHAiOjE1NzAyODIxNDh9.HTLyDZzzUsCSjyc_VS5y6s36RqIzkFayDutxbxiBBwg`
Curl command to fetch all bank branch details (UNIX):
`curl https://my-ifsc-api.herokuapp.com/branch_detail?city=mumbai&bank_name=abhyudaya%20cooperative%20bank%20limited&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZ5bGUiLCJleHAiOjE1NzAyODIxNDh9.HTLyDZzzUsCSjyc_VS5y6s36RqIzkFayDutxbxiBBwg`
Curl command to fetch all bank branch details with limit (UNIX):
`curl https://my-ifsc-api.herokuapp.com/branch_detail?limit=5&city=mumbai&bank_name=abhyudaya%20cooperative%20bank%20limited&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZ5bGUiLCJleHAiOjE1NzAyODIxNDh9.HTLyDZzzUsCSjyc_VS5y6s36RqIzkFayDutxbxiBBwg`
Curl command to fetch all bank brach details with limit and offset (UNIX):
`curl https://my-ifsc-api.herokuapp.com/branch_detail?offset=1&limit=5&city=mumbai&bank_name=abhyudaya%20cooperative%20bank%20limited&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZ5bGUiLCJleHAiOjE1NzAyODIxNDh9.HTLyDZzzUsCSjyc_VS5y6s36RqIzkFayDutxbxiBBwg`
