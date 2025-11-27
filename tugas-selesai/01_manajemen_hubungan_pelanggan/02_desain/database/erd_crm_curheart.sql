-- =====================================================
-- ERD Database CRM CUR-HEART
-- Entity Relationship Diagram
-- =====================================================

-- Table: users
-- Menyimpan data pengguna sistem (klien, terapis, admin)
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('client', 'therapist', 'admin') NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table: clients
-- Menyimpan data profil klien yang detail
CREATE TABLE clients (
    client_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT UNIQUE NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    date_of_birth DATE,
    gender ENUM('male', 'female', 'other'),
    emergency_contact VARCHAR(100),
    emergency_phone VARCHAR(20),
    medical_history TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Table: therapists
-- Menyimpan data profil terapis
CREATE TABLE therapists (
    therapist_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT UNIQUE NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    specialization VARCHAR(100),
    license_number VARCHAR(50),
    years_experience INT,
    bio TEXT,
    photo_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Table: bookings
-- Menyimpan data reservasi dan interaksi
CREATE TABLE bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    client_id INT NOT NULL,
    therapist_id INT NOT NULL,
    service_type VARCHAR(100) NOT NULL,
    booking_date DATE NOT NULL,
    booking_time TIME NOT NULL,
    duration INT DEFAULT 90, -- dalam menit
    status ENUM('pending', 'confirmed', 'completed', 'cancelled') DEFAULT 'pending',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    FOREIGN KEY (therapist_id) REFERENCES therapists(therapist_id) ON DELETE CASCADE
);

-- Table: sessions
-- Menyimpan data sesi terapi
CREATE TABLE sessions (
    session_id INT PRIMARY KEY AUTO_INCREMENT,
    booking_id INT UNIQUE NOT NULL,
    session_date TIMESTAMP NOT NULL,
    duration INT, -- durasi aktual dalam menit
    status ENUM('scheduled', 'in_progress', 'completed', 'cancelled') DEFAULT 'scheduled',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE CASCADE
);

-- Table: session_notes
-- Menyimpan catatan terapis untuk setiap sesi (SOAP format)
CREATE TABLE session_notes (
    note_id INT PRIMARY KEY AUTO_INCREMENT,
    session_id INT NOT NULL,
    subjective TEXT, -- Keluhan klien
    objective TEXT, -- Observasi terapis
    assessment TEXT, -- Diagnosis/penilaian
    plan TEXT, -- Rencana tindak lanjut
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE CASCADE
);

-- Table: messages
-- Menyimpan komunikasi antara klien dan terapis
CREATE TABLE messages (
    message_id INT PRIMARY KEY AUTO_INCREMENT,
    sender_id INT NOT NULL,
    receiver_id INT NOT NULL,
    message_text TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sender_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (receiver_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Table: reviews
-- Menyimpan ulasan dan penilaian klien
CREATE TABLE reviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    booking_id INT UNIQUE NOT NULL,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE CASCADE
);

-- Table: notifications
-- Menyimpan notifikasi untuk pengguna
CREATE TABLE notifications (
    notification_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    message TEXT NOT NULL,
    type ENUM('booking', 'session', 'message', 'review', 'system') NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- =====================================================
-- INDEXES untuk optimasi query
-- =====================================================

-- Index untuk pencarian berdasarkan email dan username
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);

-- Index untuk pencarian booking berdasarkan tanggal dan status
CREATE INDEX idx_bookings_date ON bookings(booking_date);
CREATE INDEX idx_bookings_status ON bookings(status);
CREATE INDEX idx_bookings_client ON bookings(client_id);
CREATE INDEX idx_bookings_therapist ON bookings(therapist_id);

-- Index untuk pencarian sesi berdasarkan tanggal
CREATE INDEX idx_sessions_date ON sessions(session_date);
CREATE INDEX idx_sessions_status ON sessions(status);

-- Index untuk pencarian pesan yang belum dibaca
CREATE INDEX idx_messages_receiver ON messages(receiver_id);
CREATE INDEX idx_messages_read ON messages(is_read);

-- Index untuk pencarian notifikasi yang belum dibaca
CREATE INDEX idx_notifications_user ON notifications(user_id);
CREATE INDEX idx_notifications_read ON notifications(is_read);

-- =====================================================
-- RELASI ANTAR TABEL
-- =====================================================

-- users (1) ↔ (1) clients: One-to-One
-- users (1) ↔ (1) therapists: One-to-One
-- clients (1) ↔ (N) bookings: One-to-Many
-- therapists (1) ↔ (N) bookings: One-to-Many
-- bookings (1) ↔ (1) sessions: One-to-One
-- sessions (1) ↔ (N) session_notes: One-to-Many
-- users (1) ↔ (N) messages (sender): One-to-Many
-- users (1) ↔ (N) messages (receiver): One-to-Many
-- bookings (1) ↔ (1) reviews: One-to-One
-- users (1) ↔ (N) notifications: One-to-Many
