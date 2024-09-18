# Nama Aplikasi
Biyung Cafe

## Nama: Abella Maya Santi
## Kelas: PBP B

## Link PWS Biyung Cafe
[http://abella-maya-ebiyung.pbp.cs.ui.ac.id/](http://abella-maya-ebiyung.pbp.cs.ui.ac.id/)



# Tugas 2
## Implementasi Checklist Tugas Step-by-Step 
Sebagai fondasi awal dalam mengerjakan tugas, saya mengikuti Tutorial 0 dan Tutorial 1. Namun, ada beberapa kode yang saya modifikasi berdasarkan penyesuaian terhadap web yang saya ingin kembangkan.
1. **Membuat sebuah proyek Django baru.**

   Dimulai dengan membuat proyek Django baru yang akan digunakan untuk mengembangkan web e-commerce. Pada proyek Django kali ini, saya membuat sebuah web e-commerce dalam sektor Food and Beverages, yaitu sebuah web cafe yang bernama Biyung Cafe. Dikarenakan proyek yang dikembangkan merupakan e-commerce, proyek Django yang telah saya buat di repositori lokal sebagai direktori utama saya adalah e-commerce dengan perintah yang saya gunakan:
   ~~~
       django-admin startproject e_commerce .
   ~~~
   Pada perintah tersebut, e_commerce merupakan subdirektori dari direktori utama e-commerce.
    
2. **Membuat aplikasi dengan nama main pada proyek tersebut.**

   Pada direktori utama e-commerce, virtual environment harus diaktifkan dengan cara menggunakan perintah berikut dalam terminal:
    ~~~
       source env/bin/activate
    ~~~
    Karena saya menggunakan operating system Mac OS, maka saya menggunakan perintah di atas untuk mengaktifkan virtual environment. Virtual Environment tersebut dibutuhkan sebelum melanjutkan prosedur dalam pembuatan aplikasi main. Perintah yang saya gunakan dalam mengaktifkan aplikasi main adalah sebagai berikut:
    ~~~
       python3 manage.py startapp main
    ~~~
    Aplikasi main ini nanti akan saya gunakan dalam membangun web dengan aplikasi main ini sebagai struktur awal pembuatan web Biyung Cafe.
   Agar aplikasi main ini dapat terdeteksi dalam program, aplikasi main harus didaftarkan ke dalam proyek terlebih dahulu. Pendaftaran aplikasi main dilakukan dalam file settings.py yang berada dalam subdirektori e_commerce. Aplikasi main didaftarkan ke dalam variabel INSTALLED_APPS:
   ~~~
       INSTALLED_APPS = [
           ...,
           'main'
   ~~~
   
    
3. **Melakukan routing pada proyek agar dapat menjalankan aplikasi main.**

   Apabila telah melakukan pendaftaran aplikasi main, salah satu prosedur yang dapat dilakukan agar aplikasi main dapat terbaca dan diakses melalui web adalah dengan membuat berkas urls.py, yaitu sebuah file yang dapat dibaca oleh web sehingga dapat diakses. Dengan pembuatan file urls.py, file diisi dengan:
   ~~~
      urlpatterns = [
          path('admin/', admin.site.urls),
          path('biyung/', include('main.urls')),
          path('', include('main.urls')),
      ]
   ~~~
   

4. **Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.**
   - name
   - price
   - description
   - image, atribut tambahan
  
   Pada Biyung Cafe, saya memiliki sejumlah Product yang tersedia. Product tersebut saya tambahkan dalam file models.py, dengan kode seperti berikut:
      ~~~
      class Product(models.Model):
          name = models.CharField(max_length=255)
          price = models.DecimalField(max_digits=10 , decimal_places=3)
          description = models.TextField(max_length=500)
          image = models.ImageField(upload_to='products/', null=True, blank=True)
     ~~~
   Apabila saya ingin menambah atau mengedit product, saya dapat mengaksesnya melalui Django Admin dengan membuat superuser.
      ~~~
         python manage.py createsuperuser
      ~~~
5. **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.**

   Pembuatan fungsi pada views.py menampilkan halaman Home, Model, dan Static. Fungsi dalam views.py dimodifikasi kembali dalam file urls.py agar dapat diakses dengan link url.
      ~~~
      # Create your views here.
      def show_main(request):
          
          return render(request, "main.html")
      
      def show_model_main(request):
      
          context = Product.objects.all()
          
          return render(request, "model_main.html", {'context' : context})
      
      def show_static_main(request):
          return render(request, "static_main.html")
      ~~~

6. **Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.**

   Saya memiliki tiga path url yang ditampilkan di web, yaitu Home/main, Model, dan Static. Untuk mengakses halaman main atau dalam web yang saya buat adalah biyung, maka tautan yang dapat diakses adalah:
   - Home/main: http://localhost:8000/biyung/
   - Model: http://localhost:8000/biyung/model/
   - Static: http://localhost:8000/biyung/static/
   ~~~
       from django.urls import path
       from main.views import show_main
        
       app_name = 'main'
        
       urlpatterns = [
           path('', show_main, name='show_main'),
           path('model/', show_model_main, name='show_model_main'),
           path('static/', show_static_main, name='show_static_main'),
       ]
   ~~~

7. **Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**

   Apabila web yang telah dimodifikasi telah selesai, langkah selanjutnya adalah deploy ke PWS dengan cara push ke PWS. Sebelum push ke PWS, dapat git add, commit, dan push ke git terlebih dahulu.
   ~~~
      git push pws master
   ~~~
   Sesuai dengan branch yang digunakan. 


## Bagan Request Client ke Web Aplikasi Django & Respon Client

   ```mermaid 
   gitGraph
        branch user
        checkout user
        commit id: "Client"
        branch url
        checkout url
        commit id: "Browser: HTTP"
        branch views
        checkout views
        commit id: "Akses view"
        branch models
        checkout models
        commit id: "Database"
        branch html
        checkout html
        commit id: "Template" type: REVERSE
        merge user
        checkout user
   ```

   - user mengirimkan request yang dikirim dalam bentuk http.
   - urls.py menerima request tersebut dan menentukan view yang akan diakses berdasarkan URL yang diterima.
   - views.py berisi fungsi perintah sesuai dengan request dari user, request tersebut ditangani oleh views.py. Response yang diberikan akan berupa bentuk HTML.
   - models.py mengandung program Python yang akan digunakan dan dikonek dengan tabel database.
   - tempate berisi file-file dalam bentuk HTML, CSS, maupun JavaScript yang memberikan struktur dan layout halaman aplikasi web. Ouput dari template adalah yang dikirimkan kembali ke user sebagai tampilan web.

## Fungsi git dalam Pengembangan Perangkat Lunak

Git memiliki banyak fungsi dalam pengembangan perangkat lunak, di antaranya yaitu:
1. Version Control: Git mampu melacak setiap perubahan yang ada pada sumber kode.
2. Kolaborasi: Dalam menggunakan git, mampu melaksanakan kerja sama dengan orang lain, sehingga kolaborasi kode juga memungkinkan. Ada beberapa fitur seperti branching dan merging.
3. Integritas Kode: Perubahan yang ada dalam kode dapat diuji dan dicek kembali untuk memastikan validasi kode tersebut.

## Alasan Framework Django dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak

Django sering dijadikan framework awal untuk pembelajaran karena:
1. Fitur Canggih: Django hadir dengan berbagai fitur (misalnya, otentikasi, manajemen pengguna, admin panel), sehingga memungkinkan pemula memahami konsep dasar pengembangan aplikasi web tanpa perlu membangun dari nol.
2. Dokumentasi yang Baik: Django memiliki dokumentasi yang sangat baik dan komunitas yang besar, yang memudahkan pembelajaran dan penyelesaian masalah.
3. Konvensi over Konfigurasi: Django memiliki default yang aman, sehingga pemula dapat fokus pada logika aplikasi tanpa terlalu banyak konfigurasi.

## Alasan model pada Django disebut sebagai ORM

Model pada Django disebut sebagai ORM (Object-Relational Mapping) adalah karena Django menggunakan teknik ORM untuk menghubungkan model Python dengan tabel database. ORM memungkinkan pengembang untuk berinteraksi dengan database menggunakan objek Python dan menggunakan SQL secara langsung, sehingga memudahkan penulisan detail database dan membuat kode lebih mudah dibaca dan dipelihara.





# Tugas 3

## Alasan Kenapa Data Delivery Dibutuhkan dalam Pengimplementasian sebuah Platform
   ### Data Delivery
   Proses pengiriman (transfer) data dari satu titik ke titik lain dalam jaringan atau sistem informasi. Pada saat mengimplementasikan sebuah platform yang berbasis web atau mobile, ada beberapa alasan mengapa data delivery dibutuhkan:
   1. Data yang Disediakan dengan Real-Time
      Data delivery yang cepat dan efisien memungkinkan penyediaan data atau informasi lebih akurat dan instan.
   2. Keamanan Data
      Proses keamanan data delivery memungkinkan informasi pribadi dan sensitif dapat terjaga dengan protokol keamanan seperti enkripsi yang memastikan data tersebut tidak bocor selamam proses pengiriman.
   3. User Experience
      Pengalaman pengguna dapat menjadi optimal dikarenakan data delivery yang cepat dan canggih. Contohnya adalah halaman web yang telah dimodifikasi untuk mempunyai data delivery yang efisien dan bagus sehingga pengalaman pengguna dalam menggunakan web tersebut sangat mengesankan.
   4. Skalabilitas
      Dalam sebuah platform, banyaknya pengguna dalam menggunakan data dapat mengakibatkan lambatnya sebuah platform memproses semuanya. Oleh karena itu, penggunaan data delivery dibutuhkan untuk menampung berbagai informasi dan data yang diproses dan memastikan performa yang maksimal.
   5. Konektivitas
      Data delivery dapat menghubungkan komponen-komponen yang terpisah, seperti front-end dan back-end. Sehingga, data yang diproses dan kemudian ditampilkan dapat diolah dengan lancar oleh server hingga bekerja secara optimal.

   ### Referensi
   ~~~
      Hill, J. (2021). Efficient Data Delivery for Modern Applications. O'Reilly Media.
   ~~~
      
 
## Perbandingan antara XML dan JSON. Mengapa JSON lebih populer dibandingkan XML?
   ### Struktur dan Format
        - XML (eXtensible Markup Language)
         XML menggunakan format tag yang panjang. Hal tersebut membuat program lebih kompleks dan ukuran file besar.
        - JSON (JavaScript Object Notation)
         JSON memiliki struktur dan format yang lebih sederhana dan ringkas karena JSON menggunakan format dengan notasi berbasis objek, yang mirip dengan JavaScript.
   ### Kecepatan Program
      - XML (eXtensible Markup Language)
         Dikarenakan XML memiliki struktur program yang kompleks sehingga menyebabkan program berjalan dengan lebih lambat.
      - JSON (JavaScript Object Notation)
         JSON memiliki format yang lebih ringan sehingga program berjalan lebih cepat dan mudah.
   ### Web Development Compatibility
      - XML (eXtensible Markup Language)
         Penggunaan XML dalam web platform lebih minim dibandingkan JSON.
      - JSON (JavaScript Object Notation)
         JSON memiliki compatibility banyak dalam menggunakan web development. JSON banyak diadopsi oleh berbagai API modern dan layanan web yang canggih dengan framework dan teknologi yang luas.
   ### Ukuran
      - XML (eXtensible Markup Language)
         XML memproses lebih banyak kode dibandingkan dengan JSON.
      - JSON (JavaScript Object Notation)
         JSON mentransfer data lebih cepat karena memiliki format lebih kecil dibandingkan XML.
   ### Di atas merupakan beberapa alasan mengapa JSON lebih populer dibandingkan XML. Mulai dari kapabilitas yang dapat memproses program dengan lebih efisien dan cepat dibandingkan XML.

 
## Fungsi dari method is_valid() pada Form Django dan Mengapa kita Membutuhkan Method tersebut?
   ### Fungsi is_valid()
      1. Method is_valid() dalam Django digunakan untuk memeriksa validasi data yang diinput dalam form.
      2. Membersihkan dan menyimpan data yang telah terbutkti valid sesuai pemeriksaan yang telah dilakukan sebelumnya.
      3. Mengidentifikasi error yang dapat terjadi apabila data yang diinput False.
   ### Alasan Mengapa Membutuhkan Method is_valid()
      Method is_valid() dibutuhkan karena validasi data input mudah dan otomatis dengan keamanan data yang memastikan privasi yang terjaga/tersimpan dengan baik. Dengan method tersebut, Django memungkinkan untuk memberikan feedback dengan jelas kepada pengguna sehingga pengguna mengetahui kesalahan yang terjadi dalam form input.
   ### Referensi
      - Django Documentation. *"Form and field validation"* (n.d.). Retrieved from [Django Official Documentation](https://docs.djangoproject.com/en/stable/ref/forms/api/#django.forms.Form.is_valid)
      - Vincent, A. (2020). *"Building Secure Web Forms with Django."*
 
## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
   ### Alasan membutuhkan csrf_token saat membuat form di Django
      1. Perlindungan dari Serangan CSRF. Dengan token CSRF, mekanisme yang digunakan dapat melindungi aplikasi web dari serangan Cross-Site Request Forgery.
      2. Validitas Permintaan. Permintaan POST dapat dipastikan oleh CSRF berasal dari pengguna yang valid untuk mengakses web secara langsung.
   ### Akibat tidak menambahkan csrf_token pada form Django
      Apabila csrf_token tidak ditambahkan pada form Django, dapat terjadi breach pada form Django tersebut. Tanpa adanya csrf_token, form Django rentan terhadap berbagai serangan luar, di mana penyerang mengirim sebuah permintaan atas nama pengguna tanpa sepengetahuan pengguna. Penyerang tersebut dapat menggunakan sesi aktif pengguna asli untuk mengirimkan sebuah pengiriman palsu, seperti pencurian data atau melakukan transaksi terlarang.
   ### Pemanfaatan kehilangan csrf_token pada form Django oleh penyerang
      - Eksploitasi Sesi Aktif Pengguna 
         Dengan hilangnya token CSRF, penyerang dapat memanfaatkan sesi aktif pengguna karena tidak ada keamanan yang tersedia sehingga dapat masuk dan mengirim sebuah permintaan yang palsu.
      - Pembuatan Permintaan Palsu Otentik
         Tanpa token CSRF, web akan dengan mudah diserang dengan pembuatan sebuah permintaan palsu yang tidak dapat diperiksa perbedaan antara yang asli dan yang palsu. Pembuatan permintaan tersebut tanpa sepengetahuan pengguna.
## Implementasi Checklist secara Step-by-Step
