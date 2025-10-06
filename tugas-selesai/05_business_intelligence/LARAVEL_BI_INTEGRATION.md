# BUSINESS INTELLIGENCE INTEGRATION DENGAN LARAVEL
## SATRIAMART SIMS - BI MODULE

**Universitas Nusa Mandiri**  
**Fakultas Teknologi Informasi**  
**Program Studi Sistem Informasi**  
**Semester 7**

---

**Mata Kuliah:** Business Intelligence II  
**Dosen Pengampu:** Ridan Nurfalah, M.Kom  
**Kelompok:** [Nama Kelompok - 3 Anggota]  
**Tanggal:** Oktober 2025

---

## PENDAHULUAN

### Mengapa Laravel untuk Business Intelligence?

**Business Intelligence dapat diintegrasikan langsung dengan SATRIAMART SIMS** yang sudah menggunakan Laravel. Hal ini memberikan keuntungan:

1. **Konsistensi Tech Stack** - Menggunakan framework yang sama
2. **Data Integration** - Langsung akses ke operational database
3. **Cost Efficiency** - Tidak perlu infrastruktur terpisah
4. **Development Speed** - Menggunakan expertise yang sudah ada
5. **Maintenance Simplicity** - Satu platform untuk semua

---

## ARCHITECTURE INTEGRATION

### BI sebagai Module dalam SIMS

```
┌─────────────────────────────────────────────────────────────┐
│                 SATRIAMART SIMS (Laravel)                   │
├─────────────────────────────────────────────────────────────┤
│  CRM Module  │  Orders Module  │  Inventory  │  Production  │
├─────────────────────────────────────────────────────────────┤
│                    BI ANALYTICS MODULE                       │
├─────────────────────────────────────────────────────────────┤
│   Dashboards   │   Reports   │  Data Warehouse  │  ML/AI    │
├─────────────────────────────────────────────────────────────┤
│                   SHARED LARAVEL FOUNDATION                  │
├─────────────────────────────────────────────────────────────┤
│     Database (MySQL)    │    Authentication    │   APIs     │
└─────────────────────────────────────────────────────────────┘
```

### Data Flow dalam Sistem Terintegrasi

```
Operational Data (SIMS) → Laravel ETL Commands → Data Warehouse Tables → BI Dashboards
```

---

## LARAVEL BI IMPLEMENTATION

### 1. Data Warehouse dengan Laravel Migration

```php
// database/migrations/create_bi_dimensions.php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateBiDimensions extends Migration
{
    public function up()
    {
        // Dimension Tables
        Schema::create('dim_customers', function (Blueprint $table) {
            $table->id('customer_key');
            $table->string('customer_id')->unique();
            $table->string('customer_name');
            $table->string('customer_type');
            $table->string('industry_sector')->nullable();
            $table->string('region');
            $table->string('city');
            $table->decimal('customer_value', 15, 2)->default(0);
            $table->date('registration_date');
            $table->boolean('is_current')->default(true);
            $table->timestamp('effective_date');
            $table->timestamp('expiry_date')->nullable();
            $table->timestamps();
        });

        Schema::create('dim_products', function (Blueprint $table) {
            $table->id('product_key');
            $table->string('product_id')->unique();
            $table->string('product_name');
            $table->string('category_level1');
            $table->string('category_level2')->nullable();
            $table->decimal('unit_price', 10, 2);
            $table->decimal('cost_price', 10, 2);
            $table->string('unit_of_measure');
            $table->boolean('is_current')->default(true);
            $table->timestamp('effective_date');
            $table->timestamp('expiry_date')->nullable();
            $table->timestamps();
        });

        Schema::create('dim_dates', function (Blueprint $table) {
            $table->id('date_key');
            $table->date('full_date')->unique();
            $table->integer('day_of_week');
            $table->string('day_name');
            $table->integer('day_of_month');
            $table->integer('day_of_year');
            $table->integer('week_of_year');
            $table->string('month_name');
            $table->integer('month_of_year');
            $table->integer('quarter');
            $table->integer('year');
            $table->boolean('is_weekend');
            $table->boolean('is_holiday')->default(false);
            $table->string('fiscal_quarter');
            $table->integer('fiscal_year');
        });
    }

    public function down()
    {
        Schema::dropIfExists('dim_dates');
        Schema::dropIfExists('dim_products');
        Schema::dropIfExists('dim_customers');
    }
}
```

