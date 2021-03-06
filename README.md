# IFSC_API
API that returns bank details when its IFSC code is given or fetch details of all bank branches in a city when supplied with the city name and bank name.
</br>
The data in the database is from this repo: `https://github.com/snarayanank2/indian_banks`. it has more than a 100k records. Since Heroku allows only 10,000 rows in its free tier database, only about 8k rows(shooting low, I know) are present currently in the live API.
The API is live at `https://my-ifsc-api.herokuapp.com`
</br>
All of the tokens used in the curl commands is just for demonstration, the tokens have an expiration time of 5 days. If the API request is rejected make sure you have a valid authentication token.
</br>
Syntax for bank detail:
</br>
`curl https://my-ifsc-api.herokuapp.com/bank_detail?ifsc_code=<BANK IFSC CODE HERE>&token=<YOUR AUTHENTICATION TOKEN>`
</br>
Syntax for bank branch details with limit and offset:
</br>
`curl https://my-ifsc-api.herokuapp.com/bank_detail?city=<CITY>&bank_name=<BANK NAME>&limit=<LIMIT>&offset=<OFFSET>&token=<YOUR AUTHENTICATION TOKEN>`
</br>
Curl comand to fetch bank details given an ifsc code (WINDOWS):
</br> 
`curl https://my-ifsc-api.herokuapp.com/bank_detail?ifsc_code=abhy0065001^&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZ5bGUiLCJleHAiOjE1NzAyODIxNDh9.HTLyDZzzUsCSjyc_VS5y6s36RqIzkFayDutxbxiBBwg`
</br>
Curl command to fetch all bank branch details (WINDOWS):
</br>
`curl https://my-ifsc-api.herokuapp.com/branch_detail?city=mumbai^&bank_name=abhyudaya%20cooperative%20bank%20limited^&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZ5bGUiLCJleHAiOjE1NzAyODIxNDh9.HTLyDZzzUsCSjyc_VS5y6s36RqIzkFayDutxbxiBBwg`
</br>
Curl command to fetch all bank branch details with limit (WINDOWS):
</br>
`curl https://my-ifsc-api.herokuapp.com/branch_detail?limit=5^&city=mumbai^&bank_name=abhyudaya%20cooperative%20bank%20limited^&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZ5bGUiLCJleHAiOjE1NzAyODIxNDh9.HTLyDZzzUsCSjyc_VS5y6s36RqIzkFayDutxbxiBBwg`
</br>
Curl command to fetch all bank brach details with limit and offset (WINDOWS):
</br>
`curl https://my-ifsc-api.herokuapp.com/branch_detail?offset=1^&limit=5^&city=mumbai^&bank_name=abhyudaya%20cooperative%20bank%20limited^&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZ5bGUiLCJleHAiOjE1NzAyODIxNDh9.HTLyDZzzUsCSjyc_VS5y6s36RqIzkFayDutxbxiBBwg`
</br>
The curl command listed above are for systems running windows, the character `&` is a special character in the windows terminal and needs to be escaped.
The following commands are for UNIX like systems.
</br>
Curl comand to fetch bank details given an ifsc code (UNIX): 
</br>
`curl https://my-ifsc-api.herokuapp.com/bank_detail?ifsc_code=abhy0065001&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZ5bGUiLCJleHAiOjE1NzAyODIxNDh9.HTLyDZzzUsCSjyc_VS5y6s36RqIzkFayDutxbxiBBwg`
</br>
Curl command to fetch all bank branch details (UNIX):
</br>
`curl https://my-ifsc-api.herokuapp.com/branch_detail?city=mumbai&bank_name=abhyudaya%20cooperative%20bank%20limited&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZ5bGUiLCJleHAiOjE1NzAyODIxNDh9.HTLyDZzzUsCSjyc_VS5y6s36RqIzkFayDutxbxiBBwg`
</br>
Curl command to fetch all bank branch details with limit (UNIX):
</br>
`curl https://my-ifsc-api.herokuapp.com/branch_detail?limit=5&city=mumbai&bank_name=abhyudaya%20cooperative%20bank%20limited&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZ5bGUiLCJleHAiOjE1NzAyODIxNDh9.HTLyDZzzUsCSjyc_VS5y6s36RqIzkFayDutxbxiBBwg`
</br>
Curl command to fetch all bank brach details with limit and offset (UNIX):
</br>
`curl https://my-ifsc-api.herokuapp.com/branch_detail?offset=1&limit=5&city=mumbai&bank_name=abhyudaya%20cooperative%20bank%20limited&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImZ5bGUiLCJleHAiOjE1NzAyODIxNDh9.HTLyDZzzUsCSjyc_VS5y6s36RqIzkFayDutxbxiBBwg`
