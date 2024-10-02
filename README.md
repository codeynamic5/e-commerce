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
   Melanjuti dari Tutorial 2, saya telah melaksanakan steps sesuai dengan Tutorial. Namun, mayoritas saya modifikasi menyesuaikan Tugas 3 yang telah saya kembangkan.
   1. Membuat input form untuk menambahkan objek model pada app sebelumnya.
      Sebelumnya saya telah menambahkan
      ###
            import uuid
      ###
      pada file models.py untuk mengubah menjadi UUID.
      Kemudian, saya menambahkan berkas forms.py di dalam main yang berisi:
      ###
            from django.forms import ModelForm
            from main.models import ProductEntry
            
            class ProductEntryForm(ModelForm):
                class Meta:
                    model = ProductEntry
                    fields = ["name", "price", "description"]
      ###
   3. Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
      Pada direktori main, di dalam file views.py, saya menambahkan kode:
      ###
            from django.shortcuts import render, redirect
            from main.forms import ProductEntryForm
            from main.models import ProductEntry
            from .models import ProductEntry
            from django.http import HttpResponse
            from django.core import serializers
            
            # Create your views here.
            def show_main(request):
                product_entries = ProductEntry.objects.all()
                context = {'product_entries' : product_entries}
                return render(request, "main.html",context)
            
            def show_model_main(request):
                return render(request, "model_main.html") 
            
            def show_static_main(request):
                return render(request, "static_main.html")
            
            def create_product_entry(request):
                form = ProductEntryForm(request.POST or None)

                if form.is_valid and request.method == "POST":
                    form.save()
                    return redirect('main:show_main')
                
                context = {'form': form}
                return render(request, "create_product_entry.html", context)

            def show_xml(request):
                data = ProductEntry.objects.all()
                return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
            
            def show_json(request):
                data = ProductEntry.objects.all()
                return HttpResponse(serializers.serialize("json", data), content_type="application/json")
            
            def show_xml_by_id(request, id):
                data = ProductEntry.objects.filter(pk=id)
                return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
            
            def show_json_by_id(request, id):
                data = ProductEntry.objects.filter(pk=id)
                return HttpResponse(serializers.serialize("json", data), content_type="application/json")
      ###
      dengan mengimport ProductEntry langsung dari models.py.

      Untuk menampilkan kode dalam web, saya menambahkan kode pada berkas main.html:
      ###
            {% if not product_entries %}
            <p>Belum ada data product pada Biyung Cafe.</p>
            {% else %}
            <table class="putih">
              <tr>
                <th>Product ID</th>
                <th>Product Name</th>
                <th>Price</th>
                <th>Description</th>
              </tr>
            
              {% comment %} Berikut cara memperlihatkan data product di bawah baris ini 
              {% endcomment %} 
              {% for product_entry in product_entries %}
              <tr>
                <td>{{product_entry.id}}</td>
                <td>{{product_entry.name}}</td>
                <td>{{product_entry.price}}</td>
                <td>{{product_entry.description}}</td>
              </tr>
              {% endfor %}
            </table>
            {% endif %}
            
            <br />
            
            <a href="{% url 'main:create_product_entry' %}">
              <button>Add New Product Entry</button>
            </a>
            {% endblock content %}
      ###
   5. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
      Untuk mengakses fungsi yang telah ditambah sebelumnya, saya tambahkan kode pada berkas urls.py:
      ###
            from django.urls import path
            from main.views import show_main, show_model_main, show_static_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
            
            
            
            
            app_name = 'main'
            
            urlpatterns = [
                path('', show_main, name='show_main'),
                path('model/', show_model_main, name='show_model_main'),
                path('static/', show_static_main, name='show_static_main'),
                path('create-product-entry', create_product_entry, name='create_product_entry'),
                path('xml/', show_xml, name='show_xml'),
                path('json/', show_json, name='show_json'),
                path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
                path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
               ]
      ###