### 2. Fact Tables dengan Laravel

```php
// database/migrations/create_bi_facts.php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateBiFacts extends Migration
{
    public function up()
    {
        Schema::create('fact_sales', function (Blueprint $table) {
            $table->id();
            // Foreign Keys to Dimensions
            $table->unsignedBigInteger('date_key');
            $table->unsignedBigInteger('customer_key');
            $table->unsignedBigInteger('product_key');
            
            // Business Keys
            $table->string('order_number');
            $table->integer('order_line_number');
            
            // Measures
            $table->integer('quantity_sold');
            $table->decimal('unit_price', 10, 2);
            $table->decimal('discount_amount', 10, 2)->default(0);
            $table->decimal('net_amount', 12, 2);
            $table->decimal('cost_amount', 12, 2);
            $table->decimal('gross_profit', 12, 2);
            $table->decimal('profit_margin', 5, 2);
            
            $table->timestamps();
            
            // Foreign Key Constraints
            $table->foreign('date_key')->references('date_key')->on('dim_dates');
            $table->foreign('customer_key')->references('customer_key')->on('dim_customers');
            $table->foreign('product_key')->references('product_key')->on('dim_products');
            
            // Composite Primary Key
            $table->unique(['date_key', 'customer_key', 'product_key', 'order_number', 'order_line_number']);
            
            // Indexes for Performance
            $table->index(['date_key', 'customer_key']);
            $table->index(['date_key', 'product_key']);
            $table->index(['order_number']);
        });

        Schema::create('fact_inventory', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('date_key');
            $table->unsignedBigInteger('product_key');
            $table->string('warehouse_location');
            
            // Measures
            $table->integer('beginning_balance');
            $table->integer('receipts');
            $table->integer('issues');
            $table->integer('ending_balance');
            $table->decimal('unit_cost', 10, 2);
            $table->decimal('total_value', 12, 2);
            
            $table->timestamps();
            
            $table->foreign('date_key')->references('date_key')->on('dim_dates');
            $table->foreign('product_key')->references('product_key')->on('dim_products');
            
            $table->unique(['date_key', 'product_key', 'warehouse_location']);
        });
    }

    public function down()
    {
        Schema::dropIfExists('fact_inventory');
        Schema::dropIfExists('fact_sales');
    }
}
```

### 3. Laravel Models untuk BI

```php
// app/Models/BI/DimCustomer.php
<?php

namespace App\Models\BI;

use Illuminate\Database\Eloquent\Model;

class DimCustomer extends Model
{
    protected $table = 'dim_customers';
    protected $primaryKey = 'customer_key';
    
    protected $fillable = [
        'customer_id', 'customer_name', 'customer_type', 
        'industry_sector', 'region', 'city', 'customer_value',
        'registration_date', 'is_current', 'effective_date', 'expiry_date'
    ];

    protected $casts = [
        'customer_value' => 'decimal:2',
        'registration_date' => 'date',
        'is_current' => 'boolean',
        'effective_date' => 'datetime',
        'expiry_date' => 'datetime',
    ];

    // Relationships
    public function factSales()
    {
        return $this->hasMany(FactSales::class, 'customer_key', 'customer_key');
    }

    // Business Logic
    public function getTotalRevenueAttribute()
    {
        return $this->factSales()->sum('net_amount');
    }

    public function getOrderCountAttribute()
    {
        return $this->factSales()->distinct('order_number')->count('order_number');
    }
}
```

