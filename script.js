// 1. Menyiapkan "Alat Kerja" (Mengambil elemen dari HTML)
const tombol = document.getElementById('tombol-tarik');
const wadah = document.getElementById('wadah-profil');

// 2. Memberi perintah: "Kalau tombol diklik, jalankan fungsi ini"
// Kita pakai 'async' karena kita butuh waktu untuk mengambil data dari internet
tombol.addEventListener('click', async function() {
    
    // 3. Menampilkan Status Loading
    wadah.innerHTML = '<p>Sedang memuat data...</p>';

    // 4. Mulai mencoba mengambil data (Gunakan blok try...catch untuk jaga-jaga kalau error)
    try {
        // a. Pergi ke "dapur" API untuk minta data, lalu TUNGGU (await) sampai datanya datang
        const respons = await fetch('https://randomuser.me/api/');
        
        // b. Kalau dapurnya tutup atau ada masalah server, lemparkan error!
        if (!respons.ok) {
            throw new Error('Server bermasalah!');
        }

        // c. Ubah paket data mentah dari dapur menjadi format JSON yang bisa dibaca JavaScript
        const data = await respons.json();
        
        // d. Membongkar paket data (Mengambil orang pertama dari hasil pencarian)
        const pengguna = data.results[0];
        
        // e. Mengekstrak 3 hal yang diminta senior: Foto, Nama, Email
        const foto = pengguna.picture.large;
        const namaLengkap = `${pengguna.name.first} ${pengguna.name.last}`;
        const email = pengguna.email;

        // 5. Menyajikan data ke "meja makan" (Tampilkan ke layar)
        // Kita gunakan backtick (`) agar bisa memasukkan variabel ke dalam HTML dengan mudah
        wadah.innerHTML = `
            <img src="${foto}" alt="Foto Profil">
            <h3>${namaLengkap}</h3>
            <p>Email: ${email}</p>
        `;

    } catch (error) {
        // 6. Penanganan Eror (Kalau internet mati atau langkah 4 gagal)
        wadah.innerHTML = '<p>Gagal mengambil data. Silakan coba lagi.</p>';
        console.error("Detail error:", error); // Ini untuk membantumu melihat masalah di Inspect Element
    }
});