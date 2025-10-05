# LARAVEL SETUP GUIDE
## SATRIAMART Integrated Management System (SIMS)

### Prerequisites
- **PHP:** 8.0 atau lebih baru
- **Composer:** Package manager untuk PHP
- **MySQL:** 8.0 atau lebih baru
- **Node.js:** 16.x atau lebih baru (untuk asset compilation)
- **Git:** Version control

### 1. Laravel Installation

```bash
# 1. Create new Laravel project
composer create-project laravel/laravel satriamart-sims
cd satriamart-sims

# 2. Install additional Laravel packages
composer require laravel/sanctum
composer require spatie/laravel-permission
composer require barryvdh/laravel-cors
composer require laravel/telescope

# 3. Install development dependencies
composer require --dev laravel/sail
composer require --dev phpunit/phpunit
composer require --dev pestphp/pest
composer require --dev pestphp/pest-plugin-laravel
```

### 2. Frontend Setup (TailwindCSS)

```bash
# 1. Install Node dependencies
npm install

# 2. Install TailwindCSS
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

# 3. Install additional frontend packages
npm install alpinejs
npm install chart.js
npm install @fortawesome/fontawesome-free

# 4. Configure TailwindCSS (tailwind.config.js)
module.exports = {
  content: [
    "./resources/**/*.blade.php",
    "./resources/**/*.js",
    "./resources/**/*.vue",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#667eea',
        secondary: '#764ba2'
      }
    },
  },
  plugins: [],
}
```

### 3. Environment Configuration

```bash
# 1. Copy environment file
cp .env.example .env

# 2. Generate application key
php artisan key:generate

# 3. Configure database in .env
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=satriamart_sims
DB_USERNAME=your_username
DB_PASSWORD=your_password

# 4. Configure app settings
APP_NAME="SATRIAMART SIMS"
APP_ENV=local
APP_DEBUG=true
APP_URL=http://localhost:8000
```

### 4. Database Setup

```sql
-- Create MySQL database
CREATE DATABASE satriamart_sims CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create user (optional)
CREATE USER 'sims_user'@'localhost' IDENTIFIED BY 'secure_password';
GRANT ALL PRIVILEGES ON satriamart_sims.* TO 'sims_user'@'localhost';
FLUSH PRIVILEGES;
```

### 5. Laravel Configuration

```bash
# 1. Run migrations
php artisan migrate

# 2. Install Sanctum
php artisan vendor:publish --provider="Laravel\Sanctum\SanctumServiceProvider"
php artisan migrate

# 3. Install Telescope (development only)
php artisan telescope:install
php artisan migrate

# 4. Install Spatie Permission
php artisan vendor:publish --provider="Spatie\Permission\PermissionServiceProvider"
php artisan migrate

# 5. Seed database with sample data
php artisan db:seed
```

### 6. Asset Compilation

```bash
# Development
npm run dev

# Production
npm run build

# Watch for changes
npm run watch
```

### 7. Running the Application

```bash
# Start Laravel development server
php artisan serve

# Or using Laravel Sail (Docker)
./vendor/bin/sail up

# Access application at:
# http://localhost:8000
```

### 8. Project Structure

```
satriamart-sims/
├── app/
│   ├── Http/
│   │   ├── Controllers/
│   │   │   ├── DashboardController.php
│   │   │   ├── CustomerController.php
│   │   │   ├── OrderController.php
│   │   │   ├── InventoryController.php
│   │   │   └── ProductionController.php
│   │   ├── Middleware/
│   │   ├── Requests/
│   │   └── Resources/
│   ├── Models/
│   │   ├── User.php
│   │   ├── Customer.php
│   │   ├── Order.php
│   │   ├── Product.php
│   │   └── WorkOrder.php
│   └── Services/
├── database/
│   ├── migrations/
│   ├── seeders/
│   └── factories/
├── resources/
│   ├── views/
│   │   ├── layouts/
│   │   ├── dashboard/
│   │   ├── customers/
│   │   ├── inventory/
│   │   └── production/
│   ├── js/
│   └── css/
└── routes/
    ├── web.php
    └── api.php
```