```php
// app/Models/BI/FactSales.php
<?php

namespace App\Models\BI;

use Illuminate\Database\Eloquent\Model;

class FactSales extends Model
{
    protected $table = 'fact_sales';
    
    protected $fillable = [
        'date_key', 'customer_key', 'product_key', 'order_number', 
        'order_line_number', 'quantity_sold', 'unit_price', 
        'discount_amount', 'net_amount', 'cost_amount', 
        'gross_profit', 'profit_margin'
    ];

    protected $casts = [
        'quantity_sold' => 'integer',
        'unit_price' => 'decimal:2',
        'discount_amount' => 'decimal:2',
        'net_amount' => 'decimal:2',
        'cost_amount' => 'decimal:2',
        'gross_profit' => 'decimal:2',
        'profit_margin' => 'decimal:2',
    ];

    // Relationships
    public function dimCustomer()
    {
        return $this->belongsTo(DimCustomer::class, 'customer_key', 'customer_key');
    }

    public function dimProduct()
    {
        return $this->belongsTo(DimProduct::class, 'product_key', 'product_key');
    }

    public function dimDate()
    {
        return $this->belongsTo(DimDate::class, 'date_key', 'date_key');
    }
}
```

### 4. Laravel Commands untuk ETL

```php
// app/Console/Commands/ExtractSalesData.php
<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use App\Models\Order;
use App\Models\OrderItem;
use App\Models\BI\FactSales;
use App\Models\BI\DimCustomer;
use App\Models\BI\DimProduct;
use App\Models\BI\DimDate;

class ExtractSalesData extends Command
{
    protected $signature = 'bi:extract-sales {--date=today}';
    protected $description = 'Extract sales data to BI fact tables';

    public function handle()
    {
        $this->info('Starting sales data extraction...');
        
        $date = $this->option('date') === 'today' ? now()->toDateString() : $this->option('date');
        
        // Get orders for the specified date
        $orders = Order::whereDate('created_at', $date)
                      ->with(['orderItems.product', 'customer'])
                      ->get();

        $processedCount = 0;

        foreach ($orders as $order) {
            foreach ($order->orderItems as $item) {
                // Get or create dimension keys
                $dateKey = $this->getDateKey($order->created_at);
                $customerKey = $this->getCustomerKey($order->customer);
                $productKey = $this->getProductKey($item->product);

                // Calculate measures
                $netAmount = $item->quantity * $item->unit_price - $item->discount_amount;
                $costAmount = $item->quantity * $item->product->cost_price;
                $grossProfit = $netAmount - $costAmount;
                $profitMargin = $netAmount > 0 ? ($grossProfit / $netAmount) * 100 : 0;

                // Insert or update fact record
                FactSales::updateOrCreate(
                    [
                        'date_key' => $dateKey,
                        'customer_key' => $customerKey,
                        'product_key' => $productKey,
                        'order_number' => $order->order_number,
                        'order_line_number' => $item->line_number
                    ],
                    [
                        'quantity_sold' => $item->quantity,
                        'unit_price' => $item->unit_price,
                        'discount_amount' => $item->discount_amount,
                        'net_amount' => $netAmount,
                        'cost_amount' => $costAmount,
                        'gross_profit' => $grossProfit,
                        'profit_margin' => $profitMargin
                    ]
                );

                $processedCount++;
            }
        }

        $this->info("Processed {$processedCount} sales records for {$date}");
    }

    private function getDateKey($date)
    {
        $dimDate = DimDate::where('full_date', $date->toDateString())->first();
        return $dimDate ? $dimDate->date_key : null;
    }

    private function getCustomerKey($customer)
    {
        $dimCustomer = DimCustomer::where('customer_id', $customer->id)
                                 ->where('is_current', true)
                                 ->first();
        
        if (!$dimCustomer) {
            $dimCustomer = DimCustomer::create([
                'customer_id' => $customer->id,
                'customer_name' => $customer->name,
                'customer_type' => $customer->customer_type,
                'industry_sector' => $customer->industry_sector,
                'region' => $customer->region,
                'city' => $customer->city,
                'customer_value' => 0,
                'registration_date' => $customer->created_at,
                'is_current' => true,
                'effective_date' => now()
            ]);
        }

        return $dimCustomer->customer_key;
    }

    private function getProductKey($product)
    {
        $dimProduct = DimProduct::where('product_id', $product->id)
                               ->where('is_current', true)
                               ->first();
        
        if (!$dimProduct) {
            $dimProduct = DimProduct::create([
                'product_id' => $product->id,
                'product_name' => $product->name,
                'category_level1' => $product->category,
                'unit_price' => $product->unit_price,
                'cost_price' => $product->cost_price,
                'unit_of_measure' => $product->unit_of_measure,
                'is_current' => true,
                'effective_date' => now()
            ]);
        }

        return $dimProduct->product_key;
    }
}
```

