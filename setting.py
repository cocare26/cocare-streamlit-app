import streamlit as st

# إعداد روابط الصفحات (استبدل الروابط بالصفحات الفعلية في تطبيقك)
links = {
    "change_password": "?page=password",
    "change_language": "?page=language",
    "rate_app": "?page=rate",
    "logout": "?page=logout",
    "report": "?page=report",
    "contact": "?page=contact"
}

st.markdown(f"""
    <style>
    /* 1. الخلفية بيبي بلو */
    .stApp {{
        background-color: #E0F7FA;
    }}

    .main-container {{
        max-width: 400px;
        margin: 0 auto;
        padding-top: 30px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}

    /* 2. سهم السيتنج العلوي أسود */
    .header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
    }}
    .back-arrow-top {{
        color: black; 
        font-size: 22px;
        text-decoration: none;
        font-weight: bold;
    }}
    .title {{
        color: black;
        font-size: 22px;
        font-weight: bold;
        margin-right: 10px;
    }}

    /* 3. تنسيق الأزرار كروابط */
    .menu-item-link {{
        text-decoration: none;
        color: inherit;
        display: block;
        margin-bottom: 12px;
    }}

    .menu-button {{
        background-color: white;
        border-radius: 50px;
        padding: 12px 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
        transition: 0.3s;
    }}
    
    .menu-button:hover {{
        transform: scale(1.02);
        background-color: #f8f9fa;
    }}

    .left-section {{
        display: flex;
        align-items: center;
        gap: 12px;
    }}

    .menu-text {{
        color: black;
        font-size: 15px;
        font-weight: 500;
    }}

    /* 4. الأسهم الجانبية بيضاء وعلى اليمين */
    .arrow-right {{
        background-color: white; /* لجعل السهم يظهر إذا كانت الخلفية بيضاء، نضع له حاوية أو نغير لونه */
        color: #FFFFFF; /* لون السهم أبيض */
        background: #f0f0f0; /* خلفية دائرية خفيفة للسهم ليظهر الأبيض بوضوح */
        width: 24px;
        height: 24px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 12px;
        font-weight: bold;
        text-shadow: 0px 0px 2px rgba(0,0,0,0.2); /* ظل خفيف للسهم الأبيض */
    }}

    .bottom-row {{
        display: flex;
        gap: 10px;
    }}
    .small-btn {{
        flex: 1;
        background-color: white;
        border-radius: 50px;
        padding: 10px 15px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }}
    </style>

    <div class="main-container">
        <div class="header">
            <a href="#" class="back-arrow-top"> &lt; </a>
            <div class="title">Settings</div>
            <div style="width:20px;"></div>
        </div>

        <a href="{links['change_password']}" class="menu-item-link">
            <div class="menu-button">
                <div class="left-section"><span>🔐</span> <span class="menu-text">Change Password</span></div>
                <div class="arrow-right"> &gt; </div>
            </div>
        </a>

        <a href="{links['change_language']}" class="menu-item-link">
            <div class="menu-button">
                <div class="left-section"><span>🌐</span> <span class="menu-text">Change Language</span></div>
                <div class="arrow-right"> &gt; </div>
            </div>
        </a>

        <a href="{links['rate_app']}" class="menu-item-link">
            <div class="menu-button">
                <div class="left-section"><span>⭐</span> <span class="menu-text">Rate App</span></div>
                <div class="arrow-right"> &gt; </div>
            </div>
        </a>

        <a href="{links['logout']}" class="menu-item-link">
            <div class="menu-button">
                <div class="left-section"><span>🚪</span> <span class="menu-text">Log Out</span></div>
                <div class="arrow-right"> &gt; </div>
            </div>
        </a>

        <div class="bottom-row">
            <a href="{links['report']}" class="menu-item-link" style="flex:1;">
                <div class="small-btn">
                    <div class="left-section" style="gap:5px;"><span>⚠️</span><span class="menu-text" style="font-size:12px;">Report</span></div>
                    <div class="arrow-right" style="width:18px; height:18px; font-size:10px;"> &gt; </div>
                </div>
            </a>
            <a href="{links['contact']}" class="menu-item-link" style="flex:1;">
                <div class="small-btn">
                    <div class="left-section" style="gap:5px;"><span>✉️</span><span class="menu-text" style="font-size:12px;">Contact</span></div>
                    <div class="arrow-right" style="width:18px; height:18px; font-size:10px;"> &gt; </div>
                </div>
            </a>
        </div>
import React, { useState } from 'react';

const AppSettings = () => {
  const [view, setView] = useState('main');

  // التنسيقات العامة المستوحاة من الصورة
  const styles = {
    container: {
      backgroundColor: '#d1e5f0', // الخلفية السماوية الفاتحة
      minHeight: '100vh',
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      fontFamily: 'Arial, sans-serif',
      padding: '20px'
    },
    card: {
      backgroundColor: 'rgba(255, 255, 255, 0.4)', // تأثير الشفافية للأزرار
      borderRadius: '20px',
      padding: '20px',
      width: '350px',
      boxShadow: '0 4px 15px rgba(0,0,0,0.05)',
      textAlign: 'center'
    },
    button: {
      backgroundColor: 'white',
      border: 'none',
      borderRadius: '25px',
      padding: '12px 20px',
      margin: '10px 0',
      width: '100%',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      cursor: 'pointer',
      fontSize: '16px',
      color: '#555'
    },
    input: {
      width: '100%',
      padding: '12px',
      margin: '8px 0',
      borderRadius: '10px',
      border: '1px solid #ddd',
      boxSizing: 'border-box'
    },
    saveBtn: {
      backgroundColor: 'white',
      border: 'none',
      borderRadius: '20px',
      padding: '10px 40px',
      marginTop: '20px',
      cursor: 'pointer',
      fontWeight: 'bold'
    }
  };

  // شاشة الإعدادات الرئيسية
  const MainSettings = () => (
    <div style={styles.card}>
      <h2 style={{color: '#555'}}>Settings</h2>
      <button style={styles.button} onClick={() => setView('password')}>
        <span>🔒 Change Password</span> <span>&gt;</span>
      </button>
      <button style={styles.button} onClick={() => setView('language')}>
        <span>🌐 Change Language</span> <span>&gt;</span>
      </button>
      <button style={styles.button} onClick={() => setView('rate')}>
        <span>⭐ Rate App</span> <span>&gt;</span>
      </button>
      <button style={styles.button}>
        <span>🚪 Log Out</span> <span>&gt;</span>
      </button>
      <div style={{display: 'flex', gap: '10px'}}>
        <button style={{...styles.button, fontSize: '14px'}} onClick={() => setView('report')}>
           ⚠️ Report a Problem
        </button>
        <button style={{...styles.button, fontSize: '14px'}} onClick={() => setView('contact')}>
           ✉️ Contact Us
        </button>
      </div>
    </div>
  );

  // شاشة تغيير كلمة المرور
  const PasswordView = () => (
    <div style={styles.card}>
      <h3>Change Password</h3>
      <input type="password" placeholder="Current Password" style={styles.input} />
      <input type="password" placeholder="New Password" style={styles.input} />
      <input type="password" placeholder="Re-write New Password" style={styles.input} />
      <button style={styles.saveBtn} onClick={() => setView('main')}>Save</button>
    </div>
    """, unsafe_allow_html=True)
    
  );

  return (
    <div style={styles.container}>
      {view === 'main' && <MainSettings />}
      {view === 'password' && <PasswordView />}
      {/* يمكنك إضافة باقي الشاشات (اللغة، التواصل) بنفس الطريقة */}
      {view !== 'main' && (
        <button 
          onClick={() => setView('main')} 
          style={{position: 'absolute', top: '20px', left: '20px', background: 'none', border: 'none', cursor: 'pointer', fontSize: '20px'}}
        >
          ←
        </button>
      )}
    </div>
  );
};

export default AppSettings;