## Screenshot dari hasil akses URL pada Postman 

   ### show_xml 
   <img width="1800" alt="Screenshot 2024-09-18 at 03 56 33" src="https://github.com/user-attachments/assets/8b037533-6d2d-4a25-9d92-33086c46c75f">

   ### show_json
   <img width="1800" alt="Screenshot 2024-09-18 at 03 56 44" src="https://github.com/user-attachments/assets/c96a15ad-e300-4926-a020-851227156a4a">

   ### show_xml_id
   <img width="1800" alt="Screenshot 2024-09-18 at 03 57 23" src="https://github.com/user-attachments/assets/351a8864-518b-4265-94b6-7fa74e1170af">

   ### show_json_id
   <img width="1800" alt="Screenshot 2024-09-18 at 03 56 56" src="https://github.com/user-attachments/assets/bbca1579-f73d-41bb-96a1-598782fd271f">





# Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django

## 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
   Dalam Django, HttpResponseRedirect() dan redirect() keduanya digunakan untuk mengarahkan user ke URL lain. Namun, ada beberapa perbedaan dari keduanya:
   **Perbedaan Utama:**
|           HttpResponseRedirect()          |                redirect()              |
|-------------------------------------------|----------------------------------------|
| spesifik menerima URL dalam bentuk string | fleksibel, menerima URL, views, models |
   ### HttpResponseRedirect()
   - HttpResponseRedirect() adalah kelas bawaan Django. Biasanya digunakan untuk menampilkan status respons kode HTTP 302 (redirection) dan URL tujuan request dari user.
   - HttpResponseRedirect() biasanya digunakan apabila ingin melakukan redirect ke URL dengan tujuan yang lebih spesifik. URL yang diberikan harus dalam bentuk string lengkap atau objek dari URL.
   ### redirect()
   - redirect() adalah sebuah fungsi shortcut yang digunakan untuk mengarahkan user. Sebenarnya, fungsi redirect() menggunakan HttpResponseRedirect() di dalamnya. Namun, redirect() memiliki opsi yang lebih bervariasi.
   - Fungsi ini dapat digunakan untuk mengarahkan ke berbagai hal, seperti URL dalam bentuk string, tampilan nama dalam view yang dapat dimodifikasi di urls.py, dan mengedit objek model.

## 2. Jelaskan cara kerja penghubungan model Product dengan User!
   Dalam menghubungkan model Product dan User di Django, biasanya menggunakan ForeignKey untuk memberikan produk user sebuah tanda kepemilikian.
   <br /> **Cara Kerja:** <br />
   1. Menentukan Model User &rarr; 2. Membuat Model Product &rarr; 3. Memodifikasi Views &rarr; 4. Memodifikasi Template <br />
   <br />
   1. Django memiliki model User sendiri yang biasanya digunakan dengan model untuk membuat sebuah relasi. <br />
   2. Pembuatan model product menggunakan ForeignKey untuk menghubungkan ke User. Foreignkey menggunakan parameter on_delete yang menentukan tindakan pada saat data pengguna dihapus. <br />
   3. Apabila model telah terhubung, selanjutnya adalah memodifikasi kode dalam views untuk membuat atau mengambil produk yang dimiliki oleh user spesifik. <br />
   4. Dalam menampilkan sebuah produk yang dimiliki oleh user tertentu di template, kode html yang di dalam template dapat dimodifikasi sesuai dengan desain yang akan ditampilkan pada saat login. Dari situ, user yang telah login dapat mengakses semua produk yang dimilikinya.  

