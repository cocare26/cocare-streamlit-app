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