### 5. Scheduled ETL dengan Laravel Task Scheduling

```php
// app/Console/Kernel.php
<?php

namespace App\Console;

use Illuminate\Console\Scheduling\Schedule;
use Illuminate\Foundation\Console\Kernel as ConsoleKernel;

class Kernel extends ConsoleKernel
{
    protected $commands = [
        Commands\ExtractSalesData::class,
        Commands\ExtractInventoryData::class,
        Commands\PopulateDateDimension::class,
        Commands\RefreshBIDashboard::class,
    ];

    protected function schedule(Schedule $schedule)
    {
        // Daily ETL at 2 AM
        $schedule->command('bi:extract-sales --date=yesterday')
                 ->dailyAt('02:00')
                 ->appendOutputTo(storage_path('logs/bi-etl.log'));

        $schedule->command('bi:extract-inventory --date=yesterday')
                 ->dailyAt('02:30')
                 ->appendOutputTo(storage_path('logs/bi-etl.log'));

        // Weekly aggregations on Sunday
        $schedule->command('bi:calculate-weekly-metrics')
                 ->weekly()
                 ->sundays()
                 ->at('03:00');

        // Monthly reporting
        $schedule->command('bi:generate-monthly-reports')
                 ->monthlyOn(1, '04:00');
    }
}
```

### 6. BI Dashboard Controller

