@app.route('/$methodUseCase_rest')
def $methodUseCase():
    request = {'id':1}
    return f'{$methodUseCase_rest(request)}'

