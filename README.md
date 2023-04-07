ALGORİTMA ANALİZİ VE TASARIMI DERSİ 1. KISA SINAV 2. BÖLÜM ÖDEVİ

Hazırlayan: Berkay Aydın 1210505048

Python programlam dili kullanılarak yazılan kodda kelimeler önceden belirlenmiş olup kod çalıştırıldığında hangi kelimenin kaç kez geçtiği ekrana yazdırılmaktadır.
Kodun sorunsuzca çalışabilmesi için Alice in Wonderland metninin dosya.txt adında kod ile aynı klasörde olması gerekmetedir. Bu dosya yolu kod üzerinden değiştirilebilmektedir..



Morris-Pratt:
Bu algoritma, gelişmiş bir string eşleştirme algoritmasıdır ve veri kümesi olarak bir metin (text) ve hedeflenen öğe olarak bir kalıp (pattern) kullanır.

Çalışma Şekli

Kalıp (pattern) içinden önceden hesaplanmış bir tablo (prefix tablosu veya başlangıç tablosu olarak da bilinir) oluşturulur. Tablo, kalıbın içindeki özel bir desene (prefix) dayanmaktadır.Metnin (text) başından itibaren ilerlenir ve kalıp (pattern) ile karşılaştırılır. Eğer kalıbın bir karakteri metnin ilgili karakteri ile eşleşirse, ilerleme devam eder ve sonraki karakterler karşılaştırılır. Kalıpın bir karakteri metnin ilgili karakteri ile eşleşmezse, prefix tablosu kullanılarak bir kaydırma (shift) hesaplanır ve metinde bu kaydırma kadar ilerleme yapılır. Kalıbın sonuna kadar ilerlenirse ve tüm karakterler eşleşirse, arama tamamlanmıştır ve kalıp metin içinde bulunmuştur.Arama, kalıp bulunana kadar yukarıdaki adımları tekrarlar veya metin tamamen taranıncaya kadar devam eder.



Çalışma zamanı analizi için, en iyi, en kötü ve ortalama sınırlar aşağıdaki gibi belirlenebilir:

En İyi Durum: Kalıpın metin içinde ilk karakterde bulunduğu durumdur. Bu durumda arama bir adımda bulunur ve zaman karmaşıklığı O(1)'dir.
En Kötü Durum: Metnin tamamen taranması gerektiği durumdur. Örneğin, kalıpın metin içinde hiç bulunmadığı durumda en kötü durum zaman karmaşıklığı O(n)'dir, n metnin karakter sayısını temsil eder.
Ortalama Durum: Morris-Pratt algoritmasının ortalama durum zaman karmaşıklığı O(n+m)'dir, n metnin karakter sayısını ve m kalıpın karakter sayısını temsil eder. Bu durumda prefix tablosunun hesaplanması da dikkate alınır.
Bu sınırlar, Morris-Pratt algoritmasının performansını tahmin etmek için kullanılabilir ve kalıbın metin içinde bulunma süresini belirler.



Matematiksel ve Asimptotik Analiz

Zaman Karmaşıklığı: Morris-Pratt algoritmasının zaman karmaşıklığı, metnin (text) ve kalıbın (pattern) uzunluğuna bağlıdır. Genel olarak, bu algoritmanın zaman karmaşıklığı O(n + m) olarak ifade edilir, burada n, metnin uzunluğunu ve m, kalıbın uzunluğunu temsil eder. Morris-Pratt algoritması, kalıbın prefix tablosunu önceden hesaplayarak her karakteri sadece bir kez karşılaştırdığından, kötü durum (worst case) zaman karmaşıklığı O(n + m) olarak gerçekleşir.

En İyi Durum Karmaşıklığı: Morris-Pratt algoritmasının en iyi durum karmaşıklığı O(n/m) olarak ifade edilir. Bu durum, kalıbın metin içinde hiç kaydırma yapmadan doğru eşleşmenin bulunduğu durumdur. Yani, kalıbın başındaki karakterler metin içinde tam eşleşiyorsa, en iyi durum karmaşıklığı bu şekildedir.

En Kötü Durum Karmaşıklığı: Morris-Pratt algoritmasının en kötü durum karmaşıklığı O(n + m) olarak ifade edilir. Bu durum, kalıbın metnin sonuna kadar kaydırma yapmak zorunda kaldığı durumdur. Yani, kalıbın metin içinde eşleşme olmadığı durumda en kötü durum karmaşıklığı bu şekildedir.

Ortalama Durum Karmaşıklığı: Morris-Pratt algoritmasının ortalama durum karmaşıklığı O(n + m) olarak ifade edilir. Morris-Pratt algoritması, kalıbın prefix tablosunu önceden hesaplayarak her karakteri sadece bir kez karşılaştırdığından, ortalama durum karmaşıklığı da en kötü durum karmaşıklığına eşdeğerdir.

Morris-Pratt algoritması, diğer bazı string arama algoritmalara göre daha hızlı olabilir, özellikle kalıbın uzunluğu metne göre küçük olduğunda veya kalıbın tekrar eden desenlere sahip olduğu durumlarda avantajlıdır. Ancak, algoritmanın prefix tablosunu önceden hesaplamak gerektiği için bazı ekstra bellek kullanımı gerektirebilir.
