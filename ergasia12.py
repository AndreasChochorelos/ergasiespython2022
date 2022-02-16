import requests

roundReq = requests.get(url=f"https://drand.cloudflare.com/public/latest") #request sti selida
if roundReq.status_code == 200: #an to request einai successful
    round = roundReq.json()["round"] #pairnoume to value tou round
    
    values = [] #lista pou 8a mpoun ta values tou randomness stous 100 gurous
    for i in range(100):
        #pame ston ka8e guro kai pairnoume to value tou randomness
        randomReq = requests.get(url=f"https://drand.cloudflare.com/public/{round - i}")
        randomness = randomReq.json()['randomness']

        binaryValue = "" #string pou tha mpei to diaduko
        for byte in bytearray(randomness,"utf-8"):
            binaryValue += bin(byte)[2:] # remove 0b
        
        values.append(binaryValue) #vazoume sth lista ta binary values

    maxZeros = "" #h seira pou exei ta perissotera sunexomena mhdenika
    maxZerosLen = 0 #to plu8os twn mhdenikwn

    maxOnes = "" #h seira pou exei tis perissoteres sunexomenes monades
    maxOnesLen = 0 #to plu8os twn monadwn
    for value in values: #se kathe seira
        #mhdenizontai oi metrhtes se kathe kainourgia seira
        zeros = 0
        ones = 0
        for char in value: #sto kathe pshfio ths seiras
            if char == '0': #an einai 0 tote:
                if(ones > maxOnesLen): #an oi seri monades pou exei brei ews twra einai pio polles apo autes pou exei brei hdh tote:
                    maxOnes = value #kratame th seira
                    maxOnesLen = ones #kratame to pluthos twn seri monadwn
                ones = 0 #kanoume ton metrhth 0 afou teleiwse to seri twn monadwn
                zeros +=1 #kai ksekiname to metrhma twn mhdenikwn
            elif char == '1': #an einai 0 tote:
                if(zeros > maxZerosLen): #an ta seri mhdenika pou exei brei ews twra einai pio polla apo auta pou exei brei hdh tote:
                    maxZeros = value #kratame th seira
                    maxZerosLen = zeros #kratame to pluthos twn seri mhdenikwn
                zeros = 0 #kanoume ton metrhth 0 afou teleiwse to seri twn mhdenikwn
                ones +=1 #kai ksekiname to metrhma twn monadwn
    
    #emfanizoume ta apotelesmata
    print(f"Auth h seira exei {str(maxZerosLen)} sunexomena mhdenika: {maxZeros}")
    print(' ')
    print(f"Auth h seira exei {str(maxOnesLen)} sunexomenes monades: {maxOnes}")

    #otan to treksete pairnei liga deuterolepta gia na bgalei apotelesmata