## 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
   *Authentication* dan *authorization* merupakan konsep keamanan yang sangat krusial dan sering digunakan untuk mengelola akses user pada aplikasi web. Kedua konsep tersebut sering digunakan secara bersama, tetapi memiliki perbedaan yang cukup signifikan. Berikut perbedaan dari keduanya:
   ### Authentication
   *Authentication* atau otentikasi merupakan proses verifikasi identitas pengguna yang digunakan sebagai "security measure" untuk mengukur keamanan sebuah user yang sedang melakukan proses login.
   **Proses:** <br />
   User yang sedang login akan diverifikasi identitas dan kredensial (username dan password) sesuai dengan informasi yang tersimpan dalam database. Apabila semua data benar atau sesuai, user telah terotentikasi dan dapat mengakses sistem.
   ### Authorization
   *Authorization* atau otorisasi merupakan proses setelah otentikasi, yaitu proses memeriksa kembali kredibilitas user. Proses ini menentukan apakah user yang telah terotentikasi memiliki izin untuk melanjutkan akses dalam menggunakan sistem.
   **Proses:** <br />
   Setelah melalui proses otentikasi, sistem akan memeriksa kembali hal user dalam menggunakan fitur tertentu dalam sistem tersebut. Sistem akan mengecek apakah user berhak memiliki akses dalam menggunakan halaman admin atau memodifikasi database.
   ### Proses User Login
   Proses *Authentication* (Otentikasi) &rarr; Verifikasi Kebenaran Username & Password sesuai Database oleh Django &rarr; Benar, maka User terotentikasi & User dapat menggunakan sistem &rarr; Proses *Authorization* (Otorisasi), memeriksa hak akses user
   ### Implementasi Authentication & Authorization oleh Django
   **Authentication oleh Django** <br />
   Django memiliki sistem otentikasi bawaan yang sangat efisien dengan menangani proses login, logout, register, dan penyimpanan informasi user yang telah terotentikasi dalam sistem.
   <br /> Fitur: <br />
   - Login = menggunakan `authenticate()` dan `login()` untuk melakukan verifikasi user dan apabila berhasil, membuat sesi untuk user. <br />
   - Logout = `logout()` untuk mengakhiri sesi user.
   - Middleware = `AuthenticationMiddleware` digunakan untuk memastikan setiap request yang diterima oleh Django memiliki `request.user`. Hal tersebut adalah agar user dapat terotentikasi.
   
   <br /> **Authorization oleh Django** <br />
   Django memiliki *permissions* dan *groups* yang digunakan Django untuk mengatur otorisasi user.
   <br /> Fitur: <br />
   - Permissions = `add`, `delete`, `change` yang memberikan "izin" kepada user atau *groups*.
   - Groups = Beberapa *permissions* yang memebentuk kelompok, sehingga dapat lebih mudah dikelola.
   - User.is_authenticated = memeriksa status login user, apakah sudah login atau belum.
   - User.has_perm() = memeriksa izin tertentu yang dimiliki user.
   - @login_required decorator = memastikan halaman yang terbuka hanya bisa diakses oleh user yang telah login.
   
   <br /> **Contoh Penggunaan Authentication & Authorization oleh Django** <br />
   - Login form = login form yang digunakan oleh user untuk memasukkan data seperti username dan password dengan memverifikasi kebenaran identitas user.
   - Otorisasi halaman admin = memastikan otorisasi yang diberikan kepada user adalah user yang telah melakukan login, sehingga user dapat mengakses halaman tertentu.
   