```php
// app/Http/Controllers/BI/DashboardController.php
<?php

namespace App\Http\Controllers\BI;

use App\Http\Controllers\Controller;
use App\Models\BI\FactSales;
use App\Models\BI\DimCustomer;
use App\Models\BI\DimProduct;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class DashboardController extends Controller
{
    public function index()
    {
        $metrics = $this->getKPIMetrics();
        $salesTrend = $this->getSalesTrendData();
        $topCustomers = $this->getTopCustomers();
        $productPerformance = $this->getProductPerformance();

        return view('bi.dashboard', compact(
            'metrics', 'salesTrend', 'topCustomers', 'productPerformance'
        ));
    }

    private function getKPIMetrics()
    {
        $currentMonth = now()->format('Y-m');
        $lastMonth = now()->subMonth()->format('Y-m');

        $currentSales = FactSales::join('dim_dates', 'fact_sales.date_key', '=', 'dim_dates.date_key')
                                ->where(DB::raw("DATE_FORMAT(dim_dates.full_date, '%Y-%m')"), $currentMonth)
                                ->sum('net_amount');

        $lastMonthSales = FactSales::join('dim_dates', 'fact_sales.date_key', '=', 'dim_dates.date_key')
                                  ->where(DB::raw("DATE_FORMAT(dim_dates.full_date, '%Y-%m')"), $lastMonth)
                                  ->sum('net_amount');

        $growth = $lastMonthSales > 0 ? (($currentSales - $lastMonthSales) / $lastMonthSales) * 100 : 0;

        return [
            'total_revenue' => $currentSales,
            'growth_rate' => round($growth, 2),
            'total_orders' => FactSales::join('dim_dates', 'fact_sales.date_key', '=', 'dim_dates.date_key')
                                      ->where(DB::raw("DATE_FORMAT(dim_dates.full_date, '%Y-%m')"), $currentMonth)
                                      ->distinct('order_number')
                                      ->count('order_number'),
            'average_order_value' => $currentSales > 0 ? $currentSales / FactSales::join('dim_dates', 'fact_sales.date_key', '=', 'dim_dates.date_key')
                                                                                  ->where(DB::raw("DATE_FORMAT(dim_dates.full_date, '%Y-%m')"), $currentMonth)
                                                                                  ->distinct('order_number')
                                                                                  ->count('order_number') : 0
        ];
    }

    private function getSalesTrendData()
    {
        return FactSales::join('dim_dates', 'fact_sales.date_key', '=', 'dim_dates.date_key')
                        ->select(
                            DB::raw('dim_dates.month_name as month'),
                            DB::raw('SUM(fact_sales.net_amount) as revenue'),
                            DB::raw('COUNT(DISTINCT fact_sales.order_number) as orders')
                        )
                        ->where('dim_dates.year', now()->year)
                        ->groupBy('dim_dates.month_of_year', 'dim_dates.month_name')
                        ->orderBy('dim_dates.month_of_year')
                        ->get();
    }

    private function getTopCustomers()
    {
        return DimCustomer::join('fact_sales', 'dim_customers.customer_key', '=', 'fact_sales.customer_key')
                          ->select(
                              'dim_customers.customer_name',
                              'dim_customers.customer_type',
                              DB::raw('SUM(fact_sales.net_amount) as total_revenue'),
                              DB::raw('COUNT(DISTINCT fact_sales.order_number) as total_orders')
                          )
                          ->groupBy('dim_customers.customer_key', 'dim_customers.customer_name', 'dim_customers.customer_type')
                          ->orderBy('total_revenue', 'desc')
                          ->limit(10)
                          ->get();
    }

    private function getProductPerformance()
    {
        return DimProduct::join('fact_sales', 'dim_products.product_key', '=', 'fact_sales.product_key')
                         ->select(
                             'dim_products.product_name',
                             'dim_products.category_level1',
                             DB::raw('SUM(fact_sales.quantity_sold) as total_quantity'),
                             DB::raw('SUM(fact_sales.net_amount) as total_revenue'),
                             DB::raw('AVG(fact_sales.profit_margin) as avg_margin')
                         )
                         ->groupBy('dim_products.product_key', 'dim_products.product_name', 'dim_products.category_level1')
                         ->orderBy('total_revenue', 'desc')
                         ->limit(10)
                         ->get();
    }

    public function salesAnalytics()
    {
        $customerSegments = $this->getCustomerSegmentation();
        $seasonalAnalysis = $this->getSeasonalAnalysis();
        
        return view('bi.sales-analytics', compact('customerSegments', 'seasonalAnalysis'));
    }

    private function getCustomerSegmentation()
    {
        // RFM Analysis using Laravel Eloquent
        return DB::table('fact_sales')
                 ->join('dim_customers', 'fact_sales.customer_key', '=', 'dim_customers.customer_key')
                 ->join('dim_dates', 'fact_sales.date_key', '=', 'dim_dates.date_key')
                 ->select(
                     'dim_customers.customer_name',
                     'dim_customers.customer_type',
                     DB::raw('MAX(dim_dates.full_date) as last_purchase_date'),
                     DB::raw('COUNT(DISTINCT fact_sales.order_number) as frequency'),
                     DB::raw('SUM(fact_sales.net_amount) as monetary')
                 )
                 ->groupBy('dim_customers.customer_key', 'dim_customers.customer_name', 'dim_customers.customer_type')
                 ->get()
                 ->map(function ($customer) {
                     $recency = now()->diffInDays($customer->last_purchase_date);
                     
                     // Simple RFM scoring (1-5 scale)
                     $customer->recency_score = $recency <= 30 ? 5 : ($recency <= 60 ? 4 : ($recency <= 90 ? 3 : ($recency <= 180 ? 2 : 1)));
                     $customer->frequency_score = $customer->frequency >= 10 ? 5 : ($customer->frequency >= 5 ? 4 : ($customer->frequency >= 3 ? 3 : ($customer->frequency >= 2 ? 2 : 1)));
                     $customer->monetary_score = $customer->monetary >= 5000000 ? 5 : ($customer->monetary >= 2000000 ? 4 : ($customer->monetary >= 1000000 ? 3 : ($customer->monetary >= 500000 ? 2 : 1)));
                     
                     // Assign segment based on RFM scores
                     if ($customer->recency_score >= 4 && $customer->frequency_score >= 4 && $customer->monetary_score >= 4) {
                         $customer->segment = 'Champions';
                     } elseif ($customer->recency_score >= 3 && $customer->frequency_score >= 3) {
                         $customer->segment = 'Loyal Customers';
                     } elseif ($customer->recency_score >= 4) {
                         $customer->segment = 'New Customers';
                     } elseif ($customer->frequency_score >= 3 && $customer->monetary_score >= 3) {
                         $customer->segment = 'At Risk';
                     } else {
                         $customer->segment = 'Others';
                     }
                     
                     return $customer;
                 })
                 ->groupBy('segment')
                 ->map(function ($segment) {
                     return [
                         'count' => $segment->count(),
                         'total_revenue' => $segment->sum('monetary'),
                         'avg_frequency' => $segment->avg('frequency')
                     ];
                 });
    }
}
```

