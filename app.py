from flask import Flask

app = Flask(__name__)

# تنسيق CSS بسيط لجعل الموقع يبدو أجمل
style = """
<style>
    body { font-family: sans-serif; text-align: center; margin-top: 50px; background-color: #f4f4f9; }
    h1 { color: #2c3e50; }
    p { color: #34495e; font-size: 1.2em; }
    .nav { margin-bottom: 20px; }
    .nav a { margin: 0 10px; text-decoration: none; color: #3498db; font-weight: bold; }
</style>
"""

@app.route('/')
def home():
    return f"""
    {style}
    <div class="nav">
        <a href="/">الرئيسية</a> | <a href="/about">عني</a>
    </div>
    <h1>مرحباً بك في موقعي على Kali!</h1>
    <p>هذا الموقع يعمل من داخل Termux بنجاح.</p>
    """

@app.route('/about')
def about():
    return f"""
    {style}
    <div class="nav">
        <a href="/">الرئيسية</a> | <a href="/about">عني</a>
    </div>
    <h1>صفحة عني</h1>
    <p>أنا أيوب، مبرمج أتعلم تطوير الويب باستخدام Flask.</p>
    <p>هذه هي صفحتي الثانية!</p>
    """

if __name__ == '__main__':
    # تشغيل السيرفر على جميع العناوين المتاحة
    app.run(debug=True, host='0.0.0.0', port=5000)


