var books =[]
var input = prompt("which operation u want to perform [add][list][exit]:")
while(input != "exit")
    {
        if(input = "add")
            {
                var newBook = prompt("Enter name of book:")
                books.push(newBook);
            }
        else if(input =="list")
            {
                console.log("List of available books:");
                console.log(books);
            }
        else{
            console.log("enter valid option!!");
        }
        input = prompt("what operation u want to perform [add][list][exit]")
    }
    console.log("thnks for using")