### 7. BI Dashboard View (Blade Template)

```blade
{{-- resources/views/bi/dashboard.blade.php --}}
@extends('layouts.app')

@section('title', 'Business Intelligence Dashboard')

@section('content')
<div class="max-w-7xl mx-auto px-6 py-8">
    <!-- Page Header -->
    <div class="flex justify-between items-center mb-8">
        <h1 class="text-3xl font-bold text-gray-800">Business Intelligence Dashboard</h1>
        <div class="flex space-x-4">
            <button class="bg-primary text-white px-4 py-2 rounded-lg hover:bg-primary/90">
                <i class="fas fa-download mr-2"></i>Export Report
            </button>
            <button class="bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600">
                <i class="fas fa-sync mr-2"></i>Refresh Data
            </button>
        </div>
    </div>

    <!-- KPI Metrics -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <div class="bg-white p-6 rounded-xl shadow-lg">
            <div class="flex items-center">
                <i class="fas fa-chart-line text-4xl text-blue-500 mr-4"></i>
                <div>
                    <div class="text-2xl font-bold text-gray-800">
                        Rp {{ number_format($metrics['total_revenue'], 0, ',', '.') }}
                    </div>
                    <div class="text-gray-600 text-sm">Total Revenue</div>
                    <div class="text-{{ $metrics['growth_rate'] >= 0 ? 'green' : 'red' }}-500 text-sm mt-1">
                        <i class="fas fa-arrow-{{ $metrics['growth_rate'] >= 0 ? 'up' : 'down' }}"></i>
                        {{ number_format(abs($metrics['growth_rate']), 1) }}% vs last month
                    </div>
                </div>
            </div>
        </div>

        <div class="bg-white p-6 rounded-xl shadow-lg">
            <div class="flex items-center">
                <i class="fas fa-shopping-cart text-4xl text-green-500 mr-4"></i>
                <div>
                    <div class="text-2xl font-bold text-gray-800">{{ number_format($metrics['total_orders']) }}</div>
                    <div class="text-gray-600 text-sm">Total Orders</div>
                </div>
            </div>
        </div>

        <div class="bg-white p-6 rounded-xl shadow-lg">
            <div class="flex items-center">
                <i class="fas fa-dollar-sign text-4xl text-purple-500 mr-4"></i>
                <div>
                    <div class="text-2xl font-bold text-gray-800">
                        Rp {{ number_format($metrics['average_order_value'], 0, ',', '.') }}
                    </div>
                    <div class="text-gray-600 text-sm">Average Order Value</div>
                </div>
            </div>
        </div>

        <div class="bg-white p-6 rounded-xl shadow-lg">
            <div class="flex items-center">
                <i class="fas fa-users text-4xl text-yellow-500 mr-4"></i>
                <div>
                    <div class="text-2xl font-bold text-gray-800">{{ number_format($topCustomers->count()) }}</div>
                    <div class="text-gray-600 text-sm">Active Customers</div>
                </div>
            </div>
        </div>
    </div>

    <!-- Charts -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
        <!-- Sales Trend Chart -->
        <div class="bg-white p-6 rounded-xl shadow-lg">
            <h3 class="text-xl font-semibold text-gray-800 mb-4">Sales Trend (This Year)</h3>
            <canvas id="salesTrendChart" height="300"></canvas>
        </div>

        <!-- Product Performance -->
        <div class="bg-white p-6 rounded-xl shadow-lg">
            <h3 class="text-xl font-semibold text-gray-800 mb-4">Top Products</h3>
            <canvas id="productChart" height="300"></canvas>
        </div>
    </div>

    <!-- Top Customers Table -->
    <div class="bg-white rounded-xl shadow-lg overflow-hidden">
        <div class="p-6 border-b border-gray-200">
            <h3 class="text-xl font-semibold text-gray-800">Top Customers</h3>
        </div>
        <div class="overflow-x-auto">
            <table class="w-full">
                <thead class="bg-gray-50">
                    <tr>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Customer</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Type</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Total Revenue</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Orders</th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Avg Order Value</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                    @foreach($topCustomers as $customer)
                    <tr class="hover:bg-gray-50">
                        <td class="px-6 py-4 text-sm font-medium text-gray-900">{{ $customer->customer_name }}</td>
                        <td class="px-6 py-4 text-sm text-gray-900">
                            <span class="px-3 py-1 bg-blue-100 text-blue-800 text-xs rounded-full">
                                {{ ucfirst($customer->customer_type) }}
                            </span>
                        </td>
                        <td class="px-6 py-4 text-sm text-gray-900">
                            Rp {{ number_format($customer->total_revenue, 0, ',', '.') }}
                        </td>
                        <td class="px-6 py-4 text-sm text-gray-900">{{ $customer->total_orders }}</td>
                        <td class="px-6 py-4 text-sm text-gray-900">
                            Rp {{ number_format($customer->total_revenue / $customer->total_orders, 0, ',', '.') }}
                        </td>
                    </tr>
                    @endforeach
                </tbody>
            </table>
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
// Sales Trend Chart
const salesTrendData = @json($salesTrend);
const ctx1 = document.getElementById('salesTrendChart').getContext('2d');
new Chart(ctx1, {
    type: 'line',
    data: {
        labels: salesTrendData.map(item => item.month),
        datasets: [{
            label: 'Revenue (IDR)',
            data: salesTrendData.map(item => item.revenue),
            borderColor: 'rgb(59, 130, 246)',
            backgroundColor: 'rgba(59, 130, 246, 0.1)',
            tension: 0.1
        }, {
            label: 'Orders',
            data: salesTrendData.map(item => item.orders),
            borderColor: 'rgb(34, 197, 94)',
            backgroundColor: 'rgba(34, 197, 94, 0.1)',
            yAxisID: 'y1',
            tension: 0.1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            y: {
                type: 'linear',
                display: true,
                position: 'left',
            },
            y1: {
                type: 'linear',
                display: true,
                position: 'right',
                grid: {
                    drawOnChartArea: false,
                },
            }
        }
    }
});

// Product Performance Chart
const productData = @json($productPerformance);
const ctx2 = document.getElementById('productChart').getContext('2d');
new Chart(ctx2, {
    type: 'doughnut',
    data: {
        labels: productData.map(item => item.product_name),
        datasets: [{
            data: productData.map(item => item.total_revenue),
            backgroundColor: [
                '#3B82F6', '#22C55E', '#F59E0B', '#EF4444', '#8B5CF6',
                '#06B6D4', '#F97316', '#84CC16', '#EC4899', '#6B7280'
            ]
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                position: 'bottom'
            }
        }
    }
});
</script>
@endsection
```

---

## KESIMPULAN

### Keuntungan Menggunakan Laravel untuk BI:

1. **Unified Tech Stack** - Satu framework untuk semua kebutuhan
2. **Real-time Data Access** - Langsung dari operational database
3. **Easier Maintenance** - Developers sudah familiar dengan Laravel
4. **Cost Effective** - Tidak perlu tools BI mahal seperti Tableau
5. **Customizable** - Bisa disesuaikan dengan kebutuhan spesifik SATRIAMART
6. **Scalable** - Laravel dapat handle growth perusahaan

### Implementasi Praktis:

✅ **Data Warehouse** - Laravel Migrations untuk dimensional model  
✅ **ETL Process** - Laravel Commands dengan scheduling  
✅ **Dashboards** - Blade templates dengan Chart.js  
✅ **Analytics** - PHP ML libraries untuk predictive analytics  
✅ **Reporting** - Laravel PDF generation untuk automated reports  

**Business Intelligence dengan Laravel tidak hanya mungkin, tapi sangat efektif untuk perusahaan yang sudah menggunakan Laravel ecosystem!**
