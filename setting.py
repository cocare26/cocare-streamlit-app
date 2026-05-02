<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Settings Pro</title>
    <style>
        :root {
            --bg-color: #cbdbe5;
            --card-bg: rgba(255, 255, 255, 0.4);
            --btn-bg: #ffffff;
            --text-color: #4a4a4a;
            --accent-color: #7baec2;
        }

        body {
            background-color: var(--bg-color);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            overflow: hidden;
        }

        /* حاوية الهاتف الافتراضية */
        .phone-container {
            width: 360px;
            height: 640px;
            background: var(--card-bg);
            backdrop-filter: blur(10px);
            border-radius: 40px;
            border: 8px solid rgba(255, 255, 255, 0.2);
            position: relative;
            box-shadow: 0 20px 50px rgba(0,0,0,0.1);
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }

        .screen {
            position: absolute;
            width: 100%;
            height: 100%;
            padding: 30px;
            box-sizing: border-box;
            transition: transform 0.4s ease-in-out, opacity 0.3s ease;
            opacity: 0;
            transform: translateX(100%);
            display: flex;
            flex-direction: column;
        }

        .screen.active {
            opacity: 1;
            transform: translateX(0);
        }

        .screen.exit {
            transform: translateX(-100%);
        }

        h2 { text-align: center; color: var(--text-color); margin-top: 40px; }

        /* الأزرار الاحترافية */
        .btn {
            background: var(--btn-bg);
            border: none;
            border-radius: 20px;
            padding: 16px 20px;
            margin: 10px 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0,0,0,0.02);
            transition: all 0.2s;
            font-size: 16px;
            color: var(--text-color);
            text-decoration: none;
        }

        .btn:active { transform: scale(0.97); background: #f0f0f0; }

        /* المدخلات */
        .input-group { margin-bottom: 15px; }
        input, textarea {
            width: 100%;
            padding: 15px;
            border-radius: 15px;
            border: none;
            background: white;
            box-sizing: border-box;
            font-size: 14px;
            outline: none;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);
        }

        textarea { height: 150px; background: #fef8e8; resize: none; }

        .save-btn {
            background: var(--btn-bg);
            font-weight: bold;
            padding: 15px;
            border-radius: 25px;
            border: none;
            cursor: pointer;
            margin-top: 20px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }

        .back-btn {
            cursor: pointer;
            font-size: 24px;
            color: var(--text-color);
            position: absolute;
            top: 30px;
            left: 20px;
        }

        .grid-footer {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-top: auto;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>

<div class="phone-container">
    <!-- الشاشة الرئيسية -->
    <div id="main" class="screen active">
        <h2>Settings</h2>
        <div style="margin-top: 20px;">
            <button class="btn" onclick="nav('password')"><span>🔒 Change Password</span><span>›</span></button>
            <button class="btn" onclick="nav('language')"><span>🌐 Change Language</span><span>›</span></button>
            <button class="btn" onclick="nav('rate')"><span>⭐ Rate App</span><span>›</span></button>
            <button class="btn" onclick="alert('Logged Out!')"><span>🚪 Log Out</span><span>›</span></button>
        </div>
        
        <div class="grid-footer">
            <button class="btn" style="font-size: 12px; flex-direction: column; gap: 5px;" onclick="nav('report')">
                <span>⚠️</span> Report a Problem
            </button>
            <button class="btn" style="font-size: 12px; flex-direction: column; gap: 5px;" onclick="nav('contact')">
                <span>✉️</span> Contact Us
            </button>
        </div>
    </div>

    <!-- شاشة كلمة المرور -->
    <div id="password" class="screen">
        <span class="back-btn" onclick="nav('main')">←</span>
        <h2>Change Password</h2>
        <div style="margin-top: 30px;">
            <input type="password" placeholder="Current Password">
            <input type="password" placeholder="New Password" style="margin-top: 10px;">
            <input type="password" placeholder="Re-write New Password" style="margin-top: 10px;">
            <button class="save-btn" style="width: 100%;" onclick="nav('main')">Save</button>
        </div>
    </div>

    <!-- شاشة اللغة -->
    <div id="language" class="screen">
        <span class="back-btn" onclick="nav('main')">←</span>
        <h2>Language</h2>
        <div style="margin-top: 30px;">
            <button class="btn"><span>English</span><span>✓</span></button>
            <button class="btn"><span>العربية</span><span>›</span></button>
        </div>
    </div>

    <!-- شاشة التقييم -->
    <div id="rate" class="screen">
        <span class="back-btn" onclick="nav('main')">←</span>
        <h2>Rate App</h2>
        <div style="margin-top: 30px;">
            <button class="btn">🤖 Google Play Store</button>
            <button class="btn">🍎 Apple App Store</button>
            <button class="btn">💠 Huawei AppGallery</button>
        </div>
    </div>

    <!-- شاشة البلاغات -->
    <div id="report" class="screen">
        <span class="back-btn" onclick="nav('main')">←</span>
        <h2>Report</h2>
        <textarea>I need help...</textarea>
        <button class="save-btn" onclick="nav('main')">Send Report</button>
    </div>

    <!-- شاشة التواصل -->
    <div id="contact" class="screen">
        <span class="back-btn" onclick="nav('main')">←</span>
        <h2>Contact Us</h2>
        <div style="margin-top: 30px;">
            <div class="btn">📧 Co.Care26@gmail.com</div>
            <div class="btn">📞 +962 79 123 4657</div>
        </div>
    </div>
</div>

<script>
    function nav(screenId) {
        // إزالة الكلاسات الحالية لعمل حركة الخروج والدخول
        document.querySelectorAll('.screen').forEach(s => {
            s.classList.remove('active');
            s.classList.remove('exit');
        });

        const target = document.getElementById(screenId);
        target.classList.add('active');
    }
</script>

</body>
</html>