## 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
   ### Cara Django Mengingat Pengguna yang Telah Login
   User yang berhasil login akan diberikan sesi oleh Django dan menyimpan user dalam database. Dengan menggunakan cookies, Django dapat menghubungkan user dengan sesi browser.
   <br /> **Proses:** <br />
   - Login user yang berhasil dibuatkan sesi khusus untuk user dan menyimpan data (*session ID*) dalam server.
   - Django mengirim *session ID* tersebut ke browser dalam bentuk `cookie`.
   - Setiap *request* dari user akan dikirim dalam bentuk `cookie` oleh browser ke server.
   - *Session ID* yang diterima dari cookie akan digunakan oleh Django untuk mencari data sesi yang sesuai di server. Apabila Django menemukan data yang sesuai dan mengetahui informasi user, nanti akan memuat data user seperti informasi login.
   
   ### Kegunaan Lain dari Cookies
   `Cookies` adalah file kecil yang disimpan di browser user dan biasanya dikirim oleh server. `Cookies` memiliki berbagai kegunaan, seperti berikut: 
   - *Authentication* = `Cookies` digunakan sebagai tempat untuk menyimpan *session ID* user yang telah berhasil login.
   - Melacak Aktivitas User = Banyak situs web menggunakan `cookies` untuk melacak aktivitas user dalam web tersebut. Data dari aktivitas digunakan untuk analisis algoritma target pasar.
   - *Shopping Bag* = Situs *E-Commerce* sering menggunakan `cookies` untuk menyimpan produk dalam sebuah 'kerangjang belanja'. User yang menemukan produk atau barang yang diinginkan dapat memasukkan barang tersebut ke dalam keranjang belanja untuk nantinya dapat diproses apabila ingin dibeli. Sehingga, user tidak kehilangan daftar produk yang telah disimpan saat berpindah halaman.

   ### Keamanan Cookies
   Tidak semua `cookies` aman digunakan. Berikut adalah beberapa masalah keamanan terkait dengan cookies:
   - *Session Hijacking* = Pencurian *session ID* oleh pihak luar karena *session ID* yang tidak diamankan dengan benar.
   - XSS (*Cross-Site Scripting*) = Penyisipan skrip berbahaya dalam situs web yang dapat mencuri cookies user, sehingga pihak luar dapat menggunakan cookies tersebut untuk login ke akun user sebenarnya.
   - Cookies yang Tidak Terenkripsi = Penyerangan cookies melalui HTTP (koneksi tidak aman) yang dapay menyebabkan kebocoran data.
   
## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Seperti tugas-tugas sebelumnya, saya menggunakan Tutorial, dalam kasus ini adalah Tutorial 3, sebagai fondasi dari Tugas 4 dengan mode yang telah dimodifikasi sesuai aplikasi yang saya kembangkan.
1. Mengimplementasikan Fungsi Registrasi, Login, dan Logout
   - Membuat Form Registrasi
     Untuk membuat form registrasi dapat menggunakan `UserCreationForm` yang ada di dalam Django. Saya memodifikasi beberapa file, yaitu `views.py` dan `urls.py`. Saya menambahkan file baru di templates yaitu `register.html`
     **views.py**:
     ```
      def register(request):
          form = UserCreationForm()
      
          if request.method == "POST":
              form = UserCreationForm(request.POST)
              if form.is_valid():
                  form.save()
                  messages.success(request, 'Your account has been successfully created!')
                  return redirect('main:login')
          context = {'form':form}
          return render(request, 'register.html', context)
     ```
     **urls.py**
     ```
      urlpatterns = [
          path('', show_main, name='show_main'),
          path('model/', show_model_main, name='show_model_main'),
          path('static/', show_static_main, name='show_static_main'),
          path('create-product-entry', create_product_entry, name='create_product_entry'),
          path('xml/', show_xml, name='show_xml'),
          path('json/', show_json, name='show_json'),
          path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
          path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
          path('register/', register, name='register'),
          path('login/', login_user, name='login'),
          path('logout/', logout_user, name='logout'),
      ]
     ```
     **register.html**
     ```
         {% extends 'base.html' %}

         {% block meta %}
         <title>Register</title>
         {% endblock meta %}
         
         {% block content %}
         
         <div class="login">
           <h1>Register</h1>
         
           <form method="POST">
             {% csrf_token %}
             <table>
               {{ form.as_table }}
               <tr>
                 <td></td>
                 <td><input type="submit" name="submit" value="Daftar" /></td>
               </tr>
             </table>
           </form>
         
           {% if messages %}
           <ul>
             {% for message in messages %}
             <li>{{ message }}</li>
             {% endfor %}
           </ul>
           {% endif %}
         </div>
         
         {% endblock content %}
     ```
   - Mengimplementasikan Login dan Logout
     Di dalam `views.py` saya menambahkan fungsi `login_user` dan `logout_user` dengan menambahkan file html baru di dalam templates.
     **views.py**
     `login_user`
     ```
      def login_user(request):
         if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
      
            if form.is_valid():
                  user = form.get_user()
                  login(request, user)
                  response = HttpResponseRedirect(reverse("main:show_main"))
                  response.set_cookie('last_login', str(datetime.datetime.now()))
                  return response
      
         else:
            form = AuthenticationForm(request)
         context = {'form': form}
         return render(request, 'login.html', context)
     ```
     `logout_user`
     ```
     def logout_user(request):
       logout(request)
       response = HttpResponseRedirect(reverse('main:login'))
       response.delete_cookie('last_login')
       return response
     ```
     `login.html`
     ```
      {% extends 'base.html' %}

      {% block meta %}
      <title>Login</title>
      {% endblock meta %}
      
      {% block content %}
      <div class="login">
        <h1>Login</h1>
      
        <form method="POST" action="">
          {% csrf_token %}
          <table>
            {{ form.as_table }}
            <tr>
              <td></td>
              <td><input class="btn login_btn" type="submit" value="Login" /></td>
            </tr>
          </table>
        </form>
      
        {% if messages %}
        <ul>
          {% for message in messages %}
          <li>{{ message }}</li>
          {% endfor %}
        </ul>
        {% endif %} Don't have an account yet?
        <a href="{% url 'main:register' %}">Register Now</a>
      </div>
      
      {% endblock content %}
     ```
     Untuk mengakses logout button, saya menambahkan kode di main.html dalam folder templates:
     ```
      <a href="{% url 'main:logout' %}">
        <button>Logout</button>
      </a>
     ```
