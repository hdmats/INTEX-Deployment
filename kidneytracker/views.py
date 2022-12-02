from django.shortcuts import render
from datetime import date
from .models import user, condition, journal_entry, nutrient

# Create your views here.
def indexPageView(request):
  return render(request, "kidneytracker/index.html")

def loginPageView(request):
  return render(request, "kidneytracker/login.html")

def createUserPageView(request):
  if request.method == 'POST':
      Condition = request.POST['condition']
      User = user()
      ConditionID = condition.objects.get(condition_type = Condition)
      User.condition = ConditionID
      User.first_name = request.POST['first_name']
      User.last_name = request.POST['last_name']
      User.gender = request.POST['gender']
      User.height = request.POST['height']
      User.weight = request.POST['weight']
      User.age = request.POST['age']
      User.k = request.POST['k']
      User.phos = request.POST['phos']
      User.na = request.POST['na']
      User.creatinine = request.POST['creatinine']
      User.albumin = request.POST['albumin']
      User.bloodsugar = request.POST['bloodsugar']

      User.save()
      context = {
        "User" : User
      }
      return render(request, "kidneytracker/review.html", context)
  else:
    conditions = condition.objects.all()
    context={
      "conditions": conditions
    }
    return render(request, "kidneytracker/addUser.html", context)

def trackerPageView(request):
  userID = request.GET['UserID']
  User = user.objects.get(id=userID)
  context = {
    'userID' : userID,
    'user': User
  }
  return render(request, "kidneytracker/tracker.html", context)

def returnTrackerPageView(request, userID):
  User = user.objects.get(id=userID)
  context = {
    'userID' : userID,
    'user': User
  }
  return render(request, "kidneytracker/tracker.html", context)

def userInfoPageView(request, userID):
  data = user.objects.get(id = userID)
  conditions = condition.objects.all()
  if (data.condition.condition_type == "Diabetic") or (data.condition.condition_type == "High Blood Pressure") or (data.condition == (data.condition.condition_type == "Obesity")):
    userCondition = condition.objects.get(user__id = userID)
    userCondition = userCondition.condition_type
  else: userCondition = "None"
  context = {
    'user': data,
    "conditions": conditions,
    "userCondition": userCondition
  }

  return render(request, "kidneytracker/updateUserInfo.html", context)

def updateUserInfoPageView(request):
  if request.method == 'POST':
    userID = request.POST['userID']
    User = user.objects.get(id=userID)
    Condition = request.POST['condition']
    if (Condition == "Diabetic") or (Condition == "High Blood Pressure") or (Condition == "Obesity") or (Condition == "None"):
        ConditionID = condition.objects.get(condition_type = Condition)
        User.condition = ConditionID

    User.first_name = request.POST['first_name']
    User.last_name = request.POST['last_name']
    User.height = request.POST['height']
    User.weight = request.POST['weight']
    User.gender = request.POST['gender']
    User.age = request.POST['age']
    User.k = request.POST['k']
    User.phos = request.POST['phos']
    User.na = request.POST['na']
    User.creatinine = request.POST['creatinine']
    User.albumin = request.POST['albumin']
    User.bloodsugar = request.POST['bloodsugar']

    User.save()

    return returnTrackerPageView(request, userID)

def viewLogPageView(request, userID):
  entry = journal_entry.objects.filter(user_id=userID)
  context = {
    "log" : entry,
    "userID" : userID
  }

  return render(request, "kidneytracker/viewLog.html", context)

def addLogPageView(request, userID):
  context = {
    "userID" : userID
  }

  return render(request, "kidneytracker/addLog.html", context)

def submitAddLogPageView(request):
  userID = request.POST['userID']
  Log = journal_entry()
  
  Log.meal_date = request.POST['meal_date']
  Log.meal_type = request.POST['meal_type']
  Log.user = user.objects.get(id=userID)

  Log.save()

  return viewLogPageView(request, userID)
  
def editLogPageView(request, entryID):
  log = journal_entry.objects.get(id=entryID)
  context = {
  "log": log
  }
  return render(request, "kidneytracker/editLog.html", context)

def submitEditLogPageView(request):
  entryID = request.POST['entryID']
  userID = request.POST['userID']
  Entry = journal_entry.objects.get(id=entryID)

  Entry.meal_date = request.POST['meal_date']
  Entry.meal_type = request.POST['meal_type']

  Entry.save()

  return viewLogPageView(request, userID)

def deleteLogPageView(request, entryID, userID):
  data = journal_entry.objects.get(id=entryID)

  data.delete()
  return viewLogPageView(request, userID)

