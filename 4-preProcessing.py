import re
import nltk
import os.path as __path__
import enchant
import csv
import goslate
import preprocessor
from collections import defaultdict
from googletrans import Translator
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

en = enchant.Dict("en_US")
idn = []

with open('dictionary/wordlist-id.txt', 'r') as file:
    for word in file:
        idn.append(word)


def casefolding(review):
    review = review.lower()
    return review


def filtering(review):
    review = re.sub(r'@[^\s]+', '', review)  # @username
    review = re.sub(r'#([^\s]+)', '', review)  # hashtag
    review = re.sub(r'https:[^\s]+', '', review)  # URL links
    review = re.sub(r"[.,:;+!\-_<^/=?\"'\(\)\d\*]", " ", review)  # symbol, char
    review = re.sub(r'[^\x00-\x7f]+', '', review)  # non ASCII chars
    review = re.sub(r'\s+', ' ', review)  # duplicate whitespace
    return preprocessor.clean(review)


def tokenizing(review):
    token = nltk.word_tokenize(review)
    return token


def stemming(review):
    factorySt = StemmerFactory()
    stemmer = factorySt.create_stemmer()
    review = stemmer.stem(review)
    return review


def stopWordRemoving(review):
    factorySw = StopWordRemoverFactory()
    stopword = factorySw.create_stop_word_remover()
    review = stopword.remove(review)
    return review


def slangWordConverting(review):
    slangwords = dict()
    with open('dictionary/slangword-id.txt') as wordfile:
        for word in wordfile:
            word = word.split('=')
            slangwords[word[0]] = word[1].replace('\n', '')

    wordsArray, fixed = review.split(' '), []
    for word in wordsArray:
        if word in slangwords:
            word = slangwords[word]
        fixed.append(word)
        review = ' '.join(fixed)
    return review


def characterRepeating(review):
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    tempWord = ''
    for word in review.split(' '):
        if word != '':
            if en.check(word):
                tempWord += word+' '
            elif word in idn:
                tempWord += word+' '
            else:
                tempWord += pattern.sub(r"\1", word) + ' '
    return tempWord


def translating(review):
    gs = goslate.Goslate()
    translatedText = gs.translate(review, 'id')
    return translatedText


def translating2(review):
    translator = Translator()
    translations = translator.translate(review, dest='id')
    return translations.text


def getUserTweets(usertweet):
    columns = defaultdict(list)
    infile = __path__.join(
        __path__.curdir, "dataset/crawl/tweets-@" + usertweet + ".csv")
    with open(infile, 'r', encoding='utf-8') as tweetfile:
        reader = csv.DictReader(tweetfile)
        for row in reader:
            for (k, v) in row.items():
                columns[k].append(v)

    outfile = "dataset/process/processed-tweets-@" + usertweet + ".csv"
    with open(outfile, 'w') as userPreprocessed:
        userPreprocessed.write('username,tweet')
        userPreprocessed.write('\n') 
        for tweet in columns['text']:
            print('Original: '+str(preprocessor.tokenize(tweet)))
            tweet = filtering(str(tweet))
            tweet = casefolding(str(tweet))
            tweet = characterRepeating(str(tweet))
            # tweet = translating(str(tweet))
            tweet = stemming(str(tweet))
            tweet = stopWordRemoving(str(tweet))
            tweet = slangWordConverting(str(tweet))
            print('Processed: '+str(tweet) + '\n')
            if tweet != '':
                userPreprocessed.write(str(usertweet)+','+str(tweet))
                userPreprocessed.write('\n')

    print("\n- writing to '" + outfile + "' complete.")


