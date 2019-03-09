# GuvercinYuvaPrensibi

Güvercin Yuvası (Pigeonhole Principle)

Bilgisayar bilimleri de dahil olmak üzere pek çok matematik temelli bilim ve mühendislik alanında kullanılan oldukça basit bir umdedir. İsmini güvercin yuvalarından alan bu kaideye göre yuva sayısından fazla güvercin varsa, ve bütün güvercinler bir yuvaya girecekse, en az bir yuvaya birden fazla güvercin girmek zorundadır.
Bu durumu sembollerle göstermemiz gerekirse n tane yuva ve m tane güvercin için m > n durumunda en az bir yuvada birden fazla güvercin bulunmalıdır.
Bilgisayar bilimlerinde çok sayıda sonsuz küme ile uğraşırken oldukça kullanışlı olan bu kaide, örneğin özetleme fonksiyonlarında (hashing function) bir çakışma (collision) ihtimalinin hesaplanmasında ya da kayıpsız sıkıştırma algoritmasının (lossless compression algorithm) istatistiksel analizinde kullanılabilir.
Örnek: N adet pozitif tam sayı arasında en az iki sayının farkı N-1’e tam bölünebilir.
Yukarıdaki iddiayı (hipotez) güvercin yuvası prensibi ile ispatlayalım. Öncelikle N adet tam sayımız olduğunu biliyoruz. Bu sayılara a1, a2, …, aN diyelim ve herhangi bir ai sayısı için N-1bölümünden kalan değerini ri diyelim. Yani ri = ai mod(N-1) olsun.
Şimdi güvercin yuvası prensibini kullanıyoruz ve diyoruz ki elimizde en fazla N-1 tane farklı kalan değeri olabilir. Yani ri değerinden en fazla N-1 tane olabilir. Sebebi ise basit, mod(N-1) içinde en fazla N-1 farklı sayı olabilir. Peki elimizde kaç sayı var ? N sayı. Dolayısıyla en az iki sayının bölümünden kalan değer aynı olacaktır. Diğer bir değişle N farklı sayının N-1 farklı kalana bölünmesi durumunda en az iki sayı aynı kalan sahip olacaktır. Bu sayıların farkı da aynı kalana sahip olacağından iddiamızı ispatlamış oluruz.
Örnek: N pozitif tam sayı için, sayıların bir kısmının yada tamamının toplamı N ile kalansız bölünebilir.
Bu iddianın ispatında da sayıları matematiksel olarak modelleyelim. Öncelikle toplamları b ile ifade edersek, b1 = (a1) mod(N), b2 =(a1 + a2) mod(N), b3 = (a1+a2+a3) mod(N), …, bN = (a1 + … + aN) mod(N) olarak göstermek mümkündür. Şayet sayılardan birisi 0 ise, yani b değerlerinden birisinin 0 olduğunu bulabiliyorsak, bu durumda zaten ispat yapılmış olur. Çünkü iddiamızda N ile kalansız bölünebileceğinden bahsediyorduk.
Şayet sayılardan birisi 0 değilse bu durumda toplamları elde ettiğimiz sayıların seçiminde a1 ‘den başlayarak ai gibi bir sayıya kadar olanları almak yerine (ai+1 + … + aj) mod(N) = 0, olduğunu gösterebiliriz.
Gerçekten de mod N işlemi sonucunda N-1 farklı sayı çıkacağını biliyoruz. Elimizde N sayı bulunduğunu düşünürsek o zaman yukarıdaki gösterime göre en az iki tane b değeri aynı olmalıdır. Örneğin bu değerler bi = bj olsun ve i < j olduğunu kabul edelim. Bu durumda (ai+1 + … + aj) mod(N) = 0 olduğu gösterilmiş olur.
Kaynak: http://bilgisayarkavramlari.sadievrenseker.com/2009/12/10/guvercin-yuvasi-kaidesi-pigeonhole-principle/