2. Membuat Dua Akun Pengguna dengan Masing-masing Tiga *Dummy* Data
   <br /> **Pengguna abellacantik123**
   <img width="1800" alt="Screenshot 2024-09-25 at 08 53 42" src="https://github.com/user-attachments/assets/cdd09ccd-9d50-4277-81d2-b6dd558786d5">

   **Pengguna abellahebat321**
   <img width="1800" alt="Screenshot 2024-09-25 at 09 20 05" src="https://github.com/user-attachments/assets/c9839ee6-8246-46c4-813a-84a66096cd2a">

3. Menghubungkan Model Product dengan User
   Untuk menampilkan product dengan user yang login, saya memodifikasi beberapa file:
   **models.py**
   ```
      class ProductEntry(models.Model):
   
          user = models.ForeignKey(User, on_delete=models.CASCADE)
          
   ```
   Menggunakan `ForeignKey` 
   **views.py**
   ```
      @login_required(login_url='/login')
      def show_main(request):
          product_entries = ProductEntry.objects.filter(user=request.user)
          context = {'product_entries' : product_entries, 'name': request.user.username, 'last_login': request.COOKIES['last_login']}
          return render(request, "main.html",context)
   ```
   Mengubah product_entries
   **settings.py**
   ```
      PRODUCTION = os.getenv("PRODUCTION", False)
      DEBUG = not PRODUCTION
   ```
4. Menampilkan Detail Informasi Pengguna yang Sedang Logged In
   Saya memodifikasi `file main.html` dengan memasukkan `name` dari user yang sedang menjalani sesi login, dalam kasus ini adalah abellahebat321. Implementasi file main.html adalah dari berkas `views.py` untuk menampilkan user:
   ```
      def show_main(request):
          product_entries = ProductEntry.objects.filter(user=request.user)
          context = {'product_entries' : product_entries, 'name': request.user.username, 'last_login': request.COOKIES['last_login']}
          return render(request, "main.html",context)
   ```
   **Tampilan User Login**
   <img width="1800" alt="Screenshot 2024-09-25 at 09 30 00" src="https://github.com/user-attachments/assets/dc400e5f-7d4b-414d-8e20-1fae23db2ecd">

   **Inspect Cookies**
   <img width="1800" alt="Screenshot 2024-09-25 at 09 31 32" src="https://github.com/user-attachments/assets/f80b1cb3-8f72-4434-be9d-9fc18ae54d9c">


# Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS
## 1. Urutan Prioritas CSS Selector
Apabila terdapat beberapa CSS Selector yang terdapat dalam satu elemen HTML, urutan prioritas diatur oleh *specificity* dan *importance*. Dalam kata lain, fungsi CSS selector secara spesifik dan kepentingannya dalam satu elemen HTML. Urutan CSS selector adalah sebagai berikut:
   1. **Inline Styles**
      <br />Sebuah style yang ditulis langsung dalam HTML dan memiliki prioritas tertinggi.
      <br />`<div class="navbar">`
   2. **ID Selectors**
      <br />ID selectors menggunakan elemen ID dan merupakan selector dengan tingkat prioritas tinggi.
      <br />`#header {}`
   3. **Class, Attribute, Pseudo-class Selectors**
      <br />Beberapa selector ini memiliki prioritas di bawah ID selectors.
      <br />Class: `.nav {}`
      <br />Attribute: `[type="text"] {}`
      <br />Pseudo-Class: `:hover {}`
   4. **Element & Pseudo-element Selectors**
      <br />Merupakan selecto untuk elemen HTML `p {}` atau elemen pseudo `::before {}`. Biasanya prioritas terendah dalam urutan CSS selectors.
   5. **Universal Selector, Combinators, Inheritance**
      <br />Memiliki prioritas paling rendah.
      <br />`* {}`
   6. **!important**
      <br />Tanda ini berarti apabila sebuah aturan CSS terdapat `!important`, maka aturan CSS tersebut tidak berlaku atau tidak penting untuk diimplementasikan.
