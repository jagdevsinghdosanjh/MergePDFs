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

# from flask import render_template, request, send_file, flash, redirect, url_for
# from app.services.merge_service import merge_pdfs
# from app.services.log_service import log_user_info
# import traceback
# import json
# import os

# def register_routes(app):
#     @app.route('/', methods=['GET', 'POST'])
#     def home():
#         if request.method == 'GET':
#             return render_template('index.html')

#         try:
#             log_user_info(request)
#             pdfs = request.files.getlist('pdfs')
#             if not pdfs or not all(f.filename.endswith('.pdf') and f.content_length > 0 for f in pdfs):
#                 flash("Please upload valid PDF files only.")
#                 return redirect(url_for('home'))

#             output_stream = merge_pdfs(pdfs)

#             return send_file(
#                 output_stream,
#                 as_attachment=True,
#                 download_name='merged.pdf',
#                 mimetype='application/pdf'
#             )

#         except Exception as e:
#             print("Error during merge:", e)
#             traceback.print_exc()
#             flash("Something went wrong while merging. Please try again.")
#             return redirect(url_for('home'))

#     @app.route('/admin', methods=['GET'])
#     def admin():
#         log_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'user_logs.json'))
#         logs = []
#         if os.path.exists(log_path):
#             with open(log_path, 'r') as f:
#                 try:
#                     logs = json.load(f)
#                 except json.JSONDecodeError:
#                     logs = []
#         for entry in logs:
#             entry['timestamp'] = 'now'
#         return render_template('admin.html', logs=logs)
