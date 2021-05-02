#random Number between 1 and 100
randomNumber <- as.integer(runif(1, min = 1, max = 100))

#get input from console and send to checkNumber
getInputFromConsole <- function()
{
  checkNumber(as.integer(readline("Number between 1 and 100:")))
}

#check the given number is searched number
checkNumber <- function(n) {
  if (n != randomNumber)
  {
    if (n < randomNumber)
    {
      cat("Searched number bigger!\n")
    }
    else if (n > randomNumber)
    {
      cat("Searched number smaller!\n")
    }
    getInputFromConsole()
  }
  else if (as.integer(n == randomNumber))
    {
      cat("You must be a Nostradamus!", randomNumber, "is the searched number.\n")
    }
}

getInputFromConsole()


