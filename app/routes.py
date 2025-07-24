from flask import request, render_template, send_file
from app.services.merge_service import merge_pdfs
from app.services.log_service import log_user_info

def register_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def home():
        if request.method == 'POST':
            log_user_info(request)
            output_path = merge_pdfs(request.files.getlist('pdfs'))
            return send_file(output_path, as_attachment=True)
        return render_template('index.html')

    @app.route('/admin')
    def admin():
        from app.services.log_service import read_logs
        logs = read_logs()
        return render_template('admin.html', logs=logs)