### 9. Key Features Implementation

#### Models (Eloquent)
```php
// app/Models/Customer.php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Factories\HasFactory;

class Customer extends Model
{
    use HasFactory;

    protected $fillable = [
        'name', 'email', 'phone', 'address', 
        'customer_type', 'company_name', 'contact_person'
    ];

    public function orders()
    {
        return $this->hasMany(Order::class);
    }
}
```

#### Controllers
```php
// app/Http/Controllers/CustomerController.php
<?php

namespace App\Http\Controllers;

use App\Models\Customer;
use Illuminate\Http\Request;

class CustomerController extends Controller
{
    public function index(Request $request)
    {
        $query = Customer::query();

        if ($request->has('search')) {
            $search = $request->get('search');
            $query->where(function($q) use ($search) {
                $q->where('name', 'like', "%{$search}%")
                  ->orWhere('email', 'like', "%{$search}%");
            });
        }

        $customers = $query->paginate(15);

        return view('customers.index', compact('customers'));
    }
}
```

#### Views (Blade Templates)
```blade
<!-- resources/views/customers/index.blade.php -->
@extends('layouts.app')

@section('content')
<div class="max-w-7xl mx-auto px-6 py-8">
    <div class="flex justify-between items-center mb-8">
        <h1 class="text-3xl font-bold text-gray-800">Customers</h1>
        <a href="{{ route('customers.create') }}" 
           class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600">
            Add Customer
        </a>
    </div>

    <div class="bg-white rounded-lg shadow overflow-hidden">
        <table class="w-full">
            <thead class="bg-gray-50">
                <tr>
                    <th class="px-6 py-3 text-left">Name</th>
                    <th class="px-6 py-3 text-left">Email</th>
                    <th class="px-6 py-3 text-left">Type</th>
                    <th class="px-6 py-3 text-left">Actions</th>
                </tr>
            </thead>
            <tbody>
                @foreach($customers as $customer)
                <tr class="border-t">
                    <td class="px-6 py-4">{{ $customer->name }}</td>
                    <td class="px-6 py-4">{{ $customer->email }}</td>
                    <td class="px-6 py-4">{{ ucfirst($customer->customer_type) }}</td>
                    <td class="px-6 py-4">
                        <a href="{{ route('customers.show', $customer) }}" 
                           class="text-blue-600 hover:text-blue-800">View</a>
                    </td>
                </tr>
                @endforeach
            </tbody>
        </table>
    </div>

    <div class="mt-6">
        {{ $customers->links() }}
    </div>
</div>
@endsection
```

### 10. Testing

```bash
# Run PHPUnit tests
php artisan test

# Run specific test
php artisan test --filter CustomerTest

# Run with coverage
php artisan test --coverage
```

### 11. Deployment

```bash
# Optimize for production
php artisan config:cache
php artisan route:cache
php artisan view:cache

# Clear caches (if needed)
php artisan config:clear
php artisan cache:clear
php artisan view:clear
```

### 12. Development Tips

1. **Use Laravel Telescope** untuk debugging
2. **Implement proper validation** dengan Form Requests
3. **Use Eloquent relationships** untuk efficient queries
4. **Follow Laravel conventions** untuk maintainable code
5. **Use TailwindCSS utility classes** untuk consistent styling

### 13. Helpful Commands

```bash
# Create new controller
php artisan make:controller CustomerController --resource

# Create new model with migration
php artisan make:model Customer -m

# Create new request
php artisan make:request CustomerRequest

# Create new seeder
php artisan make:seeder CustomerSeeder

# Create new factory
php artisan make:factory CustomerFactory --model=Customer

# Clear all caches
php artisan optimize:clear
```

### 14. Resources

- [Laravel Documentation](https://laravel.com/docs)
- [TailwindCSS Documentation](https://tailwindcss.com/docs)
- [Laravel Sanctum](https://laravel.com/docs/sanctum)
- [Spatie Laravel Permission](https://spatie.be/docs/laravel-permission)
