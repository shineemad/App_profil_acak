const tombol = document.getElementById("tombol-tarik");
const wadah = document.getElementById("wadah-profil");

tombol.addEventListener("click", async function () {
  tombol.disabled = true;
  wadah.classList.remove("loaded");
  wadah.innerHTML = `
        <div class="loading-state">
            <div class="loader-spin"></div>
            Sedang memuat data...
        </div>`;

  try {
    const respons = await fetch("https://randomuser.me/api/");
    if (!respons.ok) throw new Error("Server bermasalah!");

    const data = await respons.json();
    const pengguna = data.results[0];
    const foto = pengguna.picture.large;
    const namaLengkap = `${pengguna.name.first} ${pengguna.name.last}`;
    const email = pengguna.email;
    const telepon = pengguna.phone;
    const lokasi = `${pengguna.location.city}, ${pengguna.location.country}`;

    wadah.innerHTML = `
            <div style="width:100%">
                <img class="profile-avatar" src="${foto}" alt="Foto Profil">
                <div class="profile-name">${namaLengkap}</div>
                <div class="profile-location">${lokasi}</div>
                <div class="profile-divider"></div>
                <div class="profile-row">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                    ${email}
                </div>
                <div class="profile-row">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.55 12a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.46 1h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 8.43a16 16 0 0 0 5.66 5.66l1.79-1.8a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                    ${telepon}
                </div>
            </div>`;
  } catch (error) {
    wadah.innerHTML = `
            <div class="error-state">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="margin:0 auto 12px;display:block;opacity:.6">
                    <circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/>
                </svg>
                Gagal mengambil data. Silakan coba lagi.
            </div>`;
    console.error("Detail error:", error);
  } finally {
    tombol.disabled = false;
  }
});
