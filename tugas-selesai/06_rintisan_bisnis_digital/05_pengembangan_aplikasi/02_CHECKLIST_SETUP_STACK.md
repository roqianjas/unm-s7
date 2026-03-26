# Checklist Setup Stack

Stack target V1:

1. Laravel 12
2. Inertia.js
3. React + TypeScript (TSX)
4. MySQL 8

## A. Prasyarat lokal

1. PHP 8.3+
2. Composer 2+
3. Node.js 20+ dan npm
4. MySQL 8+
5. Git

## B. Bootstrap project

Contoh langkah:

```bash
composer create-project laravel/laravel curheart-app
cd curheart-app
composer require laravel/breeze --dev
php artisan breeze:install react --typescript
npm install
npm run build
php artisan key:generate
```

## C. Konfigurasi backend dasar

1. Aktifkan Sanctum bila diperlukan API token.
2. Buat role-based middleware: `guest/client/therapist/admin`.
3. Siapkan struktur module untuk: auth, bookings, payments, sessions, notifications, withdrawals.

## D. Konfigurasi database

1. Buat database `curheart_db`.
2. Sinkronkan migration sesuai baseline schema 22 tabel.
3. Seed data awal role, system settings, layanan, dan akun demo internal.

## E. Kebijakan payment wajib

1. Hanya channel VA/Bank Transfer dan Card.
2. Nonaktifkan e-wallet dan QRIS di konfigurasi gateway.
3. Tidak membuat fitur wallet user.

## F. Verify checklist

1. `npm run dev` berjalan tanpa error.
2. Login role-based berhasil.
3. Endpoint API `/api/v1` dapat diakses sesuai auth.
4. Booking -> payment callback -> status update berjalan.
