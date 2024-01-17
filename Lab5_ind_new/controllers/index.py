from app import app
import constants
from flask import render_template, request
from complex_number import Complex
from complex_number import do_operation

@app.route('/', methods=['GET'])
def index():
    show_results = request.values.get("button") == "Отправить"

    format = request.values.get("format") or "показательная"
    selected_operations = request.values.getlist("operations")
    
    first_module =request.values.get("first_module",type=float) or 0
    first_phi = request.values.get("first_phi",type=float) or 0
    second_module = request.values.get("second_module",type=float) or 0
    second_phi = request.values.get("second_phi",type=float) or 0

    print(show_results)

    html = render_template(
        'index.html',
        format=format,
        operation_selected = selected_operations,
        operations = constants.operations,
        first_module = first_module,
        first_phi = first_phi,
        second_module= second_module,
        second_phi = second_phi,
        show_results=show_results,
        do_operation = do_operation,
        len=len
    )
    return html