def viewEntryPageView(request, entryID, userID):
  entry = nutrient.objects.filter(journal_entry__id=entryID)
  EntryID = entryID
  log = journal_entry.objects.get(id=entryID)
  context = {
    "meal" : entry,
    "entryID" : EntryID,
    "userID" : userID,
    "log" : log
  }

  return render(request, "kidneytracker/viewMeal.html", context)

def editEntryPageView(request, entryID, returnID, userID):
    entry = nutrient.objects.get(id=entryID)
    context = {
    "entry" : entry,
    "entryID" : entryID,
    "returnID" : returnID,
    "userID" : userID
    }
    return render(request, "kidneytracker/editEntry.html", context)

def submitEditEntryPageView(request):
  returnID = request.POST['returnID']
  userID = request.POST['userID']
  entryID = request.POST['entryID'] 
  Entry = nutrient.objects.get(id=entryID)

  Entry.food = request.POST['food']
  Entry.measurement = request.POST['measurement']
  Entry.k = request.POST['k']
  Entry.phos = request.POST['phos']
  Entry.protein = request.POST['protein']
  Entry.water = request.POST['water']
  Entry.sodium = request.POST['na']

  Entry.save()

  return viewEntryPageView(request, returnID, userID)

def newEntryPageView(request, mealID):
  context = {
    "mealID": mealID
  }

  return render(request, "kidneytracker/newEntry.html", context)

def submitNewEntryPageView(request):
  entryID = request.POST['mealID']
  userID = journal_entry.objects.get(id=entryID)
  userID = userID.user_id
  Entry = nutrient()

  Entry.food = request.POST['food']
  Entry.measurement = request.POST['measurement']
  Entry.k = request.POST['k']
  Entry.phos = request.POST['phos']
  Entry.protein = request.POST['protein']
  Entry.water = request.POST['water']
  Entry.sodium = request.POST['na']
  
  Entry.save()
  meal = journal_entry.objects.get(id=entryID)
  meal.nutrients.add(Entry)

  return viewEntryPageView(request, entryID, userID)

def deleteEntryPageView(request, entryID, returnID, userID):
  data = nutrient.objects.get(id=entryID)
  data.delete()
  return viewEntryPageView(request, returnID, userID)

def dashboardPageView(request, userID):
  sodiumData = nutrient.objects.filter(journal_entry__meal_date = date.today(), journal_entry__user_id=userID).exclude(sodium=0)
  waterData = nutrient.objects.filter(journal_entry__meal_date = date.today(), journal_entry__user_id=userID).exclude(water=0)
  proteinData = nutrient.objects.filter(journal_entry__meal_date = date.today(), journal_entry__user_id=userID).exclude(protein=0)
  potassiumData = nutrient.objects.filter(journal_entry__meal_date = date.today(), journal_entry__user_id=userID).exclude(k=0)
  phosphorusData = nutrient.objects.filter(journal_entry__meal_date = date.today(), journal_entry__user_id=userID).exclude(phos=0)
  
  User = user.objects.get(id=userID)
  sodium = 0
  for entry in sodiumData:
    sodium += entry.sodium
  sodiumProgress = round((sodium/1495)*100,0)

  protein = 0
  for entry in proteinData:
    protein += entry.protein
  proteinLimit = User.weight * 0.28

  potassium = 0
  for entry in potassiumData:
    sodium += entry.k

  phosphorus = 0
  for entry in phosphorusData:
    sodium += entry.phos

  water = 0
  for entry in waterData:
    water += entry.water
  
  if User.gender == "Male":
    waterLimit = 3700
  else:
    waterLimit = 2700

  waterProgress = round((water/waterLimit)*100,0)
  if waterProgress == 0:
    waterProgress = 1
  waterMessage = waterLimit/1000

  context = {
    "sodiumData" : sodiumData,
    "waterData" : waterData,
    "proteinData" : proteinData,
    "potassiumData" : potassiumData,
    "phosphorusData" : phosphorusData,
    "user" : User,
    "totalSodium" : sodium,
    "sodiumProgress" : sodiumProgress,
    "totalProtein" : protein,
    "proteinLimit" : proteinLimit,
    "totalPotassium" : potassium,
    "totalPhosphorus" : phosphorus,
    "totalWater" : water,
    "waterLimit" : waterLimit,
    'waterMessage' : waterMessage,
    "waterProgress" : waterProgress
  }
  return render(request, "kidneytracker/dashboard.html", context)