## 2. Pentingnya Responsive Design dalam Pengembangan Web
**Responsive Design** adalah sebuah pendekatan yang digunakan dalam web untuk mengatur ukuran layar sehingga dapat menyesuaikan dengan perangkat yang sedang digunakan secara otomatis seperti *handphone*, *tablet*, dan *smartphone*. *Responsive Design* penting untuk pengembangan web karena beberapa alasan:
- **User Experience**
<br />Keberagaman perangkat yang digunakan menyebabkan perbedaan dalam ukuran layar, sehingga pengalaman dalam mengimplementasikan sebuah web aplikasi juga berbeda. *Responsive design* menjadi sebuah hal yang esensial agar tampilan web terlihat lebih bagus dan memiliki fungsionalitas yang tepat di berbagai layar dengan berbagai resolusi.
- **Efisiensi Pengembangan**
<br />Efektivitas dan efisiensi dalam mengembangkan sebuah web menjadi lebih canggih dengan adanya *responsive design*, yang tadinya pengembangan web dilakukan dari berbagai perangkat untuk menyesuaikan dengan *device* satu per satu. Sekarang, pengembangan web dapat dilakukan dari satu web dan menyesuaikan sesuai dengan perangkat yang digunakan.
- **SEO (Search Engine Optimization)**
<br />Prioritas web adalah situs yang *mobile-friendly* dalam hasil pencariannya. Sehingga, website yang responsif akan memiliki visibilitas yang lebih baik dan tinggi.
<br />**Contoh Aplikasi**
- Sudah Menerapkan *Responsive Design*
**Twitter**, **Instagram**, **YouTube**. Semua aplikasi tersebut telah menerapkan *responsive design*, di mana tampilan di berbagai perangkat telah disesuaikan dengan perangkat yang dimodifikasikan.
- Belum Menerapkan *Responsive Design*
Beberapa situs *e-commerce* yang lama memiliki desain yang belum dikembangkan untuk menyesuaikan dengan perkembangan perangkat yang ada.
## 3. Perbedaan antara Margin, Border, dan Padding
![image](https://github.com/user-attachments/assets/9e5c4875-ca5a-46a3-bb01-223372d8dc7c)
**Margin**
<br />Jarak antara elemen dengan elemen di sekitarnya atau di luar border.
<br />
<br />**Border**
<br />Garis pembatas di sekitar padding dan konten elemen. Border terletak di antara margin dan padding.<br />
<br />**Padding**
<br />Ruang antara konten elemen dan border elemen. Padding berada di paling dalam.
<br />
<br />**Contoh Implementasi CSS**
<br />
   ```
      div {
        margin: 20px; /* Jarak di luar elemen */
        border: 2px solid black; /* Garis batas di sekeliling elemen */
        padding: 10px; /* Jarak antara konten dan border */
      }
   ```
## 4. Konsep Flexbox dan Grid Layout Beserta Kegunaannya
**Flexbox (Flexible Box Layout)**
![image](https://github.com/user-attachments/assets/ba71af12-a539-4e2c-bd7b-4d89917c2ea0)
<br /> **Flexbox** adalah sistem tata letak satu dimensi yang digunakan untuk mengatur item dalam satu arah, antara baris atau kolom. **Flexbox** biasanya digunakan untuk mengatur elemen agar fleksibel dan menyesuaikan dengan ukuran kontainer. 
<br /> Contoh:
<br />
- Item disusun secara otomatis sesuai dengan ruang yang ada seperti stretch, wrap, dll. <br />
- Alignment secara vertikal atau horizontal: `align-items`, `justify-content` <br />
- Mengatur urutan item yang fleksibel <br />
**Contoh Implementasi Flexbox** 
```
.container {
  display: flex;
  justify-content: space-between; /* Menyebar elemen di antara space */
  align-items: center; /* Elemen berada di tengah secara vertikal */
}
```
<br />

**Grid Layout**
![image](https://github.com/user-attachments/assets/0fd4008b-9875-406b-a346-3863150840e7)
<br />**Grid Layout** adalah sistem tata letak dua dimensi dan cenderung lebih kompleks dari *Flexbox*. Grid memungkinkan pengaturan elemen dalam bentuk baris dan kolom secara bersamaan. Grid digunakan untuk membuat layout yang terstruktur dan memiliki presisi yang lebih dengan menggunakan grid (baris dan kolom). Grid juga memungkinkan pengaturan *layout kompleks* dengan cara yang lebih mudah dan efisien.
<br /> **Contoh Implementasi Grid Layout**
```
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* 3 kolom dengan lebar yang sama */
  grid-gap: 10px; /* Jarak antar elemen grid */
}
```
## Implementasi Checklist Step-by-Step
Saya menggunakan referensi tutorial untuk mengerjakan tugas. Namun, karena saya menggunakan Bootstrap, saya memodifikasi sendiri beberapa fitur dalam Tugas 5 ini.
<br />
1. Implementasikan Fungsi untuk Menghapus dan Mengedit Produk
   - Membuat View untuk Edit dan Delete Produk
      <br />Edit Produk:
     <br />Buat view yang menampilkan form edit untuk produk yang sudah ada. Pada saat form disubmit, update produk di database.
      <br />Delete Produk:
     <br />Buat view untuk menghapus produk berdasarkan product_id. Gunakan konfirmasi sebelum produk dihapus (misalnya menggunakan modal konfirmasi).
   - Implementasi URL Routing
     <br />Tambahkan routing di urls.py untuk edit dan delete produk:
     ```
     path('product/edit/<int:product_id>/', views.edit_product, name='edit_product'),
     path('product/delete/<int:product_id>/', views.delete_product, name='delete_product'),
     ```
   - Template Edit/Delete
     <br />Di dalam template HTML produk (main.html), buat dua tombol:
     <br />Tombol Edit mengarahkan pengguna ke halaman edit produk dan Tombol Delete memanggil fungsi penghapusan produk.
     ```
     <a href="{% url 'edit_product' product_entry.pk %}" class="btn btn-info">Edit</a>
      <a href="{% url 'delete_product' product_entry.pk %}" class="btn btn-danger">Delete</a>
     ```
2. Kustomisasi Desain Halaman Login, Register, dan Tambah Produk
   - Halaman Login
     <br />Gunakan form login Django, kemudian kustomisasikan menggunakan Bootstrap. Tambahkan elemen visual seperti gambar, padding, atau background warna.
     ```
     <div class="container mt-5">
        <div class="col-md-6 offset-md-3">
          <div class="card">
            <div class="card-header bg-primary text-white">
              <h3 class="text-center">Login</h3>
            </div>
            <div class="card-body">
              <form method="post">
                {% csrf_token %}
                {{ form.as_p }}
                <button type="submit" class="btn btn-success btn-block">Login</button>
              </form>
            </div>
          </div>
        </div>
      </div>
     ```
   - Halaman Add Product
     <br />Untuk halaman add product, buat form untuk memasukkan data produk (seperti nama produk, harga, dan deskripsi) dan gunakan kelas Bootstrap untuk mempercantik tampilan form.
     ```
     <div class="container mt-5">
        <div class="col-md-6 offset-md-3">
          <div class="card">
            <div class="card-header bg-success text-white">
              <h3 class="text-center">Tambah Produk Baru</h3>
            </div>
            <div class="card-body">
              <form method="post">
                {% csrf_token %}
                {{ form.as_p }}
                <button type="submit" class="btn btn-primary btn-block">Tambah Produk</button>
              </form>
            </div>
          </div>
        </div>
      </div>
     ```
3. Kustomisasi Halaman Daftar Produk
   - Kondisi Jika Tidak Ada Produk
     <br />Jika produk belum ada, tampilkan gambar dan pesan.
     ```
           {% if not product_entries %}
            <div class="text-center text-light mt-4">
              <img
                src="{% static 'products/no-cheese.png' %}"
                alt="No Products"
                class="img-fluid mb-3"
                style="max-width: 300px"
              />
              <p style="color: rgb(243, 247, 251)">
                Belum ada data product pada Biyung Cafe.
              </p>
            </div>
     ```
   - Kondisi Jika Ada Produk
     <br />Tampilkan daftar produk dalam bentuk card menggunakan grid layout, seperti yang sudah dibahas sebelumnya. Dalam file `main.html`:
     ```
         {% for product_entry in product_entries %}
          <div class="col-md-4">
            <div class="card h-50 shadow-sm">
  
           <div class="card-body">
   
               <!-- <td>{{product_entry.id}}</td> -->
               <h5 class="card-title">{{product_entry.name}}</h5>
               <p class="card-text">{{product_entry.price}}</p>
               <p class="card-text">{{product_entry.description}}</p>
   
               <!-- Action Buttons -->
               <div class="card-footer d-flex justify-content-center">
                     <a href="{% url 'main:edit_product' product_entry.pk %}">
                       <button class="btn btn-info">Edit</button>
                     </a>
   
                     <a href="{% url 'main:delete_product' product_entry.pk %}">
                       <button class="btn btn-danger">Delete</button>
                     </a>
   
               </div>
               
        </div>
     ```
   - Bootstrap
     <br />Gunakan Bootstrap grid system untuk memastikan card tampil responsif di berbagai ukuran layar. 
     ```
        .product-grid {
           display: grid;
           grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
           gap: 20px;
         }
         
         .product-card {
           background-color: #fff;
           padding: 20px;
           border-radius: 10px;
           height: 100%;
           box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
         }
     ```
4. Membuat Navigasi Bar (Navbar)
   <br />Buat navbar yang responsif dengan Bootstrap untuk mengakomodasi link ke halaman login, daftar produk, dan tambah produk. Dalam `base.html`:
   ```
   <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Biyung</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a
                class="nav-link active"
                aria-current="page"
                href="{% url 'main:show_main' %}"
                >Home</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'main:show_model_main' %}"
                >History</a
              >
            </li>
            <li class="nav-item dropdown">
              <a
                class="nav-link dropdown-toggle"
                href="#"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                Menu
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="{% url 'main:show_static_main' %}">Food</a></li>
                <li><a class="dropdown-item" href="#">Beverages</a></li>
              </ul>
            </li>
          </ul>

   ```

