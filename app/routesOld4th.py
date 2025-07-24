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
            log_user_info(request)
            pdfs = request.files.getlist('pdfs')
            if not pdfs:
                return "No files uploaded", 400

            # Use in-memory BytesIO stream from merge_pdfs
            output_stream = merge_pdfs(pdfs)

            return send_file(
                output_stream,
                as_attachment=True,
                download_name='merged.pdf',
                mimetype='application/pdf'
            )

        except Exception as e:
            print("Error:", e)
            traceback.print_exc()
            return "Internal Server Error", 500

    @app.route('/admin', methods=['GET'])
    def admin():
        return render_template('admin.html')