if __name__ == '__main__':
    users = ['achadianrani', 'almostbeyours', 'amarasyawalni', 'erickdidudidu', 'ferrafbryn', 'fridamayanti', 'ichatarina', 'jehademusa', 'laylarmdhnaa', 'lenoydew', 'liawrdhani', 'munawaroh_mona', 'nysmonworld', 'shafiraara', 'siti_sr137', '9ita7unn', '_avocada', '_chaendelier_', '_marfami', '_nilazka', '_sylvialestari', 'a2lir', 'abcdenjiii', 'adamumemo', 'adewiana14', 'adindahapsa', 'adityalinardi', 'adityandr', 'adityosusanto_', 'adlfynf', 'adorablejuneya', 'adputri_', 'afidazkyy', 'agus_trianto', 'aisyahafr', 'aiuchida', 'akhsaraa', 'akuuuberuang', 'alaaini1', 'alaniafitri', 'aldimaulana48', 'alfian_ay', 'alfinalfinn', 'alfrisadivaw', 'aliencuk', 'alifahdellaf', 'alitapuspa_', 'amalianadiene', 'amandapht', 'amhryn', 'amindwiananda', 'ana_ot', 'anakyangtangkas', 'andiniayu', 'andrisuartikaa', 'anggycaa', 'anissa_sani', 'anzjani', 'apaanmanggil', 'apdesti_', 'arangkecap', 'ardianitaap', 'ariefpopoh', 'arindyaf', 'arisetiyani12', 'arizamarine', 'arrrasseo', 'artikakristi', 'asriyahasry', 'astikhairunnisa', 'astridvivianni', 'astrifaj', 'ath_tobe', 'athayaanabila', 'attamufid', 'auliapramudya_', 'avidazr', 'awwlltl', 'ayrachma', 'azharizkita', 'azwardfauzan', 'baksopangsitnya', 'bananamilxxx', 'belfiani', 'benrskbyg', 'bestchrysalis', 'bettyindahr', 'betyratih', 'bibblegumm_', 'bintangphy', 'biyaanhaz', 'bodoamatbrou', 'borahyungg', 'brilliaflah', 'bukandove', 'bukanrohalia', 'bvdztkvlr', 'canc_ers', 'ccarenth', 'chandnidevi', 'chndooy', 'chtime__', 'chyntw_', 'cipipiw', 'citora_', 'claraang09', 'classmlild', 'copcopiaa', 'crysandh', 'dafugmbah', 'dalgonasachet', 'dannytandean', 'daranagas', 'darna17', 'dartina_', 'deliahndt', 'dellapj_', 'dennisransun', 'denokdhena', 'destaard', 'destandriyani', 'destychaniaa', 'detiaferlian', 'devia_riskaa', 'dewirossilia', 'dheaniranabila', 'dikmabelarosa', 'diniheryani', 'dippp_p', 'ditdandep', 'dsnmld', 'duwaaaay', 'dwiahkam', 'dwidys_', 'dwraoktavia', 'dyeah13', 'dzakimadhani', 'dzakyhaidar__', 'effendisgurl', 'egabetari', 'ejakulasi_', 'ekahanda', 'elidoff', 'emanggemeshin', 'erisyaeris', 'ervhans', 'esjaeruk', 'estlrsty', 'evaxevi', 'eyaaaxx', 'fadfadholic', 'fanirchm27', 'farahmhdyyh', 'febrianirevita', 'fia_lutfiazhari', 'fildzahanais', 'finaihsani', 'firda0305', 'firdahanifa_', 'firstyfelanda', 'fitriindy', 'fitrisip', 'g1tsy', 'ghias_yusuf', 'gieskalaila', 'gorjesparkle', 'gramelt', 'granweastery', 'greeniscalming', 'grestina', 'griffitpypiet', 'gthagrace', 'gustianarii', 'h3llatrash', 'haluhaluclubbb', 'hani_ristiawan', 'hapsarihn', 'hasinanr', 'hawaariyy', 'hazizaanifa', 'hermajestyrania', 'heyhestyy', 'hidadahida', 'hkawilarangg', 'hlutami', 'husnavinaa', 'hypertenshit', 'i_frankenstein', 'ibnubons', 'idrisg8', 'iffamee', 'iftitahptr', 'ikhwaaaaann', 'ilma678', 'imaashoima', 'imadamii', 'imfnia', 'indahastikas', 'inditarizky', 'indraszlaila', 'indrayyyy_', 'inesprat_', 'inkafbrn', 'innocentpep', 'intansakina28', 'introperti', 'iqbalpaz', 'ireenarum', 'isnakhairi', 'itshardys', 'ivyeol', 'januarrmdhn', 'joabaldo', 'joeniararief', 'jollajoly', 'juliandennis1', 'juliepuspita01', 'jundie_m', 'jusrambai', 'juwitasdrman', 'kalisnakal', 'kasurjalan', 'kasurlante', 'kawaipuna_', 'keiziasyf', 'kepikbesar', 'kerakteloorr', 'kharismagpri', 'khelian_ni_s', 'ki_cuu', 'kimsatgat2', 'kirannaurora', 'kodelle_', 'kokocrvnch', 'komalasari_ak', 'krisnawah', 'kucingsmanda_', 'kumanokabe_', 'ladafiq', 'lailapurnamas', 'lalenamanoban', 'latifanajla__', 'latifasyf', 'leoagung98', 'lerinarin', 'liawatii_', 'liayurh_', 'liestianoviani', 'linggaralfi', 'liputarinns', 'llakhr', 'lulufrdni', 'marisahafsyah94', 'maulanariandi', 'mautongue', 'megapsmr', 'mellamotis', 'melyst94', 'meniaclosia', 'messylusmitha', 'metinaayu_', 'micinsassae', 'miftahulilma10', 'mininoenk', 'msyitams', 'muthiaf10', 'nabilatunss', 'nadhira42', 'nadiadjibran', 'nadihng', 'nadyaulfahn', 'nailazulfanz', 'nanasambara', 'nanuazz', 'nauli_permata', 'nevienpan', 'niazmi_', 'nidakarin', 'nneninot1996', 'nopiynovi', 'normalvira', 'novia_pqr', 'novitakurniap', 'novitnurul', 'nstlstnngrm', 'nurulainiii', 'nwindaputri', 'ociirosiana', 'okkyskripsi', 'okyranda', 'oneperson01_', 'ovilsp', 'owkowkok', 'oziechonky', 'pelangikecilll', 'phoebee_ip', 'pinchipowww', 'pinochiao', 'pocagurii', 'prastikavivi', 'prialitaf', 'ptorianns', 'pujaypujilpuu', 'pujisay', 'punyauname', 'puspapradinaa', 'puten_hijau', 'puteriroro', 'putriyuniardi', 'qthrnnada', 'r_fiika', 'rafitaasr', 'rahmaarindapp', 'rahmahwanti', 'rahmatfathoni', 'rallyanta', 'ramdaneinstein', 'rdtlfiqryaj', 'readytomingie', 'rianita_sm', 'rierabcd', 'risdahlbs', 'riskaadesuryani', 'rizka_christian', 'rizkaaulia', 'rizol_rizal', 'rkhusfa', 'rkismaniar', 'rohanahrey', 'rpdelimaa', 'rvghalif', 'rzqmentari', 'saccharinande', 'salisnurk', 'salsabilabia', 'saraadaay', 'sartikadesi212', 'savirapu', 'scharrii', 'seacrabble', 'sefticare', 'sekarumn', 'selftalker', 'sfaui', 'shelfiw', 'shobronabadan', 'silmiotmiot', 'silvialucyana', 'silvihoroni', 'siti89nurjanah', 'slvdys', 'sobatqasurr', 'sora_alxean', 'stephanieayuu', 'stillyourbae', 'strybycy', 'stttopp', 'sulisprstya', 'sundalaif', 'susheetrashh', 'susiindah16', 'syifa_syifo', 't_gooners16', 't_hndr', 'tahtaallfina', 'taritahir', 'tastyducky', 'tiaraindhprmt', 'timutiimuti', 'tnrx_', 'tramadanur', 'triaisharaa', 'trisawardanis', 'ucciiill', 'ugitugitmiskoi', 'upikmera', 'ursnflwr_', 'ussiiyy', 'utho_', 'v3isvthree', 'vanillasvgar', 'viasyafiqa', 'viragutubela', 'virraaa_', 'vnyriany', 'wequte', 'wulandrshrmn', 'wydyudi_', 'yaelahir', 'yokozka', 'youcan_it', 'yovimelan', 'ysyni', 'yudkuswar', 'yulfaariza', 'yulia_danche', 'yuliawafa', 'yusrinasmarani', 'yuuta__96', 'zea_mays07']
    
    for user in users:
        getUserTweets(user)
