# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 10:59:53 2022

@author: Pierre-Henri Rossouw

Wikipedia Scraper

"""

import wikipedia as wiki

print(wiki.search("Python"))


print(wiki.suggest("Pyth"))

print(wiki.summary("Python"))       #getting summary

wiki.set_lang("fr")                 #changing summary into another language
print(wiki.summary("Python"))

wiki.set_lang("en")                 #changing summary back to English
p = wiki.page("Python")

print(p.title)                      #Getting title

print(p.url)                        #Getting URL of the article

print(p.content)                    #Scrape the full article

print(p.images)                     #Getting images

print(p.links)                      #Getting referrals

