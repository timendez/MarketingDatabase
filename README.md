# Marketing Database
So the current plan is to write a `parser.py` which will parse all of the data, and call functions in other files to insert that data into the database in the correct format.

For example, `parser.py` will parse

`549799,205620285,41,XYZ online,21040,Maryland,M,,1,EN,1/30/2014,ridetarc.org,Mid`
in the format

`CustomerID,EmailID,RegSourceID,RegSourceName,ZIP,State,Gender,IncomeLevel,Permission,Language,RegDate,DomainName,CustomerTier`

and send `RegDate,null,RegSourceID,RegSourceName,null,CustomerID,null` to a function `registrationsInsertion`.

Note: If there's something akin to JSON in python, we can just use that as the parameter.
e.g. `{RegDate: "1/30/2014", CustomerId:"549799", ...}`

`registrationsInsertion` will create the `INSERT INTO` statements for the table `Registrations`. As for now, we are doing one `INSERT INTO` at a time, for fear of blowing up if we try all at once.
