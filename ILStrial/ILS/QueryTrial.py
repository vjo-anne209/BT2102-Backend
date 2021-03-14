#Borrow Book
#input = MemberID, BookID
#Check book's availability
#isAvailable= Book.objects.get(BookId = bookid).availabilityStatus
#if (isAvailable):
  #  if (memberId in Fine and paymentStatus == "Not Approved"):
   #     return "User can not borrow book, ask them to pay the fine first"
  #  else :
  #      numberOfBook = Book.objects.get(MemberUserId = MemberID).count()
   #     #Check the number of book user has borrowed
   #     if numberOfBook >= 4 :
   #         return "User can not borrow book"
     #   else :
    #        #proceed to borrow the book
     #       #update MemberID in the book, update expectedDueDate = currentDate + 28 days, update availabilityStatus
#else:
 #   return "Book is not available at the moment"
#
#Reserve
#input = MemberID, BookID
#if (memberId in Fine and paymentStatus == "Not Approved") :
 #   return "User can't reserve the book, ask user to pay the fine first"
#else :
#    if (isReserved) :

  #      return "User can't reserve the book"
  #  else :
  #      if (isAvailable) :
  #          return "User can borrow the book""
  #       else :
            #proceed to reservation
            #update reservationStatus
            #Add new row to Reservation table --> input MemberId, BookID, BookId + MemberID as ReservationID
#3. Cancel Reservation
#input = MemberID, BookID
#Find Reservation ID in Reservation table and delete it
#Update the reservation status in Book table to false

#4. Renew Book
#input = MemberID, BookID
#if (isReserved) :
#    return "User can not renew"
#else :
#    return borrow function

#5. Return Book
#input = MemberID, BookID
#If calculateFine(memberID) > 0 : user cannot the book --> needs to pay fine first, otherwise the amount of fine will keep increasing
#update Book table --> change MemberID to null, change availability status to True, expectedDueDate to null

#6. Calculate Fine
#Check everyday --> because we need to cancel any outstanding reservations automatically
#input = MemberID 
#Find the books that user borrows in Book Table by using his memberID --> put it into list
#Fine = 0
#for book in listOfBook :
   # if book.expectedDueDate > currentDate :
      #  Fine += (currentDate - book.expectedDueDate)
    #else :
     #   continue
#if Fine > 0:
 #   if memberId in Fine :
  #      #update amountOfFine
   # else :
        #add MemberID, amountOfFine, paymentStatus = Not Approved, paymentMethod = -, paymentNo = Fine count(*) + 1 --> No need(?)



#7. Pay Fine
#input = MemberID
#Find amountOfFine in Fine table by calling CalculateFine(memberId) 
#User choose whether he wants to use credit/debit card
#Proceed to payment 
#Update paymentMethod, paymentStatus to approved

#8. Admins track users
#make a dictionary
#current books reservation --> just refer to reservation table
#current books borrowing --> filter book table --> availabilityStatus == False
#unpaid Fines --> filter Fine table --> paymentStatus == Not Approved








        


