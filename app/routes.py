from flask import render_template, request, send_file
from app.services.merge_service import merge_pdfs
from app.services.log_service import log_user_info
import traceback

def register_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def home():
        if request.method == 'GET':
            return render_template('index.html')

        try:
            user_agent = request.headers.get('User-Agent')
            log_user_info(user_agent)

            pdfs = request.files.getlist('pdfs')
            if not pdfs:
                return "No files uploaded", 400

            output_path = merge_pdfs(pdfs)
            return send_file(output_path, as_attachment=True)

        except Exception as e:
            print("Error:", e)
            traceback.print_exc()
            return "Internal Server Error", 500

    @app.route('/admin', methods=['GET'])
    def admin():
        return render_template('admin.html')
