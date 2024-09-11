## Link PWS Biyung Cafe
http://abella-maya-biyung.pbp.cs.ui.ac.id/

## Link Vercel Biyung Cafe


## Link Railway Biyung Cafe


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

~~~mermaid
Pola Django;
   User/Client -->|Request dalam bentuk HTTP| urls.py;
   urls.py -->|Memilih view| views.py;
~~~

~~~mermaid
   info
~~~


```mermaid 
   gitGraph
        commit id: "1"
        commit id: "2"
        branch nice_feature
        checkout nice_feature
        commit id: "3"
        checkout main
        commit id: "4"
        checkout nice_feature
        branch very_nice_feature
        checkout very_nice_feature
        commit id: "5"
        checkout main
        commit id: "6"
        checkout nice_feature
        commit id: "7" type: REVERSE
        checkout main
        commit id: "customID"
        merge nice_feature tag: "customTag"
        checkout very_nice_feature
        commit id: "8"
        checkout main
        commit id: "9"

   
