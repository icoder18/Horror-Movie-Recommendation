import numpy as np
import pandas as pd
import json
from ast import literal_eval
import collections
import emoji


data = pd.read_csv('Horror Movies List.csv')
data.head(n=10)

def classifyTagsGenres(data):
    tagsGenreDict={}
    for i in range(len(data)):
        movie_tagGenres=data['TagsGenres'].iloc[i]
        for j in movie_tagGenres.split(','):
            if j in tagsGenreDict:
                tagsGenreDict[j]+=1
            else:
                tagsGenreDict[j]=1
    return tagsGenreDict


tagsGenreDict = classifyTagsGenres(data)

sorted_tagsGenres = sorted(tagsGenreDict.items(),key=lambda kv:kv[1],reverse=True)
sorted_tagsGenresDict = collections.OrderedDict(sorted_tagsGenres)


similar_tags ={
    'Thriller':['thriller', 'mystery', 'serial killer','fear', 'psychological thriller', 'suspense','escape'],
    
    'Mystery':['mystery', 'giallo','mystery killer','masked killer','stalker'],
    
    'Horror Comedy':['comedy', 'mockumentary', 'satire', 'splatter comedy', 'spoof'],
    
    'Sci-fi':['sci fi', 'scientist', 'mad scientist', 'experiment', 'doctor', 'psychiatrist', 'laboratory', 'virus', 'alternate reality', 'mutation', 'computer', 'outer space', 'astronaut', 'time travel', 'time loop', 'infection'],
    
    'Kidnapping':['crime', 'kidnapping', 'bound and gagged', 'tied feet', 'mask', 'sheriff', 'police', 'abduction', 'investigation', 'mystery killer', 'Neo-noir', 'mysterious killer', 'police officer'],
    
    'Pyschotronic':['psychotronic film', 'surrealism', 'psychological horror', 'lovecraftian', 'nightmare', 'hallucination', 'coma', 'paranoia', 'dream', 'hypnosis'],
    
    'Creatures and Monsters':['creature', 'monster', 'shark', 'monster movie', 'creature feature', 'doll', 'giant spider', 'kaiju', 'snake', 'parasite', "frankensteins's monster"],
    
    
    'Vampires and Werewolves':['vampire', 'werewolf', 'full moon', 'vampire hunter', 'female vampire', 'dracula'],
    
    
    'Zombie':['zombie', 'zombie apocalypse', 'undead'],
    
    
    'Serial Killer':['slasher', 'serial killer', 'psychopath', 'slasher flick', 'masked killer', 'serial murderer', 'slasher killer', 'mental institution', 'killer', 'insanity', 'psychopathic killer', 'serial murder', 'maniac', 'stalker', 'murder spree', 'backwood slasher', 'clown', 'evil clown', 'killer clown'],
    
    
    'Ghosts':['ghost', 'haunting', 'paranormal phenomena', 'ouija board'],
    
    
    'Haunted':['haunted house', 'house', 'mansion', 'castle', 'basement', 'motel', 'haunted house attraction', 'home invasion'],
    
    
    'Supernatural':['supernatural horror', 'psychic', 'supernatural', 'telekinesis'],
    
    
    'Demons and Exorcism':['demon', 'exorcism', 'priest', 'demonic possession', 'possession', 'hell', 'cult', 'nun', 'ritual', 'occult', 'funeral', 'devil', 'deal with the devil', 'exorcist', 'evil spirit', 'evil', 'gothic horror', 'gothic'],
    
    'Occult':['cult film','witch','ouija board','black magic','killing an animal','voodoo','occult','ritual','cult','curse'],
    
    'Aliens and Tech':['alien', 'alien invasion', 'scientist', 'spaceship','sci-Fi','shared universe','based on video game','astronaut','outer space','mutation','laboratory','experiment','mad scientist'],
    
    'Blood and violence':['blood', 'gore', 'murder', 'corpse', 'violence', 'death', 'suicide', 'torture', 'characters murdered one by one', 'body horror', 'cannibal', 'cannibalism', 'decapitation', 'graphic violence', 'eaten alive', 'brutality', 'blood splatter', 'characters killed one by one', 'splatter', 'killing an animal', 'chainsaw', 'sadism', 'exploding head', 'extreme violence', 'throat-slitting', 'buried alive'],
    
    'Found Footage':['found footage', 'hidden camera', 'video camera'],
    
    'Witch':['witch', 'curse', 'witchcraft', 'voodoo', 'black magic', 'magic'],
    
    'Apocalypse':['post-apocalypse', 'apocalypse', 'dystopia', 'future'],
    
    'Urban Legend':['folk horror', 'urban legend', 'folklore', 'anthology', 'based on short story']
    
}

pumpkin=str('\U0001F383')

new_col = ['Title','Rating','Popularity','Category','URL']

def recSys(selected_tags):
    movie_selected=[]
    new_df = pd.DataFrame(columns=new_col)
    for i in range(len(data)):
        
        #Tags list of selected movie
        m_tags=data.iloc[i]['TagsGenres']
        
        for t in selected_tags:
            
            #List of associated tags
            sim_tags=similar_tags[t]
            
            for st in sim_tags:
                if st in m_tags:
                    if data.iloc[i]['Title'] not in movie_selected:
                        movie_rating=data.iloc[i]['Rating']
                        if movie_rating=='None':
                            continue
                        movie_selected.append(data.iloc[i]['Title'])
                        movie_name=data.iloc[i]['Title']
                        popularity_score=data.iloc[i]['Popularity']
                        if popularity_score==125:
                            movie_popularity=pumpkin*3
                        elif popularity_score==124:
                            movie_popularity=pumpkin*2
                        elif popularity_score>=122:
                            movie_popularity=pumpkin
                        else:
                            movie_popularity=""
                        movie_tagsMatched= t
                        movie_url = data.iloc[i]['Url']
                        app_list = {'Title':movie_name,
                                    'Rating':movie_rating,
                                    'Popularity':movie_popularity,
                                    'Category':movie_tagsMatched,
                                    'URL':movie_url}
                        new_df = new_df.append([app_list])
    
    return new_df


def recommendations(selected_tags):
    rec_movies_df=recSys(selected_tags)
    sorted_rec=rec_movies_df.sort_values(by=['Popularity','Rating'],ascending=False)[:13]
    return sorted_rec




