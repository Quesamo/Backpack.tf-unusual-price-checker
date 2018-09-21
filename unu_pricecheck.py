import requests
import json


#PUT YOUR API KEY HERE. YOU CAN GET THE KEY FROM THIS PAGE: https://backpack.tf/developer/apikey/view

while True:
    try:
        with open('api_key.txt', 'r') as api_key:
            key = api_key.read()
            break
    
    except FileNotFoundError:

        key = input('No API key found. \nEnter your API key, it can be found here: https://backpack.tf/developer/apikey/view (note that you might have to request access and stuff)\n')
        with open('api_key.txt', 'w+') as api_key:
            api_key.write(key)


payload = {'key': key}

print('Connecting...')

request = requests.get('https://backpack.tf/api/IGetPrices/v4?', params=payload)
response = request.json()

    


if response['response']['success'] == 0:
    print('Request failed. The API may have been called too many times (try again shortly if so), or the API key is wrong.')

else:
    
    
    
    effects_list = {"Nebula":"99","Burning Flames":"13","Spellbound":"74","It's A Secret To Everybody":"46","Scorching Flames":"14","Harvest Moon":"45","Arcana":"73","Abduction":"91","Sunbeams":"17","Darkblaze":"79","Bonzo The All-Gnawing":"81","Poisoned Shadows":"76","Knifestorm":"43","Stormy 13th Hour":"47","Hellfire":"78","Cloudy Moon":"38","Energy Orb":"704","Misty Skull":"44","Anti-Freeze":"69","Chiroptera Venenata":"75","Roboactive":"72","Demonflame":"80","Atomic":"92","Something Burning This Way Comes":"77","Galactic Codex":"97","Voltaic Hat Protector":"96","Purple Energy":"10","Death by Disco":"100","Green Energy":"9","Ether Trail":"103","Frostbite":"87","Subatomic":"93","Death at Dusk":"90","Ancient Codex":"98","Time Warp":"70","Cool":"703","Morning Glory":"89","Green Black Hole":"71","Amaranthine":"82","Magnetic Hat Protector":"95","Ghastly Ghosts Jr":"85","The Ooze":"84","Haunted Phantasm Jr":"86","Circling Heart":"19","Sulphurous":"64","Electric Hat Protector":"94","Eldritch Flame":"106","Cauldron Bubbles":"39","Stare From Beyond":"83","Haunted Ghosts":"8","Nether Trail":"104","It's a mystery to everyone":"101","Phosphorous":"63","Ancient Eldritch":"105","Flaming Lantern":"37","Hot":"701","Isotope":"702","It's a puzzle to me":"102","Vivid Plasma":"16","Molten Mallard":"88","Tesla Coil":"108","Eerie Orbiting Fire":"40","Haunted Phantasm":"3011","Searing Plasma":"15","Disco Beat Down":"62","Ghastly Ghosts":"3012","Starstorm Insomnia":"109","Starstorm Slumber":"110","Power Surge":"68","Circling Peace Sign":"18","Cloud 9":"58","Electrostatic":"67","Neutron Star":"107","Blizzardy Storm":"30","Circling TF Logo":"11","Infernal Flames":"3015","Infernal Smoke":"3016","Purple Confetti":"7","Stormy Storm":"29","Spectral Swirl":"3014","Holy Grail":"3003","Screaming Tiger":"3006","Miami Nights":"61","Green Confetti":"6","Fountain of Delight":"3005","Memory Leak":"65","Hellish Inferno":"3013","Showstopper":"3001","Terror-Watt":"57","Orbiting Fire":"33","Overclocked":"66","Kill-a-Watt":"56","Massed Flies":"12","Smoking":"35","Bubbling":"34","Steaming":"36","Orbiting Planets":"32","Dead Presidents":"60","Nuts n' Bolts":"31","'72":"3004","Aces High":"59","Skill Gotten Gains":"3007","Mega Strike":"3010","Silver Cyclone":"3009","Midnight Whirlwind":"3008"}
    
    
    unusual_item_list = []

    # Adds all item that can be unusual, to a list
    print('Fetching items...')

    for item in response['response']['items']:
        for quality in response['response']['items'][item]['prices'].keys():
            if quality == '5':
                unusual_item_list.append(item)
                break

    print('Sorting items...')
    unusual_item_list.sort()
    print('Complete!')
    
    # V FOR DEBUGGING V
    # print(unusual_item_list)
    
    while True:
        item_input = input('\nEnter the item and its effect (proper spacing is required, capitalization and complete words are not). \nSyntax: effectname.hatname \n')
        item_input_split = str(item_input).split('.')

        #debugging
        # item_input_split['burning', 'antler']

    # #     #Autocomplete feature for hats
 
        #Default values
        item_hat = '[DEFINITION ERROR]'
        

        for item in unusual_item_list:

            if item_input_split[1].lower() in item.lower():
                
                item_hat = item
                
                hat_error = False
                break
            else:
                hat_error = True
        
        if hat_error == True:
            print('\nAn error occured while finding the hat in the JSON file.')
            continue


        
        
        #Autocomplete feature for effects
        #Default values
        
        item_effect = '[DEFINITION ERROR]'

        for effect in effects_list:

            if item_input_split[0].lower() in effect.lower():
                
                item_effect = effect
                item_effect_dict = {item_effect : effects_list[item_effect]}
                
                #EXCEPTIONS
                if item_input_split[0].lower() == 'orbiting fire':
                    item_effect = 'Orbiting Fire' 
                    item_effect_dict = {item_effect : effects_list['Orbiting Fire']}
                
                

                effect_error = False
                break
            else:
                effect_error = True

        if effect_error == True:
            print('\nAn error occured while finding the effect in the JSON file.')
            continue


        

            
        try:
            price_currency = response['response']['items'][item_hat]['prices']['5']['Tradable']['Craftable'][item_effect_dict[item_effect].title()]['currency']
            price_low     =  response['response']['items'][item_hat]['prices']['5']['Tradable']['Craftable'][item_effect_dict[item_effect].title()]['value']
            price_high   =   response['response']['items'][item_hat]['prices']['5']['Tradable']['Craftable'][item_effect_dict[item_effect].title()]['value_high']
            price_average = (price_low + price_high)/2

            if '.' in str(price_average):
                if str(price_average)[-1] == '0':
                    price_average = int(price_average)
        except KeyError:
            
            #DEBUGGING
            print(item_effect, item_hat)
            
            print('An error occurred: this item is unpriced.')
            continue



        if hat_error == True or effect_error == True:
            print('An error occured.')

        else:
            print(f'The {item_effect} {item_hat} is priced at {price_average} {price_currency}.')
