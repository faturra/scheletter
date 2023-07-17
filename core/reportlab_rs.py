from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views import View
from reportlab.pdfgen import canvas
from io import BytesIO


class UserPDFView(View):
    def get(self, request, *args, **kwargs):
        user_data = {  # Data informasi user
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'address': '123 Main Street',
            # Tambahkan informasi user lainnya di sini
        }

        # Mengambil template Django untuk PDF
        template = get_template('administration/letter/letter_templates/user_info_template.html')
        context = Context(user_data)

        # Menerapkan data ke template
        html = template.render(context)

        # Membuat file PDF dengan ReportLab
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="user_info.pdf"'

        buffer = BytesIO()
        p = canvas.Canvas(buffer)

        # Menggabungkan konten HTML ke file PDF
        p.drawString(100, 750, 'Informasi User')
        p.drawString(100, 700, '----------------')
        p.drawString(100, 650, html)

        p.showPage()
        p.save()

        # Mengambil konten dari buffer dan mengirimkannya sebagai respons
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)

        return response
