Код:
```
for(m=1;m<M;m=m+1)
{
	for (i=1;i<N-1;i=i+1)
	{
		u[m][i]=u[m][i-1]+u[m-1][i]+u[m-1][i+1]
	}
}
```

раскрутка
```
m := 1
	i := 1
	S0(2) : u[1][1] = u[1][0] + u[0][1] + u[0][2]
	i := 2
	S0(2) : u[1][2] = u[1][1] + u[0][2] + u[0][3]
m := 2
	i := 1
	S0(2) : u[2][1] = u[2][0] + u[1][1] + u[1][2]
	i := 2
	S0(2) : u[2][2] = u[2][1] + u[1][2] + u[1][3]
m := 3
	i := 1
	S0(2) : u[3][1] = u[3][0] + u[2][1] + u[2][2]
	i := 2
	S0(2) : u[3][2] = u[3][1] + u[2][2] + u[2][3]
```

<img width="348" height="327" alt="image" src="https://github.com/user-attachments/assets/6c3f3e2b-378f-468b-9699-1af3a4019ec1" />

<img width="470" height="225" alt="image" src="https://github.com/user-attachments/assets/2b2d5a45-0bd5-48d5-974b-314c959da337" />

<img width="1193" height="562" alt="image" src="https://github.com/user-attachments/assets/9bbc011d-82ca-4b8b-8cf9-db38221f9e7e" />

<img width="237" height="268" alt="image" src="https://github.com/user-attachments/assets/3c2462ee-9dab-4357-b5dd-7c26ae7316fc" />

