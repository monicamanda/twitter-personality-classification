import csv
import tweepy
import re

apikeyData = open("apikey", "r").read().split(',')
consumer_key = apikeyData[0]
consumer_secret = apikeyData[1]
access_token = apikeyData[2]
access_token_secret = apikeyData[3]

crawl_tweets = []


def get_tweets(username):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    limit = 200

    user_tweets = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=username, include_rts=False, tweet_mode='extended').items(limit):
        actualTweet = re.sub(r'\s+', ' ', tweet.full_text)
        crawl_tweets.append([username, tweet.created_at, actualTweet])
        user_tweets.append([username, tweet.created_at, actualTweet])

    outfile = "dataset/crawl/tweets-@" + username + ".csv"
    print("- writing to '" + outfile + "' complete.")
    with open(outfile, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["username", "created_at", "text"])
        csvwriter.writerows(user_tweets)


if __name__ == '__main__':
    users = ['achadianrani', 'almostbeyours', 'amarasyawalni', 'erickdidudidu', 'ferrafbryn', 'fridamayanti', 'ichatarina', 'jehademusa', 'laylarmdhnaa', 'lenoydew', 'liawrdhani', 'munawaroh_mona', 'nysmonworld', 'shafiraara', 'siti_sr137', '9ita7unn', '_avocada', '_chaendelier_', '_marfami', '_nilazka', '_sylvialestari', 'a2lir', 'abcdenjiii', 'adamumemo', 'adewiana14', 'adindahapsa', 'adityalinardi', 'adityandr', 'adityosusanto_', 'adlfynf', 'adorablejuneya', 'adputri_', 'afidazkyy', 'agus_trianto', 'aisyahafr', 'aiuchida', 'akhsaraa', 'akuuuberuang', 'alaaini1', 'alaniafitri', 'aldimaulana48', 'alfian_ay', 'alfinalfinn', 'alfrisadivaw', 'aliencuk', 'alifahdellaf', 'alitapuspa_', 'amalianadiene', 'amandapht', 'amhryn', 'amindwiananda', 'ana_ot', 'anakyangtangkas', 'andiniayu', 'andrisuartikaa', 'anggycaa', 'anissa_sani', 'anzjani', 'apaanmanggil', 'apdesti_', 'arangkecap', 'ardianitaap', 'ariefpopoh', 'arindyaf', 'arisetiyani12', 'arizamarine', 'arrrasseo', 'artikakristi', 'asriyahasry', 'astikhairunnisa', 'astridvivianni', 'astrifaj', 'ath_tobe', 'athayaanabila', 'attamufid', 'auliapramudya_', 'avidazr', 'awwlltl', 'ayrachma', 'azharizkita', 'azwardfauzan', 'baksopangsitnya', 'bananamilxxx', 'belfiani', 'benrskbyg', 'bestchrysalis', 'bettyindahr', 'betyratih', 'bibblegumm_', 'bintangphy', 'biyaanhaz', 'bodoamatbrou', 'borahyungg', 'brilliaflah', 'bukandove', 'bukanrohalia', 'bvdztkvlr', 'canc_ers', 'ccarenth', 'chandnidevi', 'chndooy', 'chtime__', 'chyntw_', 'cipipiw', 'citora_', 'claraang09', 'classmlild', 'copcopiaa', 'crysandh', 'dafugmbah', 'dalgonasachet', 'dannytandean', 'daranagas', 'darna17', 'dartina_', 'deliahndt', 'dellapj_', 'dennisransun', 'denokdhena', 'destaard', 'destandriyani', 'destychaniaa', 'detiaferlian', 'devia_riskaa', 'dewirossilia', 'dheaniranabila', 'dikmabelarosa', 'diniheryani', 'dippp_p', 'ditdandep', 'dsnmld', 'duwaaaay', 'dwiahkam', 'dwidys_', 'dwraoktavia', 'dyeah13', 'dzakimadhani', 'dzakyhaidar__', 'effendisgurl', 'egabetari', 'ejakulasi_', 'ekahanda', 'elidoff', 'emanggemeshin', 'erisyaeris', 'ervhans', 'esjaeruk', 'estlrsty', 'evaxevi', 'eyaaaxx', 'fadfadholic', 'fanirchm27', 'farahmhdyyh', 'febrianirevita', 'fia_lutfiazhari', 'fildzahanais', 'finaihsani', 'firda0305', 'firdahanifa_', 'firstyfelanda', 'fitriindy', 'fitrisip', 'g1tsy', 'ghias_yusuf', 'gieskalaila', 'gorjesparkle', 'gramelt', 'granweastery', 'greeniscalming', 'grestina', 'griffitpypiet', 'gthagrace', 'gustianarii', 'h3llatrash', 'haluhaluclubbb', 'hani_ristiawan', 'hapsarihn', 'hasinanr', 'hawaariyy', 'hazizaanifa', 'hermajestyrania', 'heyhestyy', 'hidadahida', 'hkawilarangg', 'hlutami', 'husnavinaa', 'hypertenshit', 'i_frankenstein', 'ibnubons', 'idrisg8', 'iffamee', 'iftitahptr', 'ikhwaaaaann', 'ilma678', 'imaashoima', 'imadamii', 'imfnia', 'indahastikas', 'inditarizky', 'indraszlaila', 'indrayyyy_', 'inesprat_', 'inkafbrn', 'innocentpep', 'intansakina28', 'introperti', 'iqbalpaz', 'ireenarum', 'isnakhairi', 'itshardys', 'ivyeol', 'januarrmdhn', 'joabaldo', 'joeniararief', 'jollajoly', 'juliandennis1', 'juliepuspita01', 'jundie_m', 'jusrambai', 'juwitasdrman', 'kalisnakal', 'kasurjalan', 'kasurlante', 'kawaipuna_', 'keiziasyf', 'kepikbesar', 'kerakteloorr', 'kharismagpri', 'khelian_ni_s', 'ki_cuu', 'kimsatgat2', 'kirannaurora', 'kodelle_', 'kokocrvnch', 'komalasari_ak', 'krisnawah', 'kucingsmanda_', 'kumanokabe_', 'ladafiq', 'lailapurnamas', 'lalenamanoban', 'latifanajla__', 'latifasyf', 'leoagung98', 'lerinarin', 'liawatii_', 'liayurh_', 'liestianoviani', 'linggaralfi', 'liputarinns', 'llakhr', 'lulufrdni', 'marisahafsyah94', 'maulanariandi', 'mautongue', 'megapsmr', 'mellamotis', 'melyst94', 'meniaclosia', 'messylusmitha', 'metinaayu_', 'micinsassae', 'miftahulilma10', 'mininoenk', 'msyitams', 'muthiaf10', 'nabilatunss', 'nadhira42', 'nadiadjibran', 'nadihng', 'nadyaulfahn', 'nailazulfanz', 'nanasambara', 'nanuazz', 'nauli_permata', 'nevienpan', 'niazmi_', 'nidakarin', 'nneninot1996', 'nopiynovi', 'normalvira', 'novia_pqr', 'novitakurniap', 'novitnurul', 'nstlstnngrm', 'nurulainiii', 'nwindaputri', 'ociirosiana', 'okkyskripsi', 'okyranda', 'oneperson01_', 'ovilsp', 'owkowkok', 'oziechonky', 'pelangikecilll', 'phoebee_ip', 'pinchipowww', 'pinochiao', 'pocagurii', 'prastikavivi', 'prialitaf', 'ptorianns', 'pujaypujilpuu', 'pujisay', 'punyauname', 'puspapradinaa', 'puten_hijau', 'puteriroro', 'putriyuniardi', 'qthrnnada', 'r_fiika', 'rafitaasr', 'rahmaarindapp', 'rahmahwanti', 'rahmatfathoni', 'rallyanta', 'ramdaneinstein', 'rdtlfiqryaj', 'readytomingie', 'rianita_sm', 'rierabcd', 'risdahlbs', 'riskaadesuryani', 'rizka_christian', 'rizkaaulia', 'rizol_rizal', 'rkhusfa', 'rkismaniar', 'rohanahrey', 'rpdelimaa', 'rvghalif', 'rzqmentari', 'saccharinande', 'salisnurk', 'salsabilabia', 'saraadaay', 'sartikadesi212', 'savirapu', 'scharrii', 'seacrabble', 'sefticare', 'sekarumn', 'selftalker', 'sfaui', 'shelfiw', 'shobronabadan', 'silmiotmiot', 'silvialucyana', 'silvihoroni', 'siti89nurjanah', 'slvdys', 'sobatqasurr', 'sora_alxean', 'stephanieayuu', 'stillyourbae', 'strybycy', 'stttopp', 'sulisprstya', 'sundalaif', 'susheetrashh', 'susiindah16', 'syifa_syifo', 't_gooners16', 't_hndr', 'tahtaallfina', 'taritahir', 'tastyducky', 'tiaraindhprmt', 'timutiimuti', 'tnrx_', 'tramadanur', 'triaisharaa', 'trisawardanis', 'ucciiill', 'ugitugitmiskoi', 'upikmera', 'ursnflwr_', 'ussiiyy', 'utho_', 'v3isvthree', 'vanillasvgar', 'viasyafiqa', 'viragutubela', 'virraaa_', 'vnyriany', 'wequte', 'wulandrshrmn', 'wydyudi_', 'yaelahir', 'yokozka', 'youcan_it', 'yovimelan', 'ysyni', 'yudkuswar', 'yulfaariza', 'yulia_danche', 'yuliawafa', 'yusrinasmarani', 'yuuta__96', 'zea_mays07']
    
    for user in users:
        get_tweets(user)

