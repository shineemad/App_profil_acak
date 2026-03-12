const express = require('express');
const app = express();
const port = 3000;

// Data pura-pura (sebagai pengganti database sementara)
const dataMahasiswa = [
    { id: 1, nama: "Budi Santoso", nim: "230001", peminatan: "Jaringan" },
    { id: 2, nama: "Siti Aminah", nim: "230002", peminatan: "Kecerdasan Buatan" },
    { id: 3, nama: "Ahmad", nim: "230003", peminatan: "Rekayasa Perangkat Lunak" }
];

// Endpoint 1: Beranda
app.get('/', (req, res) => {
    res.send('Halo! Selamat datang di API Kampus buatan Ahmad.');
});

// Endpoint 2: Mengambil semua data mahasiswa
app.get('/api/mahasiswa', (req, res) => {
    res.json({
        status: "sukses",
        total: dataMahasiswa.length,
        data: dataMahasiswa
    });
});

// Menyalakan server
app.listen(port, () => {
    console.log(`🚀 Server menyala! Buka browser dan pergi ke http://localhost:${port}`);
});

// Endpoint 3: Mengambil data mahasiswa berdasarkan ID (Dynamic Routing)
app.get('/api/mahasiswa/:id', (req, res) => {
    // 1. Ambil ID yang diketik pengguna di URL
    // Catatan: Semua yang berasal dari URL bentuknya teks (String), 
    // jadi kita ubah ke angka (Integer) menggunakan parseInt()
    const idDicari = parseInt(req.params.id);

    // 2. Cari di dalam "database" (Array) menggunakan fungsi .find()
    const mahasiswaDitemukan = dataMahasiswa.find(mhs => mhs.id === idDicari);

    // 3. Cek apakah datanya ada?
    if (mahasiswaDitemukan) {
        // Jika ketemu, kirim datanya
        res.json({
            status: "sukses",
            data: mahasiswaDitemukan
        });
    } else {
        // Jika TIDAK ketemu, kirim status HTTP 404 (Not Found)
        res.status(404).json({
            status: "gagal",
            pesan: `Mahasiswa dengan ID ${idDicari} tidak ditemukan!`
        });
    }
});