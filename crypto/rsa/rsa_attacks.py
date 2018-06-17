from rsa import *

#challenge 1 find easy numbers that factor fast

def challenge2(e, m, alpha, encrypted):
    power = get_length(m, alpha)
    usernames = ['meckel', 'mceckel', 'malcolm.eckel']
    
    c_p = open("common-passwords.txt","r")
    for l in c_p:
        for ui in usernames:
            pw = prepare_string(l.strip(), alpha)
            s = 'userid:' + ui + ',password' + pw
            s = break_message(s, power)[0]
            num = string_to_int(s, alpha)
            cipher = encrypt(num, e, m)
            if cipher == encrypted:
                print(num)
                print(ui, ',', pw)

alpha = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.;:-, !\'0123456789'
e = 65537
m = 90487058565911344860746920532714345107344888706603388689414973118770115868824428038927974148369533060365472446789821522968583861289788613738073758712025234963231865997137994675667715748727317358600691229070201161969867856640249424928418473804035245009947964183514868695116591835621822263433693274598400210107
encrypted = 89897807505048742568624266076183099622868191865791675665199726198073166863517809194896619121285164863721775826174711988683028633449762554684260071137667277939952878337117007006682648484027616481552917086710938427047904293454110730563208669424803871616352517233729085665806037146392445377160226330123954583864
challenge2(e, m, alpha, encrypted)

#challenge3 find d by using a system of equation given 2 encrypted texts and their respective e values.

#challenge4 prevent cracking by randomly adding junk characters in text
