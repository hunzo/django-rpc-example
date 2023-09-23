from django.shortcuts import render, redirect
from django.contrib import messages
from .rpc import get_data_from_cardreader


def uiView(request, pk=None):
    if request.method == "POST":
        result = get_data_from_cardreader(pk)
        if result is None:
            messages.error(request, "Card reader could not be read or Incorrect service name")
        else:
            messages.success(request, result)
        return redirect("home", pk=pk)

    return render(request, "index.html")
