from django.urls import path
from .views import indexPageView, loginPageView, createUserPageView, trackerPageView, returnTrackerPageView, userInfoPageView, updateUserInfoPageView
from .views import viewLogPageView, viewEntryPageView, addLogPageView, submitAddLogPageView, editLogPageView
from .views import editEntryPageView, dashboardPageView, submitEditLogPageView, deleteLogPageView, submitEditEntryPageView, newEntryPageView, submitNewEntryPageView, deleteEntryPageView

urlpatterns = [
  path("dashboard/<int:userID>", dashboardPageView, name='dashboard'),
  path("deleteEntry/<int:entryID>/<int:returnID>/<int:userID>", deleteEntryPageView, name="deleteEntry"),
  path("submitNewEntry/", submitNewEntryPageView, name="submitNewEntry"),
  path("newEntry/<int:mealID>", newEntryPageView, name="newEntry"),
  path("submitEditEntry/", submitEditEntryPageView, name="submitEditEntry"),
  path("editEntry/<int:entryID>/<int:returnID>/<int:userID>", editEntryPageView, name ="editEntry"),
  path("viewEntry/<int:entryID>/<int:userID>", viewEntryPageView, name="viewEntry"),
  path("deleteLog/<int:entryID>/<int:userID>", deleteLogPageView, name="deleteLog"),
  path("submitEditLog/", submitEditLogPageView, name="submitEditLog"),
  path("editLog/<int:entryID>", editLogPageView, name="editLog"),
  path("submitAddLog/", submitAddLogPageView, name="submitAddLog"),
  path("addLog/<int:userID>", addLogPageView, name="addLog"),
  path("viewLog/<int:userID>", viewLogPageView, name="viewLog"),
  path("updateUserInfo/", updateUserInfoPageView, name="updateUserInfo"),
  path("userInfo/<int:userID>/", userInfoPageView, name="userInfo"),
  path("returnTracker/<int:userID>", returnTrackerPageView, name="returnTracker"),
  path("tracker/", trackerPageView, name="tracker"),
  path("createUser/", createUserPageView, name="createUser"),
  path("login/", loginPageView, name="login"),
  path("", indexPageView, name="index"),
]

